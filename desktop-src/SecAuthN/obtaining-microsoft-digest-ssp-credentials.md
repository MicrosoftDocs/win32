---
Description: User credentials are required by Microsoft Digest; both client and server must present valid credentials before they can establish a security context for message exchange. Credentials handles are used to obtain and present credentials.
ms.assetid: f97bdaf6-40a8-414e-a561-d3cb953d0bab
title: Obtaining Microsoft Digest SSP Credentials
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining Microsoft Digest SSP Credentials

User [*credentials*](security.c_gly#-security-credentials-gly) are required by Microsoft Digest; both client and server must present valid credentials before they can establish a [*security context*](security.s_gly#-security-security-context-gly) for message exchange. Credentials handles are used to obtain and present credentials.

Because the credential handle is used to store configuration information, the same handle cannot be used for both client-side and server-side operations. This means that applications that support both client and server connections must obtain a minimum of two credentials handles.

To get a handle to the credentials required by Microsoft Digest, call the [**AcquireCredentialsHandle**](/windows/win32/Sspi/?branch=master) function.

The following C language examples demonstrate obtaining credentials.

-   [Obtaining Default Digest Credentials](obtaining-default-digest-credentials.md)
-   [Obtaining Alternate Digest Credentials](obtaining-alternate-digest-credentials.md)

 

 



