---
title: DnsServerRRLStatistics class
description: DNS server statistics related to the server response rate limiting (RRL).
audience: developer
ms.assetid: 9fd47f26-72c7-43ab-9eb4-1c5315573de3
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRRLStatistics class
- DnsServerRRLStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerRRLStatistics
- DnsServerRRLStatistics.TotalResponsesSent
- DnsServerRRLStatistics.TotalResponsesDropped
- DnsServerRRLStatistics.TotalResponsesLeaked
- DnsServerRRLStatistics.TotalResponsesTruncated
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerRRLStatistics class

DNS server statistics related to the server response rate limiting (RRL).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRRLStatistics
{
  uint64 TotalResponsesSent;
  uint64 TotalResponsesDropped;
  uint64 TotalResponsesLeaked;
  uint64 TotalResponsesTruncated;
};
```

## Members

The **DnsServerRRLStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRRLStatistics** class has these properties.

<dl> <dt>

**TotalResponsesDropped**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses dropped by the DNS server.

</dd> <dt>

**TotalResponsesLeaked**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses leaked by the DNS server.

</dd> <dt>

**TotalResponsesSent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses sent by the DNS server.

</dd> <dt>

**TotalResponsesTruncated**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of responses truncated by the DNS server.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





