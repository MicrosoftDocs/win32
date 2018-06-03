---
title: PS\_DnsServerResourceRecordAAAA class
description: Represents a AAAA resource record on a DNS server.
audience: developer
ms.assetid: 9b894486-ce70-4502-b82d-242cc30f5e81
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordAAAA class
- PS_DnsServerResourceRecordAAAA class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordAAAA
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerResourceRecordAAAA class

Represents a AAAA resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordAAAA
{
};
```

## Members

The **PS\_DnsServerResourceRecordAAAA** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordAAAA** class has these methods.



| Method                                            | Description                                             |
|:--------------------------------------------------|:--------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecordaaaa.md) | Adds a AAAA resource record to a DNS server.<br/> |



 

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

 

 





