---
description: Network adapter Virtual Port settings.
ms.assetid: 0d9f368c-deb8-45aa-9cb7-492eb853be39
title: MSFT\_NetAdapterVPortSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterVPortSettingData
- MSFT_NetAdapterVPortSettingData.Caption
- MSFT_NetAdapterVPortSettingData.Description
- MSFT_NetAdapterVPortSettingData.ElementName
- MSFT_NetAdapterVPortSettingData.InstanceID
- MSFT_NetAdapterVPortSettingData.Name
- MSFT_NetAdapterVPortSettingData.InterfaceDescription
- MSFT_NetAdapterVPortSettingData.Source
- MSFT_NetAdapterVPortSettingData.SystemName
- MSFT_NetAdapterVPortSettingData.VPortID
- MSFT_NetAdapterVPortSettingData.VPortName
- MSFT_NetAdapterVPortSettingData.SwitchID
- MSFT_NetAdapterVPortSettingData.FunctionID
- MSFT_NetAdapterVPortSettingData.NumQueuePairs
- MSFT_NetAdapterVPortSettingData.InterruptModeration
- MSFT_NetAdapterVPortSettingData.VPortState
- MSFT_NetAdapterVPortSettingData.ProcessorAffinityMask
- MSFT_NetAdapterVPortSettingData.ProcessorGroup
- MSFT_NetAdapterVPortSettingData.NumFilters
- MSFT_NetAdapterVPortSettingData.FilterList
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterVPortSettingData class

Network adapter Virtual Port settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterVPortSettingData : MSFT_NetAdapterSettingData
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  string Name;
  string InterfaceDescription;
  uint32 Source;
  string SystemName;
  uint32 VPortID;
  string VPortName;
  uint32 SwitchID;
  uint16 FunctionID;
  uint32 NumQueuePairs;
  uint32 InterruptModeration;
  uint32 VPortState;
  uint64 ProcessorAffinityMask;
  uint16 ProcessorGroup;
  uint32 NumFilters;
  string FilterList[];
};
```

## Members

The **MSFT\_NetAdapterVPortSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterVPortSettingData** class has these properties.

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

**FilterList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of MAC address and VLAN ID pair filters set on the VPort.

</dd> <dt>

**FunctionID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the attached function. This could be the Vf or the PF ID.

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

**InterruptModeration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The interrupt moderation for the VPort.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Adaptive"></span><span id="adaptive"></span><span id="ADAPTIVE"></span>**Adaptive** (1)
</dt> <dt>

<span id="Off"></span><span id="off"></span><span id="OFF"></span>**Off** (2)
</dt> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>**Low** (100)
</dt> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>**Medium** (200)
</dt> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>**High** (300)
</dt> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**NumFilters**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of MAC address and VLAN ID filters set on the queue.

</dd> <dt>

**NumQueuePairs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queue pairs.

</dd> <dt>

**ProcessorAffinityMask**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A bitmap that specifies the CPU that the queue has affinity with. For example, setting bit 0 indicates CPU 0 is used, setting bit 1 indicates CPU 1 is used, and so on.

</dd> <dt>

**ProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group number for the processors specified in **ProcessorAffinityMask** property.

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

**SwitchID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier of the switch.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping System\\'s Name. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**VPortID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the VPort.

</dd> <dt>

**VPortName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the VPort.

</dd> <dt>

**VPortState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the VPort.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Activated"></span><span id="activated"></span><span id="ACTIVATED"></span>**Activated** (1)
</dt> <dt>

<span id="DeActivated"></span><span id="deactivated"></span><span id="DEACTIVATED"></span>**DeActivated** (2)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

