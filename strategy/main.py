from SayHello import SayHello
from SayGoodbye import SayGoodbye
from Context import Context

context = Context(SayHello)
context.execute_strategy()
context = Context(SayGoodbye)
context.execute_strategy()
