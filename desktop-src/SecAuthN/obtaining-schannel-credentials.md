---
description: Credentials are required by the Schannel authentication process; both client and server must obtain valid credentials to establish a security context for message exchange. For an example that demonstrates this procedure, see Getting credentials.
ms.assetid: ee4a9908-7ba8-4701-84a4-c50b6b989e82
title: Obtaining Schannel Credentials
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Schannel Credentials

Credentials are required by the Schannel authentication process; both client and server must obtain valid credentials to establish a [*security context*](../secgloss/s-gly.md) for message exchange. For an example that demonstrates this procedure, see [Getting credentials](getting-a-certificate-for-schannel.md).

Your application obtains credentials by calling the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function, which returns a handle to the requested credentials. Because credentials handles are used to store configuration information, the same handle cannot be used for both client-side and server-side operations. This means that applications that support both client and server connections must obtain a minimum of two credentials handles.

In Windows XP, an [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure specifies the following:

-   A security protocol
-   The allowable ciphers
-   Minimum and maximum cipher strengths
-   An [*X.509*](../secgloss/x-gly.md) certificate used for authentication — Required for server, optional for client unless server requests client authentication.

Pass the [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure (via the *pAuthData* parameter) to the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function. This function returns the credentials handle required to establish a [*security context*](../secgloss/s-gly.md).

For detailed information on setting the ciphers used with Schannel, see [Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md).

For information about certificates, see [Certificate and Certificate Store Functions](../seccrypto/cryptography-functions.md).

For an example that demonstrates opening a [*certificate store*](../secgloss/c-gly.md) and locating a certificate to use for Schannel authentication, see [Getting a Certificate](getting-a-certificate-for-schannel.md).

 

 
