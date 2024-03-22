# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRights(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines values for AccessRights."""

    MANAGE = "Manage"
    SEND = "Send"
    LISTEN = "Listen"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class NamespaceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Namespace status."""

    CREATED = "Created"
    CREATING = "Creating"
    SUSPENDED = "Suspended"
    DELETING = "Deleting"


class NamespaceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines values for NamespaceType."""

    MESSAGING = "Messaging"
    NOTIFICATION_HUB = "NotificationHub"


class OperationProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines values for OperationProvisioningState."""

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PENDING = "Pending"
    DISABLED = "Disabled"


class PolicyKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Shared Access Policy Key (primary or secondary)."""

    PRIMARY_KEY = "PrimaryKey"
    SECONDARY_KEY = "SecondaryKey"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of Private Endpoint Connection."""

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    UPDATING = "Updating"
    UPDATING_BY_PROXY = "UpdatingByProxy"
    DELETING = "Deleting"
    DELETING_BY_PROXY = "DeletingByProxy"
    DELETED = "Deleted"


class PrivateLinkConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of Private Link Connection."""

    DISCONNECTED = "Disconnected"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of public network access."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ReplicationRegion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allowed replication region."""

    DEFAULT = "Default"
    WEST_US2 = "WestUs2"
    NORTH_EUROPE = "NorthEurope"
    AUSTRALIA_EAST = "AustraliaEast"
    BRAZIL_SOUTH = "BrazilSouth"
    SOUTH_EAST_ASIA = "SouthEastAsia"
    SOUTH_AFRICA_NORTH = "SouthAfricaNorth"
    NONE = "None"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Namespace SKU name."""

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"


class ZoneRedundancyPreference(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Namespace SKU name."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"
