---
title: Set method of the PS\_VpnSstpProxyRule class
description: Modifies a tenant ID to gateway mapping.
audience: developer
ms.assetid: 8312715b-41d8-4a8e-9742-ac5750b556e9
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnSstpProxyRule class
- PS_VpnSstpProxyRule class, Set method
topic_type:
- apiref
api_name:
- PS_VpnSstpProxyRule.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_VpnSstpProxyRule class

Modifies a tenant ID to gateway mapping.

## Syntax


```mof
uint32 Set(
  [in]  string           TenantID,
  [in]  string           GatewayAddress[],
  [in]  boolean          PassThru,
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

List of Gateway IP Address, or the name for the tenant.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to indicate that the method returns an output object. The default is **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

If *PassThru* is **true**, returns an embedded instance of the current object.

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

 

 





