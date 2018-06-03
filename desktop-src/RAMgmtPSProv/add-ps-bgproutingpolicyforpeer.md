---
title: Add method of the PS\_BgpRoutingPolicyForPeer class
description: Assigns a set of BGP routing policies to a set of BGP peers.
audience: developer
ms.assetid: 69bdf47d-631b-471d-85c9-5ea72bb3673a
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_BgpRoutingPolicyForPeer class
- PS_BgpRoutingPolicyForPeer class, Add method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicyForPeer.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_BgpRoutingPolicyForPeer class

Assigns a set of BGP routing policies to a set of BGP peers.

## Syntax


```mof
uint32 Add(
  [in] string  PeerName[],
  [in] string  PolicyName[],
  [in] uint32  Direction,
  [in] string  RoutingDomain,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*PeerName* \[in\]
</dt> <dd>

An array that contains the names of the peers to assign to the routing policies.

</dd> <dt>

*PolicyName* \[in\]
</dt> <dd>

An array that contains the IDs of the routing policies to assign to the peers.

</dd> <dt>

*Direction* \[in\]
</dt> <dd>

The direction of the route advertisements for the routing policies.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user defined alphanumeric ID of the routing domain.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt with this procedure.

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

 

 





