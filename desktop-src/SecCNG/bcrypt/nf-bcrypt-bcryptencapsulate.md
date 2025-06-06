---
title: BCryptEncapsulate function
description: The BCryptEncapsulate function performs the Encapsulation operation of a KEM algorithm.
ms.topic: reference
ms.date: 05/27/2025
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

The **BCryptEncapsulate** function performs the Encapsulation operation of a Key Encapsulation Mechanism (KEM).
It generates a shared secret key and encrypts it with the provided public key to produce a KEM ciphertext, returning both the shared secret key and the KEM ciphertext.

## Syntax

```cpp
NTSTATUS BCryptEncapsulate(
  _In_  BCRYPT_KEY_HANDLE hKey,
  _Out_writes_bytes_to_opt_(cbSecretKey ,*pcbSecretKey)
        PUCHAR            pbSecretKey,
  _In_  ULONG             cbSecretKey,
  _Out_ ULONG             *pcbSecretKey,
  _Out_writes_bytes_to_opt_(cbCipherText ,*pcbCipherText)
        PUCHAR            pbCipherText,
  _In_  ULONG             cbCipherText,
  _Out_ ULONG             *pcbCipherText,
  _In_  ULONG             dwFlags
);
```

## Parameters

*hKey* `[in]`

The handle of the key to use for the encapsulation operation. This key must contain a public (encapsulation) key, and the handle would typically be obtained by using [BCryptImportKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptimportkeypair) with a [public key](/windows/win32/SecGloss/p-gly) BLOB for the KEM algorithm. It is also possible to use a private key handle for the encapsulation operation, as KEM private key handles represent a key pair.

*pbSecretKey* `[out]`

A pointer to a buffer that receives the shared secret key. See [remarks](#remarks) for more information.

*cbSecretKey* `[in]`

The size, in bytes, of the *pbSecretKey* buffer.

*pcbSecretKey* `[out]`

A pointer to a **ULONG** variable that the receives the number of bytes written to *pbSecretKey* buffer.

If *pbSecretKey* is `NULL`, this receives the size, in bytes, required for the shared secret key.
See [remarks](#remarks) for more information.

*pbCipherText* `[out]`

A pointer to a buffer that receives the KEM ciphertext. See [remarks](#remarks) for more information.

*cbCipherText* `[in]`

The size, in bytes, of the *pbCipherText* buffer.

*pcbCipherText* `[out]`

A pointer to a **ULONG** variable that the receives the number of bytes written to *pbCipherText* buffer.

If *pbCipherText* is `NULL`, this receives the size, in bytes, required for the KEM ciphertext.
See [remarks](#remarks) for more information.

*dwFlags* `[in]`

Reserved, must be zero.

## Return value

Returns a status code that indicates the success or failure of the function.

Possible return codes include, but are not limited to, the following.

| Return Code | Description |
|--|--|
| `STATUS_SUCCESS` | The function was successful. |
| `STATUS_INVALID_PARAMETER` | One or more required parameters (*hKey*, *pcbSecretKey*, *pcbCipherText*) is `NULL`, or one of the parameters has an invalid value. |
| `STATUS_INVALID_BUFFER_SIZE` | A buffer size (*cbSecretKey*, *cbCipherText*) does not match the expected size for the KEM parameters associated with the encapsulation key. *pcbSecretKey receives the number of bytes required for *pbSecretKey*, *pcbCipherText* receives the number of bytes required for *pbCipherText*. |
| `STATUS_BUFFER_TOO_SMALL` | An output buffer size (*cbSecretKey*, *cbCipherText*) is too small for the result encapsulation operation for the KEM parameters associated with the encapsulation key. *pcbSecretKey* receives the number of bytes required for *pbSecretKey*, *pcbCipherText* receives the number of bytes required for *pbCipherText*. |

## Remarks

To query the required sizes of the *pbSecretKey* and *pbCipherText* buffers, callers may call **BCryptEncapsulate** with `NULL` *pbSecretKey* and *pbCipherText*. The required sizes will be returned in *pcbSecretKey* and *pcbCipherText*, respectively. This query is efficient and returns the size without performing the encapsulation.
Equivalently, use [BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty) to query the **BCRYPT_KEM_SHARED_SECRET_LENGTH** property of the algorithm or key handle, and the **BCRYPT_KEM_CIPHERTEXT_LENGTH** property of the key handle.
For currently supported KEM algorithms (ML-KEM), the shared secret length is a constant size for a given algorithm and the KEM ciphertext length is a constant size for a given parameter set.

## Requirements

| Requirement | Value |
| ---- | ---- |
| **Minimum supported client** | Windows Insiders Preview [desktop apps only] |
| **Minimum supported server** | Windows Insiders Preview [desktop apps only] |
| **Library** | `Bcrypt.lib` |
| **DLL** | `Bcrypt.dll` |

## See also

[BCryptDecapsulate](nf-bcrypt-bcryptdecapsulate.md)

[BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty)
