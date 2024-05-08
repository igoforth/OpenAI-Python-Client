from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateThreadAndRunRequestToolResourcesType0FileSearch")


@_attrs_define
class CreateThreadAndRunRequestToolResourcesType0FileSearch:
    """
    Attributes:
        vector_store_ids (Union[Unset, List[str]]): The ID of the [vector store](/docs/api-reference/vector-
            stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.
    """

    vector_store_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vector_store_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.vector_store_ids, Unset):
            vector_store_ids = self.vector_store_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vector_store_ids is not UNSET:
            field_dict["vector_store_ids"] = vector_store_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vector_store_ids = cast(List[str], d.pop("vector_store_ids", UNSET))

        create_thread_and_run_request_tool_resources_type_0_file_search = cls(
            vector_store_ids=vector_store_ids,
        )

        create_thread_and_run_request_tool_resources_type_0_file_search.additional_properties = d
        return create_thread_and_run_request_tool_resources_type_0_file_search

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
