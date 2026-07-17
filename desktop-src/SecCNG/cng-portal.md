---
description: CNG is an encryption API that you can use to create encryption security software for encryption key management, cryptography and data security, and cryptography and network security.
ms.assetid: eaad88a1-4e1d-4246-9560-8eef60f8b70f
title: 'Cryptography API: Next Generation'
ms.topic: concept-article
ms.date: 07/09/2025
# customer intent: As a Windows developer, I want to learn about the Cryptography API: Next Generation (CNG) so that I can use it to create encryption security software for encryption key management, cryptography and data security, and cryptography and network security.
---

# Cryptography API: Next Generation

## Purpose

Cryptography API: Next Generation (CNG) is the long-term replacement for the [CryptoAPI](../secgloss/c-gly.md). CNG is designed to be extensible at many levels and cryptography agnostic in behavior.

## Developer audience

CNG is intended for use by developers of applications that will enable users to create and exchange documents and other data in a secure environment, especially over nonsecure media such as the Internet. Developers should be familiar with the C and C++ programming languages and the Windows-based programming environment. Although not required, an understanding of cryptography or security-related subjects is advised.

If you are developing a CNG cryptographic algorithm provider or key storage provider, you must download the [Cryptographic Provider Development Kit](https://www.microsoft.com/download/details.aspx?id=30688) from Microsoft.

## Run-time requirements

CNG is supported beginning with Windows Server 2008 and Windows Vista. For information about runtime requirements for a particular programming element, see the **Requirements** section of the reference page for that element.

## In this section

The following topics provide information about CNG and how to use it in your applications:

| Topic | Description |
|-------|-------------|
| [About CNG](about-cng.md) | Describes CNG features, cryptographic primitives, and key storage, retrieval, import, and export. |
| [Using CNG](using-cng.md) | Explains how to use the cryptography configuration features of CNG and typical CNG programming. |
| [CNG Reference](cng-reference.md) | Detailed descriptions of the CNG programming elements. These pages include reference descriptions of the API for working with CNG. |

## When to use CNG

Use CNG when you need direct control over cryptographic operations in Windows applications. The following guidance helps you choose the appropriate API:

| Scenario | Recommended API |
|----------|-----------------|
| Symmetric encryption/decryption (AES, ChaCha20-Poly1305) | CNG ([BCryptEncrypt](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptencrypt) / [BCryptDecrypt](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptdecrypt)) |
| Hashing (SHA-256, SHA-384, SHA-512) | CNG ([BCryptCreateHash](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptcreatehash)) |
| Asymmetric operations (RSA, ECDSA, ML-DSA) | CNG ([BCryptSignHash](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsignhash), [BCryptVerifySignature](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptverifysignature)) |
| Protecting user data at rest (per-user or per-machine scope) | [DPAPI](/windows/win32/api/Dpapi/nf-dpapi-cryptprotectdata) (simpler, no key management required) |
| Protecting data accessible to multiple users or machines | [DPAPI-NG](cng-dpapi.md) ([NCryptProtectSecret](/windows/win32/api/NCryptprotect/nf-ncryptprotect-ncryptprotectsecret)) |
| TLS/SSL connections | [Schannel](../SecAuthN/secure-channel.md) (uses CNG internally) |
| Legacy code that already uses CryptoAPI | Continue with CryptoAPI for maintenance, but plan migration to CNG for new features |

> [!WARNING]
> **Common cryptographic pitfalls to avoid:**
> - Do not use ECB block cipher mode — it leaks plaintext patterns. Use CBC with a random IV, or preferably an authenticated mode like GCM.
> - Do not hardcode encryption keys in source code. Use key storage providers or DPAPI for key protection.
> - Do not use MD5 or SHA-1 for integrity or security purposes. Use SHA-256 or stronger.
> - Always validate return codes from CNG functions. A failed cryptographic operation that is silently ignored can lead to data being stored unencrypted.

## Related content

[Cryptographic Provider Development Kit](https://www.microsoft.com/download/details.aspx?id=30688)

[CryptoAPI](../secgloss/c-gly.md)
