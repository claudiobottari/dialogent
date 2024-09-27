import openai
from pydantic import create_model
import inspect, json
from inspect import Parameter
from fastcore.utils import nested_idx
from src.agents.messages import MessageHandler
from src.agents.library import *
from src.utils.logger import logger
from config.config import *


openai.api_key = OPENAI_API_KEY
client = openai.OpenAI()

def get_response(messages, max_tokens=150, temperature=0.0):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return completion.choices[0].message.content

def schema(f):
    kw = {n:(o.annotation, ... if o.default==Parameter.empty else o.default)
          for n,o in inspect.signature(f).parameters.items()}
    s = create_model(f'Input for `{f.__name__}`', **kw).schema()
    return dict(name=f.__name__, description=(f.__doc__ or '').strip('\n').strip(), parameters=s)

def schemas(available_functions):
    return [schema(af) for af in available_functions]

def call_func(c, available_functions):
    fc = c.choices[0].message.function_call
    if fc.name not in [af.__name__ for af in available_functions]: return print(f'Not allowed: {fc.name}')
    f = globals()[fc.name]
    return f(**json.loads(fc.arguments))


def solve(message_handler: MessageHandler, model="gpt-4o-mini") -> str:
    system = "You are an IT infrastructure expert able to solve any enquire given all the information required. Please use the given functions in order to gather additional informations that may be beneficial to the analysis."
    available_functions = [get_weather, get_news]
    function_schemas = schemas(available_functions)
    logger.debug(function_schemas)
    steps = 0
    while True:
        steps += 1
        # print(f"\n\n{steps}. {messages[-1]['role']}:\t {messages[-1]['content']}")
        compl = client.chat.completions.create(model=model, messages=message_handler.get_messages(), functions=function_schemas)
    
        if nested_idx(compl, 'choices', 0, 'finish_reason') == 'function_call':
            fc = call_func(compl, available_functions)
            logger.info(nested_idx(compl, 'choices', 0, 'message', 'function_call', 'name'))
            if fc:
                message_handler.enqueue_message("function", fc, nested_idx(compl, 'choices', 0, 'message', 'function_call', 'name'))
        else:
            logger.info(f'\nElaboration DONE in {steps} steps.\n\n\n')
            return nested_idx(compl, 'choices', 0, 'message', 'content')