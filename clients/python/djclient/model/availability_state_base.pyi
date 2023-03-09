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


class AvailabilityStateBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An availability state base
    """


    class MetaOapg:
        required = {
            "catalog",
            "max_partition",
            "min_partition",
            "table",
            "valid_through_ts",
        }
        
        class properties:
            catalog = schemas.StrSchema
            table = schemas.StrSchema
            valid_through_ts = schemas.IntSchema
            
            
            class max_partition(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'max_partition':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class min_partition(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'min_partition':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            schema_ = schemas.StrSchema
            __annotations__ = {
                "catalog": catalog,
                "table": table,
                "valid_through_ts": valid_through_ts,
                "max_partition": max_partition,
                "min_partition": min_partition,
                "schema_": schema_,
            }
    
    catalog: MetaOapg.properties.catalog
    max_partition: MetaOapg.properties.max_partition
    min_partition: MetaOapg.properties.min_partition
    table: MetaOapg.properties.table
    valid_through_ts: MetaOapg.properties.valid_through_ts
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["catalog"]) -> MetaOapg.properties.catalog: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["table"]) -> MetaOapg.properties.table: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["valid_through_ts"]) -> MetaOapg.properties.valid_through_ts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_partition"]) -> MetaOapg.properties.max_partition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min_partition"]) -> MetaOapg.properties.min_partition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_"]) -> MetaOapg.properties.schema_: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["catalog", "table", "valid_through_ts", "max_partition", "min_partition", "schema_", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["catalog"]) -> MetaOapg.properties.catalog: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["table"]) -> MetaOapg.properties.table: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["valid_through_ts"]) -> MetaOapg.properties.valid_through_ts: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_partition"]) -> MetaOapg.properties.max_partition: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min_partition"]) -> MetaOapg.properties.min_partition: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_"]) -> typing.Union[MetaOapg.properties.schema_, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["catalog", "table", "valid_through_ts", "max_partition", "min_partition", "schema_", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        catalog: typing.Union[MetaOapg.properties.catalog, str, ],
        max_partition: typing.Union[MetaOapg.properties.max_partition, list, tuple, ],
        min_partition: typing.Union[MetaOapg.properties.min_partition, list, tuple, ],
        table: typing.Union[MetaOapg.properties.table, str, ],
        valid_through_ts: typing.Union[MetaOapg.properties.valid_through_ts, decimal.Decimal, int, ],
        schema_: typing.Union[MetaOapg.properties.schema_, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AvailabilityStateBase':
        return super().__new__(
            cls,
            *_args,
            catalog=catalog,
            max_partition=max_partition,
            min_partition=min_partition,
            table=table,
            valid_through_ts=valid_through_ts,
            schema_=schema_,
            _configuration=_configuration,
            **kwargs,
        )
