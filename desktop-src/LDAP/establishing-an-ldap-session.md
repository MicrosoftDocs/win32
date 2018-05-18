---
title: Establishing an LDAP Session
description: Establish an LDAP session before performing LDAP operations on an LDAP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'd11da030-b521-4469-9212-63800b412e68'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Establishing an LDAP Session LDAP"]
---

# Establishing an LDAP Session

Establish an LDAP session before performing LDAP operations on an LDAP server.

The steps required to establish an LDAP server session are as follows. Steps 2 and 3 are optional.

**To establish an LDAP session**

1.  [Initialize a Session](initializing-a-session.md) — Sets the default [**session option**](session-options.md) settings in the [**LDAP**](ldap.md) structure. The LDAP session state is stored in the **LDAP** structure. The **session options** can be read or set prior to binding.
2.  [Set the Session Options](getting-and-setting-session-options.md) (optional) — Reads existing [**session options**](session-options.md) and sets new **session option** values, as required. In some cases, the default values for the **session options** are acceptable. However, if **session option** changes are required, set those options at this point.
3.  [Connect to the Server](connecting-to-the-server.md) (optional) — Establishes an LDAP connection to the LDAP server. It is not required that a client call [**ldap\_connect**](ldap-connect.md) to establish a server connection. Binding will establish the server connection if it does not exist. However, using **ldap\_connect** is a recommended programming practice for detecting connectivity problems.
4.  [Bind to the server](binding-to-an-ldap-server.md) — The LDAP server authenticates the client. If the client successfully authenticates, then client can access to the LDAP server, based on the privileges of that client. This can be an explicit bind using one of the binding functions. This can also be an implicit bind as an anonymous user.

The following are examples of how to establish an LDAP session:

-   [Establishing a Session Without Encryption](example-code-for-establishing-a-session-without-encryption.md)
-   [Establishing a Session over SSL](example-code-for-establishing-a-session-over-ssl.md)

 

 




