---
title: Remove method of the PS\_BgpCustomRoute class
description: Removes network prefixes and network interfaces from a BGP routing table.
audience: developer
ms.assetid: 12d25282-faae-45b6-a8b1-e87fc8947aa7
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpCustomRoute class
- PS_BgpCustomRoute class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpCustomRoute.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_BgpCustomRoute class

Removes network prefixes and network interfaces from a BGP routing table.

## Syntax


```mof
uint32 Remove(
  [in] string  Network[],
  [in] string  Interface[],
  [in] boolean Force,
  [in] string  RoutingDomain
);
```



## Parameters

<dl> <dt>

*Network* \[in\]
</dt> <dd>

A list of Classless Inter-Domain Routing (CIDR) IP network prefixes and network masks to remove from the BGP routing table.

</dd> <dt>

*Interface* \[in\]
</dt> <dd>

A list of interface aliases that contain static routes to remove from BGP routing table.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to display a confirmation prompt before removing the custom BGP routes from the BGP routing table. **True** to remove the routes; otherwise **false**.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

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

 

 





