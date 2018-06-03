---
title: Get method of the PS\_BgpPeer class
description: Retrieves configuration information for BGP peers.
audience: developer
ms.assetid: 143ef27b-46d5-49d8-a74c-b5fd59554441
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpPeer class
- PS_BgpPeer class, Get method
topic_type:
- apiref
api_name:
- PS_BgpPeer.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_BgpPeer class

Retrieves configuration information for BGP peers.

## Syntax


```mof
uint32 Get(
  [in]  string        Name[],
  [in]  string        RoutingDomain,
  [out] BgpPeerConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The BGP peer names that identify the configuration information to retrieve.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpPeerConfig**](bgppeerconfig.md) object that receives the configuration information for the BGP peers.

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

 

 





