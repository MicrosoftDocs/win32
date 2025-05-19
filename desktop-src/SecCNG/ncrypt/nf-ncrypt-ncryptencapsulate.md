---
title: NCryptEncapsulate function
description: The NCryptEncapsulate function encapsulates a key for the ML-KEM algorithm.
ms.topic: reference
ms.date: 05/13/2025
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

The **NCryptEncapsulate** function encapsulates a key for the ML-KEM algorithm.

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

These APIs will invoke internally the corresponding BCrypt APIs [BCryptEncapsulate](../bcrypt/nf-bcrypt-bcryptencapsulate.md) and [BCryptDecapsulate](../bcrypt/nf-bcrypt-bcryptdecapsulate.md) for ML-KEM key handles.

The required buffer length for *pbSecretKey*, *pbCipherText* are static values which depend only on the parameter set in use. The sizes for each parameter set are documented in ML-KEM Key and Ciphertext Sizes.

Alternatively, callers can query the required size of the *pbSecretKey*, *pbCipherText* buffer needed for the ML-KEM ciphertext, by calling **NCryptEncapsulate** with `NULL` values in *pbSecretKey* and *pbCipherText*. The required size will be returned in *pcbSecretKey* and *pcbCipherText*, respectively. This query is efficient and returns the size without performing the encapsulation.
