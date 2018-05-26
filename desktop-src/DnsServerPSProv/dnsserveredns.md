---
title: DnsServerEDns class
description: DNS Server Extended DNS, EDNS RFC2671.
audience: developer
ms.assetid: a71e24a2-f417-4226-814a-e3bfe208fe19
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerEDns class
- DnsServerEDns class, described
topic_type:
- apiref
api_name:
- DnsServerEDns
- DnsServerEDns.EnableProbes
- DnsServerEDns.EnableReception
- DnsServerEDns.CacheTimeout
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerEDns class

DNS Server Extended DNS, EDNS RFC2671.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerEDns
{
  boolean  EnableProbes;
  boolean  EnableReception;
  datetime CacheTimeout;
};
```

## Members

The **DnsServerEDns** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerEDns** class has these properties.

<dl> <dt>

**CacheTimeout**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the number of seconds that Extended DNS (EDNS) information is cached. The minimum value is 3600, and the maximum value is 15,724,800. The default value is 604,800 seconds (one week).

</dd> <dt>

**EnableProbes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables or disables the server to probe other servers to determine if they support EDNS

</dd> <dt>

**EnableReception**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A Boolean value that indicates whether the DNS server will accept queries that contain an EDNS record

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

 

 





