---
title: Get method of the PS\_VpnS2SInterface class
description: Retrieves statistics of an S2S Interface.
audience: developer
ms.assetid: '62df9c75-7223-4bbe-ad0f-dd26cc29363a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_VpnS2SInterface class", "PS_VpnS2SInterface class, Get method"]
topic_type:
- apiref
api_name:
- PS_VpnS2SInterface.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_VpnS2SInterface class

Retrieves statistics of an S2S Interface.

## Syntax


```mof
uint32 Get(
  [in]  string          Name,
  [in]  string          RoutingDomain,
  [out] VpnS2SInterface cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the connection.

</dd> <dt>

*RoutingDomain* \[in\]
</dt> <dd>

**Windows Server 2012:** This parameter is unavailable until Windows Server 2012 R2.

The name of the routing domain.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**VpnS2SInterface**](ps-vpns2sinterface.md) object that receives the retrieved statistics.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterface**](ps-vpns2sinterface.md)
</dt> </dl>

 

 





