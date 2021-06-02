---
description: A set of cryptographic algorithms. Schannel protocols use algorithms from a cipher suite to create keys and encrypt information.
ms.assetid: 380452e2-a9c8-4380-a3bf-9c7942a0c0c2
title: TLS Cipher Suites in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# TLS Cipher Suites in Windows Vista

A cipher suite is a set of cryptographic algorithms. Schannel protocols use algorithms from a cipher suite to create keys and encrypt information. A cipher suite specifies one algorithm for each of the following tasks:

-   Key exchange
-   Bulk encryption
-   Message authentication

[*Key exchange algorithms*](../secgloss/k-gly.md) protect information required to create shared keys. These algorithms are asymmetric ([*public key algorithms*](../secgloss/p-gly.md)) and perform well for relatively small amounts of data.

Bulk encryption algorithms encrypt messages exchanged between clients and servers. These algorithms are [*symmetric*](../secgloss/s-gly.md) and perform well for large amounts of data.

[Message authentication](message-authentication-codes-in-schannel.md) algorithms generate message [*hashes*](../secgloss/h-gly.md) and signatures that ensure the [*integrity*](../secgloss/i-gly.md) of a message.

Developers specify these elements by using [**ALG\_ID**](../seccrypto/alg-id.md) data types. For more information, see [Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md).

Schannel supports the following cipher suites. The suites are listed in the default order in which they are chosen by the Microsoft Schannel Provider.

> [!IMPORTANT]
> HTTP/2 web services fail with non-HTTP/2-compatible cipher suites. To ensure your web services function with HTTP/2 clients and browsers, see [How to deploy custom cipher suite ordering](https://support.microsoft.com/help/4032720/how-to-deploy-custom-cipher-suite-ordering-in-windows-server-2016).

 



| Cipher suite                                                 | FIPS mode enabled | Exchange              | Encryption      | Hash            | Protocols                   |
|--------------------------------------------------------------|-------------------|-----------------------|-----------------|-----------------|-----------------------------|
| TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA<br/>                | Yes<br/>    | RSA<br/>        | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA<br/>                | Yes<br/>    | RSA<br/>        | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_RSA\_WITH\_RC4\_128\_SHA<br/>                     | No<br/>     | RSA<br/>        | RC4<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA<br/>               | Yes<br/>    | RSA<br/>        | 3DES<br/> | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P256<br/> | Yes<br/>    | ECDH\_P256<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P384<br/> | Yes<br/>    | ECDH\_P384<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA\_P521<br/> | Yes<br/>    | ECDH\_P521<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P256<br/> | Yes<br/>    | ECDH\_P256<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P384<br/> | Yes<br/>    | ECDH\_P384<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA\_P521<br/> | Yes<br/>    | ECDH\_P521<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P256<br/>   | Yes<br/>    | ECDH\_P256<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P384<br/>   | Yes<br/>    | ECDH\_P384<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA\_P521<br/>   | Yes<br/>    | ECDH\_P521<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P256<br/>   | Yes<br/>    | ECDH\_P256<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P384<br/>   | Yes<br/>    | ECDH\_P384<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA\_P521<br/>   | Yes<br/>    | ECDH\_P521<br/> | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA<br/>           | Yes<br/>    | DH<br/>         | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA<br/>           | Yes<br/>    | DH<br/>         | AES<br/>  | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0<br/>          |
| TLS\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA<br/>          | Yes<br/>    | DH<br/>         | 3DES<br/> | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_RC4\_128\_MD5<br/>                     | No<br/>     | RSA<br/>        | RC4<br/>  | MD5<br/>  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| SSL\_CK\_RC4\_128\_WITH\_MD5<br/>                      | No<br/>     | RSA<br/>        | RC4<br/>  | MD5<br/>  | SSL 2.0<br/>          |
| SSL\_CK\_DES\_192\_EDE3\_CBC\_WITH\_MD5<br/>           | No<br/>     | RSA<br/>        | 3DES<br/> | MD5<br/>  | SSL 2.0<br/>          |
| TLS\_RSA\_WITH\_NULL\_MD5<br/>                         | No<br/>     | RSA<br/>        |                 | MD5<br/>  | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |
| TLS\_RSA\_WITH\_NULL\_SHA<br/>                         | No<br/>     | RSA<br/>        |                 | SHA1<br/> | TLS 1.2, TLS 1.1, TLS 1.0, SSL 3.0<br/> |



 

The following cipher suites are supported by Schannel; however, they are not present by default. They must be added as necessary. For information about how to add cipher suites to the Schannel provider, see [Prioritizing Schannel Cipher Suites](prioritizing-schannel-cipher-suites.md).

-   TLS\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5
-   TLS\_RSA\_EXPORT1024\_WITH\_RC4\_56\_SHA
-   TLS\_RSA\_EXPORT1024\_WITH\_DES\_CBC\_SHA
-   SSL\_CK\_RC4\_128\_EXPORT40\_MD5
-   SSL\_CK\_DES\_64\_CBC\_WITH\_MD5
-   TLS\_RSA\_WITH\_DES\_CBC\_SHA
-   TLS\_RSA\_WITH\_NULL\_MD5
-   TLS\_RSA\_WITH\_NULL\_SHA
-   TLS\_DHE\_DSS\_EXPORT1024\_WITH\_DES\_CBC\_SHA
-   TLS\_DHE\_DSS\_WITH\_DES\_CBC\_SHA

**Windows Server 2003 and Windows XP:** For information about supported cipher suites, see the following topics.

| Topic                                                                         | Description                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [TLS Cipher Suites](tls-cipher-suites.md)<br/>                         | Information about the cipher suites available with the TLS protocol in Windows Server 2003 and Windows XP.<br/>              |
| [Secure Sockets Layer Protocol](secure-sockets-layer-protocol.md)<br/> | General information about SSL 2.0 and 3.0, including the available cipher suites in Windows Server 2003 and Windows XP.<br/> |



 

 

 
