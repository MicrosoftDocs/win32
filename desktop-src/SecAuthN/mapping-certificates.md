---
Description: Mapping Certificates
ms.assetid: 4139f927-54f4-4968-a9eb-020401bb536d
title: Mapping Certificates
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Certificates

> [!Note]  
> The information in this topic is valid only for servers that require client authentication.

 

When a server application requires client authentication, Schannel automatically attempts to map the certificate supplied by the client to a user account.

After the [*security context*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) has been established, the server application can use the [**QuerySecurityContextToken**](/windows/desktop/api/Sspi/nf-sspi-querysecuritycontexttoken) function to obtain an [*access token*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) for the user account to which the [*client certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) was mapped. Also, the server can use the [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext) function to impersonate the client.

For more information on authentication, see [Performing Authentication Using Schannel](performing-authentication-using-schannel.md).

 

 



