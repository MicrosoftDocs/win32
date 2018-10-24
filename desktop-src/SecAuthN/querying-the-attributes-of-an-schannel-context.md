---
Description: Provides Schannel-specific information about a security context.
ms.assetid: 6ff4ebcc-2362-4397-ae77-2d378db8c7e2
title: Querying the Attributes of an Schannel Context
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Attributes of an Schannel Context

The [**QueryContextAttributes (Schannel)**](https://msdn.microsoft.com/en-us/library/Aa379340(v=VS.85).aspx) function provides Schannel-specific information about a [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). Most of the information is originally specified when the context is created by using the client [**InitializeSecurityContext (Schannel)**](https://msdn.microsoft.com/en-us/library/Aa375924(v=VS.85).aspx) or server [**AcceptSecurityContext (Schannel)**](https://msdn.microsoft.com/en-us/library/Aa374708(v=VS.85).aspx) function. Some information is specified when obtaining a handle to the credential used to create the context. For more information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md).

 

 



