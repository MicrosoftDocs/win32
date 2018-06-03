---
title: Binding to an LDAP Server
description: Binding is the step where the LDAP server authenticates the client and, if the client is successfully authenticated, allows the client access to the LDAP server based on that client's privileges.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: af48c5dd-da41-43d2-9ca1-c0fb5fac150b
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Binding to an LDAP Server LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Binding to an LDAP Server

Binding is the step where the LDAP server authenticates the client and, if the client is successfully authenticated, allows the client access to the LDAP server based on that client's privileges.

If a connection was created using [**ldap\_connect**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_connect), and if no binding function is called, on a LDAP v3 server, you run as anonymous.

To explicitly bind, use one of the binding functions. If a connection was not created using [**ldap\_connect**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_connect), the binding step also makes the connection to the server. The connection is of a type originally specified in the initialization and set up of the connection block. Encryption and integrity validation is established if using SASL signing and sealing. Encryption is established if using TLS (SSL). For more information, see [Initializing a Session](initializing-a-session.md) and [Getting and Setting Session Options](getting-and-setting-session-options.md).

The LDAP client-side, run-time library automatically attempts to reconnect a broken connection. This reconnection occurs when a client attempts to access a connection that no longer exists. If the server does not respond within the set bind timeout period (the default is two minutes), the run time pings the server with ICMP packets until it receives a response. For more information, see **LDAP\_OPT\_AUTO\_RECONNECT** in [**Session Options**](session-options.md).

The bind timeout period can be set with the **LDAP\_OPT\_TIMELIMIT** session option. If this option is not set on a connection, the LDAP client uses a default timeout value of 120 seconds (2 minutes).

There are four functions that enable a client to explicitly request authentication and connection to a LDAP server - two that are synchronous and two that are asynchronous. Two of the functions, [**ldap\_simple\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_simple_bind_s) (synchronous) and [**ldap\_simple\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_simple_bind) (asynchronous) work similarly, so only the synchronous version (**ldap\_simple\_bind\_s**) is discussed here. However, because there are differences, both of the functions [**ldap\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind_s) (synchronous) and [**ldap\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind) (asynchronous) are discussed in other topics.

 

 




