---
title: Using Microsoft Pluton Key Storage Provider (preview)
description: This article demonstrates how to use the Microsoft Pluton Key Storage Provider through CNG to perform common cryptographic operations.
ms.date: 11/16/2026
ms.topic: get-started
---

# Using Microsoft Pluton Key Storage Provider (preview)

> [!IMPORTANT]
> The Microsoft Pluton Key Storage Provider is in preview and might change before release. Microsoft makes no warranties, express or implied, about the information in this article.
>
> Customers on supported devices can access this preview capability starting with the following Windows Insider Preview build:
>
> - 26H2 on the Experimental channel: 26340.10013

This article shows how to use the Microsoft Pluton Key Storage Provider through CNG to create keys, sign and verify data, and perform other supported cryptographic operations.

## Prerequisites

- Your device meets the requirements in [Microsoft Pluton Key Storage Provider](/windows/win32/seccertenroll/cng-key-storage-providers#microsoft-pluton-key-storage-provider).
- Windows SDK version 10.0.26100.4948 (August 2025) or a later version.

Refer to [Microsoft Pluton Key Storage Provider](/windows/win32/seccertenroll/cng-key-storage-providers#microsoft-pluton-key-storage-provider) for information about supported algorithms, key types and NCrypt APIs.

## Sample usage

### Sign and verify with ECDSA or RSA 
This example shows how an application creates an ECDSA or RSA key by using the **Microsoft Pluton Key Storage Provider**, signs a hash, and verifies the signature by using an exported public key. The application uses the standard Windows NCrypt APIs, with the provider-specific requirements described alongside each step.

The workflow is:

1. Open the provider and choose an algorithm.
2. Create the key, configure its properties, and finalize it.
3. Hash the data and sign the hash.
4. Export and import the public key.
5. Verify the signature.

RSA requires an explicit key length and signature-padding configuration. The remaining steps use the same API sequence for both algorithms. Where configuration differs, separate snippets are provided.

> [!NOTE]
> These snippets are parts of a larger sample, not standalone programs. They assume that the sample declares and initializes the referenced variables, constants, and `cleanup` label.
>
> The examples use SHA-256 and a 32-byte `hash` buffer. Initialize `keyLength` to `2048`, `keyUsage` to `NCRYPT_ALLOW_SIGNING_FLAG`, `pPaddingInfo` to `NULL`, and `dwPaddingFlag` to `0`. The cleanup path must release handles and allocated buffers.

#### Step 1: Open the provider

Call `NCryptOpenStorageProvider` with `MS_PLUTON_CRYPTO_PROVIDER`, which identifies `L"Microsoft Pluton Key Storage Provider"`.

```cpp
status = NCryptOpenStorageProvider(&hProvider, MS_PLUTON_CRYPTO_PROVIDER, 0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific behavior**

- On a device without Pluton, the call fails with `NTE_DEVICE_NOT_READY`.
- If the provider is disabled in the installed Windows build, the call fails with `E_NOTIMPL`.

#### Step 2: Choose the algorithm

Select the algorithm identifier and the corresponding public-key blob type.

##### ECDSA

```cpp
pszAlgId = NCRYPT_ECDSA_P256_ALGORITHM;
pszPublicBlobType = BCRYPT_ECCPUBLIC_BLOB;
```

##### RSA

```cpp
pszAlgId = NCRYPT_RSA_ALGORITHM;
pszPublicBlobType = BCRYPT_RSAPUBLIC_BLOB;
```

**Provider-specific requirements**

For ECDSA, use `NCRYPT_ECDSA_P256_ALGORITHM` or `NCRYPT_ECDSA_P384_ALGORITHM`. The provider doesn't support the curve-agnostic `NCRYPT_ECDSA_ALGORITHM` identifier; using it with `NCryptCreatePersistedKey` returns `NTE_NOT_SUPPORTED`.

The ECDSA snippets use P-256 with SHA-256. To use the recommended P-384/SHA-384 combination instead, update the curve identifier, hashing configuration, and hash buffer size together.

#### Step 3: Create the key

Call `NCryptCreatePersistedKey` to get a key handle. Pluton generates the key pair only after you finalize the key.

```cpp
status = NCryptCreatePersistedKey(
    hProvider,
    &hKey,
    pszAlgId,
    SAMPLE_KEY_NAME,
    0,
    NCRYPT_OVERWRITE_KEY_FLAG);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

| Parameter or argument | Description |
|---|---|
| `hProvider` | The provider handle from step 1. |
| `&hKey` | Receives the key handle. |
| `pszAlgId` | The algorithm identifier from step 2. |
| `SAMPLE_KEY_NAME` | The key name. A named key is saved after finalization and can be reopened by using `NCryptOpenKey`. |
| `0` | The value of `dwLegacyKeySpec`, which must be `0`. |
| `NCRYPT_OVERWRITE_KEY_FLAG` | Replaces an existing key with the same name. Without this flag, an existing key causes the call to return `NTE_EXISTS`. |

> [!CAUTION]
> This sample uses `NCRYPT_OVERWRITE_KEY_FLAG`. Use a sample-specific key name, and don't run it with the name of a key that you need to retain.

**Provider-specific requirements**

- `dwLegacyKeySpec` must be `0`. Other values return `NTE_NOT_SUPPORTED`.
- `dwFlags` can be `0` or a combination of `NCRYPT_MACHINE_KEY_FLAG`, `NCRYPT_OVERWRITE_KEY_FLAG`, and `NCRYPT_SILENT_FLAG`. Other flags return `NTE_BAD_FLAGS`.

#### Step 4: Set the key length (RSA only)

For RSA, set `NCRYPT_LENGTH_PROPERTY` to `2048`. Skip this step for ECDSA; the selected curve determines the key length.

```cpp
status = NCryptSetProperty(
    hKey,
    NCRYPT_LENGTH_PROPERTY,
    (PBYTE)&keyLength,
    sizeof(keyLength),
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- The provider supports only 2,048-bit RSA keys. `NCRYPT_LENGTHS_PROPERTY` reports `2048` as the minimum, maximum, and default key length.
- The provider creates 2,048-bit RSA keys by default. Setting the length explicitly avoids relying on that default when adapting the sample for another provider.

#### Step 5: Set the key usage

Set `NCRYPT_KEY_USAGE_PROPERTY` to `NCRYPT_ALLOW_SIGNING_FLAG`.

```cpp
status = NCryptSetProperty(
    hKey,
    NCRYPT_KEY_USAGE_PROPERTY,
    (PBYTE)&keyUsage,
    sizeof(keyUsage),
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- Keys have no default usage. If you don't set `NCRYPT_KEY_USAGE_PROPERTY`, `NCryptFinalizeKey` returns `NTE_INVALID_PARAMETER`.
- A usage value that's invalid for the algorithm returns `NTE_BAD_DATA`.
- For `NCryptSetProperty`, `dwFlags` can't include `NCRYPT_PERSIST_ONLY_FLAG`. The provider ignores `NCRYPT_PERSIST_FLAG`.
- **ECDSA:** Use `NCRYPT_ALLOW_SIGNING_FLAG`. Other values, such as `NCRYPT_ALLOW_DECRYPT_FLAG`, return `NTE_BAD_DATA`.
- **RSA:** Ordinary signing and decryption keys accept `NCRYPT_ALLOW_SIGNING_FLAG`, `NCRYPT_ALLOW_DECRYPT_FLAG`, or both. This signing-only example requires only `NCRYPT_ALLOW_SIGNING_FLAG`.

#### Step 6: Finalize the key

Call `NCryptFinalizeKey`. Pluton generates the key pair, and the provider saves the named key.

```cpp
status = NCryptFinalizeKey(hKey, 0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

// The key pair is generated in Pluton at this point.
```

**Provider-specific requirements**

- `dwFlags` can be `0` or `NCRYPT_SILENT_FLAG`. Other flags return `NTE_BAD_FLAGS`.
- After finalization, you can't change the key length and usage. Attempts to change them by using `NCryptSetProperty` return `NTE_NOT_SUPPORTED`.

#### Step 7: Hash the data

For both RSA and ECDSA, `NCryptSignHash` takes a precomputed hash, not the original message. This example uses `BCryptHash` with SHA-256.

The snippet assumes that `msg` points to a buffer containing the data to hash and sign, `cbMsg` is a `ULONG` containing the number of bytes of data in that buffer, and `hash` is a 32-byte array.

```cpp
// Hash cbMsg bytes from msg.
ntStatus = BCryptHash(
    BCRYPT_SHA256_ALG_HANDLE,
    NULL,
    0,
    (PUCHAR)msg,
    cbMsg,
    hash,
    sizeof(hash));

if (!NT_SUCCESS(ntStatus)) {
    status = HRESULT_FROM_NT(ntStatus);
    goto cleanup;
}
```

**Provider-specific requirements**

- **ECDSA:** The hash must be 32 or 48 bytes. Use SHA-256 with P-256 and SHA-384 with P-384 for the combinations illustrated by this guide.
- **RSA:** Use SHA-256, SHA-384, or SHA-512, producing a 32-, 48-, or 64-byte hash, respectively. The hash must match the algorithm specified in the padding information in step 8.

#### Step 8: Choose the padding (RSA only)

ECDSA doesn't use padding. Skip this step for ECDSA, and leave `pPaddingInfo` set to `NULL` and `dwPaddingFlag` set to `0`.

For RSA, choose PSS or PKCS #1 v1.5 padding according to the requirements of your protocol and verifier. Configure one of the following structures and its matching flag.

##### PSS padding

Use `BCRYPT_PSS_PADDING_INFO` with `NCRYPT_PAD_PSS_FLAG`.

```cpp
// PSS padding, with a salt the size of the hash.
pssInfo.pszAlgId = BCRYPT_SHA256_ALGORITHM;
pssInfo.cbSalt = SHA256_HASH_SIZE;

pPaddingInfo = &pssInfo;
dwPaddingFlag = NCRYPT_PAD_PSS_FLAG;
```

##### PKCS #1 v1.5 padding

Use `BCRYPT_PKCS1_PADDING_INFO` with `NCRYPT_PAD_PKCS1_FLAG`.

```cpp
// PKCS #1 v1.5 padding.
pkcs1Info.pszAlgId = BCRYPT_SHA256_ALGORITHM;

pPaddingInfo = &pkcs1Info;
dwPaddingFlag = NCRYPT_PAD_PKCS1_FLAG;
```

**Provider-specific requirements**

- `pszAlgId` must be `BCRYPT_SHA256_ALGORITHM`, `BCRYPT_SHA384_ALGORITHM`, or `BCRYPT_SHA512_ALGORITHM`, and must identify the hash algorithm used in step 7. Use these constants; the provider compares algorithm names exactly, including case.
- `pszAlgId` can't be `NULL`. The provider doesn't support PKCS #1 v1.5 signatures without a hash algorithm identifier. A `NULL` value returns `NTE_INVALID_PARAMETER`. Unsupported hash algorithms, such as SHA-1, return `NTE_NOT_SUPPORTED`.
- For PSS, set `cbSalt` to the hash size: 32 bytes for the SHA-256 example.

#### Step 9: Sign the hash

Call `NCryptSignHash` twice: once to determine the signature buffer size, and once to generate the signature.

##### Query the signature size and allocate a buffer

```cpp
// Get the signature size. The PKSP requires the padding and the
// hash in this call too.
status = NCryptSignHash(
    hKey,
    pPaddingInfo,
    hash,
    sizeof(hash),
    NULL,
    0,
    &cbSignature,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

pbSignature = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbSignature);

if (pbSignature == NULL) {
    status = NTE_NO_MEMORY;
    goto cleanup;
}
```

##### Generate the signature

Pluton computes the signature by using the private key.

```cpp
status = NCryptSignHash(
    hKey,
    pPaddingInfo,
    hash,
    sizeof(hash),
    pbSignature,
    cbSignature,
    &cbSignature,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

| Parameter or argument | Description |
|---|---|
| `pPaddingInfo`, `dwPaddingFlag` | The padding configuration from step 8. For ECDSA, use `NULL` and `0`. |
| `hash`, `sizeof(hash)` | The hash and its size in bytes from step 7. |
| `pbSignature`, `cbSignature` | The signature buffer and its capacity. On return, `cbSignature` contains the number of bytes written. |

**Provider-specific requirements**

- Supply the hash and the applicable padding configuration in the size-query call as well as the signing call. The provider validates them before returning the required size. Invalid parameter values can return `NTE_INVALID_PARAMETER`.
- An undersized signature buffer returns `NTE_BUFFER_TOO_SMALL`.
- **ECDSA:** `pPaddingInfo` must be `NULL`, and `dwFlags` must be `0`. Specifying `NCRYPT_SILENT_FLAG` returns `NTE_INVALID_PARAMETER`. The provider doesn't display UI, so the flag is unnecessary.
- **RSA:** Select exactly one padding scheme: `NCRYPT_PAD_PSS_FLAG` or `NCRYPT_PAD_PKCS1_FLAG`. Supply the corresponding structure in `pPaddingInfo`. Omitting the padding flag, specifying both padding flags, or passing `NULL` for `pPaddingInfo` returns `NTE_INVALID_PARAMETER`.
- **RSA:** `cbHashValue` must match the hash size identified by `pszAlgId`. A mismatch returns `NTE_INVALID_PARAMETER`.

##### Signature format

| Algorithm | Format |
|---|---|
| ECDSA | The big-endian value `r` followed by the big-endian value `s`, each padded to the curve's coordinate size. The total is 64 bytes for P-256 or 96 bytes for P-384. This isn't a DER-encoded ASN.1 signature. Convert it if the receiving API requires DER encoding. |
| RSA | A signature the size of the modulus: 256 bytes for a 2,048-bit key. |

#### Step 10: Export the public key

Call `NCryptExportKey` twice, using the public-key blob type you selected in step 2: once to determine the buffer size, and once to export the public key.

```cpp
// Get the public key blob size.
status = NCryptExportKey(hKey, 0, pszPublicBlobType, NULL, NULL, 0, &cbPublicKeyBlob, 0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

pbPublicKeyBlob = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPublicKeyBlob);

if (pbPublicKeyBlob == NULL) {
    status = NTE_NO_MEMORY;
    goto cleanup;
}

// Export the public key.
status = NCryptExportKey(
    hKey,
    0,
    pszPublicBlobType,
    NULL,
    pbPublicKeyBlob,
    cbPublicKeyBlob,
    &cbPublicKeyBlob,
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

The exported blob format depends on the algorithm:

- **ECDSA:** A `BCRYPT_ECCKEY_BLOB` structure followed by the X and Y coordinates. For P-256, `dwMagic` is `BCRYPT_ECDSA_PUBLIC_P256_MAGIC`, `cbKey` is `32`, and the blob is 72 bytes. For P-384, the corresponding values are `BCRYPT_ECDSA_PUBLIC_P384_MAGIC`, `48`, and 104 bytes.
- **RSA:** A `BCRYPT_RSAKEY_BLOB` structure followed by the public exponent and modulus. `Magic` is `BCRYPT_RSAPUBLIC_MAGIC`, and `BitLength` is `2048`.

**Provider-specific requirements**

- You can export only public keys. Supported formats are `BCRYPT_ECCPUBLIC_BLOB`, `BCRYPT_RSAPUBLIC_BLOB`, `BCRYPT_PUBLIC_KEY_BLOB`, and `BCRYPT_OPAQUE_KEY_BLOB`. The opaque format contains the public key in TPM 2.0 key blob format. Private-key blob types, such as `BCRYPT_ECCPRIVATE_BLOB` and `BCRYPT_RSAPRIVATE_BLOB`, return `NTE_BAD_TYPE`.
- `hExportKey` must be `0`, and `pParameterList` must be `NULL`. Other values return `NTE_NOT_SUPPORTED`.
- `dwFlags` can be `0` or `NCRYPT_SILENT_FLAG`.

#### Step 11: Import the public key

Call `NCryptImportKey` with the exported blob. The resulting handle contains only the public key. It can verify signatures, but can't sign.

```cpp
status = NCryptImportKey(
    hProvider,
    0,
    pszPublicBlobType,
    NULL,
    &hPublicKey,
    pbPublicKeyBlob,
    cbPublicKeyBlob,
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

| Parameter or argument | Description |
|---|---|
| `0` for `hImportKey` | No wrapping key is needed because the public-key blob isn't encrypted. |
| `pszPublicBlobType` | The public-key blob type you selected in step 2. |
| `NULL` for `pParameterList` | No key name is supplied. The imported public key isn't saved and exists only until its handle is released. |
| `0` for `dwFlags` | No import flags are required for this example. |

**Provider-specific requirements**

- `dwFlags` can be `0` or a combination of `NCRYPT_NO_KEY_VALIDATION` and `NCRYPT_IGNORE_DEVICE_STATE_FLAG`.
- The provider finalizes the imported key immediately.
- **ECDSA:** The blob's `dwMagic` must be `BCRYPT_ECDSA_PUBLIC_P256_MAGIC` or `BCRYPT_ECDSA_PUBLIC_P384_MAGIC`, as exported in step 10. Other ECC blob variants, such as generic ECDSA or ECDH blobs, return `NTE_NOT_SUPPORTED`.
- **RSA:** The blob's `Magic` must be `BCRYPT_RSAPUBLIC_MAGIC`, and `BitLength` must be `2048`. Other RSA blob variants return `NTE_NOT_SUPPORTED`.

> [!IMPORTANT]
> In an application that receives a public key from another party, establish that the key belongs to the expected signer. Importing the key doesn't establish trust in its owner.

#### Step 12: Verify the signature

Call `NCryptVerifySignature` by using the imported public key and the same hash and padding configuration used for signing.

```cpp
status = NCryptVerifySignature(
    hPublicKey,
    pPaddingInfo,
    hash,
    sizeof(hash),
    pbSignature,
    cbSignature,
    dwPaddingFlag);

// S_OK means that the signature is valid. NTE_BAD_SIGNATURE means
// that the hash, the signature, or the padding changed, or that another key
// signed it.
```

`S_OK` means the signature was verified against the supplied public key, hash, and padding configuration. `NTE_BAD_SIGNATURE` means verification failed, without identifying which input is incorrect. Treat other returned error codes as errors, not as successful verification.

**Provider-specific requirements**

- Don't add `NCRYPT_SILENT_FLAG`. For ECDSA, it returns `NTE_INVALID_PARAMETER`. For RSA, the provider passes the flags to `BCrypt` for verification, where this flag isn't accepted.
- **ECDSA:** `pPaddingInfo` must be `NULL`, and `dwFlags` must be `0`. Other values return `NTE_INVALID_PARAMETER`.
- **RSA:** Select exactly one of `NCRYPT_PAD_PSS_FLAG` and `NCRYPT_PAD_PKCS1_FLAG`, and provide non-`NULL` padding information. Omitting the padding flag, specifying both padding flags, or omitting the padding information returns `NTE_INVALID_PARAMETER`.
- **RSA:** Use the same padding scheme, hash algorithm, and, for PSS, salt length used for signing. A mismatch causes verification to fail.

#### Clean up resources

The snippets branch to a shared `cleanup` label. Implement this label in the surrounding sample to:

- Release `hPublicKey`, `hKey`, and `hProvider` by using `NCryptFreeObject` when their handles are valid.
- Release `pbSignature` with `HeapFree(GetProcessHeap(), 0, pbSignature)` and `pbPublicKeyBlob` with `HeapFree(GetProcessHeap(), 0, pbPublicKeyBlob)` when the pointers aren't `NULL`, matching their allocation with `HeapAlloc`.
- Note that releasing `hKey` doesn't delete the named key. If the key is no longer needed, delete it by using `NCryptDeleteKey` before releasing the provider. Don't call `NCryptFreeObject` on a key handle that you successfully deleted.

### Encrypt and decrypt with RSA or AES

This example shows how an application creates an RSA or AES key with the **Microsoft Pluton Key Storage Provider**, encrypts data, and decrypts the result.

The workflow is:

1. Open the provider and choose an algorithm.
2. Create the key and set its length and usage.
3. For AES, configure the chaining mode.
4. Finalize the key and configure padding.
5. Encrypt and decrypt the data.

The example uses RSA with OAEP padding. The AES example uses CBC mode with an initialization vector (IV) and PKCS #7 padding. Both algorithms use the same encryption and decryption APIs, with different configuration.

RSA with OAEP suits small inputs, such as a cryptographic key. AES supports larger inputs; with PKCS #7 padding, the plaintext doesn't need to be a multiple of the AES block size.

> [!NOTE]
> These snippets are parts of a larger sample, not standalone programs. They assume that the sample declares and initializes the referenced variables, constants, and `cleanup` label.
>
> Set `RSA_KEY_LENGTH` to `2048` and `AES_KEY_LENGTH` to `128` or `256`. Initialize `keyUsage` to `NCRYPT_ALLOW_DECRYPT_FLAG`, zero-initialize the padding structures, and declare `iv` as a 16-byte array. The cleanup path must release handles and allocated buffers.

> [!IMPORTANT]
> This example demonstrates encryption and decryption, not a complete authenticated-encryption protocol. CBC encryption and successful padding validation don't establish message authenticity. For production scenarios, use a reviewed protocol that authenticates the ciphertext and IV before CBC decryption. See [Timing vulnerabilities with CBC-mode symmetric decryption using padding](/dotnet/standard/security/vulnerabilities-cbc-mode).

#### Step 1: Open the provider

Call `NCryptOpenStorageProvider` with `MS_PLUTON_CRYPTO_PROVIDER`, which identifies `L"Microsoft Pluton Key Storage Provider"`.

```cpp
status = NCryptOpenStorageProvider(&hProvider, MS_PLUTON_CRYPTO_PROVIDER, 0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific behavior**

- On a device without Pluton, the call fails with `NTE_DEVICE_NOT_READY`.
- If the provider is disabled in the installed Windows build, the call fails with `E_NOTIMPL`.

#### Step 2: Choose the algorithm

Select the algorithm identifier and key length.

##### RSA

```cpp
pszAlgId = NCRYPT_RSA_ALGORITHM;
keyLength = RSA_KEY_LENGTH;
```

##### AES

```cpp
pszAlgId = NCRYPT_AES_ALGORITHM;
keyLength = AES_KEY_LENGTH;
```

#### Step 3: Create the key

Call `NCryptCreatePersistedKey` to get a key handle. Pluton doesn't generate the key until you finalize it.

```cpp
status = NCryptCreatePersistedKey(
    hProvider,
    &hKey,
    pszAlgId,
    SAMPLE_KEY_NAME,
    0,
    NCRYPT_OVERWRITE_KEY_FLAG);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

| Parameter or argument | Description |
|---|---|
| `hProvider` | The provider handle from step 1. |
| `&hKey` | Receives the key handle. |
| `pszAlgId` | The algorithm identifier from step 2. |
| `SAMPLE_KEY_NAME` | The key name. A named key is saved after finalization and can be reopened with `NCryptOpenKey`. |
| `0` | The value of `dwLegacyKeySpec`, which must be `0`. |
| `NCRYPT_OVERWRITE_KEY_FLAG` | Replaces an existing key with the same name. Without this flag, an existing key causes the call to return `NTE_EXISTS`. |

> [!CAUTION]
> This sample uses `NCRYPT_OVERWRITE_KEY_FLAG`. Use a sample-specific key name, and don't run it with the name of a key that you need to retain. Use different sample key names when retaining both RSA and AES keys.

**Provider-specific requirements**

- `dwLegacyKeySpec` must be `0`. Other values return `NTE_NOT_SUPPORTED`.
- `dwFlags` can be `0` or a combination of `NCRYPT_MACHINE_KEY_FLAG`, `NCRYPT_OVERWRITE_KEY_FLAG`, and `NCRYPT_SILENT_FLAG`. Other flags return `NTE_BAD_FLAGS`.

#### Step 4: Set the key length

Set `NCRYPT_LENGTH_PROPERTY` to the key length you selected in step 2.

```cpp
status = NCryptSetProperty(
    hKey,
    NCRYPT_LENGTH_PROPERTY,
    (PBYTE)&keyLength,
    sizeof(keyLength),
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- **RSA:** Only 2,048-bit keys are supported. This key length is also the default.
- **AES:** Only 128-bit and 256-bit keys are supported. The default length is 128 bits. Other lengths, such as 192 bits, return `NTE_NOT_SUPPORTED`.

#### Step 5: Set the key usage

Set `NCRYPT_KEY_USAGE_PROPERTY` to `NCRYPT_ALLOW_DECRYPT_FLAG`. For these keys, this usage permits both encryption and decryption.

```cpp
status = NCryptSetProperty(
    hKey,
    NCRYPT_KEY_USAGE_PROPERTY,
    (PBYTE)&keyUsage,
    sizeof(keyUsage),
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- Keys have no default usage. If you don't set `NCRYPT_KEY_USAGE_PROPERTY`, `NCryptFinalizeKey` returns `NTE_INVALID_PARAMETER`.
- A usage value that is invalid for the algorithm returns `NTE_BAD_DATA`.
- For `NCryptSetProperty`, `dwFlags` can't include `NCRYPT_PERSIST_ONLY_FLAG`. The provider ignores `NCRYPT_PERSIST_FLAG`.
- **RSA:** Ordinary signing and decryption keys accept `NCRYPT_ALLOW_DECRYPT_FLAG`, `NCRYPT_ALLOW_SIGNING_FLAG`, or both. This example requires decryption usage; signing-only usage is insufficient.
- **AES:** Use `NCRYPT_ALLOW_DECRYPT_FLAG` for encryption and decryption.

#### Step 6: Set the chaining mode (AES only)

For AES, set `BCRYPT_CHAINING_MODE` to `BCRYPT_CHAIN_MODE_CBC`. For RSA, skip this step.

```cpp
status = NCryptSetProperty(
    hKey,
    BCRYPT_CHAINING_MODE,
    (PBYTE)BCRYPT_CHAIN_MODE_CBC,
    sizeof(BCRYPT_CHAIN_MODE_CBC),
    0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- Use the property name `BCRYPT_CHAINING_MODE` (`L"ChainingMode"`), not `NCRYPT_CHAINING_MODE_PROPERTY` (`L"Chaining Mode"`).
- The provider supports `BCRYPT_CHAIN_MODE_CBC`, which is the default, and `BCRYPT_CHAIN_MODE_ECB`.
- Other modes, such as `BCRYPT_CHAIN_MODE_GCM`, `BCRYPT_CHAIN_MODE_CCM`, and `BCRYPT_CHAIN_MODE_CFB`, return `NTE_BAD_DATA`.
- Set the chaining mode before finalization. You can't change it afterward.

#### Step 7: Finalize the key

Call `NCryptFinalizeKey`. Pluton generates the key, and the provider saves the named key.

```cpp
status = NCryptFinalizeKey(hKey, 0);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

// The key is generated in Pluton at this point.
```

**Provider-specific requirements**

- `dwFlags` can be `0` or `NCRYPT_SILENT_FLAG`. Other flags return `NTE_BAD_FLAGS`.
- After finalization, you can't change the key length, usage, and chaining mode. Attempts to change them with `NCryptSetProperty` return `NTE_NOT_SUPPORTED`.

#### Step 8: Configure padding

Configure the padding information and matching flag for the selected algorithm.

##### RSA

Use `BCRYPT_OAEP_PADDING_INFO` with `NCRYPT_PAD_OAEP_FLAG`. This example uses SHA-256 without a label.

```cpp
// OAEP padding with SHA-256 and no label.
oaepInfo.pszAlgId = BCRYPT_SHA256_ALGORITHM;
oaepInfo.pbLabel = NULL;
oaepInfo.cbLabel = 0;

pPaddingInfo = &oaepInfo;
dwPaddingFlag = NCRYPT_PAD_OAEP_FLAG;
```

##### AES

Use `NCRYPT_CIPHER_PADDING_INFO`, defined in `ncrypt.h`, with `NCRYPT_PAD_CIPHER_FLAG`. For CBC, generate a fresh random IV by using `BCryptGenRandom`.

Although the general `NCryptEncrypt` reference describes padding information for asymmetric keys, the Pluton provider also requires a cipher-padding structure for AES operations.

```cpp
// A new random IV for each message.
ntStatus = BCryptGenRandom(
    NULL,
    iv,
    sizeof(iv),
    BCRYPT_USE_SYSTEM_PREFERRED_RNG);

if (!NT_SUCCESS(ntStatus)) {
    status = HRESULT_FROM_NT(ntStatus);
    goto cleanup;
}

// PKCS #7 padding, so that the data can be any size.
cipherInfo.cbSize = sizeof(cipherInfo);
cipherInfo.dwFlags = NCRYPT_CIPHER_BLOCK_PADDING_FLAG;
cipherInfo.pbIV = iv;
cipherInfo.cbIV = sizeof(iv);

pPaddingInfo = &cipherInfo;
dwPaddingFlag = NCRYPT_PAD_CIPHER_FLAG;
```

**Provider-specific requirements**

- **RSA:** OAEP is the only supported encryption padding scheme. PKCS #1 v1.5 encryption padding and unpadded encryption return `NTE_INVALID_PARAMETER`.
- **RSA:** `pszAlgId` must be `BCRYPT_SHA256_ALGORITHM`, `BCRYPT_SHA384_ALGORITHM`, or `BCRYPT_SHA512_ALGORITHM`. Use these constants; the provider compares algorithm names exactly, including case.
- **RSA:** The OAEP label is optional. If supplied, use the same label for decryption. Use the same OAEP hash algorithm for encryption and decryption.
- **AES:** Set `cbSize` to `sizeof(NCRYPT_CIPHER_PADDING_INFO)`. A smaller value returns `NTE_INVALID_PARAMETER`.
- **AES:** `NCRYPT_CIPHER_BLOCK_PADDING_FLAG` enables PKCS #7 padding. Without it, the input length must be a multiple of 16 bytes; otherwise, the call returns `NTE_INVALID_PARAMETER`.
- **AES:** CBC requires a 16-byte IV. ECB takes no IV: set `pbIV` to `NULL` and `cbIV` to `0`. An invalid IV configuration returns `NTE_INVALID_PARAMETER`.
- **AES:** The IV isn't secret. Retain it with the ciphertext because decryption requires the original IV. Generate a fresh random IV for each CBC message encrypted with the same key.

#### Step 9: Encrypt the data

Call `NCryptEncrypt` twice: once to determine the ciphertext buffer size, and once to encrypt the data.

The snippets assume that `msg` points to a buffer containing the data to encrypt and `cbMsg` is a `ULONG` containing the number of bytes of data in that buffer. Use the same buffer and byte count in both calls.

##### Query the ciphertext size and allocate a buffer

```cpp
// Get the ciphertext size for cbMsg bytes from msg.
status = NCryptEncrypt(
    hKey,
    (PBYTE)msg,
    cbMsg,
    pPaddingInfo,
    NULL,
    0,
    &cbCiphertext,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

pbCiphertext = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbCiphertext);

if (pbCiphertext == NULL) {
    status = NTE_NO_MEMORY;
    goto cleanup;
}
```

##### Encrypt the data

```cpp
status = NCryptEncrypt(
    hKey,
    (PBYTE)msg,
    cbMsg,
    pPaddingInfo,
    pbCiphertext,
    cbCiphertext,
    &cbCiphertext,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}
```

**Provider-specific requirements**

- An undersized output buffer returns `NTE_BUFFER_TOO_SMALL`.
- **RSA:** `dwFlags` must be exactly `NCRYPT_PAD_OAEP_FLAG`. Adding `NCRYPT_SILENT_FLAG` returns `NTE_INVALID_PARAMETER`. The provider doesn't display UI, so the flag is unnecessary.
- **RSA:** The maximum OAEP plaintext length, in bytes, is the modulus length minus twice the hash length, minus 2. For RSA-2048 with SHA-256, the maximum is `256 - (2 * 32) - 2 = 190` bytes. Larger inputs fail.
- **AES:** `dwFlags` must include `NCRYPT_PAD_CIPHER_FLAG`; otherwise, the call returns `NTE_BAD_FLAGS`. A `NULL` `pPaddingInfo` returns `NTE_INVALID_PARAMETER`.

The ciphertext size depends on the algorithm:

| Algorithm | Ciphertext size |
|---|---|
| RSA-2048 | 256 bytes, matching the modulus length. |
| AES with PKCS #7 padding | The plaintext length plus 1 to 16 padding bytes, producing a multiple of 16 bytes. For example, 16 plaintext bytes produce 32 ciphertext bytes, and 51 plaintext bytes produce 64 ciphertext bytes. |

#### Step 10: Decrypt the data

Call `NCryptDecrypt` twice: once to determine the output buffer size, and once to decrypt. Use the same padding configuration used for encryption, and, for CBC, the original IV.

##### Query the buffer size and allocate a buffer

```cpp
// Get the buffer size. It's the ciphertext size, which is enough for the
// plaintext.
status = NCryptDecrypt(
    hKey,
    pbCiphertext,
    cbCiphertext,
    pPaddingInfo,
    NULL,
    0,
    &cbPlaintext,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

pbPlaintext = (PBYTE)HeapAlloc(GetProcessHeap(), 0, cbPlaintext);

if (pbPlaintext == NULL) {
    status = NTE_NO_MEMORY;
    goto cleanup;
}
```

##### Decrypt the data

```cpp
status = NCryptDecrypt(
    hKey,
    pbCiphertext,
    cbCiphertext,
    pPaddingInfo,
    pbPlaintext,
    cbPlaintext,
    &cbPlaintext,
    dwPaddingFlag);

if (status != ERROR_SUCCESS) {
    goto cleanup;
}

// cbPlaintext is now the size of the decrypted data.
```

Use `cbPlaintext` as the length of the recovered data. The decrypted buffer isn't automatically null-terminated.

**Provider-specific requirements**

- The provider's size query returns the ciphertext size as sufficient output capacity, not the final plaintext length. After successful decryption, `pcbResult` reports the number of plaintext bytes written.
- **RSA:** The ciphertext must be 256 bytes. Other lengths return `NTE_INVALID_PARAMETER`.
- **RSA:** `dwFlags` must be exactly `NCRYPT_PAD_OAEP_FLAG`, as for encryption.
- **AES:** Use the original IV from encryption. The Pluton provider doesn't modify the IV buffer, so this example reuses the same `NCRYPT_CIPHER_PADDING_INFO` structure. Don't assume that other providers preserve the IV; keep an original copy when writing cross-provider code.
- **AES:** With PKCS #7 padding, invalid padding after decryption returns `NTE_INVALID_PARAMETER`. Possible causes include the wrong key or modified ciphertext. Valid padding doesn't prove that the ciphertext is authentic.

#### Clean up resources

The snippets branch to a shared `cleanup` label, which you must implement in the surrounding sample:

- Release `hKey` and `hProvider` with `NCryptFreeObject` when their handles are valid.
- Release `pbCiphertext` with `HeapFree(GetProcessHeap(), 0, pbCiphertext)` and `pbPlaintext` with `HeapFree(GetProcessHeap(), 0, pbPlaintext)` when the pointers aren't `NULL`, matching their allocation with `HeapAlloc`.
- Releasing `hKey` doesn't delete the named key. If you no longer need the key, delete it with `NCryptDeleteKey` before releasing the provider. Don't call `NCryptFreeObject` on a key handle that you successfully deleted.

### Clean up resources

Each workflow must release the handles and buffers it opens or allocates, and delete saved keys only when they're no longer needed. This section gives shared cleanup guidance for the **Microsoft Pluton Key Storage Provider** examples.

Releasing a key handle and deleting a saved key are different operations. Use `NCryptFreeObject` to release a handle while retaining the saved key. Use `NCryptDeleteKey` when the saved key should also be deleted.

| Resource or action | Obtained from | Cleanup function | Notes |
|---|---|---|---|
| Release a key handle and retain the saved key | `NCryptCreatePersistedKey`, `NCryptOpenKey` | `NCryptFreeObject` | The saved key isn't deleted. |
| Delete a saved key and release its handle | `NCryptCreatePersistedKey`, `NCryptOpenKey` | `NCryptDeleteKey` | Deletes the saved key and releases the handle. |
| Release an unnamed key or a public key imported without a name | `NCryptCreatePersistedKey` without a name, `NCryptImportKey` without a name | `NCryptFreeObject` | These examples don't save the key, so no saved key needs to be deleted. |
| Release a provider handle | `NCryptOpenStorageProvider` | `NCryptFreeObject` | Release the key handles before the provider handle. |
| Release a provider-allocated list | `NCryptEnumStorageProviders`, `NCryptEnumAlgorithms` | `NCryptFreeBuffer` | Free any returned allocation, even if the reported item count is zero. Don't pass an invalid or `NULL` pointer. |
| Release an application-allocated buffer | `HeapAlloc(GetProcessHeap(), 0, size)` | `HeapFree(GetProcessHeap(), 0, buffer)` | Free only non-`NULL` pointers. Before releasing sensitive data, such as decrypted plaintext, clear it with `SecureZeroMemory`. |

#### Release or delete a key

The following helper releases a key handle. If `deleteKey` is `TRUE`, it also tries to delete the saved key. It then sets the caller's handle to `0` to prevent accidental reuse.

Pass a non-`NULL` pointer to a handle that's either valid and owned by the caller or already `0`.

> [!IMPORTANT]
> The helper's deletion-failure handling is specific to the Pluton provider behavior described in the following section. Don't assume that it applies to other key storage providers. A cleared handle doesn't indicate that deletion succeeded; check the returned `SECURITY_STATUS`.

```cpp
//
// Releases a key handle and sets it to 0. If deleteKey is TRUE, the
// function also deletes the saved key.
//
SECURITY_STATUS ReleaseKey(NCRYPT_KEY_HANDLE* phKey, BOOL deleteKey)
{
    SECURITY_STATUS status = ERROR_SUCCESS;

    if (*phKey == 0) {
        return ERROR_SUCCESS;
    }

    if (deleteKey) {
        // NCryptDeleteKey frees the handle. With the Pluton provider, don't call
        // NCryptFreeObject afterward, even if NCryptDeleteKey fails.
        status = NCryptDeleteKey(*phKey, 0);
    } else {
        status = NCryptFreeObject(*phKey);
    }

    *phKey = 0;
    return status;
}
```

#### Use a shared cleanup path

Release key handles before the provider handle. Release provider-allocated lists with `NCryptFreeBuffer` and application-allocated buffers with the function that matches their allocation.

The following snippet assumes that the surrounding sample initializes handles to `0` and pointers to `NULL` before any operation can branch to `cleanup`.

```cpp
cleanup:

// This example deletes its key if it's still open, for example after an
// error. Pass FALSE to keep a saved key.
ReleaseKey(&hKey, TRUE);

if (hProvider != 0) {
    NCryptFreeObject(hProvider);
}

// Lists that NCrypt allocated.
if (pProviders != NULL) {
    NCryptFreeBuffer(pProviders);
}

if (pAlgorithms != NULL) {
    NCryptFreeBuffer(pAlgorithms);
}
```

Adapt this path to include every resource used by the workflow:

- Release any additional key handles, such as `hPublicKey`, before releasing `hProvider`.
- Clear sensitive application buffers with `SecureZeroMemory`, using the actual allocated buffer size.
- Release application buffers allocated with `HeapAlloc(GetProcessHeap(), 0, size)`, such as signature, key-blob, ciphertext, and plaintext buffers, with `HeapFree(GetProcessHeap(), 0, buffer)` when the pointers aren't `NULL`.

The snippet omits cleanup return-value handling for brevity. Production code should check or record cleanup failures without losing the original operation's error. In particular, don't assume that a saved key was deleted if `ReleaseKey` returned an error.

> [!CAUTION]
> `ReleaseKey(&hKey, TRUE)` requests deletion, including on an error path. Use this only for keys that the application is authorized to delete. Pass `FALSE` when the saved key must be retained.

#### Provider-specific requirements

- For the Pluton provider, `NCryptDeleteKey` requires `dwFlags = 0`. Unsupported flags return `NTE_BAD_FLAGS`.
- Successful deletion removes the saved key and releases its handle. Don't subsequently call `NCryptFreeObject` on that handle.
- The general `NCryptDeleteKey` reference permits applications to call `NCryptFreeObject` after deletion fails. For the Pluton-specific failure path covered by this helper, the provider releases the key handle even if deleting the saved key fails. Don't free that released handle again.
- This failure-path guidance assumes a valid key handle and supported flags. It's not a guarantee about handle lifetime after validation errors, such as an invalid handle or unsupported flags.
- For the unnamed and unsaved imported keys used in these examples, `NCryptFreeObject` is sufficient. There's no saved key to delete.

## Additional preview notes
The final version of this feature might only support creating and using machine key containers. Don't depend on user key containers. If your scenarios require user key containers, share your feedback through the Feedback Hub as described in the following section.

The provider identifier `MS_PLUTON_CRYPTO_PROVIDER`, defined in `ncrypt.h`, and its associated provider-name string may change before general availability to align with other CNG key storage providers. Applications using this preview may need to be prepared to update the identifier or provider-name string when adopting the released version.

## Got feedback?

We'd like to hear from you! Share your scenarios for the Pluton KSP, especially scenarios where you already use the Software or Platform KSPs, and any problems you encounter.

To send feedback to the feature team, use Feedback Hub and select the **Pluton** category. [Or click this link to open Feedback Hub with the Pluton category pre-populated](feedback-hub:?contextid=1365&tabid=2&newFeedback=true).

- Select **Make a suggestion** to tell us about scenarios you want to use with the Pluton KSP.
- Select **Report a problem** to tell us about bugs or other issues.
- Select **Give a compliment** to tell us what’s working well.

## Related Content

- [Microsoft Pluton security processor](/windows/security/hardware-security/pluton/microsoft-pluton-security-processor)
- [Understanding the Microsoft Pluton security processor](https://techcommunity.microsoft.com/blog/windows-itpro-blog/understanding-the-microsoft-pluton-security-processor/4370413)



