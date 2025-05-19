---
title: BCryptEncapsulate function
description: The BCryptEncapsulate function encapsulates a key for the ML-KEM algorithm.
ms.topic: reference
ms.date: 05/13/2025
req.lib: Bcrypt.lib
req.dll: Bcrypt.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Bcrypt.dll
api_name:
- BCryptEncapsulate
targetos: Windows
---

# BCryptEncapsulate function

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **BCryptEncapsulate** function generates a shared secret key and encrypts it with the provided public key. 

**BCryptEncapsulate** accepts an encapsulation or decapsulation key. The encapsulation key must be opened using [BCryptImportKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptimportkey) providing the byte encoded encapsulation key and blob type [BCRYPT_MLKEM_PUBLIC_KEY_BLOB](ns-bcrypt-bcrypt_mlkem_key_blob.md). Additionally, usage of a decapsulation key is also supported and the criteria for the decapsulation key shall be the same as is required for ML-KEM Decapsulate. The cipher text will be returned in *pbCipherText* and the derived shared secret key will be returned in *pbSecretKey*. Each call to **BCryptEncapsulate** will perform a single encapsulate operation which entails the generation of a secret key and the ciphertext encapsulation of that secret key. Repeated calls to **BCryptEncapsulate** will generate additional secret keys and their corresponding encapsulations. 

## Syntax

```cpp
NTSTATUS BCryptEncapsulate(
  _In_ BCRYPT_KEY_HANDLE hKey,
  _Out_writes_bytes_to_opt_(cbSecretKey ,*pcbSecretKey) PUCHAR pbSecretKey,
  _In_ ULONG cbSecretKey,
  _Out_ ULONG *pcbSecretKey,
  _Out_writes_bytes_to_opt_(cbCipherText ,*pcbCipherText) PUCHAR pbCipherText,
  _In_ ULONG cbCipherText,
  _Out_ ULONG *pcbCipherText,
  _In_ ULONG dwFlags
);
```

## Parameters

*hKey* `[in]`

Provides a key handle for the ML-KEM encapsulation key.

*pbSecretKey* `[out]`

A pointer to a caller allocated buffer receiving the generated shared secret key.

*cbSecretKey* `[in]`

The size, in bytes, of the buffer *pbSecretKey*.

*pcbSecretKey* `[out]`

If *pcbSecretKey* is `NULL`, it receives the number of bytes required for *pbSecretKey*. Otherwise, it returns the number of bytes written to *pbSecretKey*. See [remarks](#remarks) for more information.

*pbCipherText* `[out]`

A pointer to the caller allocated buffer receiving the ML-KEM ciphertext.

*cbCipherText* `[in]`

The size, in bytes, of *pbCipherText*. See [remarks](#remarks) for more information.

*pcbCipherText* `[out]`

If *pcbCipherText* is `NULL`, it receives the number of bytes required for *pbCipherText*. Otherwise, it returns the number of bytes written to *pbCipherText*. See [remarks](#remarks) for more information.

*dwFlags* `[in]`

Reserved, must be zero. ML-KEM currently has no flags. 

## Return value

If the function succeeds, it returns `STATUS_SUCCESS`. Otherwise, it returns an **NTSTATUS** error code. Possible error codes include:

| Status Code | Description |
|--|--|
| `STATUS_INVALID_PARAMETER` | One or more required parameters (*hKey*, *pbSecretKey*, *pbCipherText*) are missing. |
| `STATUS_BUFFER_TOO_SMALL` | One of the buffers, *pcbSecretKey* or *pcbCipherText*, are too small. If the *pbSecretKey* buffer is too small, *pcbSecretKey receives the number of bytes required for *pbSecretKey*. If buffer *pbCipherText* is too small, *pcbCipherText* receives the number of bytes required for *pbCipherText*. |

## Remarks

The required buffer length for *pbSecretKey*, *pbCipherText* are static values which depend only on the parameter set in use. The sizes for each parameter set are documented in ML-KEM Key and Ciphertext Sizes. Callers can also use [BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty) to query the BCRYPT_KEM_SHARED_SHARED_SECRET_LENGTH, BCRYPT_KEM_CIPHERTEXT_LENGTH properties on the algorithm handle. 

Alternatively, callers can query the required size of the *pbSecretKey*, *pbCipherText* buffer needed for the ML-KEM ciphertext, by calling **BCryptEncapsulate** with `NULL` values in *pbSecretKey* and *pbCipherText*. The required size will be returned in *pcbSecretKey* and *pcbCipherText*, respectively. This query is efficient and returns the size without performing the encapsulation.
