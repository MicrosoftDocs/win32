---
title: PS\_DnsServerResponseRateLimitingExceptionlist class
description: DNS Server response rate limiting exception list.
audience: developer
ms.assetid: 7c990ebe-55fa-4382-a936-addef14bd231
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResponseRateLimitingExceptionlist class
- PS_DnsServerResponseRateLimitingExceptionlist class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimitingExceptionlist
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerResponseRateLimitingExceptionlist class

DNS Server response rate limiting exception list.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResponseRateLimitingExceptionlist
{
};
```

## Members

The **PS\_DnsServerResponseRateLimitingExceptionlist** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResponseRateLimitingExceptionlist** class has these methods.



| Method                                                                 | Description                                                                |
|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**Add**](ps-dnsserverresponseratelimitingexceptionlist-add.md)       | Adds a response rate limiting exception list on the DNS server.<br/> |
| [**Get**](ps-dnsserverresponseratelimitingexceptionlist-get.md)       | Enumerates the RRL exception lists on the DNS Server.<br/>           |
| [**Remove**](ps-dnsserverresponseratelimitingexceptionlist-remove.md) | Removes a RRL exception list from the DNS server. <br/>              |
| [**Set**](ps-dnsserverresponseratelimitingexceptionlist-set.md)       | Updates the settings of a RRL exception list.<br/>                   |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





