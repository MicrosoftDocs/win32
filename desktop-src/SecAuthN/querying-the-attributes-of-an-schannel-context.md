---
Description: Provides Schannel-specific information about a security context.
ms.assetid: 6ff4ebcc-2362-4397-ae77-2d378db8c7e2
title: Querying the Attributes of an Schannel Context
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Attributes of an Schannel Context

The [**QueryContextAttributes (Schannel)**](/windows/desktop/api/Sspi/) function provides Schannel-specific information about a [*security context*](https://www.bing.com/search?q=*security context*). Most of the information is originally specified when the context is created by using the client [**InitializeSecurityContext (Schannel)**](/windows/desktop/api/Sspi/) or server [**AcceptSecurityContext (Schannel)**](/windows/desktop/api/Sspi/) function. Some information is specified when obtaining a handle to the credential used to create the context. For more information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



