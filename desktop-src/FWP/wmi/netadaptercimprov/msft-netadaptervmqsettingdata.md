---
description: Network adapter Vritual Machine Queue (VMQ) settings.
ms.assetid: d24cbc66-4b92-40bf-90b8-cf5719b8e0a5
title: MSFT\_NetAdapterVmqSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterVmqSettingData
- MSFT_NetAdapterVmqSettingData.Caption
- MSFT_NetAdapterVmqSettingData.Description
- MSFT_NetAdapterVmqSettingData.ElementName
- MSFT_NetAdapterVmqSettingData.InstanceID
- MSFT_NetAdapterVmqSettingData.Name
- MSFT_NetAdapterVmqSettingData.InterfaceDescription
- MSFT_NetAdapterVmqSettingData.Source
- MSFT_NetAdapterVmqSettingData.SystemName
- MSFT_NetAdapterVmqSettingData.Enabled
- MSFT_NetAdapterVmqSettingData.NumberOfReceiveQueues
- MSFT_NetAdapterVmqSettingData.TotalNumberOfMacAddresses
- MSFT_NetAdapterVmqSettingData.NumMacAddressesPerPort
- MSFT_NetAdapterVmqSettingData.NumVlansPerPort
- MSFT_NetAdapterVmqSettingData.VlanFilteringSupported
- MSFT_NetAdapterVmqSettingData.LookaheadSplitSupported
- MSFT_NetAdapterVmqSettingData.MinLookaheadSplitSize
- MSFT_NetAdapterVmqSettingData.MaxLookaheadSplitSize
- MSFT_NetAdapterVmqSettingData.AnyVlanSupported
- MSFT_NetAdapterVmqSettingData.DynamicProcessorAffinityChangeSupported
- MSFT_NetAdapterVmqSettingData.InterruptVectorCoalescingSupported
- MSFT_NetAdapterVmqSettingData.BaseProcessorGroup
- MSFT_NetAdapterVmqSettingData.BaseProcessorNumber
- MSFT_NetAdapterVmqSettingData.MaxProcessors
- MSFT_NetAdapterVmqSettingData.MaxProcessorNumber
- MSFT_NetAdapterVmqSettingData.NumaNode
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterVmqSettingData class

Network adapter Vritual Machine Queue (VMQ) settings

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterVmqSettingData : MSFT_NetAdapterSettingData
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
  uint32  NumberOfReceiveQueues;
  uint32  TotalNumberOfMacAddresses;
  uint32  NumMacAddressesPerPort;
  uint32  NumVlansPerPort;
  boolean VlanFilteringSupported;
  boolean LookaheadSplitSupported;
  uint32  MinLookaheadSplitSize;
  uint32  MaxLookaheadSplitSize;
  boolean AnyVlanSupported;
  boolean DynamicProcessorAffinityChangeSupported;
  boolean InterruptVectorCoalescingSupported;
  uint16  BaseProcessorGroup;
  uint8   BaseProcessorNumber;
  uint32  MaxProcessors;
  uint8   MaxProcessorNumber;
  uint16  NumaNode;
};
```

## Members

The **MSFT\_NetAdapterVmqSettingData** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetAdapterVmqSettingData** class has these methods.



| Method                                                   | Description                                                                 |
|:---------------------------------------------------------|:----------------------------------------------------------------------------|
| [**Disable**](disable-msft-netadaptervmqsettingdata.md) | Disables the Virtual Machine Queue (VMQ) on the network adapter.<br/> |
| [**Enable**](enable-msft-netadaptervmqsettingdata.md)   | Enables the Virtual Machine Queue (VMQ) on the network adapter.<br/>  |



 

### Properties

The **MSFT\_NetAdapterVmqSettingData** class has these properties.

<dl> <dt>

**AnyVlanSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the network adapter supports filtering received packets matching a MAC address and any arbitrary VLAN ID.

</dd> <dt>

**BaseProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor group number for the first VMQ processor.

</dd> <dt>

**BaseProcessorNumber**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the processor number for the first VMQ processor.

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

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object. This property inherits from [**CIM\_ManagedElement**](/previous-versions/cc136871(v=vs.85)).

</dd> <dt>

**DynamicProcessorAffinityChangeSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the network adapter supports changing the processor affinity of a queue dynamically and without restarting the queue.

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

A boolean value that is set to TRUE if VMQ is enabled and FALSE if it is not.

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

**InterruptVectorCoalescingSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicate that the network adapter supports using the same interrupt vector for multiple queues when all those queues are targeted to the same processor.

</dd> <dt>

**LookaheadSplitSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the network adapter supports splitting the received packets at a lookahead offset.

</dd> <dt>

**MaxLookaheadSplitSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum size, in bytes, of the lookahead segment if lookahead split is enabled.

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

Specifies the maximum number of VMQ processors for the network adapter.

</dd> <dt>

**MinLookaheadSplitSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum size, in bytes, of the lookahead segment if lookahead split is enabled.

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

Specifies the Numa Node for the RSS Processors.

</dd> <dt>

**NumberOfReceiveQueues**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of receive queues that the network adapter supports.

</dd> <dt>

**NumMacAddressesPerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of supported MAC addresses per port.

</dd> <dt>

**NumVlansPerPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of VLANs supported per port.

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

**TotalNumberOfMacAddresses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of MAC addresses that the network adapter supports.

</dd> <dt>

**VlanFilteringSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the network adapter supports filtering received packets based on the VLAN ID.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

