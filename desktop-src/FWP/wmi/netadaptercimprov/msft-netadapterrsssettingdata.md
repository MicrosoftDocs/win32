---
description: Receive Side Scale (RSS) settings for a network adapter.
ms.assetid: bbff4ce3-0d9f-4d34-b619-100b49d8c27d
title: MSFT\_NetAdapterRssSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# MSFT\_NetAdapterRssSettingData class

Receive Side Scale (RSS) settings for a network adapter

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterRssSettingData : MSFT_NetAdapterSettingData
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
  boolean MsiSupported;
  boolean MsiXSupported;
  boolean MsiXEnabled;
  boolean ClassificationAtIsrSupported;
  boolean ClassificationAtDpcSupported;
  boolean TcpIPv4HashSupported;
  boolean TcpIPv6HashSupported;
  boolean TcpIPv6ExtensionHashSupported;
  boolean ToeplitzHashFunctionSupported;
  boolean RssOnPortsSupported;
  uint32  NumberOfInterruptMessages;
  uint32  NumberOfReceiveQueues;
  boolean IPv4HashEnabled;
  boolean TcpIPv4HashEnabled;
  boolean IPv6HashEnabled;
  boolean IPv6ExtensionHashEnabled;
  boolean TcpIPv6HashEnabled;
  boolean TcpIPv6ExtensionHashEnabled;
  boolean ToeplitzHashFunctionEnabled;
  uint16  IndirectionTableEntryCount;
  uint16  HashKeySize;
  string  IndirectionTable[];
  uint32  Profile;
  uint16  BaseProcessorGroup;
  uint8   BaseProcessorNumber;
  uint16  MaxProcessorGroup;
  uint8   MaxProcessorNumber;
  uint32  MaxProcessors;
  uint16  NumaNode;
  uint32  RssProcessorArraySize;
  string  RssProcessorArray[];
};
```

## Members

The **MSFT\_NetAdapterRssSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterRssSettingData** class has these methods.



| Method                                                   | Description                                                                           |
|:---------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadapterrsssettingdata.md) | Disables the Receive Side Scaling (RSS) properties on the network adapter.<br/> |
| [**Enable**](enable-msft-netadapterrsssettingdata.md)   | Enables the Receive Side Scaling (RSS) properties on the network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterRssSettingData** class has these properties.

<dl> <dt>

**BaseProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor group number for the first RSS processor.

</dd> <dt>

**BaseProcessorNumber**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor number for the first RSS processor.

</dd> <dt>

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

**ClassificationAtDpcSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ClassificationAtIsrSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

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

Enabled.

</dd> <dt>

**HashKeySize**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hash key size.

</dd> <dt>

**IndirectionTable**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Pointer to the indirection table.

</dd> <dt>

**IndirectionTableEntryCount**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The indirection table entry count.

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

**IPv4HashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv4 hash enabled.

</dd> <dt>

**IPv6ExtensionHashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv6 extension hash enabled.

</dd> <dt>

**IPv6HashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv6 hash enabled.

</dd> <dt>

**MaxProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor group number for the last RSS processor.

</dd> <dt>

**MaxProcessorNumber**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor number for the last RSS processor.

</dd> <dt>

**MaxProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the maximum number of RSS processors for the network adapter.

</dd> <dt>

**MsiSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI supported.

</dd> <dt>

**MsiXEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI-X Enabled.

</dd> <dt>

**MsiXSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

MSI-X supported.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name, also known as Connection Name, "ifAlias", or InterfaceAlias, is a unique name assigned to the adapter during installation. The Name of the adapter can be changed by the administrator and is persisted across the boot or network adapter restart. This property inherits from [**MSFT\_NetAdapterSettingData**](msft-netadaptersettingdata.md).

</dd> <dt>

**NumaNode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The numa mode.

</dd> <dt>

**NumberOfInterruptMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of interrupt messages.

</dd> <dt>

**NumberOfReceiveQueues**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of receive queues.

</dd> <dt>

**Profile**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor selection and load balancing profile applied.

<dl> <dt>

<span id="Closest_Processor"></span><span id="closest_processor"></span><span id="CLOSEST_PROCESSOR"></span>**Closest Processor** (1)
</dt> <dt>

<span id="Closest_Processor_Static"></span><span id="closest_processor_static"></span><span id="CLOSEST_PROCESSOR_STATIC"></span>**Closest Processor Static** (2)
</dt> <dt>

<span id="NUMA_Scaling"></span><span id="numa_scaling"></span><span id="NUMA_SCALING"></span>**NUMA Scaling** (3)
</dt> <dt>

<span id="NUMA_Scaling_Static"></span><span id="numa_scaling_static"></span><span id="NUMA_SCALING_STATIC"></span>**NUMA Scaling Static** (4)
</dt> <dt>

<span id="Conservative_Scaling_"></span><span id="conservative_scaling_"></span><span id="CONSERVATIVE_SCALING_"></span>**Conservative Scaling** (5)
</dt> </dl>

</dd> <dt>

**RssOnPortsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RSS on ports supported.

</dd> <dt>

**RssProcessorArray**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

pointer to the RSS processor array.

</dd> <dt>

**RssProcessorArraySize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The RSS processor array size.

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

</dd> <dt>

**TcpIPv4HashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TCP/IPv4 hash enabled.

</dd> <dt>

**TcpIPv4HashSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**TcpIPv6ExtensionHashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TCP/IPv6 extension hash enabled.

</dd> <dt>

**TcpIPv6ExtensionHashSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TCP/IPv6 extension hash supported.

</dd> <dt>

**TcpIPv6HashEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TCP/IPv6 hash enabled.

</dd> <dt>

**TcpIPv6HashSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TCP/IPv6 hash supported.

</dd> <dt>

**ToeplitzHashFunctionEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ToeplitzHashFunctionSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

