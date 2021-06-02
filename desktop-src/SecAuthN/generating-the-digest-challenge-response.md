---
description: After receiving a challenge from the server, the client creates the Digest challenge response by calling the InitializeSecurityContext (Digest) function.
ms.assetid: b26b5676-a614-4017-a4e5-a5395292a667
title: Generating the Digest Challenge Response
ms.topic: article
ms.date: 05/31/2018
---

# Generating the Digest Challenge Response

After receiving a challenge from the server, the client creates the Digest challenge response by calling the [**InitializeSecurityContext (Digest)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function. This function generates an MD5 [*hash*](/windows/desktop/SecGloss/h-gly) fingerprint by using information about the requested resource and data from the challenge, and outputs a security token that represents a partial [*security context*](/windows/desktop/SecGloss/s-gly). To complete the authentication, the client must return the token to the server that issued the challenge.

The following table describes the parameters of the [**InitializeSecurityContext (Digest)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) [*function*](/windows/desktop/SecGloss/c-gly), and the values to supply when constructing a Digest challenge response.



| Parameter                  | Description                                                                                                                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *fContextReq*<br/>   | The security context attributes requested by the client. For more information, see Digest Challenge Response Context Requirements.<br/>                                                             |
| *pszTargetName*<br/> | HTTP: Null-terminated string that specifies the target URL.<br/> SASL: Null-terminated string that specifies the DNS/SPN target.<br/>                                                         |
| *pInput*<br/>        | Buffers that contain information required by the Digest SSP. For more information, see [Input Buffers for the Digest Challenge Response](input-buffers-for-the-digest-challenge-response.md).<br/> |
| *pfContextAttr*<br/> | Receives the attributes supported by the returned security context. For more information, see Digest Challenge Response Context Requirements.<br/>                                                  |
| *pOutput*<br/>       | Address of a SECBUFFER\_TOKEN type buffer that receives a security token to send back to the server.<br/>                                                                                           |



 

## Digest Challenge Response Context Requirements

Context requirements are flags that determine:

-   Whether Microsoft Digest functions as a SASL mechanism or HTTP authentication protocol.
-   The quality of protection supported by the [*security context*](/windows/desktop/SecGloss/s-gly) shared by the client and server.

By default, Microsoft Digest functions as a SASL mechanism.

Context requirements are specified as flags passed to the *fContextReq* parameter of the [**InitializeSecurityContext**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function. The flags affect the security context's quality of protection by controlling the qop directive in the challenge response.

By default, the qop directive is set to "auth". To generate a challenge response that sets qop to "auth-int", the following must occur:

1.  The Digest challenge must have had a qop directive set to "auth-int".
2.  The client must specify one or more of the following flags:

    -   ISC\_REQ\_INTEGRITY
    -   ISC\_REQ\_REPLAY\_DETECT
    -   ISC\_REQ\_SEQUENCE\_DETECT

For SASL only: Generate a challenge response with the qop directive set to "auth-conf" by specifying the ISC\_REQ\_CONFIDENTIALITY flag. Because this flag is not valid for HTTP authentication, it cannot be used with the ISC\_REQ\_HTTP flag.

## Verifying the Quality of Protection

The client must examine the security context attributes flags returned in the [**InitializeSecurityContext**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function's *pfContextAttr* parameter. The client should send the challenge response to the server only if the quality of protection indicated by the flags is sufficient for its purposes. The relevant flags can be any combination of the following:

-   ISC\_RET\_INTEGRITY
-   ISC\_RET\_REPLAY\_DETECT
-   ISC\_RET\_SEQUENCE\_DETECT
-   ISC\_RET\_CONFIDENTIALITY (SASL contexts only)

For more information about the qop directive, see [Quality of Protection and Ciphers](quality-of-protection-and-ciphers.md).

For more information about challenge response directives, see [Contents of a Digest Challenge Response](contents-of-a-digest-challenge-response.md).

 

