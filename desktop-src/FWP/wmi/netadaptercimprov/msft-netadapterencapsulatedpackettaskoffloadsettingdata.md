---
description: Encapsulated packet task offload properties for a network adapter.
ms.assetid: 1ab0366a-dbf2-4b80-972f-3a7223f58e93
title: MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.Caption
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.Description
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.ElementName
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.InstanceID
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.Name
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.InterfaceDescription
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.Source
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.SystemName
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.EncapsulatedPacketTaskOffloadEnabled
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData.EncapsulatedPacketTaskOffloadHardwareCapabilities
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData class

Encapsulated packet task offload properties for a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterEncapsulatedPacketTaskOffloadSettingData : MSFT_NetAdapterSettingData
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  string  Name;
  string  InterfaceDescription;
  uint32  Source;
  string  SystemName;
  boolean EncapsulatedPacketTaskOffloadEnabled;
  string  EncapsulatedPacketTaskOffloadHardwareCapabilities;
};
```

## Members

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData** class has these methods.



| Method                                                                             | Description                                                                      |
|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadapterencapsulatedpackettaskoffloadsettingdata.md) | Disables the Encapsulation Offload properties on the network adapter.<br/> |
| [**Enable**](enable-msft-netadapterencapsulatedpackettaskoffloadsettingdata.md)   | Enables the Encapsulation Offload properties on the network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadSettingData** class has these properties.

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

**EncapsulatedPacketTaskOffloadEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if Encapsulated Packet Task Offloads are currently enabled for this Adapter

</dd> <dt>

**EncapsulatedPacketTaskOffloadHardwareCapabilities**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An encapsulated instance of the [**MSFT\_NetAdapterEncapsulatedPacketTaskOffloadCapabilities**](msft-netadapterencapsulatedpackettaskoffloadcapabilities.md) class that describes the Encapsulated Packet Task Offload hardware capabilities of this Adapter

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



 

