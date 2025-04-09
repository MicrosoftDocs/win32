---
description: SRIOV settings for a network adapter.
ms.assetid: 300fcb85-de8f-4afc-b7bc-ef617dc1e405
title: MSFT\_NetAdapterSriovSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterSriovSettingData
- MSFT_NetAdapterSriovSettingData.Caption
- MSFT_NetAdapterSriovSettingData.Description
- MSFT_NetAdapterSriovSettingData.ElementName
- MSFT_NetAdapterSriovSettingData.InstanceID
- MSFT_NetAdapterSriovSettingData.Name
- MSFT_NetAdapterSriovSettingData.InterfaceDescription
- MSFT_NetAdapterSriovSettingData.Source
- MSFT_NetAdapterSriovSettingData.SystemName
- MSFT_NetAdapterSriovSettingData.Enabled
- MSFT_NetAdapterSriovSettingData.SriovSupport
- MSFT_NetAdapterSriovSettingData.HardwareCapabilities
- MSFT_NetAdapterSriovSettingData.CurrentCapabilities
- MSFT_NetAdapterSriovSettingData.SwitchType
- MSFT_NetAdapterSriovSettingData.SwitchName
- MSFT_NetAdapterSriovSettingData.NumVFs
- MSFT_NetAdapterSriovSettingData.NumAllocatedVFs
- MSFT_NetAdapterSriovSettingData.NumVPorts
- MSFT_NetAdapterSriovSettingData.NumActiveVPorts
- MSFT_NetAdapterSriovSettingData.NumQueuePairsForDefaultVPort
- MSFT_NetAdapterSriovSettingData.NumQueuePairsForNonDefaultVPorts
- MSFT_NetAdapterSriovSettingData.NumActiveDefaultVPortMacAddresses
- MSFT_NetAdapterSriovSettingData.NumActiveNonDefaultVPortMacAddresses
- MSFT_NetAdapterSriovSettingData.NumActiveDefaultVPortVlanIds
- MSFT_NetAdapterSriovSettingData.NumActiveNonDefaultVPortVlanIds
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterSriovSettingData class

SRIOV settings for a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterSriovSettingData : MSFT_NetAdapterSettingData
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  string  Name;
  string  InterfaceDescription;
  uint32  Source;
  string  SystemName;
  boolean Enabled;
  uint8   SriovSupport;
  string  HardwareCapabilities;
  string  CurrentCapabilities;
  uint16  SwitchType;
  string  SwitchName;
  uint32  NumVFs;
  uint32  NumAllocatedVFs;
  uint32  NumVPorts;
  uint32  NumActiveVPorts;
  uint32  NumQueuePairsForDefaultVPort;
  uint32  NumQueuePairsForNonDefaultVPorts;
  uint32  NumActiveDefaultVPortMacAddresses;
  uint32  NumActiveNonDefaultVPortMacAddresses;
  uint32  NumActiveDefaultVPortVlanIds;
  uint32  NumActiveNonDefaultVPortVlanIds;
};
```

## Members

The **MSFT\_NetAdapterSriovSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterSriovSettingData** class has these methods.



| Method                                                     | Description                                                      |
|:-----------------------------------------------------------|:-----------------------------------------------------------------|
| [**Disable**](disable-msft-netadaptersriovsettingdata.md) | Disables the SRIOV properties on the network adapter.<br/> |
| [**Enable**](enable-msft-netadaptersriovsettingdata.md)   | Enables the SRIOV properties on the network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterSriovSettingData** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** ( 64 )
</dt> </dl>

A short textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**CurrentCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SRIOV capabilities currently enabled on the network adapter.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property enables each instance to define a display name in addition to its key properties, identity data, and description information. Be aware that the Name property of ManagedSystemElement is also defined as a display name. However, it is often subclassed to be a Key. The same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if SRIOV is currently enabled on the Adapter.

</dd> <dt>

**HardwareCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SRIOV capabilities reported by the network adapter.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

This property inherits from [**CIM\_SettingData**](/previous-versions/windows/desktop/ipamserverpsprov/cim-settingdata).

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Interface Description, also known as "ifDesc" or display name is a unique name assigned to the network adapter during installation. This name cannot be changed and is persisted as long as the network adapter is not uninstalled. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**NumActiveDefaultVPortMacAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of active Mac addresses on the default VPort.

</dd> <dt>

**NumActiveDefaultVPortVlanIds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of active Vlan Ids on the default VPort

</dd> <dt>

**NumActiveNonDefaultVPortMacAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of active Mac addresses on the non default VPorts

</dd> <dt>

**NumActiveNonDefaultVPortVlanIds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of active Vlan Ids on the non default VPorts

</dd> <dt>

**NumActiveVPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of VPorts currently allocated on the switch

</dd> <dt>

**NumAllocatedVFs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of Virtual functions currently allocated.

</dd> <dt>

**NumQueuePairsForDefaultVPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of Queue pairs for the default VPort

</dd> <dt>

**NumQueuePairsForNonDefaultVPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of Queue pairs for the non default VPort

</dd> <dt>

**NumVFs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of Virtual functions that can be allocated on the switch

</dd> <dt>

**NumVPorts**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of VPorts that can be allocated on the switch

</dd> <dt>

**Source**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source of the setting data. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Device"></span><span id="device"></span><span id="DEVICE"></span>**Device** (2)
</dt> <dt>

<span id="Persistent_storage"></span><span id="persistent_storage"></span><span id="PERSISTENT_STORAGE"></span>**Persistent storage** (3)
</dt> </dl>

</dd> <dt>

**SriovSupport**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the SRIOV support for the device.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Supported"></span><span id="supported"></span><span id="SUPPORTED"></span>**Supported** (1)
</dt> <dt>

<span id="Missing_ACS"></span><span id="missing_acs"></span><span id="MISSING_ACS"></span>**Missing ACS** (2)
</dt> <dt>

<span id="Missing_PF_Driver"></span><span id="missing_pf_driver"></span><span id="MISSING_PF_DRIVER"></span>**Missing PF Driver** (3)
</dt> <dt>

<span id="No_bus_resources"></span><span id="no_bus_resources"></span><span id="NO_BUS_RESOURCES"></span>**No bus resources** (4)
</dt> <dt>

<span id="No_IOMMU_support"></span><span id="no_iommu_support"></span><span id="NO_IOMMU_SUPPORT"></span>**No IOMMU support** (5)
</dt> <dt>

<span id="Did_not_Get_Vf_BarSpace"></span><span id="did_not_get_vf_barspace"></span><span id="DID_NOT_GET_VF_BARSPACE"></span>**Did not Get Vf BarSpace** (6)
</dt> <dt>

<span id="No_OCS_Support"></span><span id="no_ocs_support"></span><span id="NO_OCS_SUPPORT"></span>**No OCS Support** (7)
</dt> </dl>

</dd> <dt>

**SwitchName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the switch

</dd> <dt>

**SwitchType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of the embedded switch

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="External"></span><span id="external"></span><span id="EXTERNAL"></span>**External** (1)
</dt> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping System\\'s Name. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

