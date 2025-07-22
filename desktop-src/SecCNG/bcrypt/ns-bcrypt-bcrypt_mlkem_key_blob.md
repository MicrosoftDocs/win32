---
title: BCRYPT_MLKEM_KEY_BLOB structure
description: This structure is used to import and export keys for the ML-KEM algorithm.
ms.topic: reference
ms.date: 05/27/2025
req.header: bcrypt.h
req.target-min-winverclnt: Windows Insiders Preview
req.target-min-winversvr: Windows Insiders Preview
req.lib:
req.dll:
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Bcrypt.dll
api_name:
- BCRYPT_MLKEM_KEY_BLOB
targetos: Windows
---

# BCRYPT_MLKEM_KEY_BLOB structure

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **BCRYPT_MLKEM_KEY_BLOB** structure is used as a header for an ML-KEM [public key](/windows/win32/SecGloss/p-gly) (byte-encoded encapsulation key) or [private key](/windows/win32/SecGloss/p-gly) [BLOB](/windows/win32/SecGloss/b-gly) in memory.

## Syntax

```cpp
typedef struct _BCRYPT_MLKEM_KEY_BLOB {
  ULONG dwMagic;
  ULONG cbParameterSet;             // Byte size of parameterSet[]
  ULONG cbKey;                      // Byte size of key[]
  // WCHAR parameterSet[cbParameterSet / sizeof(WCHAR)];  // Including \0-terminated
  // BYTE key[cbKey];                                     // Key material
} BCRYPT_MLKEM_KEY_BLOB, *PBCRYPT_MLKEM_KEY_BLOB;
```

## Fields

### dwMagic

The **dwMagic** field is a 4-byte value that indicates the format of the key being used. The following values are defined:

| Value | Meaning |
|--|--|
| **BCRYPT_MLKEM_PUBLIC_MAGIC** `0x504B4C4D` | The structure represents a public key. |
| **BCRYPT_MLKEM_PRIVATE_MAGIC** `0x524B4C4D` | The structure represents an expanded private key. |
| **BCRYPT_MLKEM_PRIVATE_SEED_MAGIC** `0x534B4C4D` | The structure represents a private seed. |

### cbParameterSet

The length, in bytes, of the buffer **parameterSet** directly following the struct. This buffer contains a null-terminated Unicode string that identifies the parameter set of the key. The following values (per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)) are currently supported:

| parameterSet | cbParameterSet | Meaning |
|--|--|--|
| **BCRYPT_MLKEM_PARAMETER_SET_512** `L"512"` | 8 | ML-KEM-512, security category 1. |
| **BCRYPT_MLKEM_PARAMETER_SET_768** `L"768"` | 8 | ML-KEM-768, security category 3. |
| **BCRYPT_MLKEM_PARAMETER_SET_1024** `L"1024"` | 10 | ML-KEM-1024, security category 5. |

### cbKey

The length, in bytes, of the buffer **key** directly following **parameterSet**. This size is static and depends on the key format and parameter set in use.

## Remarks

**BCRYPT_MLKEM_PRIVATE_SEED_BLOB** supports import and export of ML-KEM seeds. The blob has **dwMagic**  value `BCRYPT_MLKEM_PRIVATE_SEED_MAGIC` and the **key** field contains the KEM seed (defined as the 64-byte concatenation of `d || z` per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)), so **cbKey** is currently always `64`.

**BCRYPT_MLKEM_PRIVATE_BLOB** (also aliased as **BCRYPT_MLKEM_DECAPSULATION_BLOB**) supports import and export of standard byte-encoded ML-KEM decapsulation keys per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). The blob has **dwMagic** value `BCRYPT_MLKEM_PRIVATE_MAGIC` and the **key** field contains the byte-encoded key. 

**BCRYPT_MLKEM_PUBLIC_BLOB** (also aliased as **BCRYPT_MLKEM_ENCAPSULATION_BLOB**) supports import and export of standard byte-encoded ML-KEM encapsulation keys per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). The blob has **dwMagic** value `BCRYPT_MLKEM_PUBLIC_MAGIC` and the **key** field contains the byte-encoded key.

The byte sizes of the byte-encoded keys can be found in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) Section 8 Table 3. Many callers can instead dynamically query the required blob sizes using **BCryptExportKey** with `NULL` *pbOutput*.

## Requirements

| Requirement | Value |
| ---- | ---- |
| **Minimum supported client** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Minimum supported server** | **Windows Insiders (build 27843):** Support for ML-KEM begins. [desktop apps only] |
| **Header** | `bcrypt.h` |

## See also

[BCryptGenerateKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgeneratekeypair)

[BCryptImportKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptimportkeypair)

[BCryptFinalizeKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptfinalizekeypair)

[BCryptExportKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptexportkey)

[BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty)

[BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty)

[BCryptEncapsulate](nf-bcrypt-bcryptencapsulate.md)

[BCryptDecapsulate](nf-bcrypt-bcryptdecapsulate.md)
