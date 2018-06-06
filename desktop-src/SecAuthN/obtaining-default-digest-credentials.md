---
Description: Both clients and servers must obtain credentials before they can establish a security context for message exchange.
ms.assetid: a72404b8-1ec9-4f58-b3a6-09811070ea29
title: Obtaining Default Digest Credentials
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Default Digest Credentials

Both clients and servers must obtain [*credentials*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) before they can establish a [*security context*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) for message exchange. The default behavior of the [**AcquireCredentialsHandle**](/windows/desktop/api/Sspi/) function is to provide credentials for the security principal associated with the current logon [*session*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50).

The following example demonstrates a server-side call to obtain the default credentials.


```C++
SECURITY_STATUS SecStatus; 
TimeStamp tsLifetime; 
CredHandle hCred;
SecStatus = AcquireCredentialsHandle (
       NULL,                  // Default principal.
       WDIGEST_SP_NAME,       // Microsoft Digest SSP. 
       SECPKG_CRED_INBOUND,   // Server will use the credentials.
       NULL,                  // Use the current LOGON id.
       NULL,                  // Default credentials.
       NULL,                  // Not used with Digest SSP.
       NULL,                  // Not used with Digest SSP.
       &amp;hCred,                // Receives the credential handle.
       &amp;tsLifetime            // Receives the credential time limit.
);
```



The client-side call for default credentials is identical, except the third parameter must specify SECPKG\_CRED\_OUTBOUND to indicate that the client will use the credentials handle returned by the function.

For an example that demonstrates obtaining credentials for a security principal other than the logged on user, see [Obtaining Alternate Credentials](obtaining-alternate-digest-credentials.md).

 

 



