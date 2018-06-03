---
title: Get method of the PS\_DnsServerResponseRateLimiting class
description: Gets the response rate limiting on a DNS server.
audience: developer
ms.assetid: 6a374bfd-3771-4fee-b29d-9b91beaaf2d2
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerResponseRateLimiting class
- PS_DnsServerResponseRateLimiting class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerResponseRateLimiting.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerResponseRateLimiting class

Gets the response rate limiting on a DNS server.

## Syntax


```mof
uint32 Get(
  [in]  string                        ComputerName,
  [out] DnsServerResponseRateLimiting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerResponseRateLimiting**](dnsserverresponseratelimiting.md) object that contains the response rate limiting (RRL) for a DNS server.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerResponseRateLimiting**](ps-dnsserverresponseratelimiting.md)
</dt> </dl>

 

 





