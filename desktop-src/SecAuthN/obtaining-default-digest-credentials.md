---
Description: 'Both clients and servers must obtain credentials before they can establish a security context for message exchange.'
ms.assetid: 'a72404b8-1ec9-4f58-b3a6-09811070ea29'
title: Obtaining Default Digest Credentials
---

# Obtaining Default Digest Credentials

Both clients and servers must obtain [*credentials*](security.c_gly#-security-credentials-gly) before they can establish a [*security context*](security.s_gly#-security-security-context-gly) for message exchange. The default behavior of the [**AcquireCredentialsHandle**](acquirecredentialshandle--general-.md) function is to provide credentials for the security principal associated with the current logon [*session*](security.s_gly#-security-session-gly).

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

 

 



