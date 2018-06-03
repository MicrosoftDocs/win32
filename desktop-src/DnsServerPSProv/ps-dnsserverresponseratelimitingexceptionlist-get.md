---
title: Get method of the PS\_DnsServerResponseRateLimitingExceptionlist class
description: The Get-DnsServerResponseRateExceptionlist cmdlet enumerates the RRL exceptionlists on the DNS Server.
audience: developer
ms.assetid: 84e439c5-5675-4420-a080-43a41357bcc9
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerResponseRateLimitingExceptionlist class
- PS_DnsServerResponseRateLimitingExceptionlist class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimitingExceptionlist.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerResponseRateLimitingExceptionlist class

The Get-DnsServerResponseRateExceptionlist cmdlet enumerates the RRL exceptionlists on the DNS Server.

## Syntax


```mof
uint32 Get(
  [in]  string                                     ComputerName,
  [in]  string                                     Name,
  [out] DnsServerResponseRateLimitingExceptionlist cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the RRL exception list.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an array of [**DnsServerResponseRateLimitingExceptionlist**](dnsserverresponseratelimitingexceptionlist.md) embedded instances, which have the following fields:

-   Name
-   Condition
-   ClientSubNet
-   Fqdn
-   ServerInterfaceIP

This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResponseRateLimitingExceptionlist**](ps-dnsserverresponseratelimitingexceptionlist.md)
</dt> </dl>

 

 





