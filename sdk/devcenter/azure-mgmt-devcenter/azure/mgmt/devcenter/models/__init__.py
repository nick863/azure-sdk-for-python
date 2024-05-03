# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AllowedEnvironmentType
from ._models_py3 import AllowedEnvironmentTypeListResult
from ._models_py3 import AttachedNetworkConnection
from ._models_py3 import AttachedNetworkListResult
from ._models_py3 import Capability
from ._models_py3 import Catalog
from ._models_py3 import CatalogConflictError
from ._models_py3 import CatalogErrorDetails
from ._models_py3 import CatalogListResult
from ._models_py3 import CatalogProperties
from ._models_py3 import CatalogResourceValidationErrorDetails
from ._models_py3 import CatalogSyncError
from ._models_py3 import CatalogUpdate
from ._models_py3 import CatalogUpdateProperties
from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import CheckScopedNameAvailabilityRequest
from ._models_py3 import CustomerManagedKeyEncryption
from ._models_py3 import CustomerManagedKeyEncryptionKeyIdentity
from ._models_py3 import DevBoxDefinition
from ._models_py3 import DevBoxDefinitionListResult
from ._models_py3 import DevBoxDefinitionProperties
from ._models_py3 import DevBoxDefinitionUpdate
from ._models_py3 import DevBoxDefinitionUpdateProperties
from ._models_py3 import DevCenter
from ._models_py3 import DevCenterListResult
from ._models_py3 import DevCenterProjectCatalogSettings
from ._models_py3 import DevCenterProperties
from ._models_py3 import DevCenterSku
from ._models_py3 import DevCenterUpdate
from ._models_py3 import DevCenterUpdateProperties
from ._models_py3 import Encryption
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import EnvironmentDefinition
from ._models_py3 import EnvironmentDefinitionListResult
from ._models_py3 import EnvironmentDefinitionParameter
from ._models_py3 import EnvironmentRole
from ._models_py3 import EnvironmentType
from ._models_py3 import EnvironmentTypeListResult
from ._models_py3 import EnvironmentTypeProperties
from ._models_py3 import EnvironmentTypeUpdate
from ._models_py3 import EnvironmentTypeUpdateProperties
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Gallery
from ._models_py3 import GalleryListResult
from ._models_py3 import GitCatalog
from ._models_py3 import HealthCheck
from ._models_py3 import HealthCheckStatusDetails
from ._models_py3 import HealthCheckStatusDetailsListResult
from ._models_py3 import HealthStatusDetail
from ._models_py3 import Image
from ._models_py3 import ImageListResult
from ._models_py3 import ImageReference
from ._models_py3 import ImageValidationErrorDetails
from ._models_py3 import ImageVersion
from ._models_py3 import ImageVersionListResult
from ._models_py3 import ListUsagesResult
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import NetworkConnection
from ._models_py3 import NetworkConnectionListResult
from ._models_py3 import NetworkConnectionUpdate
from ._models_py3 import NetworkConnectionUpdateProperties
from ._models_py3 import NetworkProperties
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationStatus
from ._models_py3 import OperationStatusResult
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import OutboundEnvironmentEndpointCollection
from ._models_py3 import Pool
from ._models_py3 import PoolListResult
from ._models_py3 import PoolProperties
from ._models_py3 import PoolUpdate
from ._models_py3 import PoolUpdateProperties
from ._models_py3 import Project
from ._models_py3 import ProjectCatalogSettings
from ._models_py3 import ProjectEnvironmentType
from ._models_py3 import ProjectEnvironmentTypeListResult
from ._models_py3 import ProjectEnvironmentTypeProperties
from ._models_py3 import ProjectEnvironmentTypeUpdate
from ._models_py3 import ProjectEnvironmentTypeUpdateProperties
from ._models_py3 import ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignment
from ._models_py3 import ProjectListResult
from ._models_py3 import ProjectProperties
from ._models_py3 import ProjectUpdate
from ._models_py3 import ProjectUpdateProperties
from ._models_py3 import ProxyResource
from ._models_py3 import RecommendedMachineConfiguration
from ._models_py3 import Resource
from ._models_py3 import ResourceRange
from ._models_py3 import Schedule
from ._models_py3 import ScheduleListResult
from ._models_py3 import ScheduleProperties
from ._models_py3 import ScheduleUpdate
from ._models_py3 import ScheduleUpdateProperties
from ._models_py3 import Sku
from ._models_py3 import SkuListResult
from ._models_py3 import StopOnDisconnectConfiguration
from ._models_py3 import SyncErrorDetails
from ._models_py3 import SyncStats
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import TrackedResourceUpdate
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import UserRoleAssignmentValue

