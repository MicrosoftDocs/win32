---
title: Get method of the PS\_BgpRouter class
description: Retrieves the configuration information of a BGP router.
audience: developer
ms.assetid: 220df461-95dc-462f-bb64-7cdf14723ea1
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpRouter class
- PS_BgpRouter class, Get method
topic_type:
- apiref
api_name:
- PS_BgpRouter.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_BgpRouter class

Retrieves the configuration information of a BGP router.

## Syntax


```mof
uint32 Get(
  [in]  string          RoutingDomain[],
  [out] BgpRouterConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The unique identifiers of the tenants that manage the BGP router.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRouterConfig**](bgprouterconfig.md) objects to receive the configuration information.

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

[**PS\_BgpRouter**](ps-bgprouter.md)
</dt> </dl>

 

 





