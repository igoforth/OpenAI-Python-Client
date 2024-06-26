from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantToolResourcesType0CodeInterpreter")


@_attrs_define
class AssistantToolResourcesType0CodeInterpreter:
    """
    Attributes:
        file_ids (Union[Unset, List[str]]): A list of [file](/docs/api-reference/files) IDs made available to the
            `code_interpreter`` tool. There can be a maximum of 20 files associated with the tool.
    """

    file_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_ids = cast(List[str], d.pop("file_ids", UNSET))

        assistant_tool_resources_type_0_code_interpreter = cls(
            file_ids=file_ids,
        )

        assistant_tool_resources_type_0_code_interpreter.additional_properties = d
        return assistant_tool_resources_type_0_code_interpreter

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
