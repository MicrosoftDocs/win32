---
title: Set method of the PS\_BgpRoutingPolicyForPeer class
description: Updates an existing set of BGP routing policy assignments for a set of BGP peers.
audience: developer
ms.assetid: d79400de-db8c-49bd-bd98-0b1975829f8a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_BgpRoutingPolicyForPeer class
- PS_BgpRoutingPolicyForPeer class, Set method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicyForPeer.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_BgpRoutingPolicyForPeer class

Updates an existing set of BGP routing policy assignments for a set of BGP peers.

## Syntax


```mof
uint32 Set(
  [in] string  PolicyName[],
  [in] string  PeerName[],
  [in] uint32  Direction,
  [in] boolean Force,
  [in] string  RoutingDomain
);
```



## Parameters

<dl> <dt>

*PolicyName* \[in\]
</dt> <dd>

An array that contains the IDs of the routing policies in the list.

</dd> <dt>

*PeerName* \[in\]
</dt> <dd>

An array that contains the names of the peers to assign to the routing policies.

</dd> <dt>

*Direction* \[in\]
</dt> <dd>

The direction of the route advertisements for the routing policies.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt with this procedure.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user defined alphanumeric ID of the routing domain.

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

[**PS\_BgpRoutingPolicyForPeer**](ps-bgproutingpolicyforpeer.md)
</dt> </dl>

 

 





