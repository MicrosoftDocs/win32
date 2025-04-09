---
description: Network adapter VMQ settings for each queue.
ms.assetid: 22b55552-dbd8-4d36-b049-761a3a5cb3ef
title: MSFT\_NetAdapterVmqQueueSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterVmqQueueSettingData
- MSFT_NetAdapterVmqQueueSettingData.Caption
- MSFT_NetAdapterVmqQueueSettingData.Description
- MSFT_NetAdapterVmqQueueSettingData.ElementName
- MSFT_NetAdapterVmqQueueSettingData.InstanceID
- MSFT_NetAdapterVmqQueueSettingData.Name
- MSFT_NetAdapterVmqQueueSettingData.InterfaceDescription
- MSFT_NetAdapterVmqQueueSettingData.Source
- MSFT_NetAdapterVmqQueueSettingData.SystemName
- MSFT_NetAdapterVmqQueueSettingData.IsDefault
- MSFT_NetAdapterVmqQueueSettingData.IsCurrent
- MSFT_NetAdapterVmqQueueSettingData.IsNext
- MSFT_NetAdapterVmqQueueSettingData.IsMinimum
- MSFT_NetAdapterVmqQueueSettingData.IsMaximum
- MSFT_NetAdapterVmqQueueSettingData.ManagedElement
- MSFT_NetAdapterVmqQueueSettingData.SettingData
- MSFT_NetAdapterVmqQueueSettingData.QueueID
- MSFT_NetAdapterVmqQueueSettingData.State
- MSFT_NetAdapterVmqQueueSettingData.NumFilters
- MSFT_NetAdapterVmqQueueSettingData.ProcessorAffinityMask
- MSFT_NetAdapterVmqQueueSettingData.ProcessorGroup
- MSFT_NetAdapterVmqQueueSettingData.VmID
- MSFT_NetAdapterVmqQueueSettingData.VmFriendlyName
- MSFT_NetAdapterVmqQueueSettingData.QueueName
- MSFT_NetAdapterVmqQueueSettingData.FilterList
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterVmqQueueSettingData class

