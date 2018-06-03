---
title: Get method of the PS\_BgpRoutingPolicy class
description: Retrieves configuration information from the policy store, for one or more BGP routing policies.
audience: developer
ms.assetid: 0835cbfd-8039-4b15-9ae1-54b578dab71f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_BgpRoutingPolicy class
- PS_BgpRoutingPolicy class, Get method
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicy.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_BgpRoutingPolicy class

Retrieves configuration information from the policy store, for one or more BGP routing policies.

## Syntax


```mof
uint32 Get(
  [in]  string                 Name[],
  [in]  uint32                 PolicyType,
  [in]  string                 RoutingDomain,
  [out] BgpRoutingPolicyConfig cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

An array that contains the policy IDs that to retrieve from the policy store.

</dd> <dt>

*PolicyType* \[in\]
</dt> <dd>

The type of BGP routing policies to retrieve.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined alphanumeric ID of the routing domain.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**BgpRoutingPolicyConfig**](bgproutingpolicyconfig.md) object that receives the retrieved configuration information.

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

[**PS\_BgpRoutingPolicy**](ps-bgproutingpolicy.md)
</dt> </dl>

 

 





