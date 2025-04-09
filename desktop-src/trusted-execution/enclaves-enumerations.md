---
description: The following enumerations are used when working with enclaves that are used to create trusted execution environments.
ms.assetid: 7B122E1F-AAF8-4834-B262-CD641D16DA4E
title: Enclave Enumerations (Trusted Execution)
titleSuffix: Secure Enclaves
ms.topic: reference
ms.date: 11/20/2024
---

# Enclave Enumerations

The following enumerations are used when working with enclaves that are used to create trusted execution environments.

> [!NOTE]
> Using these APIs for a VBS Enclave requires Windows 11 Build 26100.2314 or later or Windows Server 2025 or later.

## In this section

| Topic | Description |
|--------|--------|
| [ENCLAVE_SEALING_IDENTITY_POLICY](/windows/win32/api/ntenclv/ne-ntenclv-enclave_sealing_identity_policy) | Defines values that specify how another enclave must be related to the enclave that calls [EnclaveSealData](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavesealdata) for the enclave to unseal the data. |

## See also

- [Enclave Functions](enclaves-functions.md)
- [Enclave Structures](enclaves-structures.md)
