---
Description: Provides Schannel-specific information about a security context.
ms.assetid: 6ff4ebcc-2362-4397-ae77-2d378db8c7e2
title: Querying the Attributes of an Schannel Context
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying the Attributes of an Schannel Context

The [**QueryContextAttributes (Schannel)**](/windows/win32/Sspi/?branch=master) function provides Schannel-specific information about a [*security context*](security.s_gly#-security-security-context-gly). Most of the information is originally specified when the context is created by using the client [**InitializeSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) or server [**AcceptSecurityContext (Schannel)**](/windows/win32/Sspi/?branch=master) function. Some information is specified when obtaining a handle to the credential used to create the context. For more information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



