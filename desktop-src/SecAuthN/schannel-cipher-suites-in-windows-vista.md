---
description: A set of cryptographic algorithms. Schannel protocols use algorithms from a cipher suite to create keys and encrypt information.
ms.assetid: 380452e2-a9c8-4380-a3bf-9c7942a0c0c2
title: TLS Cipher Suites in Windows Vista
ms.topic: reference
ms.date: 06/26/2024
---

# TLS Cipher Suites in Windows Vista

A cipher suite is a set of cryptographic algorithms. Schannel protocols use algorithms from a cipher suite to create keys and encrypt information. A cipher suite specifies one algorithm for each of the following tasks:

- Key exchange
- Bulk encryption
- Message authentication

[*Key exchange algorithms*](../secgloss/k-gly.md) protect information required to create shared keys. These algorithms are asymmetric ([*public key algorithms*](../secgloss/p-gly.md)) and perform well for relatively small amounts of data.

Bulk encryption algorithms encrypt messages exchanged between clients and servers. These algorithms are [*symmetric*](../secgloss/s-gly.md) and perform well for large amounts of data.

[Message authentication](message-authentication-codes-in-schannel.md) algorithms generate message [*hashes*](../secgloss/h-gly.md) and signatures that ensure the [*integrity*](../secgloss/i-gly.md) of a message.

Developers specify these elements by using [**ALG\_ID**](../seccrypto/alg-id.md) data types. For more information, see [Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md).

Schannel supports the following cipher suites. The suites are listed in the default order in which they are chosen by the Microsoft Schannel Provider.

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](/troubleshoot/windows-server/windows-security/deploy-custom-cipher-suite-ordering).

| Cipher suite | FIPS mode enabled | Exchange | Encryption | Hash | Protocols |
|--------------|-------------------|----------|------------|------|-----------|
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA                     | Yes         | RSA             | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA                     | Yes         | RSA             | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_RSA\_WITH\_RC4\_128\_SHA                          | No          | RSA             | RC4       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA                    | Yes         | RSA             | 3DES      | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P256      | Yes         | ECDH\_P256      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P384      | Yes         | ECDH\_P384      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P521      | Yes         | ECDH\_P521      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P256      | Yes         | ECDH\_P256      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P384      | Yes         | ECDH\_P384      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P521      | Yes         | ECDH\_P521      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P256        | Yes         | ECDH\_P256      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P384        | Yes         | ECDH\_P384      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P521        | Yes         | ECDH\_P521      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P256        | Yes         | ECDH\_P256      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P384        | Yes         | ECDH\_P384      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P521        | Yes         | ECDH\_P521      | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA                | Yes         | DH              | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA                | Yes         | DH              | AES       | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0               |
| TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA               | Yes         | DH              | 3DES      | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_RC4\_128\_MD5                          | No          | RSA             | RC4       | MD5       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| SSL\_CK\_RC4\_128\_WITH\_MD5                           | No          | RSA             | RC4       | MD5       | SSL 2.0               |
| SSL\_CK\_DES\_192\_EDE3\_CBC\_WITH\_MD5                | No          | RSA             | 3DES      | MD5       | SSL 2.0               |
| TLS\_RSA\_WITH\_NULL\_MD5                              | No          | RSA             |                 | MD5       | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |
| TLS\_RSA\_WITH\_NULL\_SHA                              | No          | RSA             |                 | SHA1      | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0      |

The following cipher suites are supported by Schannel; however, they are not present by default. They must be added as necessary. For information about how to add cipher suites to the Schannel provider, see [Prioritizing Schannel Cipher Suites](prioritizing-schannel-cipher-suites.md).

- TLS_RSA_EXPORT_WITH_RC4_40_MD5
- TLS_RSA_EXPORT1024_WITH_RC4_56_SHA
- TLS_RSA_EXPORT1024_WITH_DES_CBC_SHA
- SSL_CK_RC4_128_EXPORT40_MD5
- SSL_CK_DES_64_CBC_WITH_MD5
- TLS_RSA_WITH\_DES_CBC_SHA
- TLS_RSA_WITH\_NULL_MD5
- TLS_RSA_WITH\_NULL_SHA
- TLS_DHE_DSS_EXPORT1024_WITH_DES_CBC_SHA
- TLS_DHE_DSS_WITH_DES_CBC_SHA

**Windows Server 2003 and Windows XP:** For information about supported cipher suites, see the following topics.

| Topic | Description |
|-------|-------------|
| [TLS Cipher Suites](/windows/win32/secauthn/cipher-suites-in-schannel) | Information about the cipher suites available with the TLS protocol in Windows Server 2003 and Windows XP. |
| [Secure Sockets Layer Protocol](secure-sockets-layer-protocol.md) | General information about SSL 2.0 and 3.0, including the available cipher suites in Windows Server 2003 and Windows XP. |
