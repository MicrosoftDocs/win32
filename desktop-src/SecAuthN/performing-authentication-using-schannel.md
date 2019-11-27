---
Description: All Schannel protocols require the server to provide a certificate from a trusted certification authority (CA) as proof of its identity.
ms.assetid: 060981e0-b52a-4cc2-bfd2-4cf24f921f16
title: Performing Authentication Using Schannel
ms.topic: article
ms.date: 05/31/2018
---

# Performing Authentication Using Schannel

All Schannel protocols require the server to provide a [*certificate*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) from a trusted [*certification authority*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) (CA) as proof of its identity. This process is called server authentication. Client authentication, where the client provides proof of its identity, is optional and may be requested by the server at any time.

## Authenticating the Server

The default behavior of Schannel is to use the [**WinVerifyTrust**](https://msdn.microsoft.com/library/Aa388208(v=VS.85).aspx) function to verify the [*integrity*](https://msdn.microsoft.com/library/ms721588(v=VS.85).aspx) and ownership of the [*server certificate*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx). To disable this feature, specify ISC\_REQ\_MANUAL\_CRED\_VALIDATION when calling the [**InitializeSecurityContext (Schannel)**](https://msdn.microsoft.com/library/Aa375924(v=VS.85).aspx) function. For more information, see [Manually Validating Schannel Credentials](manually-validating-schannel-credentials.md).

## Authenticating the Client

Schannel does not validate client's certificates; the server must perform this authentication manually. Typically, the server will check the client's identity in a database containing user account information. For servers that need to obtain a client's account using a certificate, see [Mapping Certificates](mapping-certificates.md).

When the server requests client authentication, the client must send the server one of its certificates. By default, Schannel will, with no notification to the client, attempt to locate a [*client certificate*](https://msdn.microsoft.com/library/ms721572(v=VS.85).aspx) and send it to the server. To disable this feature, clients specify ISC\_REQ\_USE\_SUPPLIED\_CREDS when calling the [**InitializeSecurityContext (Schannel)**](https://msdn.microsoft.com/library/Aa375924(v=VS.85).aspx) function. When this flag is specified, Schannel will return SEC\_I\_INCOMPLETE\_CREDENTIALS to the client when the server requests authentication and the client has not previously supplied a certificate.

 

 



