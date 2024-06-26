from enum import Enum


class CreateCompletionRequestModelType1(str, Enum):
    BABBAGE_002 = "babbage-002"
    DAVINCI_002 = "davinci-002"
    GPT_3_5_TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"

    def __str__(self) -> str:
        return str(self.value)
