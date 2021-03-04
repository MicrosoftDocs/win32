---
description: A cipher suite is a set of cryptographic algorithms.
ms.assetid: 513e5e73-12f8-4b64-86e4-179518c3582d
title: Cipher Suites in TLS/SSL (Schannel SSP)
ms.topic: article
ms.date: 05/31/2018
---

# Cipher Suites in TLS/SSL (Schannel SSP)

A cipher suite is a set of cryptographic algorithms. The schannel SSP implementation of the TLS/SSL protocols use algorithms from a cipher suite to create keys and encrypt information. A cipher suite specifies one algorithm for each of the following tasks:

-   Key exchange
-   Bulk encryption
-   Message authentication

[*Key exchange algorithms*](/windows/desktop/SecGloss/k-gly) protect information required to create shared keys. These algorithms are asymmetric ([*public key algorithms*](/windows/desktop/SecGloss/p-gly)) and perform well for relatively small amounts of data.

Bulk encryption algorithms encrypt messages exchanged between clients and servers. These algorithms are [*symmetric*](/windows/desktop/SecGloss/s-gly) and perform well for large amounts of data.

[Message authentication](message-authentication-codes-in-schannel.md) algorithms generate message [*hashes*](/windows/desktop/SecGloss/h-gly) and signatures that ensure the [*integrity*](/windows/desktop/SecGloss/i-gly) of a message.

Developers specify these elements by using [**ALG\_ID**](/windows/desktop/SecCrypto/alg-id) data types. For more information, see [Specifying Schannel Ciphers and Cipher Strengths](specifying-schannel-ciphers-and-cipher-strengths.md).

In earlier versions of Windows, TLS cipher suites and elliptical curves were configured by using a single string:

![Diagram that shows a single string for a Cipher Suite.](images/tls-cipher-suite.png)

Different Windows versions support different TLS cipher suites and priority order. See the corresponding Windows version for the default order in which they are chosen by the Microsoft Schannel Provider.

**Windows Server 2022:** For information about supported cipher suites, see [TLS Cipher Suites in Windows Server 2022](tls-cipher-suites-in-windows-server-2022.md)

**Windows 10, version 1903:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1903](tls-cipher-suites-in-windows-10-v1903.md)

**Windows 10, version 1809:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1809](tls-cipher-suites-in-windows-10-v1809.md)

**Windows 10, version 1803:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1803](tls-cipher-suites-in-windows-10-v1803.md)

**Windows 10, version 1709:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1709](tls-cipher-suites-in-windows-10-v1709.md)

**Windows 10, version 1703:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1703](tls-cipher-suites-in-windows-10-v1703.md)

**Windows Server 2016 and Windows 10, version 1607:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1607](tls-cipher-suites-in-windows-10-v1607.md)

**Windows 10, version 1511:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1511](tls-cipher-suites-in-windows-10-v1511.md)

**Windows 10, version 1507:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 10 v1507](./tls-cipher-suites-in-windows-10--version-1507.md)

**Windows Server 2012 R2 and Windows 8.1:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 8.1](tls-cipher-suites-in-windows-8-1.md)

**Windows Server 2012 and Windows 8:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 8](tls-cipher-suites-in-windows-8.md)

**Windows Server 2008 R2 and Windows 7:** For information about supported cipher suites, see [TLS Cipher Suites in Windows 7](tls-cipher-suites-in-windows-7.md)

**Windows Server 2008 and Windows Vista:** For information about supported cipher suites, see [TLS Cipher Suites in Windows Vista](schannel-cipher-suites-in-windows-vista.md)

**Windows Server 2003 and Windows XP:** For information about supported cipher suites, see the following topics.

| Topic                                                                         | Description                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [TLS Cipher Suites](tls-cipher-suites.md)<br/>                         | Information about the cipher suites available with the TLS protocol in Windows Server 2003 and Windows XP.<br/>              |
| [Secure Sockets Layer Protocol](secure-sockets-layer-protocol.md)<br/> | General information about SSL 2.0 and 3.0, including the available cipher suites in Windows Server 2003 and Windows XP.<br/> |



 

> [!Note]  
> Prior to Windows 10, cipher suite strings were appended with the elliptic curve to determine the curve priority. Windows 10 supports an elliptic curve priority order setting so the elliptic curve suffix is not required and is overridden by the new elliptic curve priority order, when provided, to allow organizations to use group policy to configure different versions of Windows with the same cipher suites.

 

