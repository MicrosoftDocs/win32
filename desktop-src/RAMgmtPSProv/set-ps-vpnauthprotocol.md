---
title: Set method of the PS\_VpnAuthProtocol class
description: Updates the authentication method of an incoming S2S VPN interface of a RRAS server.
audience: developer
ms.assetid: 6ce9fbb9-7c43-4c7d-a9b1-470a9238e3cc
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_VpnAuthProtocol class
- PS_VpnAuthProtocol class, Set method
topic_type:
- apiref
api_name:
- PS_VpnAuthProtocol.Set
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_VpnAuthProtocol class

Updates the authentication method of an incoming S2S VPN interface of a RRAS server.

## Syntax


```mof
uint32 Set(
  [in]  string          UserAuthProtocolAccepted[],
  [in]  string          TunnelAuthProtocolsAdvertised,
  [in]  uint8           RootCertificateNameToAccept[],
  [in]  uint8           CertificateAdvertised[],
  [in]  string          SharedSecret,
  [in]  boolean         PassThru,
  [in]  string          CertificateEKUsToAccept[],
  [out] VpnAuthProtocol cmdletOutput
);
```



## Parameters

<dl> <dt>

*UserAuthProtocolAccepted* \[in\]
</dt> <dd>

Specifies Local Authentication protocols that are allowed.

</dd> <dt>

*TunnelAuthProtocolsAdvertised* \[in\]
</dt> <dd>

Specifies the remote AuthenticationMethod used by the RRAS server. If PreSharedKey is specified, SharedSecret parameter becomes mandatory. If Certificates is specified, UserMachineCert parameter becomes mandatory. Only one of them can be specified.

</dd> <dt>

*RootCertificateNameToAccept* \[in\]
</dt> <dd>

Root certificates to be allowed. Applicable only if *UserAuthProtocolAccepted* contains certificates.

</dd> <dt>

*CertificateAdvertised* \[in\]
</dt> <dd>

Certificate to be sent to peer. Applicable only if *TunnelAuthProtocolsAdvertised* contains "Certificate".

</dd> <dt>

*SharedSecret* \[in\]
</dt> <dd>

Text of the Shared Secret to be used in dialing the connection. Applicable only if AuthenticationMethod is set to "PSK".

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates whether the *cmdletOutput* parameter returns an object. **True** to return an object; otherwise **false**.

</dd> <dt>

*CertificateEKUsToAccept* \[in\]
</dt> <dd>

**Windows Server 2012:** This parameter is unavailable prior to Windows Server 2012 R2.

An array that contains the names of the allowed Enhanced Key Usage (EKU) certificates.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives the [**VpnAuthProtocol**](ps-vpnauthprotocol.md) object that contains the updated authentication method.

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

[**PS\_VpnAuthProtocol**](ps-vpnauthprotocol.md)
</dt> </dl>

 

 





