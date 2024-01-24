---
description: Lists the cryptographic service providers available from Microsoft.
ms.assetid: 1461914e-5506-4f24-97da-3d2148aafd1c
title: Microsoft Cryptographic Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Cryptographic Service Providers

The following [*cryptographic service providers*](../secgloss/c-gly.md) (CSP) are currently available from Microsoft.



| Provider                                                                                                                                 | Description                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Microsoft Base Cryptographic Provider](microsoft-base-cryptographic-provider.md)                                                       | A broad set of basic cryptographic functionality that can be exported to other countries or regions.                                                                                                                                                     |
| [Microsoft Strong Cryptographic Provider](microsoft-strong-cryptographic-provider.md)                                                   | An extension of the Microsoft Base Cryptographic Provider available with Windows XP and later.                                                                                                                                                           |
| [Microsoft Enhanced Cryptographic Provider](microsoft-enhanced-cryptographic-provider.md)                                               | Microsoft Base Cryptographic Provider with through longer keys and additional algorithms.                                                                                                                                                                |
| [Microsoft AES Cryptographic Provider](microsoft-aes-cryptographic-provider.md)                                                         | Microsoft Enhanced Cryptographic Provider with support for AES encryption algorithms.                                                                                                                                                                    |
| [Microsoft DSS Cryptographic Provider](microsoft-dss-cryptographic-provider.md)                                                         | Provides hashing, data signing, and signature verification capability using the Secure Hash Algorithm ([*SHA*](../secgloss/s-gly.md)) and Digital Signature Standard (DSS) algorithms. |
| [Microsoft Base DSS and Diffie-Hellman Cryptographic Provider](microsoft-base-dss-and-diffie-hellman-cryptographic-provider.md)         | A superset of the DSS Cryptographic Provider that also supports Diffie-Hellman key exchange, hashing, data signing, and signature verification using the Secure Hash Algorithm (SHA) and Digital Signature Standard (DSS) algorithms.                    |
| [Microsoft Enhanced DSS and Diffie-Hellman Cryptographic Provider](microsoft-enhanced-dss-and-diffie-hellman-cryptographic-provider.md) | Supports Diffie-Hellman key exchange (a 40-bit DES derivative), SHA hashing, DSS data signing, and DSS signature verification.                                                                                                                           |
| [Microsoft DSS and Diffie-Hellman/Schannel Cryptographic Provider](microsoft-dss-and-diffie-hellman-schannel-cryptographic-provider.md) | Supports hashing, data signing with DSS, generating Diffie-Hellman (D-H) keys, exchanging D-H keys, and exporting a D-H key. This CSP supports key derivation for the SSL3 and TLS1 protocols.                                                           |
| [Microsoft RSA/Schannel Cryptographic Provider](microsoft-rsa-schannel-cryptographic-provider.md)                                       | Supports hashing, data signing, and signature verification. The algorithm identifier CALG\_SSL3\_SHAMD5 is used for SSL 3.0 and TLS 1.0 client authentication. This CSP supports key derivation for the SSL2, PCT1, SSL3 and TLS1 protocols.             |
| [Microsoft RSA Signature Cryptographic Provider](microsoft-rsa-signature-cryptographic-provider.md)                                     | Provides data signing and signature verification.                                                                                                                                                                                                        |



 

 

 
