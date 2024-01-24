---
description: 'Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs).'
ms.assetid: bd4aadc5-d953-4971-b862-00f6d4db0572
title: CNG Key Storage Providers
ms.topic: article
ms.date: 05/31/2018
---

# CNG Key Storage Providers

Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs). KSPs can be used to create, delete, export, import, open and store keys. Depending on implementation, they can also be used for asymmetric encryption, secret agreement, and signing. Microsoft installs the following KSPs beginning with Windows Vista and Windows Server 2008. Vendors can create and install other providers.

## Microsoft Software Key Storage Provider

Supports software key creation and storage and the following algorithms.



| Algorithm                                          | Purpose                           | Key length (bits)                 |
|----------------------------------------------------|-----------------------------------|-----------------------------------|
| Diffie-Hellman (DH)                                | Secret agreement and key exchange | 512 to 4096 in 64-bit increments  |
| Digital Signature Algorithm (DSA)                  | Signatures                        | 512 to 1024 in 64-bit increments  |
| Elliptic Curve Diffie-Hellman (ECDH)               | Secret agreement and key exchange | P256, P384, P521                  |
| Elliptic Curve Digital Signature Algorithm (ECDSA) | Signatures                        | P256, P384, P521                  |
| RSA                                                | Asymmetric encryption and signing | 512 to 16384 in 64-bit increments |



 

## Microsoft Smart Card Key Storage Provider

Supports smart card key creation and storage and the following algorithms.



| Algorithm                                          | Purpose                           | Key length (bits)                 |
|----------------------------------------------------|-----------------------------------|-----------------------------------|
| Diffie-Hellman (DH)                                | Secret agreement and key exchange | 512 to 4096 in 64-bit increments  |
| Elliptic Curve Diffie-Hellman (ECDH)               | Secret agreement and key exchange | P256, P384, P521                  |
| Elliptic Curve Digital Signature Algorithm (ECDSA) | Signatures                        | P256, P384, P521                  |
| RSA                                                | Asymmetric encryption and signing | 512 to 16384 in 64-bit increments |



 

## Related topics

<dl> <dt>

[**CNG Algorithm Identifiers**](/windows/desktop/SecCNG/cng-algorithm-identifiers)
</dt> <dt>

[CNG Key Storage Functions](/windows/desktop/SecCNG/cng-key-storage-functions)
</dt> <dt>

[Understanding Cryptographic Providers](understanding-cryptographic-providers.md)
</dt> </dl>

 

 
