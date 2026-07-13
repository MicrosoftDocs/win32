---
title: NCryptEncapsulate function
description: The NCryptEncapsulate function performs the Encapsulation operation of a KEM algorithm.
ms.topic: reference
ms.date: 05/27/2025
req.lib: Ncrypt.lib
req.dll: Ncrypt.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Ncrypt.dll
api_name:
- NCryptEncapsulate
targetos: Windows
---

# NCryptEncapsulate function

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **NCryptEncapsulate** function performs the Encapsulation operation of a Key Encapsulation Mechanism (KEM).
It generates a shared secret key and encrypts it with the provided public key to produce a KEM ciphertext, returning both the shared secret key and the KEM ciphertext.

## Syntax

```cpp
NTSTATUS NCryptEncapsulate (
    [in]    NCRYPT_KEY_HANDLE hKey
    [out]   PBYTE             pbSecretKey,
    [in]    ULONG             cbSecretKey,
    [out]   ULONG             *pcbSecretKey,
    [out]   PBYTE             pbCipherText,
    [in]    ULONG             cbCipherText,
    [out]   ULONG             *pcbCipherText,
    [in]    ULONG             dwFlags
);
```

## Parameters

*hKey* `[in]`

The handle of the key to use for the encapsulation operation.

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
| `ERROR_SUCCESS` | The function was successful. |
| `NTE_BAD_FLAGS` | The *dwFlags* parameter contains a value that is not valid. |
| `NTE_INVALID_PARAMETER` | One or more required parameters (*hKey*, *pcbSecretKey*, *pcbCipherText*) is `NULL`, or one of the parameters has an invalid value. |
| `NTE_BUFFER_TOO_SMALL` | An output buffer size (*cbSecretKey*, *cbCipherText*) is too small for the result of the encapsulation for the KEM parameters associated with the encapsulation key. *pcbSecretKey* receives the number of bytes required for *pbSecretKey*, *pcbCipherText* receives the number of bytes required for *pbCipherText*. |

## Remarks

To query the required sizes of the *pbSecretKey* and *pbCipherText* buffers, callers may call **NCryptEncapsulate** with `NULL` values in *pbSecretKey* and *pbCipherText*. The required size will be returned in *pcbSecretKey* and *pcbCipherText*, respectively. This query is efficient and returns the size without performing the encapsulation.
Equivalently, use [NCryptGetProperty](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) to query the **NCRYPT_KEM_SHARED_SECRET_LENGTH_PROPERTY** property of the algorithm or key handle, and the **NCRYPT_KEM_CIPHERTEXT_LENGTH_PROPERTY** property of the key handle.
For currently supported KEM algorithms (ML-KEM), the shared secret length is a constant size for a given algorithm and the KEM ciphertext length is a constant size for a given parameter set.

## Requirements

| Requirement | Value |
| ---- | ---- |
| **Minimum supported client** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Minimum supported server** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Library** | `Ncrypt.lib` |
| **DLL** | `Ncrypt.dll` |

## See also

[NCryptDecapsulate](./nf-ncrypt-ncryptdecapsulate.md)

[NCryptGetProperty](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty)

[BCryptEncapsulate](../bcrypt/nf-bcrypt-bcryptencapsulate.md)

[BCryptDecapsulate](../bcrypt/nf-bcrypt-bcryptdecapsulate.md)
