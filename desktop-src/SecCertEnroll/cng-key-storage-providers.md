---
description: 'Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs).'
ms.assetid: bd4aadc5-d953-4971-b862-00f6d4db0572
title: CNG Key Storage Providers
ms.topic: concept-article
ms.date: 06/12/2026
# Customer intent: As a Windows developer, I want to learn about the Cryptography API: Next Generation (CNG) key storage providers in Windows.
---

# CNG Key Storage Providers

Unlike Cryptography API (CryptoAPI), Cryptography API: Next Generation (CNG) separates cryptographic providers from key storage providers (KSPs). Use KSPs to create, delete, export, import, open, and store keys. Depending on the implementation, use them for asymmetric encryption, secret agreement, and signing. Microsoft installs the following KSPs on Windows. However, vendors can create and install other providers.

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

## Microsoft Platform Crypto Provider

The **Microsoft Platform Crypto Provider** is a key storage provider (KSP) that utilizes the Trusted Platform Module (TPM) for enhanced security. This provider is particularly useful for scenarios requiring hardware-backed security for cryptographic operations.

The Microsoft Platform Crypto Provider is designed to work with the TPM, a hardware-based security module that provides robust protection for cryptographic keys. By leveraging the TPM, this provider ensures that private keys are securely stored and cannot be extracted, even by malicious software.

### Key Features

The following are some of the key features of the Microsoft Platform Crypto Provider:

- **Hardware-backed security**: Utilizes the TPM to store cryptographic keys securely.
- **Enhanced protection**: Prevents unauthorized access to private keys.
- **Integration with Windows**: Fully integrated with the Windows Cryptography API: Next Generation (CNG).

### Usage

To use the Microsoft Platform Crypto Provider, you can specify it when opening a storage provider using the `NCryptOpenStorageProvider` function. For example:

```c
#include <ncrypt.h>

NCRYPT_PROV_HANDLE hProvider = NULL;
SECURITY_STATUS status = NCryptOpenStorageProvider(
    &hProvider,
    MS_PLATFORM_CRYPTO_PROVIDER,
    0
);

if (status == ERROR_SUCCESS) {
    // Successfully opened the Microsoft Platform Crypto Provider
}
```

In this example, the `MS_PLATFORM_CRYPTO_PROVIDER` constant is used to specify the Microsoft Platform Crypto Provider.

### Additional Resources

For more information, see [NCryptOpenStorageProvider](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenstorageprovider).

## Related content

**[CNG Algorithm Identifiers](/windows/win32/SecCNG/cng-algorithm-identifiers)**

[CNG Key Storage Functions](/windows/win32/SecCNG/cng-key-storage-functions)

[Understanding Cryptographic Providers](understanding-cryptographic-providers.md)
