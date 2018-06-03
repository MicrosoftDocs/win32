---
title: Remove method of the PS\_BgpRoutingPolicyForPeer class
description: Removes a set of BGP routing policies from a set of BGP peers.
audience: developer
ms.assetid: 83b1e244-eb02-4dfb-a3bf-a83be0817d98
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_BgpRoutingPolicyForPeer class
- PS_BgpRoutingPolicyForPeer class, Remove method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicyForPeer.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_BgpRoutingPolicyForPeer class

Removes a set of BGP routing policies from a set of BGP peers.

## Syntax


```mof
uint32 Remove(
  [in] string  PeerName[],
  [in] string  PolicyName[],
  [in] uint32  Direction,
  [in] boolean Force,
  [in] string  RoutingDomain
);
```



## Parameters

<dl> <dt>

*PeerName* \[in\]
</dt> <dd>

An array that contains the names of the peers.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

An array that contains the IDs of the routing policies to remove from the peers.

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

 

 





