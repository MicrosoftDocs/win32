---
title: DnsServerQuery2Statistics class
description: Represents DNS server statistics related to internal server processing.
audience: developer
ms.assetid: 048d1776-fc10-4567-9c92-de73e149c12c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerQuery2Statistics class
- DnsServerQuery2Statistics class, described
topic_type:
- apiref
api_name:
- DnsServerQuery2Statistics
- DnsServerQuery2Statistics.TotalQueries
- DnsServerQuery2Statistics.Standard
- DnsServerQuery2Statistics.Notify
- DnsServerQuery2Statistics.Update
- DnsServerQuery2Statistics.TKeyNego
- DnsServerQuery2Statistics.TypeA
- DnsServerQuery2Statistics.TypeNs
- DnsServerQuery2Statistics.TypeSoa
- DnsServerQuery2Statistics.TypeMx
- DnsServerQuery2Statistics.TypePtr
- DnsServerQuery2Statistics.TypeSrv
- DnsServerQuery2Statistics.TypeAll
- DnsServerQuery2Statistics.TypeIxfr
- DnsServerQuery2Statistics.TypeAxfr
- DnsServerQuery2Statistics.TypeOther
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerQuery2Statistics class

Represents DNS server statistics related to internal server processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerQuery2Statistics
{
  uint32 TotalQueries;
  uint32 Standard;
  uint32 Notify;
  uint32 Update;
  uint32 TKeyNego;
  uint32 TypeA;
  uint32 TypeNs;
  uint32 TypeSoa;
  uint32 TypeMx;
  uint32 TypePtr;
  uint32 TypeSrv;
  uint32 TypeAll;
  uint32 TypeIxfr;
  uint32 TypeAxfr;
  uint32 TypeOther;
};
```

## Members

The **DnsServerQuery2Statistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerQuery2Statistics** class has these properties.

<dl> <dt>

**Notify**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of zone notification requests received by the server.

</dd> <dt>

**Standard**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of standard DNS queries received by the server

</dd> <dt>

**TKeyNego**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TKEY, RFC2930, and negotiation requests received by the server.

</dd> <dt>

**TotalQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received by the server.

</dd> <dt>

**TypeA**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_A.

</dd> <dt>

**TypeAll**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_ALL.

</dd> <dt>

**TypeAxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_AXFR.

</dd> <dt>

**TypeIxfr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_IXFR.

</dd> <dt>

**TypeMx**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_MX.

</dd> <dt>

**TypeNs**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_NS.

</dd> <dt>

**TypeOther**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for other types of record.

</dd> <dt>

**TypePtr**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_PTR.

</dd> <dt>

**TypeSoa**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_SOA.

</dd> <dt>

**TypeSrv**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received for record type DNS\_TYPE\_SRV.

</dd> <dt>

**Update**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of dynamic update requests received by the server.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





