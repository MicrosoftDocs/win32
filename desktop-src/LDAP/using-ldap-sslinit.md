---
title: Using ldap\_sslinit
description: The ldap\_sslinit function operates identical to ldap\_init, except that it has one additional parameter, secure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 8755b8bb-3a75-4204-b892-7594653ea42c
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Using ldap_sslinit LDAP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using ldap\_sslinit

The [**ldap\_sslinit**](/windows/previous-versions/Winldap/nf-winldap-ldap_sslinit?branch=master) function operates identical to [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master), except that it has one additional parameter, *secure*. If this parameter is set to zero, an unencrypted session is created. Be aware that even if the *secure* parameter is set to zero, if the *PortNumber* parameter is set to LDAP\_SSL\_PORT (636) or to LDAP\_SSL\_GC\_PORT (3269), an encrypted session is initiated. Also, if the *secure* parameter is set to a nonzero value, again, an encrypted session is initiated, regardless of the port number passed in the *PortNumber* parameter. For more information, see [Using ldap\_init](using-ldap-init.md).

> [!Note]  
> If SSL, now TLS, is selected as the encryption method, certificates must be set up prior to binding, on both the client and the server.

 

For more information and a code example of using [**ldap\_sslinit**](/windows/previous-versions/Winldap/nf-winldap-ldap_sslinit?branch=master) to establish a session, see [Example Code for Establishing a Session over SSL](example-code-for-establishing-a-session-over-ssl.md).

 

 




