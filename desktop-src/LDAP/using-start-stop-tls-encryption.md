---
title: Using Start-Stop TLS Encryption
description: The start and stop TLS functions enable transport level security (TLS), formerly known as SSL, to be enabled on an LDAP connection not initially created using TLS (SSL), and then to stop using TLS when it is no longer required.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 10e97876-21ae-49d3-9cf7-890e95b0e93d
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Start-Stop TLS Encryption

The start and stop TLS functions enable transport level security (TLS), formerly known as SSL, to be enabled on an LDAP connection not initially created using TLS (SSL), and then to stop using TLS when it is no longer required. Creating a TLS (SSL) LDAP connection the conventional way, either by connecting on port 636 or by specifying **LDAP\_OPT\_SSL**, creates a connection that is encrypted for its duration. In contrast, using the start and stop TLS functions lets you take a conventional, unencrypted LDAP session (for example, on port 389), perform various unencrypted operations on it, then call [**ldap\_start\_tls\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_start_tls_sa?branch=master) to enable encryption. You can then perform encrypted LDAP operations; when you no longer require encryption, call [**ldap\_stop\_tls\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_stop_tls_s?branch=master) to return to an unencrypted session. This lets you protect security-sensitive portions of an LDAP session with encryption, without the overhead of encrypting the entire session. The same requirements regarding certificates, for example, the client must trust the CA that issued the server's certificate, and so on, are required for the start and stop TLS functions as they are for port 636 TLS (SSL) sessions.

Start and stop TLS (SSL) requires that the server have matching support, specifically, support for the extended operation 1.3.6.14.1.1466.20037. Start and stop TLS (SSL) affects the global connection state; for example, the connection is affected for all threads that use it.

 

 




