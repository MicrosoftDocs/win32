---
title: DnsServerResourceRecordWins class
description: Represents a WINS resource record on a DNS server.
audience: developer
ms.assetid: a800f018-b99a-4c5b-9475-6fba926ad964
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordWins class
- DnsServerResourceRecordWins class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordWins
- DnsServerResourceRecordWins.Replicate
- DnsServerResourceRecordWins.LookupTimeout
- DnsServerResourceRecordWins.CacheTimeout
- DnsServerResourceRecordWins.WinsServers
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordWins class

Represents a WINS resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordWins : DnsServerResourceRecordData
{
  boolean  Replicate;
  datetime LookupTimeout;
  datetime CacheTimeout;
  string   WinsServers[];
};
```

## Members

The **DnsServerResourceRecordWins** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordWins** class has these properties.

<dl> <dt>

**CacheTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The cache timeout value for the resource record.

</dd> <dt>

**LookupTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The lookup timeout for the resource record.

</dd> <dt>

**Replicate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable the replicate mapping flag for the resource record; otherwise, **false**.

</dd> <dt>

**WinsServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array that contains IP addresses of the servers that are assigned to the resource record.

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





