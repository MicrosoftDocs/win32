---
Description: Provides Schannel-specific information about a credential.
ms.assetid: 0c357996-b85a-4231-b258-40b35ab83ae2
title: Querying the Attributes of an Schannel Credential
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Querying the Attributes of an Schannel Credential

The [**QueryCredentialsAttributes**](/windows/win32/Sspi/nf-sspi-querycredentialsattributesa?branch=master) function provides Schannel-specific information about a credential. This information is originally specified when the credential is created. For more information, see [Obtaining Schannel Credentials](obtaining-schannel-credentials.md). The information reported by this function is valid for any connections ([*security contexts*](security.s_gly#-security-security-context-gly)) created by using the specified credential.

 

 



