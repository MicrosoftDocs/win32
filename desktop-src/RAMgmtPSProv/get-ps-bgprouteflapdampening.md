---
title: Get method of the PS\_BgpRouteFlapDampening class
description: Retrieves the configuration of BGP Route dampening engine.
audience: developer
ms.assetid: bb25756a-6492-4c39-be8e-781120cd0146
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpRouteFlapDampening class
- PS_BgpRouteFlapDampening class, Get method
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_BgpRouteFlapDampening class

Retrieves the configuration of BGP Route dampening engine.

## Syntax


```mof
uint32 Get(
  [in]  string                      RoutingDomain,
  [out] BgpRouteFlapDampeningConfig cmdletOutput
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

User-defined unique alphanumeric identifier for the Routing domain or tenant.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the current object.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpRouteFlapDampening**](ps-bgprouteflapdampening.md)
</dt> </dl>

 

 