from ._dev_center_mgmt_client_enums import ActionType
from ._dev_center_mgmt_client_enums import CatalogConnectionState
from ._dev_center_mgmt_client_enums import CatalogItemSyncEnableStatus
from ._dev_center_mgmt_client_enums import CatalogItemType
from ._dev_center_mgmt_client_enums import CatalogResourceValidationStatus
from ._dev_center_mgmt_client_enums import CatalogSyncState
from ._dev_center_mgmt_client_enums import CatalogSyncType
from ._dev_center_mgmt_client_enums import CheckNameAvailabilityReason
from ._dev_center_mgmt_client_enums import CreatedByType
from ._dev_center_mgmt_client_enums import DomainJoinType
from ._dev_center_mgmt_client_enums import EnvironmentTypeEnableStatus
from ._dev_center_mgmt_client_enums import HealthCheckStatus
from ._dev_center_mgmt_client_enums import HealthStatus
from ._dev_center_mgmt_client_enums import HibernateSupport
from ._dev_center_mgmt_client_enums import IdentityType
from ._dev_center_mgmt_client_enums import ImageValidationStatus
from ._dev_center_mgmt_client_enums import LicenseType
from ._dev_center_mgmt_client_enums import LocalAdminStatus
from ._dev_center_mgmt_client_enums import ManagedServiceIdentityType
from ._dev_center_mgmt_client_enums import Origin
from ._dev_center_mgmt_client_enums import ParameterType
from ._dev_center_mgmt_client_enums import ProvisioningState
from ._dev_center_mgmt_client_enums import ScheduleEnableStatus
from ._dev_center_mgmt_client_enums import ScheduledFrequency
from ._dev_center_mgmt_client_enums import ScheduledType
from ._dev_center_mgmt_client_enums import SingleSignOnStatus
from ._dev_center_mgmt_client_enums import SkuTier
from ._dev_center_mgmt_client_enums import StopOnDisconnectEnableStatus
from ._dev_center_mgmt_client_enums import UsageUnit
from ._dev_center_mgmt_client_enums import VirtualNetworkType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AllowedEnvironmentType",
    "AllowedEnvironmentTypeListResult",
    "AttachedNetworkConnection",
    "AttachedNetworkListResult",
    "Capability",
    "Catalog",
    "CatalogConflictError",
    "CatalogErrorDetails",
    "CatalogListResult",
    "CatalogProperties",
    "CatalogResourceValidationErrorDetails",
    "CatalogSyncError",
    "CatalogUpdate",
    "CatalogUpdateProperties",
    "CheckNameAvailabilityRequest",
    "CheckNameAvailabilityResponse",
    "CheckScopedNameAvailabilityRequest",
    "CustomerManagedKeyEncryption",
    "CustomerManagedKeyEncryptionKeyIdentity",
    "DevBoxDefinition",
    "DevBoxDefinitionListResult",
    "DevBoxDefinitionProperties",
    "DevBoxDefinitionUpdate",
    "DevBoxDefinitionUpdateProperties",
    "DevCenter",
    "DevCenterListResult",
    "DevCenterProjectCatalogSettings",
    "DevCenterProperties",
    "DevCenterSku",
    "DevCenterUpdate",
    "DevCenterUpdateProperties",
    "Encryption",
    "EndpointDependency",
    "EndpointDetail",
    "EnvironmentDefinition",
    "EnvironmentDefinitionListResult",
    "EnvironmentDefinitionParameter",
    "EnvironmentRole",
    "EnvironmentType",
    "EnvironmentTypeListResult",
    "EnvironmentTypeProperties",
    "EnvironmentTypeUpdate",
    "EnvironmentTypeUpdateProperties",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Gallery",
    "GalleryListResult",
    "GitCatalog",
    "HealthCheck",
    "HealthCheckStatusDetails",
    "HealthCheckStatusDetailsListResult",
    "HealthStatusDetail",
    "Image",
    "ImageListResult",
    "ImageReference",
    "ImageValidationErrorDetails",
    "ImageVersion",
    "ImageVersionListResult",
    "ListUsagesResult",
    "ManagedServiceIdentity",
    "NetworkConnection",
    "NetworkConnectionListResult",
    "NetworkConnectionUpdate",
    "NetworkConnectionUpdateProperties",
    "NetworkProperties",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationStatus",
    "OperationStatusResult",
    "OutboundEnvironmentEndpoint",
    "OutboundEnvironmentEndpointCollection",
    "Pool",
    "PoolListResult",
    "PoolProperties",
    "PoolUpdate",
    "PoolUpdateProperties",
    "Project",
    "ProjectCatalogSettings",
    "ProjectEnvironmentType",
    "ProjectEnvironmentTypeListResult",
    "ProjectEnvironmentTypeProperties",
    "ProjectEnvironmentTypeUpdate",
    "ProjectEnvironmentTypeUpdateProperties",
    "ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignment",
    "ProjectListResult",
    "ProjectProperties",
    "ProjectUpdate",
    "ProjectUpdateProperties",
    "ProxyResource",
    "RecommendedMachineConfiguration",
    "Resource",
    "ResourceRange",
    "Schedule",
    "ScheduleListResult",
    "ScheduleProperties",
    "ScheduleUpdate",
    "ScheduleUpdateProperties",
    "Sku",
    "SkuListResult",
    "StopOnDisconnectConfiguration",
    "SyncErrorDetails",
    "SyncStats",
    "SystemData",
    "TrackedResource",
    "TrackedResourceUpdate",
    "Usage",
    "UsageName",
    "UserAssignedIdentity",
    "UserRoleAssignmentValue",
    "ActionType",
    "CatalogConnectionState",
    "CatalogItemSyncEnableStatus",
    "CatalogItemType",
    "CatalogResourceValidationStatus",
    "CatalogSyncState",
    "CatalogSyncType",
    "CheckNameAvailabilityReason",
    "CreatedByType",
    "DomainJoinType",
    "EnvironmentTypeEnableStatus",
    "HealthCheckStatus",
    "HealthStatus",
    "HibernateSupport",
    "IdentityType",
    "ImageValidationStatus",
    "LicenseType",
    "LocalAdminStatus",
    "ManagedServiceIdentityType",
    "Origin",
    "ParameterType",
    "ProvisioningState",
    "ScheduleEnableStatus",
    "ScheduledFrequency",
    "ScheduledType",
    "SingleSignOnStatus",
    "SkuTier",
    "StopOnDisconnectEnableStatus",
    "UsageUnit",
    "VirtualNetworkType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
