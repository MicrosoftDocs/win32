---
title: BCRYPT_PQDSA_KEY_BLOB structure
description: This structure is used to import and export keys for Post-Quantum Digital Signature algorithms (PQDSA).
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
- BCRYPT_PQDSA_KEY_BLOB
targetos: Windows
---

# BCRYPT_PQDSA_KEY_BLOB structure

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This structure is used to import and export keys for Post-Quantum Digital Signature algorithms (PQDSA).

## Syntax

```cpp
typedef struct _BCRYPT_PQDSA_KEY_BLOB {
  ULONG dwMagic;
  ULONG dwAlg;
  ULONG cbKey;
  // Followed by key material
} BCRYPT_PQDSA_KEY_BLOB, *PBCRYPT_PQDSA_KEY_BLOB; 
```

## Fields
### Field dwMagic

The **dwMagic** field is a 4-byte value that indicates the format of the key being used. The following values are defined:

| Value | Description |
|--|--|
| **BCRYPT_MLDSA_PUBLIC_MAGIC** | The key is a public key. |
| **BCRYPT_MLDSA_PRIVATE_MAGIC** | The key is a private key. |
| **BCRYPT_MLDSA_PRIVATE_SEED_MAGIC** | This is a private seed. |

### Field dwAlg

The **dwAlg** field indicates the algorithm used. The parameter should be set for ML-DSA and SLH-DSA, and zero for LMS, XMSS. The following values are defined:

| Value | Description |
|--|--|
| **BCRYPT_MLDSA_PARAMETER_SET_44** `L"44"` | NIST parameter set 44 for ML-DSA, security category 3. |
| **BCRYPT_MLDSA_PARAMETER_SET_65** `L"65"` | NIST parameter set 65 for ML-DSA, security category 4. |
| **BCRYPT_MLDSA_PARAMETER_SET_87** `L"87"` | NIST parameter set 87 for ML-DSA, security category 5. |

### Field cbKey

Size of the buffer "Key" directly following the struct. This size is static and depends on the key format and parameter set in use.

## Remarks

The consumers of Post-Quantum Digital Signature algorithms will use the same subset of the BCrypt API as the existing (non-Post-Quantum) Digital Signature Algorithms supported by CNG in order to perform the operations the algorithms support. These are: 

- Algorithm handle manipulation: [BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider), [BCryptCloseAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptclosealgorithmprovider)
- Key management: [BCryptGenerateKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgeneratekeypair), [BCryptImportKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptimportkeypair), [BCryptExportKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptexportkey), [BCryptDestroyKey](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptdestroykey), [BCryptFinalizeKeyPair](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptfinalizekeypair)
- Signature generation/verification: [BCryptSignHash](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsignhash), [BCryptVerifySignature](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptverifysignature)
- Updating/Querying properties: [BCryptGetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptgetproperty), [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty)
