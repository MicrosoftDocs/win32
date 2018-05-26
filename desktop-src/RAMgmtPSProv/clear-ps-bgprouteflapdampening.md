---
title: Clear method of the PS\_BgpRouteFlapDampening class
description: Clears the route dampening information for the specified set of BGP routes.
audience: developer
ms.assetid: a6422eb6-7a50-4893-82b3-fff0bdf22901
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Clear method
- Clear method, PS_BgpRouteFlapDampening class
- PS_BgpRouteFlapDampening class, Clear method
topic_type:
- apiref
api_name:
- PS_BgpRouteFlapDampening.Clear
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Clear method of the PS\_BgpRouteFlapDampening class

Clears the route dampening information for the specified set of BGP routes.

## Syntax


```mof
uint32 Clear(
  [in] string  RoutingDomain,
  [in] boolean Force,
  [in] string  Prefix[]
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

**true** for no confirmation prompt for clearing route flap dampening from the specified set of BGP routes. The default is **false**.

</dd> <dt>

*Prefix* \[in\]
</dt> <dd>

A list of the classless IP address prefixes and their prefix lengths, for which the flap dampening is to be cleared / reset.

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

 

 





