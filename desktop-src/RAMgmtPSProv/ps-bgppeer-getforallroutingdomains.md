---
title: GetForAllRoutingDomains method of the PS\_BgpPeer class
description: Retrieves the BGP Peer configuration information for all BGP peers from all routing domains.
audience: developer
ms.assetid: '08ff73cd-2722-4037-b7be-233d8a6a175f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetForAllRoutingDomains method", "GetForAllRoutingDomains method, PS_BgpPeer class", "PS_BgpPeer class, GetForAllRoutingDomains method"]
topic_type:
- apiref
api_name:
- PS_BgpPeer.GetForAllRoutingDomains
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# GetForAllRoutingDomains method of the PS\_BgpPeer class

Retrieves the BGP Peer configuration information for all BGP peers from all routing domains.

## Syntax


```mof
uint32 GetForAllRoutingDomains(
  [in]  boolean       AllRoutingDomains,
  [out] BgpPeerConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*AllRoutingDomains* \[in\]
</dt> <dd>

**true** to retrieve peers for all routing domains.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains a [**BgpPeerConfig**](bgppeerconfig.md) that describes the peer configuration information.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpPeer**](ps-bgppeer.md)
</dt> </dl>

 

 





