---
title: VpnS2SInterfaceStatistics class
description: Represents the VPN S2S interface statistics.
audience: developer
ms.assetid: 02de13ea-c66c-463f-a54e-e6ae3188a13b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnS2SInterfaceStatistics class
- VpnS2SInterfaceStatistics class, described
topic_type:
- apiref
api_name:
- VpnS2SInterfaceStatistics
- VpnS2SInterfaceStatistics.BytesTransmitted
- VpnS2SInterfaceStatistics.CumulativeBytesReceived
- VpnS2SInterfaceStatistics.CumulativeBytesTransmitted
- VpnS2SInterfaceStatistics.BytesReceived
- VpnS2SInterfaceStatistics.FramesTransmitted
- VpnS2SInterfaceStatistics.FramesReceived
- VpnS2SInterfaceStatistics.CrcErrors
- VpnS2SInterfaceStatistics.TimeoutErrors
- VpnS2SInterfaceStatistics.AlignmentErrors
- VpnS2SInterfaceStatistics.HardwareOverrunErrors
- VpnS2SInterfaceStatistics.FramingErrors
- VpnS2SInterfaceStatistics.BufferOverrunErrors
- VpnS2SInterfaceStatistics.RxRateKbps
- VpnS2SInterfaceStatistics.TxRateKbps
- VpnS2SInterfaceStatistics.RxRateLimitedPacketsDropped
- VpnS2SInterfaceStatistics.TxRateLimitedPacketsDropped
- VpnS2SInterfaceStatistics.RxTotalPacketsDropped
- VpnS2SInterfaceStatistics.TxTotalPacketsDropped
- VpnS2SInterfaceStatistics.LastClearedTime
- VpnS2SInterfaceStatistics.ConnectionUpTime
- VpnS2SInterfaceStatistics.Name
- VpnS2SInterfaceStatistics.RoutingDomain
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VpnS2SInterfaceStatistics class

Represents the VPN S2S interface statistics

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnS2SInterfaceStatistics
{
  uint64   BytesTransmitted;
  uint64   CumulativeBytesReceived;
  uint64   CumulativeBytesTransmitted;
  uint64   BytesReceived;
  uint32   FramesTransmitted;
  uint32   FramesReceived;
  uint32   CrcErrors;
  uint32   TimeoutErrors;
  uint32   AlignmentErrors;
  uint32   HardwareOverrunErrors;
  uint32   FramingErrors;
  uint32   BufferOverrunErrors;
  uint32   RxRateKbps;
  uint32   TxRateKbps;
  uint32   RxRateLimitedPacketsDropped;
  uint32   TxRateLimitedPacketsDropped;
  uint32   RxTotalPacketsDropped;
  uint32   TxTotalPacketsDropped;
  datetime LastClearedTime;
  uint32   ConnectionUpTime;
  string   Name;
  string   RoutingDomain;
};
```

## Members

The **VpnS2SInterfaceStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnS2SInterfaceStatistics** class has these properties.

<dl> <dt>

**AlignmentErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The alignment errors on the port

</dd> <dt>

**BufferOverrunErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The buffer overrun errors on the port

</dd> <dt>

**BytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of compressed data received on the port

</dd> <dt>

**BytesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of compressed data transmitted on the port

</dd> <dt>

**ConnectionUpTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time the interface has been in the connected state, in seconds

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**CrcErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cyclic redundancy check (CRC) errors on the port

</dd> <dt>

**CumulativeBytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of data received by the interface since it was created

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**CumulativeBytesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of data transmitted by the interface since it was created, in bytes

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**FramesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The frames received on the port

</dd> <dt>

**FramesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The frames transmitted on the port

</dd> <dt>

**FramingErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The framing errors on the port

</dd> <dt>

**HardwareOverrunErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hardware overrun errors on the port

</dd> <dt>

**LastClearedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time that the statistics were reset

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The alias of the interface

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the routing domain

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

</dd> <dt>

**RxRateKbps**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rate of received bytes, in Kbps

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**RxRateLimitedPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of receive packets dropped due to rate limiting

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**RxTotalPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of receive packets dropped

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**TimeoutErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time-out errors on the port

</dd> <dt>

**TxRateKbps**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rate of transmitted bytes, in Kbps

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**TxRateLimitedPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of transmit packets dropped due to rate limiting

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**TxTotalPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of transmit packets dropped

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





