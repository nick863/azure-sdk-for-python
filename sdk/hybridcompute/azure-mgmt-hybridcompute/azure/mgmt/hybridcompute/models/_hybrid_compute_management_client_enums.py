# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Property that impacts a resource's logging behavior and its connectivity with other resources
    and public networks.
    """

    ENFORCED = "enforced"
    """Indicates that resource access is controlled by the NSP definition."""
    AUDIT = "audit"
    """Dry run mode, where traffic is evaluated against NSP Rules, logged but not enforced."""
    LEARNING = "learning"
    """Enables traffic evaluation to fall back to resource-specific firewall configurations."""


class AccessRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates direction of an access rule."""

    INBOUND = "Inbound"
    """Traffic originates outside of network."""
    OUTBOUND = "Outbound"
    """Traffic originates inside the network"""


class AgentConfigurationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of configuration mode to use. Modes are pre-defined configurations of security controls,
    extension allowlists and guest configuration, maintained by Microsoft.
    """

    FULL = "full"
    MONITOR = "monitor"


class ArcKindEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc."""

    AVS = "AVS"
    HCI = "HCI"
    SCVMM = "SCVMM"
    V_MWARE = "VMware"
    EPS = "EPS"
    GCP = "GCP"
    AWS = "AWS"


class AssessmentModeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the assessment mode."""

    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class EsuEligibility(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ESU eligibility."""

    ELIGIBLE = "Eligible"
    INELIGIBLE = "Ineligible"
    UNKNOWN = "Unknown"


class EsuKeyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ESU key state."""

    INACTIVE = "Inactive"
    ACTIVE = "Active"


class EsuServerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The server types for Esu."""

    STANDARD = "Standard"
    DATACENTER = "Datacenter"


class ExecutionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Script execution status."""

    UNKNOWN = "Unknown"
    PENDING = "Pending"
    RUNNING = "Running"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    TIMED_OUT = "TimedOut"
    CANCELED = "Canceled"


class ExtensionsStatusLevelTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level code."""

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"


class LastAttemptStatusEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the status of Agent Upgrade."""

    SUCCESS = "Success"
    FAILED = "Failed"


class LicenseAssignmentState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the license assignment state (Assigned or NotAssigned)."""

    ASSIGNED = "Assigned"
    NOT_ASSIGNED = "NotAssigned"


class LicenseCoreType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the license core type (pCore or vCore)."""

    P_CORE = "pCore"
    V_CORE = "vCore"


class LicenseEdition(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the edition of the license. The values are either Standard or Datacenter."""

    STANDARD = "Standard"
    DATACENTER = "Datacenter"


class LicenseProfileProductType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The product type of the license."""

    WINDOWS_SERVER = "WindowsServer"
    WINDOWS_IO_T_ENTERPRISE = "WindowsIoTEnterprise"


class LicenseProfileSubscriptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Subscription status of the OS or Product feature."""

    UNKNOWN = "Unknown"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class LicenseProfileSubscriptionStatusUpdate(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the new subscription status of the OS or Product Features."""

    ENABLE = "Enable"
    DISABLE = "Disable"


class LicenseState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the state of the license."""

    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"


class LicenseStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The license status."""

    UNLICENSED = "Unlicensed"
    LICENSED = "Licensed"
    OOB_GRACE = "OOBGrace"
    OOT_GRACE = "OOTGrace"
    NON_GENUINE_GRACE = "NonGenuineGrace"
    NOTIFICATION = "Notification"
    EXTENDED_GRACE = "ExtendedGrace"


class LicenseTarget(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the license target server."""

    WINDOWS_SERVER2012 = "Windows Server 2012"
    WINDOWS_SERVER2012_R2 = "Windows Server 2012 R2"


class LicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the license resource."""

    ESU = "ESU"


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system type of the machine."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class PatchModeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the patch mode."""

    IMAGE_DEFAULT = "ImageDefault"
    AUTOMATIC_BY_PLATFORM = "AutomaticByPlatform"
    AUTOMATIC_BY_OS = "AutomaticByOS"
    MANUAL = "Manual"


class PatchOperationStartedBy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates if operation was triggered by user or by platform."""

    USER = "User"
    PLATFORM = "Platform"


class PatchOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The overall success or failure status of the operation. It remains "InProgress" until the
    operation completes. At that point it will become "Unknown", "Failed", "Succeeded", or
    "CompletedWithWarnings.".
    """

    UNKNOWN = "Unknown"
    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"


class PatchServiceUsed(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the patch service used for the operation."""

    UNKNOWN = "Unknown"
    WU = "WU"
    WU_WSUS = "WU_WSUS"
    YUM = "YUM"
    APT = "APT"
    ZYPPER = "Zypper"


class ProvisioningIssueSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Severity of the provisioning issue."""

    WARNING = "Warning"
    """Warnings can cause connectivity issues after provisioning succeeds."""
    ERROR = "Error"
    """Errors will cause association provisioning to fail."""


class ProvisioningIssueType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of provisioning issue."""

    MISSING_PERIMETER_CONFIGURATION = "MissingPerimeterConfiguration"
    """Perimeter configuration is missing."""
    MISSING_IDENTITY_CONFIGURATION = "MissingIdentityConfiguration"
    """Identity configuration is missing."""
    CONFIGURATION_PROPAGATION_FAILURE = "ConfigurationPropagationFailure"
    """Configuration failed to propagate."""
    OTHER = "Other"
    """Other failure."""


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state, which only appears in the response."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    ACCEPTED = "Accepted"
    CANCELED = "Canceled"
    DELETED = "Deleted"


class PublicNetworkAccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network access policy to determine if Azure Arc agents can use public Azure Arc service
    endpoints. Defaults to disabled (access to Azure Arc services only via private link).
    """

    ENABLED = "Enabled"
    """Allows Azure Arc agents to communicate with Azure Arc services over both public (internet) and
    private endpoints."""
    DISABLED = "Disabled"
    """Does not allow Azure Arc agents to communicate with Azure Arc services over public (internet)
    endpoints. The agents must use the private link."""


class StatusLevelTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level code."""

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"


class StatusTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the hybrid machine agent."""

    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    ERROR = "Error"


class VMGuestPatchClassificationLinux(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VMGuestPatchClassificationLinux."""

    CRITICAL = "Critical"
    SECURITY = "Security"
    OTHER = "Other"


class VMGuestPatchClassificationWindows(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VMGuestPatchClassificationWindows."""

    CRITICAL = "Critical"
    SECURITY = "Security"
    UPDATE_ROLL_UP = "UpdateRollUp"
    FEATURE_PACK = "FeaturePack"
    SERVICE_PACK = "ServicePack"
    DEFINITION = "Definition"
    TOOLS = "Tools"
    UPDATES = "Updates"


class VMGuestPatchRebootSetting(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines when it is acceptable to reboot a VM during a software update operation."""

    IF_REQUIRED = "IfRequired"
    NEVER = "Never"
    ALWAYS = "Always"


class VMGuestPatchRebootStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reboot state of the VM following completion of the operation."""

    UNKNOWN = "Unknown"
    NOT_NEEDED = "NotNeeded"
    REQUIRED = "Required"
    STARTED = "Started"
    FAILED = "Failed"
    COMPLETED = "Completed"
