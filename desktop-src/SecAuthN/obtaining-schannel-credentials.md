---
description: Learn how to obtain Schannel credentials required for authentication. Both client and server must get valid credentials to establish a security context for secure message exchange.
ms.assetid: ee4a9908-7ba8-4701-84a4-c50b6b989e82
title: Obtaining Schannel Credentials
ms.topic: concept-article
ms.date: 09/23/2025
---

# Obtaining Schannel Credentials

Credentials are required by the Schannel authentication process; both client and server must obtain valid credentials to establish a [security context](../secgloss/s-gly.md) for message exchange. For an example that demonstrates this procedure, see [Getting credentials](getting-a-certificate-for-schannel.md).

Your application obtains credentials by calling the [AcquireCredentialsHandle](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function, which returns a handle to the requested credentials. Because credentials handles are used to store configuration information, the same handle cannot be used for both client-side and server-side operations. This means that applications that support both client and server connections must obtain a minimum of two credentials handles.

An [SCHANNEL\_CRED](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure specifies the following:

-   A security protocol
-   The allowable ciphers
-   Minimum and maximum cipher strengths
-   An [X.509](../secgloss/x-gly.md) certificate used for authentication — Required for server, optional for client unless server requests client authentication.

Pass the [SCHANNEL\_CRED](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure (via the *pAuthData* parameter) to the [AcquireCredentialsHandle](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function. This function returns the credentials handle required to establish a [security context](../secgloss/s-gly.md).

Security support provider interface (SSPI) callers can use TLS 1.3 by passing the new crypto-agile [SCH\_CREDENTIALS](/windows/win32/api/schannel/ns-schannel-sch_credentials) structure when calling [AcquireCredentialsHandle](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea), which enables TLS 1.3 by default. SSPI callers using TLS 1.3 need to make sure their code correctly handles [SEC\_I\_RENEGOTIATE](recognizing-a-request-to-renegotiate-a-connection.md). See the blog post [Taking Transport Layer Security (TLS) to the next level with TLS 1.3](https://www.microsoft.com/security/blog/2020/08/20/taking-transport-layer-security-tls-to-the-next-level-with-tls-1-3/) for more information.

For detailed information on setting the ciphers used with Schannel, see [Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md).

For information about certificates, see [Certificate and Certificate Store Functions](../seccrypto/cryptography-functions.md).

For an example that demonstrates opening a [certificate store](../secgloss/c-gly.md) and locating a certificate to use for Schannel authentication, see [Getting a Certificate](getting-a-certificate-for-schannel.md).

## Related content

[Getting credentials](getting-a-certificate-for-schannel.md)

[Taking Transport Layer Security (TLS) to the next level with TLS 1.3](https://www.microsoft.com/security/blog/2020/08/20/taking-transport-layer-security-tls-to-the-next-level-with-tls-1-3/)

[AcquireCredentialsHandle](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea)

