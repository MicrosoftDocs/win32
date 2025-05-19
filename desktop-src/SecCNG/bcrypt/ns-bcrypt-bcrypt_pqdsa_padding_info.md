---
title: BCRYPT_PQDSA_PADDING_INFO structure
description: This structure is used to specify the padding scheme for Post-Quantum Digital Signature algorithms (PQDSA).
ms.date: 05/13/2025
ms.topic: reference
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
- BCRYPT_PQDSA_PADDING_INFO
targetos: Windows
---

# BCRYPT_PQDSA_PADDING_INFO structure

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This structure is used to specify the padding scheme for Post-Quantum Digital Signature algorithms (PQDSA).

## Syntax

```cpp
typedef struct _BCRYPT_PQDSA_PADDING_INFO {
PUCHAR		pbCtx;
ULONG		cbCtx;
LPCWSTR	pszPrehashAlgId;
} BCRYPT_PQDSA_PADDING_INFO;
```

## Fields

### Field pbCtx

A pointer to the buffer that contains the context string.

May be `NULL`. If *pbCtx* is `NULL`, then *cbCtx* must be set to `0`.

### Field cbCtx

The size, in bytes, of the context string pointed to by *pbCtx*. Its value must be `0` if *pbCtx* is `NULL`. Otherwise, it must be a non-zero integer less than `256`.

### Field pszPrehashAlgId

A CNG hash algorithm identifier. This parameter indicates whether the pure or the pre-hash variant of ML-DSA/SLH-DSA will be used. Because a hash identifier is only required for the pre-hash variants, a `NULL` value indicates the use of pure ML-DSA or pure SLH-DSA. To use a pre-hash variant, this identifier must refer to an approved hash algorithm: SHA-2, SHA-3, or SHAKE.

## Remarks
