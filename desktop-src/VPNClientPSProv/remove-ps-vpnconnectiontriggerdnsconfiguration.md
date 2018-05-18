---
title: Remove method of the PS\_VpnConnectionTriggerDnsConfiguration class
description: Removes DNS suffixes and the corresponding DNS servers from the configuration.
audience: developer
ms.assetid: 'B8B87ABB-F4F5-4700-81AE-99488A95E576'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_VpnConnectionTriggerDnsConfiguration class", "PS_VpnConnectionTriggerDnsConfiguration class, Remove method"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionTriggerDnsConfiguration.Remove
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# Remove method of the PS\_VpnConnectionTriggerDnsConfiguration class

Removes DNS suffixes and the corresponding DNS servers from the configuration.

## Syntax


```mof
uint32 Remove(
  [in]  string                               ConnectionName,
  [in]  string                               DnsSuffix[],
  [in]  boolean                              PassThru,
  [in]  boolean                              Force,
  [out] VpnConnectionTriggerDnsConfiguration cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile to modify.

</dd> <dt>

*DnsSuffix* \[in\]
</dt> <dd>

The DNS suffixes.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) object that contains the DNS configuration for VPN triggering; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the removal of the Name Resolution Policy Table (NRPT) rule from the VPN profile; otherwise, **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionTriggerDnsConfiguration**](vpnconnectiontriggerdnsconfiguration.md) objects that holds the DNS configurations for VPN triggering.

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

[**PS\_VpnConnectionTriggerDnsConfiguration**](ps-vpnconnectiontriggerdnsconfiguration.md)
</dt> </dl>

 

 





