---
title: NewByEapTlsAuth method of the PS\_EapConfiguration class
description: Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Transport Layer Security (EAP-TLS) secure protocol.
audience: developer
ms.assetid: e97bdccf-dd28-4353-be5a-d2548ed5cfbd
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewByEapTlsAuth method
- NewByEapTlsAuth method, PS_EapConfiguration class
- PS_EapConfiguration class, NewByEapTlsAuth method
topic_type:
- apiref
api_name:
- PS_EapConfiguration.NewByEapTlsAuth
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewByEapTlsAuth method of the PS\_EapConfiguration class

Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Transport Layer Security (EAP-TLS) secure protocol.

## Syntax


```mof
static uint32 NewByEapTlsAuth(
  [in]  boolean          Tls,
  [in]  boolean          UserCertificate,
  [in]  boolean          VerifyServerIdentity,
  [out] EapConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*Tls* \[in\]
</dt> <dd>

**True** to use EAP-TLS (smart card or user certificate) as the authentication method; **false** to not use it.

</dd> <dt>

*UserCertificate* \[in\]
</dt> <dd>

If *Tls* is **True**: **True** to use a user certificate for authentication; **false** to use a smart card for authentication.

</dd> <dt>

*VerifyServerIdentity* \[in\]
</dt> <dd>

**True** to validate the identity of the server when connecting with VPN; otherwise, **false**. This parameter is used with Protected Extensible Authentication Protocol (PEAP) and EAP-TLS (with tunneled EAP client authentication).

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**EapConfiguration**](eapconfiguration.md) object.

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

[**PS\_EapConfiguration**](ps-eapconfiguration.md)
</dt> </dl>

 

 





