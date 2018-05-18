---
title: Add method of the PS\_BgpCustomRoute class
description: Adds custom BGP routes to a BGP routing table.
audience: developer
ms.assetid: '1acf8fef-3963-4388-9da4-f5fad6d05d81'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Add method", "Add method, PS_BgpCustomRoute class", "PS_BgpCustomRoute class, Add method"]
topic_type:
- apiref
api_name:
- PS_BgpCustomRoute.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Add method of the PS\_BgpCustomRoute class

Adds custom BGP routes to a BGP routing table.

## Syntax


```mof
uint32 Add(
  [in]  boolean              PassThru,
  [in]  string               RoutingDomain,
  [in]  string               Interface[],
  [in]  string               Network[],
  [out] BgpCustomNetworkInfo cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether *cmdletOutput* parameter returns an output object.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

The user-defined unique alphanumeric ID of the routing domain.

</dd> <dt>

*Interface* \[in\]
</dt> <dd>

A list of interface aliases that contain static routes to add to the BGP routing table.

</dd> <dt>

*Network* \[in\]
</dt> <dd>

A list of Classless Inter-Domain Routing (CIDR) IP network prefixes and network masks to add to the BGP routing table.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the [**BgpCustomNetworkInfo**](bgpcustomnetworkinfo.md) object that contains the custom BGP routes.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_BgpCustomRoute**](ps-bgpcustomroute.md)
</dt> </dl>

 

 





