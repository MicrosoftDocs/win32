---
title: DnsServerZoneTransferStatistics class
description: Represents zone transfer statistics for the specified transfer type.
audience: developer
ms.assetid: efbcccce-aeaa-46ff-bc66-9c7bce6cd9f3
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerZoneTransferStatistics class
- DnsServerZoneTransferStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerZoneTransferStatistics
- DnsServerZoneTransferStatistics.TransferType
- DnsServerZoneTransferStatistics.RequestReceived
- DnsServerZoneTransferStatistics.RequestSent
- DnsServerZoneTransferStatistics.ResponseReceived
- DnsServerZoneTransferStatistics.SuccessReceived
- DnsServerZoneTransferStatistics.SuccessSent
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerZoneTransferStatistics class

Represents zone transfer statistics for the specified transfer type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerZoneTransferStatistics
{
  string TransferType;
  uint64 RequestReceived;
  uint64 RequestSent;
  uint64 ResponseReceived;
  uint64 SuccessReceived;
  uint64 SuccessSent;
};
```

## Members

The **DnsServerZoneTransferStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerZoneTransferStatistics** class has these properties.

<dl> <dt>

**RequestReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone transfer requests received by the primary server of the zone.

</dd> <dt>

**RequestSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone transfer requests sent by the secondary server of the zone.

</dd> <dt>

**ResponseReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone transfer responses received by the secondary server of the zone.

</dd> <dt>

**SuccessReceived**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of successful zone transfers received by the secondary server of the zone.

</dd> <dt>

**SuccessSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of successful zone transfers sent by the primary server of the zone.

</dd> <dt>

**TransferType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The transfer type of the zone statistics.

The possible values are.

<dt>

<span id="AXFR"></span><span id="axfr"></span>

**AXFR** ("ZONE\_STATS\_TYPE\_TRANSFER\_AXFR")


</dt> <dd></dd> <dt>

<span id="IXFR"></span><span id="ixfr"></span>

**IXFR** ("ZONE\_STATS\_TYPE\_TRANSFER\_IXFR")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





