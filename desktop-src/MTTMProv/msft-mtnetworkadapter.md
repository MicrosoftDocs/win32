---
title: MSFT\_MTNetworkAdapter class
description: The Network adapter data object. Statistic data is calculated based on current interval seconds setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ba642c1a-d9db-463b-8d15-094aec65306e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_MTNetworkAdapter class", "MSFT_MTNetworkAdapter class, described"]
topic_type:
- apiref
api_name:
- MSFT_MTNetworkAdapter
- MSFT_MTNetworkAdapter.InstanceID
- MSFT_MTNetworkAdapter.Caption
- MSFT_MTNetworkAdapter.Description
- MSFT_MTNetworkAdapter.ElementName
- MSFT_MTNetworkAdapter.Name
- MSFT_MTNetworkAdapter.InterfaceDescription
- MSFT_MTNetworkAdapter.IPv4Address
- MSFT_MTNetworkAdapter.IPv6Address
- MSFT_MTNetworkAdapter.DNSName
- MSFT_MTNetworkAdapter.MachineJoinedName
- MSFT_MTNetworkAdapter.MachineJoinedType
- MSFT_MTNetworkAdapter.NdisMedium
- MSFT_MTNetworkAdapter.NdisPhysicalMedium
- MSFT_MTNetworkAdapter.OperationStatus
- MSFT_MTNetworkAdapter.Utilization
- MSFT_MTNetworkAdapter.LinkSpeed
- MSFT_MTNetworkAdapter.InterfaceGuid
- MSFT_MTNetworkAdapter.BytesSent
- MSFT_MTNetworkAdapter.BytesReceived
- MSFT_MTNetworkAdapter.BytesTotal
- MSFT_MTNetworkAdapter.UniCastsSent
- MSFT_MTNetworkAdapter.UniCastsReceived
- MSFT_MTNetworkAdapter.UniCastsTotal
- MSFT_MTNetworkAdapter.NonUniCastsSent
- MSFT_MTNetworkAdapter.NonUniCastsReceived
- MSFT_MTNetworkAdapter.NonUniCastsTotal
- MSFT_MTNetworkAdapter.IntervalSeconds
- MSFT_MTNetworkAdapter.CurrentIndex
- MSFT_MTNetworkAdapter.SentThroughput
- MSFT_MTNetworkAdapter.ReceivedThroughput
- MSFT_MTNetworkAdapter.SentBitsPerSecond
- MSFT_MTNetworkAdapter.ReceivedBitsPerSecond
- MSFT_MTNetworkAdapter.MaxSentBitsPerSecond
- MSFT_MTNetworkAdapter.MaxReceivedBitsPerSecond
- MSFT_MTNetworkAdapter.BytesSentThroughput
- MSFT_MTNetworkAdapter.BytesReceivedThroughput
- MSFT_MTNetworkAdapter.BytesTotalThroughput
- MSFT_MTNetworkAdapter.BytesSentPerInterval
- MSFT_MTNetworkAdapter.BytesReceivedPerInterval
- MSFT_MTNetworkAdapter.BytesTotalPerInterval
- MSFT_MTNetworkAdapter.UniCastsSentPerInterval
- MSFT_MTNetworkAdapter.UniCastsReceivedPerInterval
- MSFT_MTNetworkAdapter.UniCastsTotalPerInterval
- MSFT_MTNetworkAdapter.NonUniCastsSentPerInterval
- MSFT_MTNetworkAdapter.NonUniCastsReceivedPerInterval
- MSFT_MTNetworkAdapter.NonUniCastsTotalPerInterval
api_location:
- MtTmProv.dll
api_type:
- DllExport
---

# MSFT\_MTNetworkAdapter class

