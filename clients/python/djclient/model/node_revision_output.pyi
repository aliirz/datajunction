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


class NodeRevisionOutput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Output for a node revision with information about columns and if it is a metric.
    """


    class MetaOapg:
        required = {
            "mode",
            "node_revision_id",
            "tables",
            "updated_at",
            "columns",
            "name",
            "display_name",
            "type",
            "version",
            "materialization_configs",
            "node_id",
            "status",
        }
        
        class properties:
            node_revision_id = schemas.IntSchema
            node_id = schemas.IntSchema
        
            @staticmethod
            def type() -> typing.Type['NodeType']:
                return NodeType
            name = schemas.StrSchema
            display_name = schemas.StrSchema
            version = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['NodeStatus']:
                return NodeStatus
        
            @staticmethod
            def mode() -> typing.Type['NodeMode']:
                return NodeMode
            
            
            class columns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ColumnOutput']:
                        return ColumnOutput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ColumnOutput'], typing.List['ColumnOutput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ColumnOutput':
                    return super().__getitem__(i)
            
            
            class tables(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TableOutput']:
                        return TableOutput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TableOutput'], typing.List['TableOutput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tables':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TableOutput':
                    return super().__getitem__(i)
            updated_at = schemas.DateTimeSchema
            
            
            class materialization_configs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MaterializationConfigOutput']:
                        return MaterializationConfigOutput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['MaterializationConfigOutput'], typing.List['MaterializationConfigOutput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'materialization_configs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MaterializationConfigOutput':
                    return super().__getitem__(i)
            description = schemas.StrSchema
            query = schemas.StrSchema
        
            @staticmethod
            def availability() -> typing.Type['AvailabilityState']:
                return AvailabilityState
            __annotations__ = {
                "node_revision_id": node_revision_id,
                "node_id": node_id,
                "type": type,
                "name": name,
                "display_name": display_name,
                "version": version,
                "status": status,
                "mode": mode,
                "columns": columns,
                "tables": tables,
                "updated_at": updated_at,
                "materialization_configs": materialization_configs,
                "description": description,
                "query": query,
                "availability": availability,
            }
    
    mode: 'NodeMode'
    node_revision_id: MetaOapg.properties.node_revision_id
    tables: MetaOapg.properties.tables
    updated_at: MetaOapg.properties.updated_at
    columns: MetaOapg.properties.columns
    name: MetaOapg.properties.name
    display_name: MetaOapg.properties.display_name
    type: 'NodeType'
    version: MetaOapg.properties.version
    materialization_configs: MetaOapg.properties.materialization_configs
    node_id: MetaOapg.properties.node_id
    status: 'NodeStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_revision_id"]) -> MetaOapg.properties.node_revision_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'NodeStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> 'NodeMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tables"]) -> MetaOapg.properties.tables: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["materialization_configs"]) -> MetaOapg.properties.materialization_configs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availability"]) -> 'AvailabilityState': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["node_revision_id", "node_id", "type", "name", "display_name", "version", "status", "mode", "columns", "tables", "updated_at", "materialization_configs", "description", "query", "availability", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_revision_id"]) -> MetaOapg.properties.node_revision_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_id"]) -> MetaOapg.properties.node_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'NodeStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> 'NodeMode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tables"]) -> MetaOapg.properties.tables: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["materialization_configs"]) -> MetaOapg.properties.materialization_configs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availability"]) -> typing.Union['AvailabilityState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["node_revision_id", "node_id", "type", "name", "display_name", "version", "status", "mode", "columns", "tables", "updated_at", "materialization_configs", "description", "query", "availability", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mode: 'NodeMode',
        node_revision_id: typing.Union[MetaOapg.properties.node_revision_id, decimal.Decimal, int, ],
        tables: typing.Union[MetaOapg.properties.tables, list, tuple, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        display_name: typing.Union[MetaOapg.properties.display_name, str, ],
        type: 'NodeType',
        version: typing.Union[MetaOapg.properties.version, str, ],
        materialization_configs: typing.Union[MetaOapg.properties.materialization_configs, list, tuple, ],
        node_id: typing.Union[MetaOapg.properties.node_id, decimal.Decimal, int, ],
        status: 'NodeStatus',
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        availability: typing.Union['AvailabilityState', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeRevisionOutput':
        return super().__new__(
            cls,
            *_args,
            mode=mode,
            node_revision_id=node_revision_id,
            tables=tables,
            updated_at=updated_at,
            columns=columns,
            name=name,
            display_name=display_name,
            type=type,
            version=version,
            materialization_configs=materialization_configs,
            node_id=node_id,
            status=status,
            description=description,
            query=query,
            availability=availability,
            _configuration=_configuration,
            **kwargs,
        )

from djclient.model.availability_state import AvailabilityState
from djclient.model.column_output import ColumnOutput
from djclient.model.materialization_config_output import MaterializationConfigOutput
from djclient.model.node_mode import NodeMode
from djclient.model.node_status import NodeStatus
from djclient.model.node_type import NodeType
from djclient.model.table_output import TableOutput
