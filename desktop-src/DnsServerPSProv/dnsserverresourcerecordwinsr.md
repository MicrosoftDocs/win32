---
title: DnsServerResourceRecordWinsR class
description: Represents a WINS-R reverse lookup resource record on DNS server.
audience: developer
ms.assetid: 7befd602-e8f8-46bf-a327-0290e97965f1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordWinsR class
- DnsServerResourceRecordWinsR class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordWinsR
- DnsServerResourceRecordWinsR.Replicate
- DnsServerResourceRecordWinsR.LookupTimeout
- DnsServerResourceRecordWinsR.CacheTimeout
- DnsServerResourceRecordWinsR.ResultDomain
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordWinsR class

Represents a WINS-R reverse lookup resource record on DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordWinsR : DnsServerResourceRecordData
{
  boolean  Replicate;
  datetime LookupTimeout;
  datetime CacheTimeout;
  string   ResultDomain;
};
```

## Members

The **DnsServerResourceRecordWinsR** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordWinsR** class has these properties.

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

**ResultDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
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

 

 





