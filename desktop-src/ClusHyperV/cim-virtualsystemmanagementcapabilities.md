---
title: CIM\_VirtualSystemManagementCapabilities class
description: Represents the capabilities of a CIM\_VirtualSystemManagementService object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd680a3b8-b83b-4e59-a330-9fb3a24c43f9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_VirtualSystemManagementCapabilities class", "CIM_VirtualSystemManagementCapabilities class, described"]
topic_type:
- apiref
api_name:
- CIM_VirtualSystemManagementCapabilities
- CIM_VirtualSystemManagementCapabilities.Caption
- CIM_VirtualSystemManagementCapabilities.Description
- CIM_VirtualSystemManagementCapabilities.InstanceID
- CIM_VirtualSystemManagementCapabilities.ElementName
- CIM_VirtualSystemManagementCapabilities.ElementNameEditSupported
- CIM_VirtualSystemManagementCapabilities.MaxElementNameLen
- CIM_VirtualSystemManagementCapabilities.RequestedStatesSupported
- CIM_VirtualSystemManagementCapabilities.ElementNameMask
- CIM_VirtualSystemManagementCapabilities.VirtualSystemTypesSupported
- CIM_VirtualSystemManagementCapabilities.SynchronousMethodsSupported
- CIM_VirtualSystemManagementCapabilities.AsynchronousMethodsSupported
- CIM_VirtualSystemManagementCapabilities.IndicationsSupported
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_VirtualSystemManagementCapabilities class

