---
title: Get method of the PS\_BgpCustomRoute class
description: Retrieves custom BGP routing information from a BGP routing table.
audience: developer
ms.assetid: a57f2e07-1639-4a81-8547-55cd987e0b9c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpCustomRoute class
- PS_BgpCustomRoute class, Get method
topic_type:
- apiref
api_name:
- PS_BgpCustomRoute.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_BgpCustomRoute class

Retrieves custom BGP routing information from a BGP routing table.

## Syntax


```mof
uint32 Get(
  [in]  string               RoutingDomain,
  [out] BgpCustomNetworkInfo cmdletOutput
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

Routing domain ID/ Tenant IDfor which the BGP custom route information is to be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the [**BgpCustomNetworkInfo**](bgpcustomnetworkinfo.md) object that contains the custom routing information.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpCustomRoute**](ps-bgpcustomroute.md)
</dt> </dl>

 

 





