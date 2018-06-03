---
title: PS\_DnsServerResponseRateLimiting class
description: DNS server response rate limiting.
audience: developer
ms.assetid: 66f7513b-4afd-4ab5-a2f3-8aca6d668475
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResponseRateLimiting class
- PS_DnsServerResponseRateLimiting class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimiting
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerResponseRateLimiting class

DNS server response rate limiting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResponseRateLimiting
{
};
```

## Members

The **PS\_DnsServerResponseRateLimiting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResponseRateLimiting** class has these methods.



| Method                                                                      | Description                                                                |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**Get**](ps-dnsserverresponseratelimiting-get.md)                         | Gets the response rate limiting on a DNS server.<br/>                |
| [**SetDnsServerRRL**](ps-dnsserverresponseratelimiting-setdnsserverrrl.md) | The sets the DNS server response rate limiting on a DNS server.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





