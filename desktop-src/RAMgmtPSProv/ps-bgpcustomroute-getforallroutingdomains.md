---
title: GetForAllRoutingDomains method of the PS\_BgpCustomRoute class
description: Retrieves the custom/administrator-configured route information from the BGP routing table for all routing domains.
audience: developer
ms.assetid: '8321a51e-5d77-4630-be22-c0eb99cc014d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetForAllRoutingDomains method", "GetForAllRoutingDomains method, PS_BgpCustomRoute class", "PS_BgpCustomRoute class, GetForAllRoutingDomains method"]
topic_type:
- apiref
api_name:
- PS_BgpCustomRoute.GetForAllRoutingDomains
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# GetForAllRoutingDomains method of the PS\_BgpCustomRoute class

Retrieves the custom/administrator-configured route information from the BGP routing table for all routing domains.

## Syntax


```mof
uint32 GetForAllRoutingDomains(
  [in]  boolean              AllRoutingDomains,
  [out] BgpCustomNetworkInfo cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*AllRoutingDomains* \[in\]
</dt> <dd>

**true** to return the custom/administrator-configured route information for all routing domains.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On success, contains a [**BgpCustomNetworkInfo**](bgpcustomnetworkinfo.md) that describes the custom network information.

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

[**PS\_BgpCustomRoute**](ps-bgpcustomroute.md)
</dt> </dl>

 

 





