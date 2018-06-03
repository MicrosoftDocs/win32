---
title: Get method of the PS\_DnsServerTrustAnchor class
description: Retrieves TAs on the server.
audience: developer
ms.assetid: cbb778a4-984e-46cf-9fd7-a394504e2866
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerTrustAnchor class
- PS_DnsServerTrustAnchor class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DnsServerTrustAnchor class

Retrieves TAs on the server.

## Syntax


```mof
uint32 Get(
  [in]  string               ComputerName,
  [in]  string               Name,
  [out] DnsServerTrustAnchor cmdletOutput[]
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

Name of the trust anchor.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

One or more embedded instances of the [**DnsServerTrustAnchor**](dnsservertrustanchor.md) class.

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

[**PS\_DnsServerTrustAnchor**](ps-dnsservertrustanchor.md)
</dt> </dl>

 

 





