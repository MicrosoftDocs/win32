---
description: 'Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs).'
ms.assetid: bd4aadc5-d953-4971-b862-00f6d4db0572
title: CNG Key Storage Providers
ms.topic: concept-article
ms.date: 11/21/2024
# Customer intent: As a Windows developer, I want to learn about the Cryptography API: Next Generation (CNG) key storage providers in Windows.
---

# CNG Key Storage Providers

Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs). KSPs can be used to create, delete, export, import, open and store keys. Depending on implementation, they can also be used for asymmetric encryption, secret agreement, and signing. Microsoft installs the following KSPs on Windows. However, vendors can create and install other providers.

## Microsoft Software Key Storage Provider

The **Microsoft Software Key Storage Provider** supports software key creation and storage and the following algorithms.

| Algorithm                                          | Purpose                           | Key length (bits)                 |
|----------------------------------------------------|-----------------------------------|-----------------------------------|
| Diffie-Hellman (DH)                                | Secret agreement and key exchange | 512 to 4096 in 64-bit increments  |
| Digital Signature Algorithm (DSA)                  | Signatures                        | 512 to 1024 in 64-bit increments  |
| Elliptic Curve Diffie-Hellman (ECDH)               | Secret agreement and key exchange | P256, P384, P521                  |
| Elliptic Curve Digital Signature Algorithm (ECDSA) | Signatures                        | P256, P384, P521                  |
| RSA                                                | Asymmetric encryption and signing | 512 to 16384 in 64-bit increments |

## Microsoft Smart Card Key Storage Provider

The **Microsoft Smart Card Key Storage Provider** supports smart card key creation and storage and the following algorithms.

| Algorithm                                          | Purpose                           | Key length (bits)                 |
|----------------------------------------------------|-----------------------------------|-----------------------------------|
| Diffie-Hellman (DH)                                | Secret agreement and key exchange | 512 to 4096 in 64-bit increments  |
| Elliptic Curve Diffie-Hellman (ECDH)               | Secret agreement and key exchange | P256, P384, P521                  |
| Elliptic Curve Digital Signature Algorithm (ECDSA) | Signatures                        | P256, P384, P521                  |
| RSA                                                | Asymmetric encryption and signing | 512 to 16384 in 64-bit increments |

## Related content

[**CNG Algorithm Identifiers**](/windows/win32/SecCNG/cng-algorithm-identifiers)

[CNG Key Storage Functions](/windows/win32/SecCNG/cng-key-storage-functions)

[Understanding Cryptographic Providers](understanding-cryptographic-providers.md)
