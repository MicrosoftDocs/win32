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

## Microsoft Pluton Cryptographic Provider

> [!NOTE]
> The Microsoft Pluton Cryptographic Provider is in preview and may change before release. Microsoft makes no warranties, express or implied, about the information here.
>
> This capability will be available to customers on supported devices starting with Windows Insider Preview build 26340.10012.

The **Microsoft Pluton Cryptographic Provider** is a key storage provider (KSP) that uses the Microsoft Pluton security processor - built directly into the CPU system-on-chip (SoC) - to provide hardware-protected cryptographic key storage and operations through CNG. To learn more about Microsoft Pluton, see [Understanding the Microsoft Pluton security processor](https://techcommunity.microsoft.com/blog/windows-itpro-blog/understanding-the-microsoft-pluton-security-processor/4370413).

### Supported devices

To use the Microsoft Pluton Cryptographic Provider, a device must:

- Run the minimum supported Windows Insider Preview build 26340.10012.
- Have a processor from a supported processor family (see table below), with the Pluton security processor enabled.
- Meet the minimum Pluton firmware version for that processor family.

| Processor family | Minimum Pluton firmware version |
|---|---|
| Intel® Core™ Ultra Series 3 processors | 11.0.0.265 |
| AMD Ryzen™ AI 300 and 400 series processors | 10.6.0.10 |
| Qualcomm Snapdragon® X Series processors | No minimum firmware version required |

### Supported algorithms

The following table lists supported algorithms and their key types:

| Algorithm | Purpose | Key types |
|---|---|---|
| RSA | Asymmetric encryption and signing | 2,048 bits |
| Elliptic Curve Digital Signature Algorithm (ECDSA) | Signatures | P256, P384 |
| Advanced Encryption Standard (AES) | Symmetric encryption | 128, 256 bits | 
| Hash-based Message Authentication Code (HMAC) with SHA-256 or SHA-384 | Message authentication | 256 bits for HMAC-SHA256; 384 bits for HMAC-SHA384 | 

### Supported NCrypt APIs

The Microsoft Pluton Cryptographic Provider supports the NCrypt APIs listed below. <!-- Only these APIs are supported in this preview, subject to the restrictions described in the [usage guide](https://aka.ms/plutonksppreview-usage). -->

| Operation | Supported APIs |
|---|---|
| Discover and open providers | [NCryptEnumStorageProviders](/windows/win32/api/ncrypt/nf-ncrypt-ncryptenumstorageproviders), [NCryptOpenStorageProvider](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenstorageprovider) |
| Create keys | [NCryptCreatePersistedKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey), [NCryptFinalizeKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfinalizekey) | 
| Open and delete keys | [NCryptOpenKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenkey), [NCryptDeleteKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdeletekey) |
| Read and configure properties | [NCryptGetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptgetproperty), [NCryptSetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptsetproperty) |
| Sign and verify | [NCryptSignHash](/windows/win32/api/ncrypt/nf-ncrypt-ncryptsignhash), [NCryptVerifySignature](/windows/win32/api/ncrypt/nf-ncrypt-ncryptverifysignature) | 
| Encrypt and decrypt | [NCryptEncrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptencrypt), [NCryptDecrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdecrypt) | 
| Export public keys | [NCryptExportKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptexportkey) | 
| Import public keys and wrapped HMAC keys | [NCryptImportKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptimportkey) | 
| Discover supported algorithms | [NCryptIsAlgSupported](/windows/win32/api/ncrypt/nf-ncrypt-ncryptisalgsupported), [NCryptEnumAlgorithms](/windows/win32/api/ncrypt/nf-ncrypt-ncryptenumalgorithms) |
| Release resources | [NCryptFreeObject](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfreeobject), [NCryptFreeBuffer](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfreebuffer) | 

<!-- ### Usage

For examples and provider-specific requirements, see [Using the Microsoft Pluton Cryptographic Provider (preview)](https://aka.ms/plutonksppreview-usage). -->

## Related content

**[CNG Algorithm Identifiers](/windows/win32/SecCNG/cng-algorithm-identifiers)**

[CNG Key Storage Functions](/windows/win32/SecCNG/cng-key-storage-functions)

[Understanding Cryptographic Providers](understanding-cryptographic-providers.md)
