---
title: Using ldap\_bind\_s
description: Provides a distinguished name (DN) and an authentication credential, such as a password, that identifies the person, device, or application attempting to connect to the LDAP server. The type of credentials used depend upon the authentication method used.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '56be8077-aa12-4a04-8600-f6662583d29d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# Using ldap\_bind\_s

The [**ldap\_bind\_s**](ldap-bind-s.md) function provides a distinguished name (DN) and an authentication credential, such as a password, that identifies the person, device, or application attempting to connect to the LDAP server. The type of credentials used depend upon the authentication method used.

The [**ldap\_simple\_bind\_s**](ldap-simple-bind-s.md) function uses a plaintext password for authentication. Call [**ldap\_bind\_s**](ldap-bind-s.md) to use authentication services, such as Kerberos, NTLM, or Digest. For more information about supported authentication services, see **ldap\_bind\_s** and [Using ldap\_init](using-ldap-init.md).

To keep the name and password secure, and you do not require a secure session, then use **ldap\_bind\_s** with any authentication method discussed above. Kerberos and NTLM, for example, do not actually transmit the password; they transmit a representation of the password that cannot be traced back to the original password. Because the password is not transmitted, there is no urgent need to encrypt the process. For more information, and an example of this type of bind, see [Example Code for Establishing a Session Without Encryption](example-code-for-establishing-a-session-without-encryption.md).

If you are sensitive to someone eavesdropping on any part of the session, set up an encrypted session. To encrypt portions of a session, use [**ldap\_start\_tls\_s**](ldap-start-tls-s.md) and [**ldap\_stop\_tls\_s**](ldap-stop-tls-s.md).

> [!Note]  
> LDAP 2 requires that a client bind even for an anonymous connection. Not all LDAP implementations enforce this requirement, but you should include the bind step in order to maintain compatibility with all LDAP 2 services.

 

For more information, and a list of the authentication and encryption options, see [**Session Options**](session-options.md).

 

 