Represents the capabilities of a [**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md) object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.23.0"), UMLPackagePath("CIM::Core::Virtualization")]
class CIM_VirtualSystemManagementCapabilities : CIM_EnabledLogicalElementCapabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean ElementNameEditSupported;
  uint16  MaxElementNameLen;
  uint16  RequestedStatesSupported[];
  string  ElementNameMask;
  string  VirtualSystemTypesSupported[];
  uint16  SynchronousMethodsSupported[];
  uint16  AsynchronousMethodsSupported[];
  uint16  IndicationsSupported[];
};
```

## Members

The **CIM\_VirtualSystemManagementCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_VirtualSystemManagementCapabilities** class has these properties.

<dl> <dt>

**AsynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains method names for the [**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md) class methods that are supported for asynchronous operations.

The possible values are.

<dt>

<span id="DefineSystemSupported"></span><span id="definesystemsupported"></span><span id="DEFINESYSTEMSUPPORTED"></span>

**DefineSystemSupported** (2)


</dt> <dd></dd> <dt>

<span id="DestroySystemSupported"></span><span id="destroysystemsupported"></span><span id="DESTROYSYSTEMSUPPORTED"></span>

**DestroySystemSupported** (3)


</dt> <dd></dd> <dt>

<span id="DestroySystemConfigurationSupported"></span><span id="destroysystemconfigurationsupported"></span><span id="DESTROYSYSTEMCONFIGURATIONSUPPORTED"></span>

**DestroySystemConfigurationSupported** (4)


</dt> <dd></dd> <dt>

<span id="ModifyResourceSettingsSupported"></span><span id="modifyresourcesettingssupported"></span><span id="MODIFYRESOURCESETTINGSSUPPORTED"></span>

**ModifyResourceSettingsSupported** (5)


</dt> <dd></dd> <dt>

<span id="ModifySystemSettingsSupported"></span><span id="modifysystemsettingssupported"></span><span id="MODIFYSYSTEMSETTINGSSUPPORTED"></span>

**ModifySystemSettingsSupported** (6)


</dt> <dd></dd> <dt>

<span id="RemoveResourcesSupported"></span><span id="removeresourcessupported"></span><span id="REMOVERESOURCESSUPPORTED"></span>

**RemoveResourcesSupported** (7)


</dt> <dd></dd> <dt>

<span id="SelectSystemConfigurationSupported"></span><span id="selectsystemconfigurationsupported"></span><span id="SELECTSYSTEMCONFIGURATIONSUPPORTED"></span>

**SelectSystemConfigurationSupported** (8)


</dt> <dd></dd> <dt>

<span id="SnapshotSystemSupported"></span><span id="snapshotsystemsupported"></span><span id="SNAPSHOTSYSTEMSUPPORTED"></span>

**SnapshotSystemSupported** (9)


</dt> <dd></dd> <dt>

<span id="AddResourcesSupported"></span><span id="addresourcessupported"></span><span id="ADDRESOURCESSUPPORTED"></span>

**AddResourcesSupported** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11–23766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767–65535</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this class instance. In addition, the user friendly name can be used as a index property for a query. This value does not have to be unique within its namespace.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**ElementNameEditSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_UNIT\_CONFIG\_CAPS\_T\|EditName"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ManagedElement**](cim-managedelement.md).**ElementName**")
</dt> </dl>

**true** if the **ElementName** property of the enabled logical element can be modified; otherwise, **false**.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**ElementNameMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).**MaxElementNameLen**")
</dt> </dl>

A regular expression that indicates the restrictions on the **ElementName** property of the enable logical element. See *DMTF standard ABNF with the Management Profile Specification Usage Guide*, appendix C for the permitted syntax.

> [!Note]  
> If this property and the **ElementNameMask** property of the enable logical element describe the maximum length of **ElementName**, the smaller value is used.

 

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**IndicationsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the supported indications types of the implementation.

The possible values are.

<dt>

<span id="VirtualResourceStateChangeIndicationsSupported"></span><span id="virtualresourcestatechangeindicationssupported"></span><span id="VIRTUALRESOURCESTATECHANGEINDICATIONSSUPPORTED"></span>

**VirtualResourceStateChangeIndicationsSupported** (2)


</dt> <dd></dd> <dt>

<span id="ConcreteJobStateChangeIndicationsSupported"></span><span id="concretejobstatechangeindicationssupported"></span><span id="CONCRETEJOBSTATECHANGEINDICATIONSSUPPORTED"></span>

**ConcreteJobStateChangeIndicationsSupported** (3)


</dt> <dd></dd> <dt>

<span id="VirtualSystemStateChangeIndicationsSupported"></span><span id="virtualsystemstatechangeindicationssupported"></span><span id="VIRTUALSYSTEMSTATECHANGEINDICATIONSSUPPORTED"></span>

**VirtualSystemStateChangeIndicationsSupported** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–23766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767–65535</dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**MaxElementNameLen**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("FC-SWAPI.INCITS-T11\|SWAPI\_UNIT\_CONFIG\_CAPS\_T\|MaxNameChars"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_FCSwitchCapabilities.ElementNameEditSupported", "[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).**ElementNameMask**")
</dt> </dl>

The maximum supported length of the **ElementName** property of the enabled logical element.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

</dd> <dt>

**RequestedStatesSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md).**RequestStateChange**")
</dt> </dl>

The possible states that can be requested on the enabled logical element by the [**RequestStateChange**](cim-enabledlogicalelement-requeststatechange.md) method.

This property is inherited from [**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md).

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>

**Defer** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> </dl>

</dd> <dt>

**SynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains method names for the [**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md) class methods that are supported for synchronous operations.

The possible values are.

<dt>

<span id="DefineSystemSupported"></span><span id="definesystemsupported"></span><span id="DEFINESYSTEMSUPPORTED"></span>

**DefineSystemSupported** (2)


</dt> <dd></dd> <dt>

<span id="DestroySystemSupported"></span><span id="destroysystemsupported"></span><span id="DESTROYSYSTEMSUPPORTED"></span>

**DestroySystemSupported** (3)


</dt> <dd></dd> <dt>

<span id="DestroySystemConfigurationSupported"></span><span id="destroysystemconfigurationsupported"></span><span id="DESTROYSYSTEMCONFIGURATIONSUPPORTED"></span>

**DestroySystemConfigurationSupported** (4)


</dt> <dd></dd> <dt>

<span id="ModifyResourceSettingsSupported"></span><span id="modifyresourcesettingssupported"></span><span id="MODIFYRESOURCESETTINGSSUPPORTED"></span>

**ModifyResourceSettingsSupported** (5)


</dt> <dd></dd> <dt>

<span id="ModifySystemSettingsSupported"></span><span id="modifysystemsettingssupported"></span><span id="MODIFYSYSTEMSETTINGSSUPPORTED"></span>

**ModifySystemSettingsSupported** (6)


</dt> <dd></dd> <dt>

<span id="RemoveResourcesSupported"></span><span id="removeresourcessupported"></span><span id="REMOVERESOURCESSUPPORTED"></span>

**RemoveResourcesSupported** (7)


</dt> <dd></dd> <dt>

<span id="SelectSystemConfigurationSupported"></span><span id="selectsystemconfigurationsupported"></span><span id="SELECTSYSTEMCONFIGURATIONSUPPORTED"></span>

**SelectSystemConfigurationSupported** (8)


</dt> <dd></dd> <dt>

<span id="SnapshotSystemSupported"></span><span id="snapshotsystemsupported"></span><span id="SNAPSHOTSYSTEMSUPPORTED"></span>

**SnapshotSystemSupported** (9)


</dt> <dd></dd> <dt>

<span id="AddResourcesSupported"></span><span id="addresourcessupported"></span><span id="ADDRESOURCESSUPPORTED"></span>

**AddResourcesSupported** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11–23766</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32767–65535</dd> </dl>

</dd> <dt>

**VirtualSystemTypesSupported**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md).**VirtualSystemType**")
</dt> </dl>

The type of virtual systems supported by the implementation.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





