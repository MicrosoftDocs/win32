---
title: SetByCustomPolicy method of the PS\_VpnConnectionIPsecConfiguration class
description: Sets the IPsec custom policy configuration of a VPN profile.
audience: developer
ms.assetid: '7806F44D-8084-408D-B8FE-513287544DFC'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByCustomPolicy method", "SetByCustomPolicy method, PS_VpnConnectionIPsecConfiguration class", "PS_VpnConnectionIPsecConfiguration class, SetByCustomPolicy method"]
topic_type:
- apiref
api_name:
- PS_VpnConnectionIPsecConfiguration.SetByCustomPolicy
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# SetByCustomPolicy method of the PS\_VpnConnectionIPsecConfiguration class

Sets the IPsec custom policy configuration of a VPN profile.

## Syntax


```mof
uint32 SetByCustomPolicy(
  [in]  string                          ConnectionName,
  [in]  uint32                          AuthenticationTransformConstants,
  [in]  uint32                          CipherTransformConstants,
  [in]  uint32                          EncryptionMethod,
  [in]  uint32                          IntegrityCheckMethod,
  [in]  uint32                          PfsGroup,
  [in]  uint32                          DHGroup,
  [in]  boolean                         PassThru,
  [in]  boolean                         Force,
  [in]  boolean                         AllUserConnection,
  [out] VpnConnectionIPsecConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*ConnectionName* \[in\]
</dt> <dd>

The name of the VPN connection profile.

</dd> <dt>

*AuthenticationTransformConstants* \[in\]
</dt> <dd>

The authentication transform plumbed in IPsec policy.

</dd> <dt>

*CipherTransformConstants* \[in\]
</dt> <dd>

The cipher transform plumbed in IPsec Policy.

</dd> <dt>

*EncryptionMethod* \[in\]
</dt> <dd>

The encryption method plumbed in IPsec policy.

</dd> <dt>

*IntegrityCheckMethod* \[in\]
</dt> <dd>

The integrity method plumbed in IPsec policy.

</dd> <dt>

*PfsGroup* \[in\]
</dt> <dd>

The PFS group plumbed in IPsec policy.

</dd> <dt>

*DHGroup* \[in\]
</dt> <dd>

The DH Group plumbed in IPsec policy.

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

When this method returns, contains the [**VpnConnectionIPsecConfiguration**](vpnconnectionipsecconfiguration.md) object. These destination fields are populated: **EncryptionMethod**, **IntegrityCheckMethod**, **CipherTransformConstants**, **DHGroup**, **AuthenticationTransformConstants** and **PfsGroup** .

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

[**PS\_VpnConnectionIPsecConfiguration**](ps-vpnconnectionipsecconfiguration.md)
</dt> </dl>

 

 





