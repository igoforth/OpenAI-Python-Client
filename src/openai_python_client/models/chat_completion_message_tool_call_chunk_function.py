from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionMessageToolCallChunkFunction")


@_attrs_define
class ChatCompletionMessageToolCallChunkFunction:
    """
    Attributes:
        name (Union[Unset, str]): The name of the function to call.
        arguments (Union[Unset, str]): The arguments to call the function with, as generated by the model in JSON
            format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by
            your function schema. Validate the arguments in your code before calling your function.
    """

    name: Union[Unset, str] = UNSET
    arguments: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        arguments = self.arguments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        arguments = d.pop("arguments", UNSET)

        chat_completion_message_tool_call_chunk_function = cls(
            name=name,
            arguments=arguments,
        )

        chat_completion_message_tool_call_chunk_function.additional_properties = d
        return chat_completion_message_tool_call_chunk_function

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
