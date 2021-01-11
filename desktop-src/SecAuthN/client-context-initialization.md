---
description: Client Context Initialization
ms.assetid: 0c8aad3e-e726-49ce-8fc9-94dbd60cc5cb
title: Client Context Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Client Context Initialization

To establish a secure connection, the client acquires an outbound [*credentials*](/windows/desktop/SecGloss/c-gly) handle before sending an authentication request to the server. The server creates a security context for the client from the authentication request. There are two client-side SSPI functions involved in authentication setup:

-   [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) obtains a reference to previously obtained logon [*credentials*](/windows/desktop/SecGloss/c-gly).
-   [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) creates the initial authentication request security tokens.

Code for this process can be seen in the **GenClientContext** function in [Using SSPI with a Windows Sockets Client](using-sspi-with-a-windows-sockets-client.md).

If a client program needs to use credentials in addition to its own logon credentials, such as a different user name, domain name, and password, it provides them in the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) call with a [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/win32/api/sspi/ns-sspi-sec_winnt_auth_identity_a) structure specifying the additional credentials. For more information on credentials functions, see [Credential Management](authentication-functions.md).

> [!Note]  
> The **Flags** member of the [**SEC\_WINNT\_AUTH\_IDENTITY**](/windows/win32/api/sspi/ns-sspi-sec_winnt_auth_identity_a) structure can be set to SEC\_WINNT\_AUTH\_IDENTITY\_ANSI when strings in the structure are ASCI or OEM. ANSI strings can be used with the **Flags** member of the **SEC\_WINNT\_AUTH\_IDENTITY** structure set to SEC\_WINNT\_AUTH\_IDENTITY\_UNICODE if they are first converted to [*Unicode*](/windows/desktop/SecGloss/u-gly) by using the [**MultiByteToWideChar**](/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar) function.

 

To initiate the first leg of the authentication, the client calls [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) to obtain an initial security token to be sent in a connection request message to the server.

The client uses the security token information received in the output buffer descriptor to generate a message to send to the server. The construction of the message, in terms of placement of various buffers and so forth, is part of the [*application protocol*](/windows/desktop/SecGloss/a-gly) and must be understood by both parties.

The client checks the return status from [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) to see if authentication will complete in a single call. A return status of SEC\_I\_CONTINUE\_NEEDED indicates that the security protocol requires multiple authentication messages. For more information on context functions, see [Context Management](authentication-functions.md).

 

 
