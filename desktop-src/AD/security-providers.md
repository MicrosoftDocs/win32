---
title: Security Providers
description: The Security Support Provider Interface (SSPI) provides support for mutual authentication and is exposed directly through the SSPI APIs and services layered on SSPI, including RPC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '3aa64aa1-c707-489f-a0a3-08bf6ac151ec'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# Security Providers

The Security Support Provider Interface (SSPI) provides support for mutual authentication and is exposed directly through the SSPI APIs and services layered on SSPI, including RPC.

Not all security packages available to SSPI support mutual authentication. To obtain mutual authentication, the application must request mutual authentication and a security package that supports it. For example, the code example in [Mutual Authentication in a Windows Sockets Service with an SCP](mutual-authentication-in-a-windows-sockets-service-with-an-scp.md) uses the "negotiate" package in Secur32.dll, which is included with Windows 2000.

 

 




