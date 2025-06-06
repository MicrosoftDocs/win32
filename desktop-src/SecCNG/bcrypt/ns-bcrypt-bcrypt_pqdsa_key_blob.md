---
title: BCRYPT_PQDSA_KEY_BLOB structure
description: This structure is used to import and export keys for Post-Quantum Digital Signature algorithms (PQDSA).
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
- BCRYPT_PQDSA_KEY_BLOB
targetos: Windows
---

# BCRYPT_PQDSA_KEY_BLOB structure

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This structure is used to import and export keys for Post-Quantum Digital Signature algorithms (PQDSA).
The **BCRYPT_PQDSA_KEY_BLOB** structure is used as a header for a Post-Quantum Digital Signature algorithm (PQDSA)
[public key](/windows/win32/SecGloss/p-gly) (byte-encoded encapsulation key) or [private key](/windows/win32/SecGloss/p-gly) [BLOB](/windows/win32/SecGloss/b-gly) in memory.

## Syntax

```cpp
typedef struct _BCRYPT_PQDSA_KEY_BLOB {
  ULONG dwMagic;
  ULONG cbParameterSet;                                   // Byte size of parameterSet[]
  ULONG cbKey;                                            // Byte size of key[]
  // WCHAR parameterSet[cbParameterSet / sizeof(WCHAR)];  // Including \0 terminator
  // BYTE key[cbKey];                                     // Key material
} BCRYPT_PQDSA_KEY_BLOB, *PBCRYPT_PQDSA_KEY_BLOB;
```

## Fields

### dwMagic

The **dwMagic** field is a 4-byte value that indicates the format of the key being used. The following values are defined:

| Value | Meaning |
|--|--|
| **BCRYPT_MLDSA_PUBLIC_MAGIC** `0x4B505344` | The structure represents a public key. |
| **BCRYPT_MLDSA_PRIVATE_MAGIC** `0x4B535344` | The structure represents an expanded private key. |
| **BCRYPT_MLDSA_PRIVATE_SEED_MAGIC** `0x53535344` | The structure represents a private seed. |

### cbParameterSet

The length, in bytes, of the buffer `parameterSet` directly following the struct. This buffer contains a null-terminated Unicode string that identifies the parameter set of the key. The following values are currently supported:

| parameterSet | cbParameterSet | Meaning |
|--|--|--|
| **BCRYPT_MLDSA_PARAMETER_SET_44** `L"44"` | 6 | ML-DSA-44, security category 2. |
| **BCRYPT_MLDSA_PARAMETER_SET_65** `L"65"` | 6 | ML-DSA-65, security category 3. |
| **BCRYPT_MLDSA_PARAMETER_SET_87** `L"87"` | 6 | ML-DSA-87, security category 5. |

### cbKey

The length, in bytes, of the buffer **key** directly following **parameterSet**. This size is static and depends on the key format and parameter set in use.

## Remarks

The consumers of Post-Quantum Digital Signature algorithms will use the same subset of the BCrypt API as the existing (non-Post-Quantum) Digital Signature Algorithms supported by CNG in order to perform the operations the algorithms support. These are: 

- Algorithm handle manipulation: [BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider), [BCryptCloseAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptclosealgorithmprovider)
- Key management: [BCryptGenerateKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgeneratekeypair), [BCryptImportKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptimportkeypair), [BCryptExportKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptexportkey), [BCryptDestroyKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptdestroykey), [BCryptFinalizeKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptfinalizekeypair)
- Signature generation/verification: [BCryptSignHash](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsignhash), [BCryptVerifySignature](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptverifysignature)
- Updating/Querying properties: [BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty), [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty)

## Requirements

| Requirement | Value |
| ---- | ---- |
| **Minimum supported client** | Windows Insiders Preview [desktop apps only] |
| **Minimum supported server** | Windows Insiders Preview [desktop apps only] |
| **Header** | `bcrypt.h` |
