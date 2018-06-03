---
title: Remove method of the PS\_VpnSstpProxyRule class
description: Removes one or more Tenant ID to Gateway mappings for the SSTP proxy.
audience: developer
ms.assetid: 5f9e7456-4243-4c1e-93f1-7ebeb7497823
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_VpnSstpProxyRule class
- PS_VpnSstpProxyRule class, Remove method
topic_type:
- apiref
api_name:
- PS_VpnSstpProxyRule.Remove
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the PS\_VpnSstpProxyRule class

Removes one or more Tenant ID to Gateway mappings for the SSTP proxy.

## Syntax


```mof
uint32 Remove(
  [in] string  TenantID[],
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*TenantID* \[in\]
</dt> <dd>

The Tenant or Group ID to configure the SSTP proxy mapping.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnSstpProxyRule**](ps-vpnsstpproxyrule.md)
</dt> </dl>

 

 





