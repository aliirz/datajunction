# coding: utf-8

"""
    DJ server

    A DataJunction metrics layer  # noqa: E501

    The version of the OpenAPI document: 0.0.post1.dev1+g4e49348
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from djclient import schemas  # noqa: F401


class Database(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A database.

A simple example:

    name: druid
    description: An Apache Druid database
    URI: druid://localhost:8082/druid/v2/sql/
    read-only: true
    async_: false
    cost: 1.0
    """


    class MetaOapg:
        required = {
            "name",
            "URI",
        }
        
        class properties:
            name = schemas.StrSchema
            URI = schemas.StrSchema
            id = schemas.IntSchema
            uuid = schemas.UUIDSchema
            description = schemas.StrSchema
            extra_params = schemas.DictSchema
            read_only = schemas.BoolSchema
            async_ = schemas.BoolSchema
            cost = schemas.NumberSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "name": name,
                "URI": URI,
                "id": id,
                "uuid": uuid,
                "description": description,
                "extra_params": extra_params,
                "read_only": read_only,
                "async_": async_,
                "cost": cost,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    name: MetaOapg.properties.name
    URI: MetaOapg.properties.URI
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["URI"]) -> MetaOapg.properties.URI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra_params"]) -> MetaOapg.properties.extra_params: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["read_only"]) -> MetaOapg.properties.read_only: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["async_"]) -> MetaOapg.properties.async_: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> MetaOapg.properties.cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "URI", "id", "uuid", "description", "extra_params", "read_only", "async_", "cost", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["URI"]) -> MetaOapg.properties.URI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra_params"]) -> typing.Union[MetaOapg.properties.extra_params, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["read_only"]) -> typing.Union[MetaOapg.properties.read_only, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["async_"]) -> typing.Union[MetaOapg.properties.async_, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cost"]) -> typing.Union[MetaOapg.properties.cost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "URI", "id", "uuid", "description", "extra_params", "read_only", "async_", "cost", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        URI: typing.Union[MetaOapg.properties.URI, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        extra_params: typing.Union[MetaOapg.properties.extra_params, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        read_only: typing.Union[MetaOapg.properties.read_only, bool, schemas.Unset] = schemas.unset,
        async_: typing.Union[MetaOapg.properties.async_, bool, schemas.Unset] = schemas.unset,
        cost: typing.Union[MetaOapg.properties.cost, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Database':
        return super().__new__(
            cls,
            *_args,
            name=name,
            URI=URI,
            id=id,
            uuid=uuid,
            description=description,
            extra_params=extra_params,
            read_only=read_only,
            async_=async_,
            cost=cost,
            created_at=created_at,
            updated_at=updated_at,
            _configuration=_configuration,
            **kwargs,
        )
