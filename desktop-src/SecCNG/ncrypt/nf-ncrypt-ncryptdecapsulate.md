---
title: NCryptDecapsulate function
description: The NCryptDecapsulate function takes the ML-KEM cipher text and decrypts it with the provided private key, yielding the shared secret key.
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
- NCryptDecapsulate
targetos: Windows
---

# NCryptDecapsulate function

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **NCryptDecapsulate** function takes the cipher text and decrypts it with the provided private key, yielding the shared secret key.

**NCryptDecapsulate** accepts a key imported with [NCryptImportKey](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptimportkey). The ciphertext from encapsulate is the input and the shared secret key is the output. Decapsulation does not modify the handle pointed to by *hKey*, the decapsulated secret key is not imported into the handle. Multiple decapsulation operations can be performed using the same decapsulation key.

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

Provides a key handle for the ML-KEM decapsulation key.

*pbCipherText* `[in]`

A pointer to a caller allocated buffer containing the ciphertext produced by [NCryptEncapsulate](nf-ncrypt-ncryptencapsulate.md). 

*cbCipherText* `[in]`

The size, in bytes, of *pbCipherText*. 

*pbSecretKey* `[out]`

A pointer to a caller allocated buffer receiving the shared secret key. See [remarks](#remarks) for more information.

*cbSecretKey* `[in]`

The size, in bytes, of pbSecretKey. See [remarks](#remarks) for more information.

pcbSecretKey – If pbSecretKey is NULL, receives the number of bytes required for pbSecretKey. Otherwise, returns the number of bytes written to pbSecretKey. See [remarks](#remarks) for more information.

*dwFlags* `[in]`

Reserved, must be zero. ML-KEM currently has no flags. 

## Return value

If the function succeeds, the return value is `STATUS_SUCCESS`. Otherwise, it returns an NTSTATUS code that indicates the error.

| Error Code | Description |
|------------|-------------|
| `STATUS_INVALID_BUFFER_SIZE` | Returned if required parameters are missing, or if the ciphertext is of the incorrect size for the version of ML-KEM associated with the decapsulation key. |
| `STATUS_BUFFER_TOO_SMALL` | Returned if the buffer *pbSecretKey* is too small. *pcbSecretKey* receives the number of bytes required for *pbSecretKey*. |

## Remarks

These APIs will invoke internally the corresponding BCrypt APIs [BCryptEncapsulate](../bcrypt/nf-bcrypt-bcryptencapsulate.md) and [BCryptDecapsulate](../bcrypt/nf-bcrypt-bcryptdecapsulate.md) for ML-KEM key handles.

To query the required size of the *pbSecretKey* buffer needed for the ML-KEM shared secret key, call [NCryptDecrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdecrypt) with a `NULL` *pbSecretKey*. The required size will be returned in *pcbSecretKey*. This query is efficient and returns the size without performing the decapsulation. Equivalently, use [NCryptGetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptgetproperty) to query the **NCRYPT_KEM_SHARED_SECRET_LENGTH** property of the algorithm handle. The secret key size for each algorithm is detailed in ML-KEM Key and Ciphertext Sizes.

### Special note (per the SymCrypt documentation)

Given an invalid, but correctly-sized, ciphertext, the ML-KEM decapsulation operation will *implicitly reject* the ciphertext by returning success in equal time to a valid decapsulation operation, with pseudo-random agreed secret output. This forces higher-level protocols to fail later when symmetric keys of peers don't match. So, decapsulate will only ever fail if there are programming errors (i.e. incorrect size, use of uninitialized *pkMlKemkey*), or something fundamentally goes wrong with the environment (i.e. internal memory allocation fails, or self-test detect hardware error).

NCrypt shall expose this same failure interface in part because Symcrypt does not expose granular control of the failure mode and because this method avoids the possibility of leaking data through timing side channels for callers of the API.

## See also

[NCryptEncapsulate](nf-ncrypt-ncryptencapsulate.md)

[NCryptDecrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdecrypt)

[NCryptGetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptgetproperty)
