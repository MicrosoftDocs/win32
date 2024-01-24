---
description: The following example demonstrates how a typical client would obtain Schannel credentials.
ms.assetid: 8f912af8-fd64-467a-b154-28c60cb14929
title: Getting Schannel Credentials
ms.topic: article
ms.date: 05/31/2018
---

# Getting Schannel Credentials

The following example demonstrates how a typical client would obtain Schannel credentials. The example follows the recommended practice of using the system defaults for ciphers and cipher strengths. This allows the Schannel package to use the strongest possible algorithms to secure the channel.


```C++
#include <windows.h>
#include <ntsecapi.h>
#include <stdio.h>
#include <sspi.h>
#include <schnlsp.h>

void getSchannelClientHandle(PCredHandle ppClientCred)
{
  SECURITY_STATUS SecStatus;
  TimeStamp Lifetime;
  CredHandle hCred;
  SCHANNEL_CRED credData;

  ZeroMemory(&credData, sizeof(credData));
  credData.dwVersion = SCHANNEL_CRED_VERSION;

  //-------------------------------------------------------
  // Specify the TLS V1.0 (client-side) security protocol.
  credData.grbitEnabledProtocols = SP_PROT_TLS1_CLIENT; 
    
  SecStatus = AcquireCredentialsHandle (
       NULL,                  // default principal
       UNISP_NAME,            // name of the SSP
       SECPKG_CRED_OUTBOUND,  // client will use the credentials
       NULL,                  // use the current LOGON id
       &credData,             // protocol-specific data
       NULL,                  // default
       NULL,                  // default
       &hCred,                // receives the credential handle
       &Lifetime              // receives the credential time limit
  );
  printf("Client credentials status: 0x%x\n", SecStatus);
  // Return the handle to the caller.
  if(ppClientCred != NULL)
      *ppClientCred = hCred;

  return;
  //-------------------------------------------------------
  // When you have finished with this handle,
  // free the handle by calling the 
  // FreeCredentialsHandle function.
}
```



The primary difference between the client-side and server-side request for credentials is that the server must provide a certificate using a [**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context) structure as follows:


```C++
  PCCERT_CONTEXT serverCert; // server-side certificate
  //-------------------------------------------------------
  // Get the server certificate. 

  if (! (serverCert = getServerCertificate())) return;

  // getServerCertificate is a placeholder function.
  credData.paCred = &serverCert;
```



The example function *getServerCertificate* is a placeholder function for this application-specific activity. For an example implementation of the *getServerCertificate* function, see [Getting a Certificate](getting-a-certificate-for-schannel.md).

> [!Note]  
> When requesting credentials to be used by the server, change the third (*fCredentialUse*) parameter of the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function from SECPKG\_CRED\_OUTBOUND to SECPKG\_CRED\_INBOUND.

 

 

 