The Network adapter data object. Statistic data is calculated based on current interval seconds setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("mttmprov"), AMENDMENT]
class MSFT_MTNetworkAdapter : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string Name;
  string InterfaceDescription;
  string IPv4Address;
  string IPv6Address;
  string DNSName;
  string MachineJoinedName;
  uint16 MachineJoinedType;
  uint32 NdisMedium;
  uint32 NdisPhysicalMedium;
  uint16 OperationStatus;
  real32 Utilization;
  uint64 LinkSpeed;
  string InterfaceGuid;
  uint64 BytesSent;
  uint64 BytesReceived;
  uint64 BytesTotal;
  uint64 UniCastsSent;
  uint64 UniCastsReceived;
  uint64 UniCastsTotal;
  uint64 NonUniCastsSent;
  uint64 NonUniCastsReceived;
  uint64 NonUniCastsTotal;
  uint16 IntervalSeconds;
  uint16 CurrentIndex;
  real32 SentThroughput[];
  real32 ReceivedThroughput[];
  real32 SentBitsPerSecond[];
  real32 ReceivedBitsPerSecond[];
  real32 MaxSentBitsPerSecond[];
  real32 MaxReceivedBitsPerSecond[];
  real32 BytesSentThroughput;
  real32 BytesReceivedThroughput;
  real32 BytesTotalThroughput;
  uint64 BytesSentPerInterval;
  uint64 BytesReceivedPerInterval;
  uint64 BytesTotalPerInterval;
  uint64 UniCastsSentPerInterval;
  uint64 UniCastsReceivedPerInterval;
  uint64 UniCastsTotalPerInterval;
  uint64 NonUniCastsSentPerInterval;
  uint64 NonUniCastsReceivedPerInterval;
  uint64 NonUniCastsTotalPerInterval;
};
```

## Members

The **MSFT\_MTNetworkAdapter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MTNetworkAdapter** class has these properties.

<dl> <dt>

**BytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes received on the connection to date.

</dd> <dt>

**BytesReceivedPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes received on the connection in the polling time interval.

</dd> <dt>

**BytesReceivedThroughput**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the percentage of connection bandwidth used by traffic received by the machine in the polling time period.

</dd> <dt>

**BytesSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes sent on the connection to date.

</dd> <dt>

**BytesSentPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes sent on the connection in the polling time interval.

</dd> <dt>

**BytesSentThroughput**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the percentage of connection bandwidth used by traffic sent from the machine in the polling time period.

</dd> <dt>

**BytesTotal**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes sent and received on the connection to date.

</dd> <dt>

**BytesTotalPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes received and sent on the connection in the polling time interval.

</dd> <dt>

**BytesTotalThroughput**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the percentage of connection bandwidth used by both sent and received traffic in the polling time period.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**CurrentIndex**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data sample index. Increment at every data sample.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DNSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the domain name of the computer system joined on the network.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the **Name** property of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties. Note that if there is an associated instance of **CIM\_EnabledLogicalElementCapabilities**, restrictions on this properties may exist as defined in **ElementNameMask** and **MaxElementNameLen** properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**InstanceID** is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below. To ensure uniqueness within the NameSpace, the value of **InstanceID** should be constructed using the following "preferred" algorithm: "*OrgID*:*LocalID*" Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the **InstanceID** or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in **InstanceID** must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting **InstanceID** is not reused across any **InstanceID**s produced by this or other providers for the NameSpace of this instance. If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to "CIM".

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InterfaceDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the network adapter device.

</dd> <dt>

**InterfaceGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the GUID of the network adapter.

</dd> <dt>

**IntervalSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current data collection interval in seconds.

</dd> <dt>

**IPv4Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the IPv4 network address configured on the network adapter.

</dd> <dt>

**IPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the IPv6 network address configured on the network adapter.

</dd> <dt>

**LinkSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total link speed of the network adapter, in bits per second.

</dd> <dt>

**MachineJoinedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the machine joined domain or workgroup name of the computer system.

</dd> <dt>

**MachineJoinedType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the machine joined type on the network.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Unjoined"></span><span id="unjoined"></span><span id="UNJOINED"></span>

**Unjoined** (1)


</dt> <dd></dd> <dt>

<span id="Workgroup"></span><span id="workgroup"></span><span id="WORKGROUP"></span>

**Workgroup** (2)


</dt> <dd></dd> <dt>

<span id="Domain"></span><span id="domain"></span><span id="DOMAIN"></span>

**Domain** (3)


</dt> <dd></dd> <dt>

<span id="VerifiedError"></span><span id="verifiederror"></span><span id="VERIFIEDERROR"></span>

**VerifiedError** (4)


</dt> <dd></dd> <dt>

<span id="NotVerified"></span><span id="notverified"></span><span id="NOTVERIFIED"></span>

**NotVerified** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**MaxReceivedBitsPerSecond**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of the maximum received bits per second at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**MaxSentBitsPerSecond**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of maximum sent bits per second at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Gets the name of connection on the network adapter device.

</dd> <dt>

**NdisMedium**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the network adapter media type.

<dt>

<span id="802.3"></span>

**802.3** (0)


</dt> <dd></dd> <dt>

<span id="802.5"></span>

**802.5** (1)


</dt> <dd></dd> <dt>

<span id="FDDI"></span><span id="fddi"></span>

**FDDI** (2)


</dt> <dd></dd> <dt>

<span id="WAN"></span><span id="wan"></span>

**WAN** (3)


</dt> <dd></dd> <dt>

<span id="Local_Talk"></span><span id="local_talk"></span><span id="LOCAL_TALK"></span>

**Local Talk** (4)


</dt> <dd></dd> <dt>

<span id="DIX"></span><span id="dix"></span>

**DIX** (5)


</dt> <dd></dd> <dt>

<span id="Raw_Arcnet"></span><span id="raw_arcnet"></span><span id="RAW_ARCNET"></span>

**Raw Arcnet** (6)


</dt> <dd></dd> <dt>

<span id="878.2"></span>

**878.2** (7)


</dt> <dd></dd> <dt>

<span id="ATM"></span><span id="atm"></span>

**ATM** (8)


</dt> <dd></dd> <dt>

<span id="Wireless_WAN"></span><span id="wireless_wan"></span><span id="WIRELESS_WAN"></span>

**Wireless WAN** (9)


</dt> <dd></dd> <dt>

<span id="IRDA"></span><span id="irda"></span>

**IRDA** (10)


</dt> <dd></dd> <dt>

<span id="BPC"></span><span id="bpc"></span>

**BPC** (11)


</dt> <dd></dd> <dt>

<span id="Connection_Oriented_WAN"></span><span id="connection_oriented_wan"></span><span id="CONNECTION_ORIENTED_WAN"></span>

**Connection Oriented WAN** (12)


</dt> <dd></dd> <dt>

<span id="IP_1394"></span><span id="ip_1394"></span>

**IP 1394** (13)


</dt> <dd></dd> <dt>

<span id="IB"></span><span id="ib"></span>

**IB** (14)


</dt> <dd></dd> <dt>

<span id="Tunnel"></span><span id="tunnel"></span><span id="TUNNEL"></span>

**Tunnel** (15)


</dt> <dd></dd> <dt>

<span id="Native_802.11"></span><span id="native_802.11"></span><span id="NATIVE_802.11"></span>

**Native 802.11** (16)


</dt> <dd></dd> <dt>

<span id="Loopback"></span><span id="loopback"></span><span id="LOOPBACK"></span>

**Loopback** (17)


</dt> <dd></dd> <dt>

<span id="WiMAX"></span><span id="wimax"></span><span id="WIMAX"></span>

**WiMAX** (18)


</dt> <dd></dd> <dt>

<span id="IP"></span><span id="ip"></span>

**IP** (19)


</dt> <dd></dd> </dl>

</dd> <dt>

**NdisPhysicalMedium**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the types of physical media that the network adapter supports.

<dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>

**Unspecified** (0)


</dt> <dd></dd> <dt>

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>

**Wireless LAN** (1)


</dt> <dd></dd> <dt>

<span id="Cable_Modem"></span><span id="cable_modem"></span><span id="CABLE_MODEM"></span>

**Cable Modem** (2)


</dt> <dd></dd> <dt>

<span id="Phone_Line"></span><span id="phone_line"></span><span id="PHONE_LINE"></span>

**Phone Line** (3)


</dt> <dd></dd> <dt>

<span id="Power_Line"></span><span id="power_line"></span><span id="POWER_LINE"></span>

**Power Line** (4)


</dt> <dd></dd> <dt>

<span id="DSL"></span><span id="dsl"></span>

**DSL** (5)


</dt> <dd></dd> <dt>

<span id="FC"></span><span id="fc"></span>

**FC** (6)


</dt> <dd></dd> <dt>

<span id="1394"></span>

**1394** (7)


</dt> <dd></dd> <dt>

<span id="Wireless_WAN"></span><span id="wireless_wan"></span><span id="WIRELESS_WAN"></span>

**Wireless WAN** (8)


</dt> <dd></dd> <dt>

<span id="Native_802.11"></span><span id="native_802.11"></span><span id="NATIVE_802.11"></span>

**Native 802.11** (9)


</dt> <dd></dd> <dt>

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>

**BlueTooth** (10)


</dt> <dd></dd> <dt>

<span id="Infiniband"></span><span id="infiniband"></span><span id="INFINIBAND"></span>

**Infiniband** (11)


</dt> <dd></dd> <dt>

<span id="WiMAX"></span><span id="wimax"></span><span id="WIMAX"></span>

**WiMAX** (12)


</dt> <dd></dd> <dt>

<span id="UWB"></span><span id="uwb"></span>

**UWB** (13)


</dt> <dd></dd> <dt>

<span id="802.3"></span>

**802.3** (14)


</dt> <dd></dd> <dt>

<span id="802.5"></span>

**802.5** (15)


</dt> <dd></dd> <dt>

<span id="IRDA"></span><span id="irda"></span>

**IRDA** (16)


</dt> <dd></dd> <dt>

<span id="Wired_WAN"></span><span id="wired_wan"></span><span id="WIRED_WAN"></span>

**Wired WAN** (17)


</dt> <dd></dd> <dt>

<span id="Wired_Connection_Oriented_WAN"></span><span id="wired_connection_oriented_wan"></span><span id="WIRED_CONNECTION_ORIENTED_WAN"></span>

**Wired Connection Oriented WAN** (18)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (19)


</dt> <dd></dd> </dl>

</dd> <dt>

**NonUniCastsReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes from nonsubnet-unicast addresses delivered to higher-level protocols by on the connection to date.

</dd> <dt>

**NonUniCastsReceivedPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes from nonsubnet-unicast addresses delivered to higher-level protocols on the connection in the polling time interval.

</dd> <dt>

**NonUniCastsSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes requested to be transmitted to nonsubnet-unicast addresses by higher-level protocols on the connection to date.

</dd> <dt>

**NonUniCastsSentPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes requested to be transmitted to nonsubnet-unicast addresses by higher-level protocols on the connection in the polling time interval.

</dd> <dt>

**NonUniCastsTotal**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of nonunicast Sent and nonunicast Received packets to date.

</dd> <dt>

**NonUniCastsTotalPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of nonunicast Sent and nonunicast Received packets in the polling time interval.

</dd> <dt>

**OperationStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the operational status of the network adapter.

<dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>

**Up** (1)


</dt> <dd></dd> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>

**Down** (2)


</dt> <dd></dd> <dt>

<span id="Testing"></span><span id="testing"></span><span id="TESTING"></span>

**Testing** (3)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (4)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (5)


</dt> <dd></dd> <dt>

<span id="Not_Present"></span><span id="not_present"></span><span id="NOT_PRESENT"></span>

**Not Present** (6)


</dt> <dd></dd> <dt>

<span id="Lower_Layer_Down"></span><span id="lower_layer_down"></span><span id="LOWER_LAYER_DOWN"></span>

**Lower Layer Down** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReceivedBitsPerSecond**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of received bits per second at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**ReceivedThroughput**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of percentages of received throughput at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**SentBitsPerSecond**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of sent bits per second at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**SentThroughput**
</dt> <dd> <dl> <dt>

Data type: **real32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a list of the percentages of sent throughput at each interval. The statistics are logged with the latest 60 samples, with each interval defined in **IntervalSeconds** (second).

</dd> <dt>

**UniCastsReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes received from unicast addresses by higher-level protocols.

</dd> <dt>

**UniCastsReceivedPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes from subnet-unicast addresses delivered to higher-level protocols on the connection in the polling time interval.

</dd> <dt>

**UniCastsSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes requested to be transmitted to unicast addresses by higher-level protocols. The value includes the packets that were discarded or not sent.

</dd> <dt>

**UniCastsSentPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of bytes requested to be transmitted to subnet-unicast addresses by higher-level protocols on the connection in the polling time interval.

</dd> <dt>

**UniCastsTotal**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of Unicast Sent and Unicast Received packets to date.

</dd> <dt>

**UniCastsTotalPerInterval**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the total number of Unicast Sent and Unicast Received packets for the connection in the polling time interval.

</dd> <dt>

**Utilization**
</dt> <dd> <dl> <dt>

Data type: **real32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the percentage of network utilization at the latest interval.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                    |
| MOF<br/>                      | <dl> <dt>MtTmProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MtTmProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[Management Tools Task Manager WMI Provider](management-tools-task-manager-wmi-provider-portal.md)
</dt> </dl>

 

 





