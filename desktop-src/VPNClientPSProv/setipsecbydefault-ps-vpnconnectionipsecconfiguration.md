---
title: SetIpSecByDefault method of the PS\_VpnConnectionIPsecConfiguration class
description: Removes the IPsec custom policy configuration and restores the default configuration of a VPN profile.
audience: developer
ms.assetid: 649FBE1E-C7C0-4B29-BC9C-70919246A7AE
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetIpSecByDefault method
- SetIpSecByDefault method, PS_VpnConnectionIPsecConfiguration class
- PS_VpnConnectionIPsecConfiguration class, SetIpSecByDefault method
topic_type:
- apiref
api_name:
- PS_VpnConnectionIPsecConfiguration.SetIpSecByDefault
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetIpSecByDefault method of the PS\_VpnConnectionIPsecConfiguration class

Removes the IPsec custom policy configuration and restores the default configuration of a VPN profile.

## Syntax


```mof
uint32 SetIpSecByDefault(
  [in]  string                          ConnectionName,
  [in]  boolean                         RevertToDefault,
  [in]  boolean                         PassThru,
  [in]  boolean                         Force,
  [in]  boolean                         AllUserConnection,
  [out] VpnConnectionIPsecConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile.

</dd> <dt>

*RevertToDefault* \[in\]
</dt> <dd>

**true** to set the IPsec parameters to default values; otherwise, **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the [**VpnConnectionIPsecConfiguration**](vpnconnectionipsecconfiguration.md) object; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to force the modification of IPsec configuration of the VPN profile; otherwise, **false**.

</dd> <dt>

*AllUserConnection* \[in\]
</dt> <dd>

**True** if the VPN connection profile is for all users; **false** if it is for a single user.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**VpnConnectionIPsecConfiguration**](vpnconnectionipsecconfiguration.md) object. The destination **EncryptionMethod**, **IntegrityCheckMethod**, **CipherTransformConstants**, **DHGroup**, **AuthenticationTransformConstants** and **PfsGroup** fields are populated.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnConnectionIPsecConfiguration**](ps-vpnconnectionipsecconfiguration.md)
</dt> </dl>

 

 





