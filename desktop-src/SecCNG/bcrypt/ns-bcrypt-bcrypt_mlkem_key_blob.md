---
title: BCRYPT_MLKEM_KEY_BLOB structure
description: This structure is used to import and export keys for the ML-KEM algorithm.
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
- BCRYPT_MLKEM_KEY_BLOB
targetos: Windows
---

# BCRYPT_MLKEM_KEY_BLOB structure

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **BCRYPT_MLKEM_KEY_BLOB** structure is used as a header for the ML-KEM private seed, public key (byte-encoded encapsulation key), and private key (byte-encoded decapsulation key) BLOB in memory.

## Syntax

```cpp
typedef struct _BCRYPT_MLKEM_KEY_BLOB
{
    ULONG   dwMagic;
    DWORD   dwParameterSet;
    ULONG   cbKey;
    // Key[cbKey]
} BCRYPT_MLKEM_KEY_BLOB, *PBCRYPT_MLKEM_KEY_BLOB;
```

## Fields

### Field dwMagic

The **dwMagic** field is a 4-byte value that indicates the format of the key being used. The following values are defined:

| Value | Description |
|--|--|
| **BCRYPT_MLKEM_PUBLIC_MAGIC**<br/>`0x504B4C4D` "MLKP" | The key is a public key. |
| **BCRYPT_MLKEM_PRIVATE_MAGIC**<br/>`0x524B4C4D` "MLKR" | The key is a private key. |
| **BCRYPT_MLKEM_SEED_MAGIC**<br/>`0x534B4C4D` "MLKS" | The key is a seed key. |

### Field dwParameterSet

Indicates the ML-KEM parameter set this key is being used with.

To denote the **dwParameterSet**, reuse the pseudo-handle values, i.e. `dwParameterSet = BCRYPT_MLKEM_512_ALG` when using **ML-KEM 512**. When importing, the declared **dwParameterSet** must match the parameter set of the algorithm handle used. For ML-KEM, the standard byte encoding defined in [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf) is intended to be opaque to higher level protocols so the key itself will be a single binary buffer.

| Value | Description |
|--|--|
| **BCRYPT_MLKEM_PARAMETER_SET_512** `L"512"` | NIST parameter set 512 for ML-KEM, security category 2. |
| **BCRYPT_MLKEM_PARAMETER_SET_768** `L"768"` | NIST parameter set 768 for ML-KEM, security category 3. |
| **BCRYPT_MLKEM_PARAMETER_SET_1024** `L"1024"` | NIST parameter set 1024 for ML-KEM, security category 5. |

### Field cbKey

Size of the buffer "Key" directly following the struct. This size is static and depends on the key format and parameter set in use.

## Remarks

**BCRYPT_MLKEM_PRIVATE_SEED_BLOB** provides import and export of ML-KEM seeds. The blob has **dwMagic** **BCRYPT_MLKEM_SEED_MAGIC** and the **Key** field contains the KEM seed (defined as the 64-byte concatenation of `d || z` per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf)).

**BCRYPT_MLKEM_PRIVATE_BLOB** (also aliased as **BCRYPT_MLKEM_DECAPSULATION_BLOB**) provides import and export of standard byte-encoded ML-KEM decapsulation keys per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). The blob has magic **BCRYPT_MLKEM_PRIVATE_MAGIC** and the **Key** field contains the byte-encoded key. The sizes of the private keys for each algorithm are shown in ML-KEM Key and Ciphertext Sizes under column "Decapsulation Key Size".

**BCRYPT_MLKEM_PUBLIC_BLOB** (also aliased as **BCRYPT_MLKEM_ENCAPSULATION_BLOB**) provides import and export of standard byte-encoded ML-KEM encapsulation keys per [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). The blob has magic **BCRYPT_MLKEM_PUBLIC_MAGIC** and the **Key** field contains the byte-encoded key. The sizes of the public keys for each algorithm are shown in ML-KEM Key and Ciphertext Sizes under column "Encapsulation Key Size".

For example, the encapsulation key for ML-KEM 512 would be imported/exported using type **BCRYPT_MLKEM_ENCAPSULATION_BLOB**. The blob will have magic **BCRYPT_MLKEM_PUBLIC_MAGIC**, **BCRYPT_MLKEM_512_ALG** is 812 bytes in length.

## See also
