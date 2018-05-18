---
title: WinRM Constants and Enumerations
description: Windows Remote Management has bit flags used in creating sessions and enumerations, and for access types and authentication to a proxy server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '17e59245-26a3-4383-a741-4a09f3cfcec6'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-remote-management'
ms.tgt_platform: multiple
---

# WinRM Constants and Enumerations

Windows Remote Management has bit flags used in creating sessions and enumerations, and for access types and authentication to a proxy server. The following list lists the different bit flags.

<dl> <dt>

<span id="Session_Constants"></span><span id="session_constants"></span><span id="SESSION_CONSTANTS"></span>[Session Constants](session-constants.md)
</dt> <dd>

Flags used in *flags* parameter of the [**WSMan.CreateSession**](wsman-createsession.md) or [**IWSMan::CreateSession**](iwsman-createsession.md) methods.

</dd> <dt>

<span id="Enumeration_Constants"></span><span id="enumeration_constants"></span><span id="ENUMERATION_CONSTANTS"></span>[**Enumeration Constants**](enumeration-constants.md)
</dt> <dd>

Flags used in *flags* parameter of call to [**Session.Enumerate**](session-enumerate.md) or [**IWSManSession::Enumerate**](iwsmansession-enumerate.md).

</dd> <dt>

<span id="WSManProxyAuthenticationFlags"></span><span id="wsmanproxyauthenticationflags"></span><span id="WSMANPROXYAUTHENTICATIONFLAGS"></span>[**WSManProxyAuthenticationFlags**](wsmanproxyauthenticationflags.md)
</dt> <dd>

Flags used in *authenticationMechanism* parameter of call to [**IWSManConnectionOptionsEx2::SetProxy**](iwsmanconnectionoptionsex2-setproxy.md).

</dd> <dt>

<span id="WSManProxyAccessTypeFlags"></span><span id="wsmanproxyaccesstypeflags"></span><span id="WSMANPROXYACCESSTYPEFLAGS"></span>[**WSManProxyAccessTypeFlags**](wsmanproxyaccesstypeflags.md)
</dt> <dd>

Flags used in *accessType* parameter of call to [**IWSManConnectionOptionsEx2::SetProxy**](iwsmanconnectionoptionsex2-setproxy.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> <dt>

[**WSMan.CreateSession**](wsman-createsession.md)
</dt> <dt>

[**IWSMan::CreateSession**](iwsman-createsession.md)
</dt> <dt>

[**IWSManConnectionOptionsEx2::SetProxy**](iwsmanconnectionoptionsex2-setproxy.md)
</dt> </dl>

 

 




