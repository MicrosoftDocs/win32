---
title: Stop method of the PS\_BgpPeer class
description: Stops a BGP routing session for one or more peers.
audience: developer
ms.assetid: a993f66c-fea5-4743-ac66-99abb9dc8f02
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Stop method
- Stop method, PS_BgpPeer class
- PS_BgpPeer class, Stop method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Stop
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Stop method of the PS\_BgpPeer class

Stops a BGP routing session for one or more peers.

## Syntax


```mof
uint32 Stop(
  [in] string  Name[],
  [in] string  RoutingDomain,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The BGP peer names that identify the peers in the routing session.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether to use a confirmation prompt to stop the routing session. **True** to use a confirmation prompt; otherwise **false**.

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

 

 





