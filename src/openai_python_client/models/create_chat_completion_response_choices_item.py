from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_chat_completion_response_choices_item_finish_reason import (
    CreateChatCompletionResponseChoicesItemFinishReason,
)

if TYPE_CHECKING:
    from ..models.chat_completion_response_message import ChatCompletionResponseMessage
    from ..models.create_chat_completion_response_choices_item_logprobs_type_0 import (
        CreateChatCompletionResponseChoicesItemLogprobsType0,
    )


T = TypeVar("T", bound="CreateChatCompletionResponseChoicesItem")


@_attrs_define
class CreateChatCompletionResponseChoicesItem:
    """
    Attributes:
        finish_reason (CreateChatCompletionResponseChoicesItemFinishReason): The reason the model stopped generating
            tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
            `length` if the maximum number of tokens specified in the request was reached,
            `content_filter` if content was omitted due to a flag from our content filters,
            `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
        index (int): The index of the choice in the list of choices.
        message (ChatCompletionResponseMessage): A chat completion message generated by the model.
        logprobs (Union['CreateChatCompletionResponseChoicesItemLogprobsType0', None]): Log probability information for
            the choice.
    """

    finish_reason: CreateChatCompletionResponseChoicesItemFinishReason
    index: int
    message: "ChatCompletionResponseMessage"
    logprobs: Union["CreateChatCompletionResponseChoicesItemLogprobsType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.create_chat_completion_response_choices_item_logprobs_type_0 import (
            CreateChatCompletionResponseChoicesItemLogprobsType0,
        )

        finish_reason = self.finish_reason.value

        index = self.index

        message = self.message.to_dict()

        logprobs: Union[Dict[str, Any], None]
        if isinstance(self.logprobs, CreateChatCompletionResponseChoicesItemLogprobsType0):
            logprobs = self.logprobs.to_dict()
        else:
            logprobs = self.logprobs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finish_reason": finish_reason,
                "index": index,
                "message": message,
                "logprobs": logprobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_response_message import ChatCompletionResponseMessage
        from ..models.create_chat_completion_response_choices_item_logprobs_type_0 import (
            CreateChatCompletionResponseChoicesItemLogprobsType0,
        )

        d = src_dict.copy()
        finish_reason = CreateChatCompletionResponseChoicesItemFinishReason(d.pop("finish_reason"))

        index = d.pop("index")

        message = ChatCompletionResponseMessage.from_dict(d.pop("message"))

        def _parse_logprobs(data: object) -> Union["CreateChatCompletionResponseChoicesItemLogprobsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logprobs_type_0 = CreateChatCompletionResponseChoicesItemLogprobsType0.from_dict(data)

                return logprobs_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CreateChatCompletionResponseChoicesItemLogprobsType0", None], data)

        # for llama.cpp compatibility
        try:
            logprobs = _parse_logprobs(d.pop("logprobs"))
        except TypeError:
            logprobs = None

        create_chat_completion_response_choices_item = cls(
            finish_reason=finish_reason,
            index=index,
            message=message,
            logprobs=logprobs,
        )

        create_chat_completion_response_choices_item.additional_properties = d
        return create_chat_completion_response_choices_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
