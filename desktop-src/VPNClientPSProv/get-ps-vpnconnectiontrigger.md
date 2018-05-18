---
title: Get method of the PS\_VpnConnectionTrigger class
description: Returns the trigger properties of a VPN connection.
audience: developer
ms.assetid: '7BF92F5E-B6AD-451C-A881-CE81CA89EF1C'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_VpnConnectionTrigger class", "PS_VpnConnectionTrigger class, Get method"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionTrigger.Get
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_VpnConnectionTrigger class

Returns the trigger properties of a VPN connection.

## Syntax


```mof
uint32 Get(
  [in]  string               ConnectionName,
  [out] VpnConnectionTrigger cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTrigger**](vpnconnectiontrigger.md) object (the trigger properties of the VPN connection).

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionTrigger**](ps-vpnconnectiontrigger.md)
</dt> </dl>

 

 





