---
description: Explains how to generate, exchange, import, and export Diffie-Hellman keys using the Cryptography API: Next Generation (CNG).
ms.assetid: 623a8c9e-3f6a-470b-be30-dec13342bb90
title: Diffie-Hellman Keys
ms.topic: concept-article
ms.date: 04/12/2026
---

# Diffie-Hellman Keys

> [!IMPORTANT]
> This article uses the [Cryptography API: Next Generation (CNG)](/windows/win32/seccng/cng-portal), which is the recommended API for new Windows cryptographic applications. For most new applications, consider using [Elliptic Curve Diffie-Hellman (ECDH)](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsecretagreement) with a standard named curve such as P-256 or P-384, which provides equivalent or stronger security with shorter keys and less parameter management overhead.
>
> The legacy CryptoAPI (CAPI1) functions (`CryptGenKey`, `CryptExportKey`, `CryptAcquireContext`, and so on) are deprecated. Do not use them in new applications.

- [Generating Diffie-Hellman Keys](#generating-diffie-hellman-keys)
- [Exchanging Diffie-Hellman Keys](#exchanging-diffie-hellman-keys)
- [Exporting a Diffie-Hellman Private Key](#exporting-a-diffie-hellman-private-key)
- [Example Code](#example-code)
- [Related content](#related-content)

## Generating Diffie-Hellman Keys

To generate a Diffie-Hellman key pair using CNG, perform the following steps:

1. Call [**BCryptOpenAlgorithmProvider**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) with `BCRYPT_DH_ALGORITHM` to get an algorithm provider handle.

2. Call [**BCryptGenerateKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair) to create the key pair, specifying the key size in bits. Use at least 2048 bits for adequate security; 512-bit keys (as used in legacy CAPI1 examples) are cryptographically weak and must not be used in new code.

3. Set DH parameters (the prime *P* and generator *G*) by calling [**BCryptSetProperty**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetproperty) with the `BCRYPT_DH_PARAMETERS` property before calling [**BCryptFinalizeKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair). The property value must be a [**BCRYPT_DH_PARAMETER_HEADER**](/windows/win32/api/bcrypt/ns-bcrypt-bcrypt_dh_parameter_header) structure followed immediately by the *P* value and then the *G* value, each `cbKeyLength` bytes in length, in big-endian byte order.

   Both parties must use the same *P* and *G* values; the `BCRYPT_DH_PUBLIC_BLOB` export format includes *P* and *G* so the recipient can extract them.

4. Call [**BCryptFinalizeKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair) to complete the key generation. This function must be called before the key can be used or exported.

5. When the key is no longer needed, call [**BCryptDestroyKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroykey) to release the key handle, and [**BCryptCloseAlgorithmProvider**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptclosealgorithmprovider) to release the provider handle.

## Exchanging Diffie-Hellman Keys

The purpose of the Diffie-Hellman algorithm is to make it possible for two or more parties to create and share an identical, secret value by sharing information over a network that is not secure. The information that gets shared over the network is each party's Diffie-Hellman public key. The process used by two key-exchange parties is as follows:

- Both parties agree on Diffie-Hellman parameters: a prime number (*P*) and a generator number (*G*).
- Party 1 sends its Diffie-Hellman public key to Party 2.
- Party 2 computes the shared secret by using its own private key and Party 1's public key.
- Party 2 sends its Diffie-Hellman public key to Party 1.
- Party 1 computes the shared secret by using its own private key and Party 2's public key.
- Both parties now have the same shared secret, which can be used to derive a symmetric encryption key.

**To prepare a Diffie-Hellman public key for transmission:**

1. After generating and finalizing the key pair, call [**BCryptExportKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) with `BCRYPT_DH_PUBLIC_BLOB` as the blob type to get the public key bytes. The blob includes the *P*, *G*, and public key *Y* values, all in big-endian byte order.

2. Transmit those bytes to the other party over the network.

> [!NOTE]
> Key material in CNG DH blobs (`BCRYPT_DH_PUBLIC_BLOB`, `BCRYPT_DH_PRIVATE_BLOB`) is in **big-endian** byte order. This is the opposite of the little-endian format used by the deprecated CryptoAPI (CAPI1). Take care when interoperating with CAPI1-encoded key material.

**To import a Diffie-Hellman public key and derive the shared secret:**

1. Call [**BCryptImportKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkeypair) with `BCRYPT_DH_PUBLIC_BLOB` to import the other party's public key. This requires an algorithm provider handle opened with `BCRYPT_DH_ALGORITHM`.

2. Call [**BCryptSecretAgreement**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsecretagreement) with your own private key handle and the imported public key handle. This produces a *secret agreement* handle representing the raw shared secret value, (Y^X) mod P.

3. Call [**BCryptDeriveKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekey) to derive usable key material from the shared secret. Use a key derivation function (KDF) appropriate for your scenario; `BCRYPT_KDF_HASH` with `SHA-256` is a suitable general-purpose choice.

4. Use the derived key bytes to construct a symmetric key (for example, call [**BCryptGenerateSymmetricKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratesymmetrickey) with `BCRYPT_AES_ALGORITHM`) for subsequent encryption or decryption.

5. When finished, call [**BCryptDestroySecret**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroysecret) to release the secret agreement handle, and [**BCryptDestroyKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroykey) to release all key handles.

## Exporting a Diffie-Hellman Private Key

> [!CAUTION]
> Exporting private keys is a security-sensitive operation. Only export private key material when absolutely necessary, and protect it appropriately. For keys stored in a key storage provider (KSP), the provider may restrict export based on key policy.

To export a Diffie-Hellman private key as a memory blob, call [**BCryptExportKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) with `BCRYPT_DH_PRIVATE_BLOB`. The resulting blob contains a [**BCRYPT_DH_KEY_BLOB**](/windows/win32/api/bcrypt/ns-bcrypt-bcrypt_dh_key_blob) header followed by the *P*, *G*, public *Y*, and private *X* values, each in big-endian byte order.

To later import the private key, call [**BCryptImportKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkeypair) with `BCRYPT_DH_PRIVATE_BLOB`.

## Example Code

The following example demonstrates a Diffie-Hellman key exchange between two parties using CNG. Both parties derive the same shared secret, which is then used to construct an AES-256 symmetric key.

> [!NOTE]
> **FEEDBACK REQUIRED** — Please review the parameter sizes, KDF usage, and AES key derivation in this example for correctness and completeness before publication. In particular, verify that: (1) the `BCRYPT_DH_PARAMETERS` blob layout (P then G, big-endian) is correct; (2) `BCryptDeriveKey` with `BCRYPT_KDF_HASH` produces output suitable for direct use as AES-256 key material without additional processing; (3) the Party 2 parameter-reuse approach (extracting P/G from Party 1's public blob) is the recommended pattern.

```cpp
#include <windows.h>
#include <bcrypt.h>
#include <stdio.h>
#include <cstring>
#pragma comment(lib, "bcrypt.lib")

#define NT_SUCCESS(Status) (((NTSTATUS)(Status)) >= 0)
#define CHECK(s, fn) if (!NT_SUCCESS(s)) { wprintf(L"Error in %s: 0x%08x\n", fn, s); goto cleanup; }

// 2048-bit MODP Group 14 prime (RFC 3526), big-endian.
// FEEDBACK REQUIRED: Confirm use of a standardized group is appropriate here,
// or whether the example should generate parameters dynamically instead.
static const BYTE g_Prime2048[] =
{
    0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xC9,0x0F,0xDA,0xA2,0x21,0x68,0xC2,0x34,
    0xC4,0xC6,0x62,0x8B,0x80,0xDC,0x1C,0xD1,0x29,0x02,0x4E,0x08,0x8A,0x67,0xCC,0x74,
    0x02,0x0B,0xBE,0xA6,0x3B,0x13,0x9B,0x22,0x51,0x4A,0x08,0x79,0x8E,0x34,0x04,0xDD,
    0xEF,0x95,0x19,0xB3,0xCD,0x3A,0x43,0x1B,0x30,0x2B,0x0A,0x6D,0xF2,0x5F,0x14,0x37,
    0x4F,0xE1,0x35,0x6D,0x6D,0x51,0xC2,0x45,0xE4,0x85,0xB5,0x76,0x62,0x5E,0x7E,0xC6,
    0xF4,0x4C,0x42,0xE9,0xA6,0x37,0xED,0x6B,0x0B,0xFF,0x5C,0xB6,0xF4,0x06,0xB7,0xED,
    0xEE,0x38,0x6B,0xFB,0x5A,0x89,0x9F,0xA5,0xAE,0x9F,0x24,0x11,0x7C,0x4B,0x1F,0xE6,
    0x49,0x28,0x66,0x51,0xEC,0xE4,0x5B,0x3D,0xC2,0x00,0x7C,0xB8,0xA1,0x63,0xBF,0x05,
    0x98,0xDA,0x48,0x36,0x1C,0x55,0xD3,0x9A,0x69,0x16,0x3F,0xA8,0xFD,0x24,0xCF,0x5F,
    0x83,0x65,0x5D,0x23,0xDC,0xA3,0xAD,0x96,0x1C,0x62,0xF3,0x56,0x20,0x85,0x52,0xBB,
    0x9E,0xD5,0x29,0x07,0x70,0x96,0x96,0x6D,0x67,0x0C,0x35,0x4E,0x4A,0xBC,0x98,0x04,
    0xF1,0x74,0x6C,0x08,0xCA,0x18,0x21,0x7C,0x32,0x90,0x5E,0x46,0x2E,0x36,0xCE,0x3B,
    0xE3,0x9E,0x77,0x2C,0x18,0x0E,0x86,0x03,0x9B,0x27,0x83,0xA2,0xEC,0x07,0xA2,0x8F,
    0xB5,0xC5,0x5D,0xF0,0x6F,0x4C,0x52,0xC9,0xDE,0x2B,0xCB,0xF6,0x95,0x58,0x17,0x18,
    0x39,0x95,0x49,0x7C,0xEA,0x95,0x6A,0xE5,0x15,0xD2,0x26,0x18,0x98,0xFA,0x05,0x10,
    0x15,0x72,0x8E,0x5A,0x8A,0xAC,0xAA,0x68,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF
};

// Generator for MODP Group 14 (g = 2), big-endian, zero-padded to 256 bytes.
static BYTE g_Generator2048[256] = { 0 };  // initialized to zero; set g_Generator2048[255] = 2 below

#define KEY_SIZE_BITS  2048
#define KEY_SIZE_BYTES (KEY_SIZE_BITS / 8)

int wmain()
{
    // Set generator value (g = 2)
    g_Generator2048[KEY_SIZE_BYTES - 1] = 2;

    NTSTATUS status;
    BCRYPT_ALG_HANDLE hAlg1 = NULL, hAlg2 = NULL;
    BCRYPT_KEY_HANDLE hKey1 = NULL, hKey2 = NULL;
    BCRYPT_KEY_HANDLE hPubKey1 = NULL, hPubKey2 = NULL;
    BCRYPT_SECRET_HANDLE hSecret1 = NULL, hSecret2 = NULL;
    PBYTE pbPubBlob1 = NULL, pbPubBlob2 = NULL;
    PBYTE pbParams = NULL;
    PBYTE pbDerivedKey1 = NULL, pbDerivedKey2 = NULL;
    ULONG cbPubBlob1 = 0, cbPubBlob2 = 0;
    ULONG cbDerivedKey = 0;

    // Build the BCRYPT_DH_PARAMETERS blob: header + P + G (all big-endian).
    ULONG cbParams = sizeof(BCRYPT_DH_PARAMETER_HEADER) + 2 * KEY_SIZE_BYTES;
    pbParams = (PBYTE)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, cbParams);
    if (!pbParams) { wprintf(L"Out of memory\n"); goto cleanup; }

    BCRYPT_DH_PARAMETER_HEADER* pHeader = (BCRYPT_DH_PARAMETER_HEADER*)pbParams;
    pHeader->cbLength    = cbParams;
    pHeader->dwMagic     = BCRYPT_DH_PARAMETERS_MAGIC;
    pHeader->cbKeyLength = KEY_SIZE_BYTES;
    memcpy(pbParams + sizeof(BCRYPT_DH_PARAMETER_HEADER),                   g_Prime2048,     KEY_SIZE_BYTES); // P
    memcpy(pbParams + sizeof(BCRYPT_DH_PARAMETER_HEADER) + KEY_SIZE_BYTES,  g_Generator2048, KEY_SIZE_BYTES); // G

    //
    // --- Party 1: generate key pair ---
    //
    status = BCryptOpenAlgorithmProvider(&hAlg1, BCRYPT_DH_ALGORITHM, NULL, 0);
    CHECK(status, L"BCryptOpenAlgorithmProvider (Party 1)");

    status = BCryptGenerateKeyPair(hAlg1, &hKey1, KEY_SIZE_BITS, 0);
    CHECK(status, L"BCryptGenerateKeyPair (Party 1)");

    status = BCryptSetProperty(hKey1, BCRYPT_DH_PARAMETERS, pbParams, cbParams, 0);
    CHECK(status, L"BCryptSetProperty BCRYPT_DH_PARAMETERS (Party 1)");

    status = BCryptFinalizeKeyPair(hKey1, 0);
    CHECK(status, L"BCryptFinalizeKeyPair (Party 1)");

    // Export Party 1's public key blob (includes P, G, Y).
    status = BCryptExportKey(hKey1, NULL, BCRYPT_DH_PUBLIC_BLOB, NULL, 0, &cbPubBlob1, 0);
    CHECK(status, L"BCryptExportKey size (Party 1)");

    pbPubBlob1 = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPubBlob1);
    if (!pbPubBlob1) { wprintf(L"Out of memory\n"); goto cleanup; }

    status = BCryptExportKey(hKey1, NULL, BCRYPT_DH_PUBLIC_BLOB, pbPubBlob1, cbPubBlob1, &cbPubBlob1, 0);
    CHECK(status, L"BCryptExportKey (Party 1)");

    //
    // --- Party 2: generate key pair using same P and G ---
    //
    status = BCryptOpenAlgorithmProvider(&hAlg2, BCRYPT_DH_ALGORITHM, NULL, 0);
    CHECK(status, L"BCryptOpenAlgorithmProvider (Party 2)");

    status = BCryptGenerateKeyPair(hAlg2, &hKey2, KEY_SIZE_BITS, 0);
    CHECK(status, L"BCryptGenerateKeyPair (Party 2)");

    // Party 2 reuses the same DH parameters as Party 1.
    status = BCryptSetProperty(hKey2, BCRYPT_DH_PARAMETERS, pbParams, cbParams, 0);
    CHECK(status, L"BCryptSetProperty BCRYPT_DH_PARAMETERS (Party 2)");

    status = BCryptFinalizeKeyPair(hKey2, 0);
    CHECK(status, L"BCryptFinalizeKeyPair (Party 2)");

    // Export Party 2's public key blob.
    status = BCryptExportKey(hKey2, NULL, BCRYPT_DH_PUBLIC_BLOB, NULL, 0, &cbPubBlob2, 0);
    CHECK(status, L"BCryptExportKey size (Party 2)");

    pbPubBlob2 = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPubBlob2);
    if (!pbPubBlob2) { wprintf(L"Out of memory\n"); goto cleanup; }

    status = BCryptExportKey(hKey2, NULL, BCRYPT_DH_PUBLIC_BLOB, pbPubBlob2, cbPubBlob2, &cbPubBlob2, 0);
    CHECK(status, L"BCryptExportKey (Party 2)");

    //
    // --- Party 1: import Party 2's public key, compute shared secret ---
    //
    status = BCryptImportKeyPair(hAlg1, NULL, BCRYPT_DH_PUBLIC_BLOB, &hPubKey2, pbPubBlob2, cbPubBlob2, 0);
    CHECK(status, L"BCryptImportKeyPair Party 2 public key (into Party 1)");

    status = BCryptSecretAgreement(hKey1, hPubKey2, &hSecret1, 0);
    CHECK(status, L"BCryptSecretAgreement (Party 1)");

    // Derive 32 bytes of key material using SHA-256.
    BCryptBufferDesc kdfParams = { 0 };
    BCryptBuffer kdfBuffer = { 0 };
    WCHAR szHashAlg[] = BCRYPT_SHA256_ALGORITHM;
    kdfBuffer.BufferType = KDF_HASH_ALGORITHM;
    kdfBuffer.cbBuffer   = sizeof(szHashAlg);
    kdfBuffer.pvBuffer   = szHashAlg;
    kdfParams.ulVersion  = BCRYPTBUFFER_VERSION;
    kdfParams.cBuffers   = 1;
    kdfParams.pBuffers   = &kdfBuffer;

    status = BCryptDeriveKey(hSecret1, BCRYPT_KDF_HASH, &kdfParams, NULL, 0, &cbDerivedKey, 0);
    CHECK(status, L"BCryptDeriveKey size (Party 1)");

    pbDerivedKey1 = (PBYTE)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, cbDerivedKey);
    if (!pbDerivedKey1) { wprintf(L"Out of memory\n"); goto cleanup; }

    status = BCryptDeriveKey(hSecret1, BCRYPT_KDF_HASH, &kdfParams, pbDerivedKey1, cbDerivedKey, &cbDerivedKey, 0);
    CHECK(status, L"BCryptDeriveKey (Party 1)");

    //
    // --- Party 2: import Party 1's public key, compute shared secret ---
    //
    status = BCryptImportKeyPair(hAlg2, NULL, BCRYPT_DH_PUBLIC_BLOB, &hPubKey1, pbPubBlob1, cbPubBlob1, 0);
    CHECK(status, L"BCryptImportKeyPair Party 1 public key (into Party 2)");

    status = BCryptSecretAgreement(hKey2, hPubKey1, &hSecret2, 0);
    CHECK(status, L"BCryptSecretAgreement (Party 2)");

    pbDerivedKey2 = (PBYTE)HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, cbDerivedKey);
    if (!pbDerivedKey2) { wprintf(L"Out of memory\n"); goto cleanup; }

    ULONG cbDerivedKey2 = cbDerivedKey;
    status = BCryptDeriveKey(hSecret2, BCRYPT_KDF_HASH, &kdfParams, pbDerivedKey2, cbDerivedKey2, &cbDerivedKey2, 0);
    CHECK(status, L"BCryptDeriveKey (Party 2)");

    //
    // Verify both parties derived the same key material.
    //
    if (cbDerivedKey == cbDerivedKey2 && memcmp(pbDerivedKey1, pbDerivedKey2, cbDerivedKey) == 0)
    {
        wprintf(L"Success: both parties derived the same %u-byte key material.\n", cbDerivedKey);
    }
    else
    {
        wprintf(L"Error: derived keys do not match.\n");
    }

cleanup:
    if (pbDerivedKey2)  { SecureZeroMemory(pbDerivedKey2, cbDerivedKey); HeapFree(GetProcessHeap(), 0, pbDerivedKey2); }
    if (pbDerivedKey1)  { SecureZeroMemory(pbDerivedKey1, cbDerivedKey); HeapFree(GetProcessHeap(), 0, pbDerivedKey1); }
    if (hSecret2)       BCryptDestroySecret(hSecret2);
    if (hSecret1)       BCryptDestroySecret(hSecret1);
    if (hPubKey1)       BCryptDestroyKey(hPubKey1);
    if (hPubKey2)       BCryptDestroyKey(hPubKey2);
    if (pbPubBlob2)     HeapFree(GetProcessHeap(), 0, pbPubBlob2);
    if (pbPubBlob1)     HeapFree(GetProcessHeap(), 0, pbPubBlob1);
    if (hKey2)          BCryptDestroyKey(hKey2);
    if (hKey1)          BCryptDestroyKey(hKey1);
    if (hAlg2)          BCryptCloseAlgorithmProvider(hAlg2, 0);
    if (hAlg1)          BCryptCloseAlgorithmProvider(hAlg1, 0);
    if (pbParams)       HeapFree(GetProcessHeap(), 0, pbParams);

    return 0;
}
```

## Related content

- [Cryptography API: Next Generation (CNG)](/windows/win32/seccng/cng-portal)
- [Overview of typical CNG programming](/windows/win32/seccng/typical-cng-programming)
- [**BCryptOpenAlgorithmProvider**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)
- [**BCryptGenerateKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair)
- [**BCryptFinalizeKeyPair**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair)
- [**BCryptSecretAgreement**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsecretagreement)
- [**BCryptDeriveKey**](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekey)
- [**BCRYPT_DH_KEY_BLOB**](/windows/win32/api/bcrypt/ns-bcrypt-bcrypt_dh_key_blob)
- [**BCRYPT_DH_PARAMETER_HEADER**](/windows/win32/api/bcrypt/ns-bcrypt-bcrypt_dh_parameter_header)
- [CNG Algorithm Identifiers](/windows/win32/seccng/cng-algorithm-identifiers)




 

 
