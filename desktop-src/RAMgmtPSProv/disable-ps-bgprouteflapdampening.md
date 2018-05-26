---
title: Disable method of the PS\_BgpRouteFlapDampening class
description: Stops performing route Dampening for the flapping BGP routes.
audience: developer
ms.assetid: 3c8a7a28-0a13-4431-87cf-c8db36deb1ca
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method
- Disable method, PS_BgpRouteFlapDampening class
- PS_BgpRouteFlapDampening class, Disable method
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening.Disable
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Disable method of the PS\_BgpRouteFlapDampening class

stops performing route Dampening for the flapping BGP routes.

## Syntax


```mof
uint32 Disable(
  [in] string  RoutingDomain,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

User-defined unique alphanumeric identifier for the routing domain or tenant.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** for no confirmation prompt for stopping the route flap dampening engine. The default is **false**.

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

 

 





