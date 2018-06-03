---
title: Get method of the PS\_BgpStatistics class
description: Retrieves the BGP peering message and route advertisement statistics for a set of peers.
audience: developer
ms.assetid: b9d00b81-8a2a-4969-aa5f-94c87bf438ed
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpStatistics class
- PS_BgpStatistics class, Get method
topic_type:
- apiref
api_name:
- PS_BgpStatistics.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_BgpStatistics class

Retrieves the BGP peering message and route advertisement statistics for a set of peers.

## Syntax


```mof
uint32 Get(
  [in]  string        RoutingDomain,
  [in]  string        PeerName[],
  [out] BgpStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user defined alphanumeric ID of the routing domain that hosts the route advertisement.

</dd> <dt>

*PeerName* \[in\]
</dt> <dd>

An array that contains the peer names associated with the statistics.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpStatistics**](bgpstatistics.md) object that receives the updates set of statistics.

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

[**PS\_BgpStatistics**](ps-bgpstatistics.md)
</dt> </dl>

 

 





