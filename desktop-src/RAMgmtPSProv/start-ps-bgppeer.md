---
title: Start method of the PS\_BgpPeer class
description: Starts a BGP routing session for one or more peers.
audience: developer
ms.assetid: 69e610d3-3a78-43f0-8d6a-e3524382b267
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Start method
- Start method, PS_BgpPeer class
- PS_BgpPeer class, Start method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Start
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Start method of the PS\_BgpPeer class

Starts a BGP routing session for one or more peers.

## Syntax


```mof
uint32 Start(
  [in] string RoutingDomain,
  [in] string Name[]
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The BGP peer names that identify the peers in the routing session.

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

[**PS\_BgpPeer**](ps-bgppeer.md)
</dt> </dl>

 

 





