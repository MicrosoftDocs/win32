---
title: New method of the PS\_VpnSstpProxyRule class
description: Creates a tenant ID to gateway mapping object.
audience: developer
ms.assetid: 480a768f-20ff-4cc0-a76c-c8511461ec9f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- New method
- New method, PS_VpnSstpProxyRule class
- PS_VpnSstpProxyRule class, New method
topic_type:
- apiref
api_name:
- PS_VpnSstpProxyRule.New
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# New method of the PS\_VpnSstpProxyRule class

Creates a tenant ID to gateway mapping object.

## Syntax


```mof
uint32 New(
  [in]  string           TenantID,
  [in]  string           GatewayAddress[],
  [out] VpnSstpProxyRule cmdletOutput
);
```



## Parameters

<dl> <dt>

*TenantID* \[in\]
</dt> <dd>

The Tenant or Group ID to configure the SSTP proxy mapping.

</dd> <dt>

*GatewayAddress* \[in\]
</dt> <dd>

List of gateway IP address, or the name for the tenant.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the current object.

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

 

 





