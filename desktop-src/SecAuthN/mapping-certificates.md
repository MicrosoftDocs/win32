---
Description: Mapping Certificates
ms.assetid: 4139f927-54f4-4968-a9eb-020401bb536d
title: Mapping Certificates
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Mapping Certificates

> [!Note]  
> The information in this topic is valid only for servers that require client authentication.

 

When a server application requires client authentication, Schannel automatically attempts to map the certificate supplied by the client to a user account.

After the [*security context*](security.s_gly#-security-security-context-gly) has been established, the server application can use the [**QuerySecurityContextToken**](/windows/win32/Sspi/nf-sspi-querysecuritycontexttoken?branch=master) function to obtain an [*access token*](security.a_gly#-security-access-token-gly) for the user account to which the [*client certificate*](security.c_gly#-security-client-certificate-gly) was mapped. Also, the server can use the [**ImpersonateSecurityContext**](/windows/win32/Sspi/nf-sspi-impersonatesecuritycontext?branch=master) function to impersonate the client.

For more information on authentication, see [Performing Authentication Using Schannel](performing-authentication-using-schannel.md).

 

 



