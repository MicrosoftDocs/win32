---
Description: Mapping Certificates
ms.assetid: 4139f927-54f4-4968-a9eb-020401bb536d
title: Mapping Certificates
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Certificates

> [!Note]  
> The information in this topic is valid only for servers that require client authentication.

 

When a server application requires client authentication, Schannel automatically attempts to map the certificate supplied by the client to a user account.

After the [*security context*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) has been established, the server application can use the [**QuerySecurityContextToken**](/windows/desktop/api/Sspi/nf-sspi-querysecuritycontexttoken) function to obtain an [*access token*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) for the user account to which the [*client certificate*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) was mapped. Also, the server can use the [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext) function to impersonate the client.

For more information on authentication, see [Performing Authentication Using Schannel](performing-authentication-using-schannel.md).

 

 



