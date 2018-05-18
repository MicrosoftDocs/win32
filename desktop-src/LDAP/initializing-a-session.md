---
title: Initializing a Session
description: To establish an LDAP session, initialize a connection block (LDAP structure) to its default values.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '218b4cf2-e582-4052-8206-35c2ba2fe302'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# Initializing a Session

To establish an LDAP session, initialize a connection block ([**LDAP**](ldap.md) structure) to its default values. The connection block is created and initialized with a call to [**ldap\_init**](ldap-init.md) or to [**ldap\_sslinit**](ldap-sslinit.md), passing in the server name and the system port to use. Either call returns a handle to an **LDAP** structure (connection block) that maintains state status data for the session. Use the [**cldap\_open**](cldap-open.md) function to establish a connectionless UDP-based session.

When a session is created and initialized using [**ldap\_init**](ldap-init.md) or [**ldap\_sslinit**](ldap-sslinit.md), all members of the [**LDAP**](ldap.md) structure get initialized to default values. For more information, and a description of these members, see [Session Options](session-options.md). For more information about setting these options, see [Getting and Setting Session Options](getting-and-setting-session-options.md). For more information about establishing a secure connection, see [Using ldap\_init](using-ldap-init.md) and [Using ldap\_sslinit](using-ldap-sslinit.md). For example code, see [Example Code for Establishing a Session Without Encryption](example-code-for-establishing-a-session-without-encryption.md) and [Example Code for Establishing a Session over SSL](example-code-for-establishing-a-session-over-ssl.md).

 

 




