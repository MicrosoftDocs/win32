---
title: NewByEapMsChapv2Auth method of the PS\_EapConfiguration class
description: Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Microsoft Challenge Handshake Authentication Protocol version 2 (EAP-MSCHAPv2).
audience: developer
ms.assetid: 510e9719-9a52-4a9b-aa80-216e8df2eede
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewByEapMsChapv2Auth method
- NewByEapMsChapv2Auth method, PS_EapConfiguration class
- PS_EapConfiguration class, NewByEapMsChapv2Auth method
topic_type:
- apiref
api_name:
- PS_EapConfiguration.NewByEapMsChapv2Auth
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NewByEapMsChapv2Auth method of the PS\_EapConfiguration class

Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Microsoft Challenge Handshake Authentication Protocol version 2 (EAP-MSCHAPv2).

## Syntax


```mof
static uint32 NewByEapMsChapv2Auth(
  [in]  boolean          UseWinlogonCredential,
  [out] EapConfiguration cmdletOutput
);
```



## Parameters

<dl> <dt>

*UseWinlogonCredential* \[in\]
</dt> <dd>

**True** to use EAP-MSCHAPv2 as the authentication method, and to use Windows logon credentials automatically when connecting; otherwise, **false**.

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

 

 





