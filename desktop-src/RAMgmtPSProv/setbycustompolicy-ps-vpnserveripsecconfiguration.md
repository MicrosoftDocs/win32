---
title: SetByCustomPolicy method of the PS\_VpnServerIPsecConfiguration class
description: Updates an Internet Protocol Security (IPsec) VPN server configuration for custom policies.
audience: developer
ms.assetid: d5fcb081-3875-47be-9e39-0429e41810dd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByCustomPolicy method
- SetByCustomPolicy method, PS_VpnServerIPsecConfiguration class
- PS_VpnServerIPsecConfiguration class, SetByCustomPolicy method
topic_type:
- apiref
api_name:
- PS_VpnServerIPsecConfiguration.SetByCustomPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByCustomPolicy method of the PS\_VpnServerIPsecConfiguration class

Updates an Internet Protocol Security (IPsec) VPN server configuration for custom policies.

**Windows Server 2012:** The order of the parameters for this method were changed in Windows Server 2012 R2.

## Syntax


```mof
uint32 SetByCustomPolicy(
  [in]  boolean                     PassThru,
  [in]  uint32                      TunnelType,
  [in]  uint32                      IdleDisconnectSeconds,
  [in]  uint32                      SALifeTimeSeconds,
  [in]  uint32                      MMSALifeTimeSeconds,
  [in]  uint32                      SADataSizeForRenegotiationKilobytes,
  [in]  boolean                     CustomPolicy,
  [in]  uint32                      EncryptionMethod,
  [in]  uint32                      IntegrityCheckMethod,
  [in]  uint32                      SstpPorts,
  [in]  uint32                      CipherTransformConstants,
  [in]  uint32                      PfsGroup,
  [in]  uint32                      AuthenticationTransformConstants,
  [in]  uint32                      DHGroup,
  [in]  uint32                      Ikev2Ports,
  [in]  uint32                      L2tpPorts,
  [in]  uint32                      GrePorts,
  [out] VpnServerIPsecConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the [**VpnServerIPsecConfiguration**](vpnserveripsecconfiguration.md) parameter returns an object.

</dd> <dt>

*TunnelType* \[in\]
</dt> <dd>

The tunnel type of the server configuration.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*IdleDisconnectSeconds* \[in\]
</dt> <dd>

A value that specifies the time, in seconds, after which an idle connection is terminated. Unless the idle time-out is disabled, the entire connection is terminated if the connection is idle for the specified interval.

</dd> <dt>

*SALifeTimeSeconds* \[in\]
</dt> <dd>

Lifetime of a security association (SA) in seconds, after which the SA is no longer valid.

</dd> <dt>

*MMSALifeTimeSeconds* \[in\]
</dt> <dd>

Lifetime of main mode security association (SA) in seconds, after which the MM SA is no longer valid.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is supported starting with Windows Server 2016.

</dd> <dt>

*SADataSizeForRenegotiationKilobytes* \[in\]
</dt> <dd>

The number of kilobytes that are allowed to transfer using a SA. After the transfer, the SA will be renegotiated.

</dd> <dt>

*CustomPolicy* \[in\]
</dt> <dd>

Specifies custom IKE IPsec policies.

</dd> <dt>

*EncryptionMethod* \[in\]
</dt> <dd>

Encryption method plumbed in IKE policy.

</dd> <dt>

*IntegrityCheckMethod* \[in\]
</dt> <dd>

Integrity method plumbed in IPsec policy.

</dd> <dt>

*SstpPorts* \[in\]
</dt> <dd>

The Secure Socket Tunneling Protocol (SSTP) of the VPN tunnel.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*CipherTransformConstants* \[in\]
</dt> <dd>

Cipher plumbed in IPsec policy.

</dd> <dt>

*PfsGroup* \[in\]
</dt> <dd>

PFS Group plumbed in IPsec policy.

</dd> <dt>

*AuthenticationTransformConstants* \[in\]
</dt> <dd>

Auth transform plumbed in IPsec policy.

</dd> <dt>

*DHGroup* \[in\]
</dt> <dd>

DH Group Plumbed in IPsec policy.

</dd> <dt>

*Ikev2Ports* \[in\]
</dt> <dd>

Number of IKEv2 ports that are created.

</dd> <dt>

*L2tpPorts* \[in\]
</dt> <dd>

Number of L2TP ports that are created.

</dd> <dt>

*GrePorts* \[in\]
</dt> <dd>

Number of GRE ports that are created.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is supported starting with Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnServerIPsecConfiguration**](ps-vpnserveripsecconfiguration.md)
</dt> </dl>

 

 





