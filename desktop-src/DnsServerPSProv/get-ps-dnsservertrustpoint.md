---
title: Get method of the PS\_DnsServerTrustPoint class
description: Retrieves Trust points on the server.
audience: developer
ms.assetid: 852b08de-3db4-4d38-aeb9-914391d51e8c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DnsServerTrustPoint class
- PS_DnsServerTrustPoint class, Get method
topic_type:
- apiref
api_name:
- PS_DnsServerTrustPoint.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_DnsServerTrustPoint class

Retrieves Trust points on the server

## Syntax


```mof
uint32 Get(
  [in]  string              Name[],
  [in]  string              ComputerName,
  [out] DnsServerTrustPoint cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

One or more embedded instances of the [**DnsServerTrustPoint**](dnsservertrustpoint.md) class.

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

[**PS\_DnsServerTrustPoint**](ps-dnsservertrustpoint.md)
</dt> </dl>

 

 





