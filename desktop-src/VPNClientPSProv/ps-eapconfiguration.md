---
title: PS\_EapConfiguration class
description: The PS\_EapConfiguration class provides methods to create new Extensible Authentication Protocol (EAP) configuration objects that use certain authentication protocols.
audience: developer
ms.assetid: 510e9719-9a52-4a9b-aa80-216e8df2eede
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_EapConfiguration class
- PS_EapConfiguration class, described
topic_type:
- apiref
api_name:
- PS_EapConfiguration
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_EapConfiguration class

The **PS\_EapConfiguration** class provides methods to create new Extensible Authentication Protocol (EAP) configuration objects that use certain authentication protocols.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class PS_EapConfiguration
{
};
```

## Members

The **PS\_EapConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_EapConfiguration** class has these methods.



| Method                                                                   | Description                                                                                                                                                                           |
|:-------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NewByEapMsChapv2Auth**](newbyeapmschapv2auth-ps-eapconfiguration.md) | Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Microsoft Challenge Handshake Authentication Protocol version 2 (EAP-MSCHAPv2).<br/> |
| [**NewByEapTlsAuth**](newbyeaptlsauth-ps-eapconfiguration.md)           | Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Transport Layer Security (EAP-TLS) secure protocol.<br/>                             |
| [**NewByEapTtlsAuth**](newbyeapttlsauth-ps-eapconfiguration.md)         | Creates an Extensible Authentication Protocol (EAP) configuration object that uses the EAP Tunneled Transport Layer Security (EAP-TTLS) secure protocol.<br/>                   |
| [**NewByPeapAuth**](newbypeapauth-ps-eapconfiguration.md)               | Creates an Extensible Authentication Protocol (EAP) configuration object that uses the Protected Extensible Authentication Protocol (PEAP) authentication protocol.<br/>        |



 

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

[**EapConfiguration**](eapconfiguration.md)
</dt> </dl>

 

 





