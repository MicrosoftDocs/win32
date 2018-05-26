---
title: Add method of the PS\_VpnSstpProxyRule class
description: Adds a tenant ID to a gateway mapping.
audience: developer
ms.assetid: 5f996a21-5570-472a-8985-21aca44390aa
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_VpnSstpProxyRule class
- PS_VpnSstpProxyRule class, Add method
topic_type:
- apiref
api_name:
- PS_VpnSstpProxyRule.Add
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Add method of the PS\_VpnSstpProxyRule class

Adds a tenant ID to a gateway mapping.

## Syntax


```mof
uint32 Add(
  [in]  VpnSstpProxyRule Rule[],
  [in]  boolean          PassThru,
  [out] VpnSstpProxyRule cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Rule* \[in\]
</dt> <dd>

The Tenant or Group ID to configure the SSTP proxy mapping.

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

 

 





