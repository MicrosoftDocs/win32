---
title: NewByPeapAuth method of the PS\_EapConfiguration class
description: Creates an Extensible Authentication Protocol (EAP) configuration object that uses the Protected Extensible Authentication Protocol (PEAP) authentication protocol.
audience: developer
ms.assetid: '409dad48-a427-42e4-bc58-137c7ac3ddee'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewByPeapAuth method", "NewByPeapAuth method, PS_EapConfiguration class", "PS_EapConfiguration class, NewByPeapAuth method"]
topic_type:
- apiref
api_name:
- PS_EapConfiguration.NewByPeapAuth
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# NewByPeapAuth method of the PS\_EapConfiguration class

Creates an Extensible Authentication Protocol (EAP) configuration object that uses the Protected Extensible Authentication Protocol (PEAP) authentication protocol.

## Syntax


```mof
static uint32 NewByPeapAuth(
  [in]  boolean          Peap,
  [in]  boolean          VerifyServerIdentity,
  [in]  boolean          EnableNap,
  [in]  boolean          FastReconnect,
  [in]  string           TunnledEapAuthMethod,
  [out] EapConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*Peap* \[in\]
</dt> <dd>

**True** to use PEAP as the authentication method; otherwise, **false**.

</dd> <dt>

*VerifyServerIdentity* \[in\]
</dt> <dd>

**True** to validate the identity of the server when connecting with VPN; otherwise, **false**. This parameter is used with Protected Extensible Authentication Protocol (PEAP) and EAP Transport Layer Security (EAP-TLS) with tunneled EAP client authentication.

</dd> <dt>

*EnableNap* \[in\]
</dt> <dd>

**True** to enable Network Access Protection (NAP) for PEAP; otherwise, **false**.

</dd> <dt>

*FastReconnect* \[in\]
</dt> <dd>

**True** to enable fast reconnection in the current configuration for PEAP; otherwise, **false**.

</dd> <dt>

*TunnledEapAuthMethod* \[in\]
</dt> <dd>

The configuration XML blob for tunneled EAP, EAP Tunneled Transport Layer Security (EAP-TTLS), or Protected Extensible Authentication Protocol (PEAP) authentication protocols.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains the [**EapConfiguration**](eapconfiguration.md) object.

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

[**PS\_EapConfiguration**](ps-eapconfiguration.md)
</dt> </dl>

 

 