Network adapter VMQ settings for each queue

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterVmqQueueSettingData : MSFT_NetAdapterSettingData
{
  string                         Caption;
  string                         Description;
  string                         ElementName;
  string                         InstanceID;
  string                         Name;
  string                         InterfaceDescription;
  uint32                         Source;
  string                         SystemName;
  uint16                     REF IsDefault;
  uint16                     REF IsCurrent;
  uint16                     REF IsNext;
  uint16                     REF IsMinimum = 0;
  uint16                     REF IsMaximum = 0;
  MSFT_NetAdapter            REF ManagedElement;
  MSFT_NetAdapterSettingData REF SettingData;
  uint32                         QueueID;
  uint32                         State;
  uint32                         NumFilters;
  uint64                         ProcessorAffinityMask;
  uint16                         ProcessorGroup;
  string                         VmID;
  string                         VmFriendlyName;
  string                         QueueName;
  string                         FilterList[];
};
```

## Members

The **MSFT\_NetAdapterVmqQueueSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterVmqQueueSettingData** class has these methods.



| Method                                                                                  | Description                                                  |
|:----------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| [**GetByInstanceID**](/previous-versions//hh872313(v=vs.85)) | Gets a list of VMQ queues of the network adapter.<br/> |
| [**GetByName**](/previous-versions//hh872319(v=vs.85))             | Gets a list of VMQ queues of the network adapter.<br/> |



 

### Properties

The **MSFT\_NetAdapterVmqQueueSettingData** class has these properties.

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

An array of MAC address and VLAN ID pair filters set on the queue.

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

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is currently used in the operation of the element or that this information is unknown. For a given managed element and all instances of a setting data subclass, there shall be at most one instance of ElementSettingData which references the managed element and an instance of the SettingData subclass where there is a specified non-null, non-key property of the SettingData subclass, and the IsMaximum property on the referencing ElementSettingData instance has a value of "Is Maximum" or the IsMinimum property on the referencing ElementSettingData instance has a value of "Is Minimum" and the IsCurrent property on the referencing ElementSettingData instance has a value of "Is Current".

There shall be at most one instance of ElementSettingData which references a managed element and an instance of a SettingData subclass where the IsCurrent property has a value of "Is Current" and the IsMinimum property does not have a value of "Is Minimum" and the IsMaximum property does not have a value of "Is Maximum".

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>**Is Current** (1)
</dt> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>**Is Not Current** (2)
</dt> </dl>

</dd> <dt>

**IsDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is a default setting for the element or that this information is unknown. This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>**Is Default** (1)
</dt> <dt>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>**Is Not Default** (2)
</dt> </dl>

</dd> <dt>

**IsMaximum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated SettingData instance. All other properties of the associated SettingData instance are not affected by this property. Note: It is assumed that the semantics of each property of this set are designed to be compared mathematically. When IsMaximum = "Is Maximum", this property indicates that the affected property values specified in the associated SettingData instance shall define maximum setting values. When IsMaximum = "Is Not Maximum", this property indicates that the affected property values specified in the associated SettingData instance shall not define maximum setting values. When IsMaximum = "Unknown", this property indicates that the affected property values specified in the associated SettingData instance may correspond to maximum setting values. When IsMaximum = "Not Applicable", this property indicates that the affected property values specified in the associated SettingData instance shall not be interpreted with respect to whether each defines a maximum.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)
</dt> <dt>

<span id="Is_Maximum"></span><span id="is_maximum"></span><span id="IS_MAXIMUM"></span>**Is Maximum** (2)
</dt> <dt>

<span id="Is_Not_Maximum"></span><span id="is_not_maximum"></span><span id="IS_NOT_MAXIMUM"></span>**Is Not Maximum** (3)
</dt> </dl>

</dd> <dt>

**IsMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated SettingData instance. All other properties of the associated SettingData instance are not affected by this property. Be aware that it is assumed that the semantics of each property of this set are designed to be compared mathematically. When IsMinimum = "Is Minimum", this property indicates that the affected property values specified in the associated SettingData instance shall define minimum setting values. When IsMinimum = "Is Not Minimum", this property indicates that the affected property values specified in the associated SettingData instance shall not define minimum setting values. When IsMinimum = "Unknown", this property indicates that the affected property values specified in the associated SettingData instance may correspond to minimum setting values. When IsMinimum = "Not Applicable", this property indicates that the affected property values specified in the associated SettingData instance shall not be interpreted with respect to whether each defines a minimum.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)
</dt> <dt>

<span id="Is_Minimum"></span><span id="is_minimum"></span><span id="IS_MINIMUM"></span>**Is Minimum** (2)
</dt> <dt>

<span id="Is_Not_Minimum"></span><span id="is_not_minimum"></span><span id="IS_NOT_MINIMUM"></span>**Is Not Minimum** (3)
</dt> </dl>

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether or not the referenced setting is the next setting to be applied. For example, the application could occur on a reinitialization, reset, or reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied.

If this flag is specified (that is, set to a value other than "Unknown"), then this takes precedence over any SettingData that may have been specified as Default. For example: If the managed element is a computer system, and the value of this flag is "Is Next", then the setting will be effective next time the system resets. Unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to "Is Next For Single Use", then this setting will only be used once and the flag would be reset after that to "Is Not Next". In the preceding example, if the system restarts in a quick succession, the setting will not be used at the second restart.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Next"></span><span id="is_next"></span><span id="IS_NEXT"></span>**Is Next** (1)
</dt> <dt>

<span id="Is_Not_Next"></span><span id="is_not_next"></span><span id="IS_NOT_NEXT"></span>**Is Not Next** (2)
</dt> <dt>

<span id="Is_Next_For_Single_Use"></span><span id="is_next_for_single_use"></span><span id="IS_NEXT_FOR_SINGLE_USE"></span>**Is Next For Single Use** (3)
</dt> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The managed element. This property inherits from [**MSFT\_NetAdapterElementSettingData**](msft-netadapterelementsettingdata.md).

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

The group number for the processors specified in ProcessorAffinityMask property.

</dd> <dt>

**QueueID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The queue identifier

</dd> <dt>

**QueueName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that identifies the queue.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapterSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The SettingData object associated with the element. This property inherits from [**MSFT\_NetAdapterElementSettingData**](msft-netadapterelementsettingdata.md).

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

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operational state of the queue.

<dl> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>**Undefined** (0)
</dt> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (1)
</dt> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (2)
</dt> <dt>

<span id="DmaStopped_"></span><span id="dmastopped_"></span><span id="DMASTOPPED_"></span>**DmaStopped** (3)
</dt> </dl>

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The scoping System\\'s Name. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**VmFriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name the Virtual Machine to which the queue is assigned.

</dd> <dt>

**VmID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ID of the Virtual Machine to which the queue is assigned.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

