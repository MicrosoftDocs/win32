---
title: NewByEapTtlsAuth method of the PS\_EapConfiguration class
description: Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Tunneled Transport Layer Security (EAP-TTLS) secure protocol.
audience: developer
ms.assetid: '6d387570-0fb1-428f-9e48-4f5ce6d2af00'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NewByEapTtlsAuth method", "NewByEapTtlsAuth method, PS_EapConfiguration class", "PS_EapConfiguration class, NewByEapTtlsAuth method"]
topic_type:
- apiref
api_name:
- PS_EapConfiguration.NewByEapTtlsAuth
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
---

# NewByEapTtlsAuth method of the PS\_EapConfiguration class

Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Tunneled Transport Layer Security (EAP-TTLS) secure protocol.

## Syntax


```mof
static uint32 NewByEapTtlsAuth(
  [in]  boolean          Ttls,
  [in]  boolean          UseWinlogonCredential,
  [in]  string           TunnledNonEapAuthMethod,
  [in]  string           TunnledEapAuthMethod,
  [out] EapConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*Ttls* \[in\]
</dt> <dd>

**True** to use TTLS as the authentication method; **false** to not use it.

</dd> <dt>

*UseWinlogonCredential* \[in\]
</dt> <dd>

**True** to use EAP-MSCHAPv2 as the authentication method, and to automatically use the Windows logon credentials when connecting; otherwise, **false**.

</dd> <dt>

*TunnledNonEapAuthMethod* \[in\]
</dt> <dd>

The simple EAP-TTLS client authentication methods.

<dt>

<span id="Chap"></span><span id="chap"></span><span id="CHAP"></span>

<span id="Chap"></span><span id="chap"></span><span id="CHAP"></span>**Chap** ("Chap")


</dt> <dd>

Challenge Handshake Authentication Protocol (CHAP).

</dd> <dt>

<span id="MsChap"></span><span id="mschap"></span><span id="MSCHAP"></span>

<span id="MsChap"></span><span id="mschap"></span><span id="MSCHAP"></span>**MsChap** ("MsChap")


</dt> <dd>

Microsoft Challenge Handshake Authentication Protocol (MSCHAP) version 1.

</dd> <dt>

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>

<span id="MsChapv2"></span><span id="mschapv2"></span><span id="MSCHAPV2"></span>**MsChapv2** ("MsChapv2")


</dt> <dd>

Microsoft Challenge Handshake Authentication Protocol version 2 (MSCHAPv2).

</dd> <dt>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>

<span id="Pap"></span><span id="pap"></span><span id="PAP"></span>**Pap** ("Pap")


</dt> <dd>

Password Authentication Protocol (PAP).

</dd> </dl> </dd> <dt>

*TunnledEapAuthMethod* \[in\]
</dt> <dd>

The configuration XML blob for tunneled EAP, EAP-TTLS, or Protected Extensible Authentication Protocol (PEAP) authentication.

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

 

 





