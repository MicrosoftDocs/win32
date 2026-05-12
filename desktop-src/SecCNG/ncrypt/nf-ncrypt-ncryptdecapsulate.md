---
title: NCryptDecapsulate function
description: The NCryptDecapsulate function performs the Decapsulation operation of a KEM algorithm.
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
- NCryptDecapsulate
targetos: Windows
---

# NCryptDecapsulate function

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **NCryptDecapsulate** function performs the Decapsulation operation of a Key Encapsulation Mechanism (KEM).
It takes a KEM ciphertext and it decrypts with the provided private key, returning the shared secret key.

If the ciphertext is correctly formatted but does not match the decapsulation key, this API will succeed but a random shared secret key will be generated.

## Syntax

```cpp
SECURITY_STATUS NCryptDecapsulate (
 [in]    NCRYPT_KEY_HANDLE hKey,
 [in]    PCBYTE            pbCipherText,
 [in]    ULONG             cbCipherText,
 [out]   PBYTE             pbSecretKey,
 [in]    ULONG             cbSecretKey,
 [out]   ULONG             *pcbSecretKey,
 [in]    ULONG             dwFlags
);
```

## Parameters

*hKey* `[in]`

The handle of the key to use for the decapsulation operation.

*pbCipherText* `[in]`

A pointer to a buffer that contains the KEM ciphertext. The [NCryptEncapsulate](nf-ncrypt-ncryptencapsulate.md) function may be used to create a KEM ciphertext.

*cbCipherText* `[in]`

The size, in bytes, of the *pbCipherText* buffer.

*pbSecretKey* `[out]`

A pointer to a buffer that receives the shared secret key. See [remarks](#remarks) for more information.

*cbSecretKey* `[in]`

The size, in bytes, of the *pbSecretKey* buffer.

*pcbSecretKey* `[out]`

A pointer to a **ULONG** variable that the receives the number of bytes written to *pbSecretKey* buffer.

If *pbSecretKey* is `NULL`, this receives the size, in bytes, required for the shared secret key.
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
| `NTE_INVALID_PARAMETER` | One or more required parameters (*hKey*, *pcbSecretKey*, *pcbCipherText*) is NULL, or one of the parameters has an invalid value. |
| `NTE_BUFFER_TOO_SMALL` | An output buffer size (*cbSecretKey*) is too small for the result decapsulation operation for the KEM parameters associated with the decapsulation key. *pcbSecretKey* receives the number of bytes required for *pbSecretKey*. |

## Remarks

To query the required size of the *pbSecretKey* buffer needed for the KEM shared secret key, call **NCryptDecapsulate** with a `NULL` *pbSecretKey*. The required size will be returned in *pcbSecretKey*. This query is efficient and returns the size without performing the decapsulation.
Equivalently, use [NCryptGetProperty](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty) to query the **NCRYPT_KEM_SHARED_SECRET_LENGTH_PROPERTY** property of the algorithm or key handle.
For currently supported KEM algorithms (ML-KEM), the shared secret length is a constant size for a given algorithm.

### Additional remarks

Given an invalid, but correctly-sized, ciphertext, the ML-KEM decapsulation operation will *implicitly reject* the ciphertext by returning success in equal time to a valid decapsulation operation, with pseudo-random agreed secret output. This forces higher-level protocols to fail later when symmetric keys of peers don't match. So, decapsulate will only ever fail if there are programming errors (i.e. incorrect size, use of uninitialized *hKey*), or something fundamentally goes wrong with the environment (i.e. internal memory allocation fails, or self-test detect hardware error).

## Requirements

| Requirement | Value |
| ---- | ---- |
| **Minimum supported client** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Minimum supported server** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Library** | `Ncrypt.lib` |
| **DLL** | `Ncrypt.dll` |

## See also

[NCryptEncapsulate](nf-ncrypt-ncryptencapsulate.md)

[NCryptGetProperty](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptgetproperty)

[BCryptEncapsulate](../bcrypt/nf-bcrypt-bcryptencapsulate.md)

[BCryptDecapsulate](../bcrypt/nf-bcrypt-bcryptdecapsulate.md)
