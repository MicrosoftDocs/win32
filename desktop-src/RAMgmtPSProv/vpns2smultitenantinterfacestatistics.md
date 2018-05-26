---
title: VpnS2SMultiTenantInterfaceStatistics class
description: Retrieves statistics for a site-to-site (S2S) VPN interface to a multi-tenant gateway.
audience: developer
ms.assetid: 83a0b1d6-2596-4010-b9f3-b795b9c4cb9b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnS2SMultiTenantInterfaceStatistics class
- VpnS2SMultiTenantInterfaceStatistics class, described
topic_type:
- apiref
api_name:
- VpnS2SMultiTenantInterfaceStatistics
- VpnS2SMultiTenantInterfaceStatistics.BytesTransmitted
- VpnS2SMultiTenantInterfaceStatistics.CumulativeBytesReceived
- VpnS2SMultiTenantInterfaceStatistics.CumulativeBytesTransmitted
- VpnS2SMultiTenantInterfaceStatistics.BytesReceived
- VpnS2SMultiTenantInterfaceStatistics.FramesTransmitted
- VpnS2SMultiTenantInterfaceStatistics.FramesReceived
- VpnS2SMultiTenantInterfaceStatistics.CrcErrors
- VpnS2SMultiTenantInterfaceStatistics.TimeoutErrors
- VpnS2SMultiTenantInterfaceStatistics.AlignmentErrors
- VpnS2SMultiTenantInterfaceStatistics.HardwareOverrunErrors
- VpnS2SMultiTenantInterfaceStatistics.FramingErrors
- VpnS2SMultiTenantInterfaceStatistics.BufferOverrunErrors
- VpnS2SMultiTenantInterfaceStatistics.RxRateKbps
- VpnS2SMultiTenantInterfaceStatistics.TxRateKbps
- VpnS2SMultiTenantInterfaceStatistics.RxRateLimitedPacketsDropped
- VpnS2SMultiTenantInterfaceStatistics.TxRateLimitedPacketsDropped
- VpnS2SMultiTenantInterfaceStatistics.RxTotalPacketsDropped
- VpnS2SMultiTenantInterfaceStatistics.TxTotalPacketsDropped
- VpnS2SMultiTenantInterfaceStatistics.LastClearedTime
- VpnS2SMultiTenantInterfaceStatistics.ConnectionUpTime
- VpnS2SMultiTenantInterfaceStatistics.Name
- VpnS2SMultiTenantInterfaceStatistics.RoutingDomain
- VpnS2SMultiTenantInterfaceStatistics.Bandwidth
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnS2SMultiTenantInterfaceStatistics class

Retrieves statistics for a site-to-site (S2S) VPN interface to a multi-tenant gateway.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnS2SMultiTenantInterfaceStatistics : VpnS2SInterfaceStatistics
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
  uint64   Bandwidth;
};
```

## Members

The **VpnS2SMultiTenantInterfaceStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnS2SMultiTenantInterfaceStatistics** class has these properties.

<dl> <dt>

**AlignmentErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The alignment errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**Bandwidth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the bandwidth consumption, in kbps.

</dd> <dt>

**BufferOverrunErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The buffer overrun errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**BytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of compressed data received on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**BytesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of compressed data transmitted on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**ConnectionUpTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time the interface has been in the connected state, in seconds

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**CrcErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cyclic redundancy check (CRC) errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**CumulativeBytesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bytes of data received by the interface since it was created

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**CumulativeBytesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of data transmitted by the interface since it was created, in bytes

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**FramesReceived**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The frames received on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**FramesTransmitted**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The frames transmitted on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**FramingErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The framing errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**HardwareOverrunErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The hardware overrun errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**LastClearedTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The last time that the statistics were reset

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The alias of the interface

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**RoutingDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the routing domain

**Windows Server 2012:** This property is not available before Windows Server 2012 R2.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**RxRateKbps**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rate of received bytes, in Kbps

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**RxRateLimitedPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of receive packets dropped due to rate limiting

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**RxTotalPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of receive packets dropped

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**TimeoutErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time-out errors on the port

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**TxRateKbps**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The rate of transmitted bytes, in Kbps

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**TxRateLimitedPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of transmit packets dropped due to rate limiting

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> <dt>

**TxTotalPacketsDropped**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of transmit packets dropped

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

This property is inherited from [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md)
</dt> <dt>

[RAMgmtPSProvider Provider Classes](remote-access-management.md)
</dt> </dl>

 

 





