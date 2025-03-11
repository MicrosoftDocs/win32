---
description: Network adapter statistics.
ms.assetid: 4e7b2657-d9f2-488c-a22e-e6aaea7d4842
title: MSFT\_NetAdapterStatisticsSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterStatisticsSettingData
- MSFT_NetAdapterStatisticsSettingData.Caption
- MSFT_NetAdapterStatisticsSettingData.Description
- MSFT_NetAdapterStatisticsSettingData.ElementName
- MSFT_NetAdapterStatisticsSettingData.InstanceID
- MSFT_NetAdapterStatisticsSettingData.Name
- MSFT_NetAdapterStatisticsSettingData.InterfaceDescription
- MSFT_NetAdapterStatisticsSettingData.Source
- MSFT_NetAdapterStatisticsSettingData.SystemName
- MSFT_NetAdapterStatisticsSettingData.SupportedStatistics
- MSFT_NetAdapterStatisticsSettingData.ReceivedBytes
- MSFT_NetAdapterStatisticsSettingData.ReceivedUnicastPackets
- MSFT_NetAdapterStatisticsSettingData.ReceivedMulticastPackets
- MSFT_NetAdapterStatisticsSettingData.ReceivedBroadcastPackets
- MSFT_NetAdapterStatisticsSettingData.ReceivedUnicastBytes
- MSFT_NetAdapterStatisticsSettingData.ReceivedMulticastBytes
- MSFT_NetAdapterStatisticsSettingData.ReceivedBroadcastBytes
- MSFT_NetAdapterStatisticsSettingData.ReceivedDiscardedPackets
- MSFT_NetAdapterStatisticsSettingData.ReceivedPacketErrors
- MSFT_NetAdapterStatisticsSettingData.SentBytes
- MSFT_NetAdapterStatisticsSettingData.SentUnicastPackets
- MSFT_NetAdapterStatisticsSettingData.SentMulticastPackets
- MSFT_NetAdapterStatisticsSettingData.SentBroadcastPackets
- MSFT_NetAdapterStatisticsSettingData.SentUnicastBytes
- MSFT_NetAdapterStatisticsSettingData.SentMulticastBytes
- MSFT_NetAdapterStatisticsSettingData.SentBroadcastBytes
- MSFT_NetAdapterStatisticsSettingData.OutboundDiscardedPackets
- MSFT_NetAdapterStatisticsSettingData.OutboundPacketErrors
- MSFT_NetAdapterStatisticsSettingData.RdmaStatistics
- MSFT_NetAdapterStatisticsSettingData.RscStatistics
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterStatisticsSettingData class

Network adapter statistics

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterStatisticsSettingData : MSFT_NetAdapterSettingData
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
  string Name;
  string InterfaceDescription;
  uint32 Source;
  string SystemName;
  uint32 SupportedStatistics;
  uint64 ReceivedBytes;
  uint64 ReceivedUnicastPackets;
  uint64 ReceivedMulticastPackets;
  uint64 ReceivedBroadcastPackets;
  uint64 ReceivedUnicastBytes;
  uint64 ReceivedMulticastBytes;
  uint64 ReceivedBroadcastBytes;
  uint64 ReceivedDiscardedPackets;
  uint64 ReceivedPacketErrors;
  uint64 SentBytes;
  uint64 SentUnicastPackets;
  uint64 SentMulticastPackets;
  uint64 SentBroadcastPackets;
  uint64 SentUnicastBytes;
  uint64 SentMulticastBytes;
  uint64 SentBroadcastBytes;
  uint64 OutboundDiscardedPackets;
  uint64 OutboundPacketErrors;
  string RdmaStatistics;
  string RscStatistics;
};
```

## Members

The **MSFT\_NetAdapterStatisticsSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterStatisticsSettingData** class has these properties.

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

**OutboundDiscardedPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of outgoing packets that were discarded even though they did not have errors.

</dd> <dt>

**OutboundPacketErrors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of outgoing packets that were discarded because of errors.

</dd> <dt>

**RdmaStatistics**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RDMA statistics

</dd> <dt>

**ReceivedBroadcastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of broadcast bytes received without errors through this interface.

</dd> <dt>

**ReceivedBroadcastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of broadcast packets received without errors through this interface.

</dd> <dt>

**ReceivedBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of bytes of data received without errors through this interface. This value includes bytes in unicast, broadcast, and multicast packets.

</dd> <dt>

**ReceivedDiscardedPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of inbound packets which were chosen to be discarded even though no errors were detected to prevent the packets from being deliverable to a higher-layer protocol.

</dd> <dt>

**ReceivedMulticastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of multicast bytes received without errors through this interface.

</dd> <dt>

**ReceivedMulticastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of multicast packets received without errors through this interface.

</dd> <dt>

**ReceivedPacketErrors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of incoming packets that were discarded because of errors.

</dd> <dt>

**ReceivedUnicastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unicast bytes received without errors through this interface.

</dd> <dt>

**ReceivedUnicastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unicast packets received without errors through this interface.

</dd> <dt>

**RscStatistics**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RSC statistics

</dd> <dt>

**SentBroadcastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of broadcast bytes transmitted without errors through this interface.

</dd> <dt>

**SentBroadcastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of broadcast packets transmitted without errors through this interface.

</dd> <dt>

**SentBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of bytes of data transmitted without errors through this interface. This value includes bytes in unicast, broadcast, and multicast packets.

</dd> <dt>

**SentMulticastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of multicast bytes transmitted without errors through this interface.

</dd> <dt>

**SentMulticastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of multicast packets transmitted without errors through this interface.

</dd> <dt>

**SentUnicastBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unicast bytes transmitted without errors through this interface.

</dd> <dt>

**SentUnicastPackets**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unicast packets transmitted without errors through this interface.

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

**SupportedStatistics**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported statistics

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



 

