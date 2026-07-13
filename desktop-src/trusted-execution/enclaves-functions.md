---
description: The following functions are used when working with enclaves that are used to create trusted execution environments.
ms.assetid: DF6CDEE1-CAAA-429C-9939-DDC844302027
title: Enclave Functions (Trusted Execution)
titleSuffix: Secure Enclaves
ms.topic: reference
ms.date: 11/20/2024
---

# Enclave Functions

The following functions are used when working with enclaves that are used to create trusted execution environments.

> [!NOTE]
> Using these APIs for a VBS Enclave requires Windows 11 Build 26100.2314 or later or Windows Server 2025 or later.

## In this section

| Topic | Description |
|--------|--------|
| [CallEnclave](/windows/win32/api/Enclaveapi/nf-enclaveapi-callenclave) | Calls a function within an enclave. |
| [CreateEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-createenclave) | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave. |
| [DeleteEnclave](/windows/win32/api/Enclaveapi/nf-enclaveapi-deleteenclave) | Deletes the specified enclave. |
| [EnclaveCopyIntoEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyintoenclave) | Copies data from an untrusted address (outside of the enclave) into the enclave. |
| [EnclaveCopyOutOfEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyoutofenclave) | Copies data from the enclave to an untrusted address (outside of the enclave). |
| [EnclaveGetAttestationReport](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavegetattestationreport) | Gets an enclave attestation report that describes the current enclave and is signed by the authority that is responsible for the type of the enclave. |
| [EnclaveGetEnclaveInformation](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavegetenclaveinformation) | Gets information about the currently executing enclave. |
| [EnclaveRestrictContainingProcessAccess](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaverestrictcontainingprocessaccess) | Restricts (or restores) access by an enclave to the address space of its containing process. |
| [EnclaveSealData](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavesealdata) | Generates an encrypted binary large object (blob) from unencypted data. |
| [EnclaveUnsealData](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaveunsealdata) | Decrypts an encrypted binary large object (blob). |
| [EnclaveVerifyAttestationReport](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaveverifyattestationreport) | Verifies an attestation report that was generated on the current system. |
| [InitializeEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-initializeenclave) | Initializes an enclave that you created and loaded with data. |
| [IsEnclaveTypeSupported](/windows/win32/api/enclaveapi/nf-enclaveapi-isenclavetypesupported) | Retrieves whether the specified type of enclave is supported. |
| [LoadEnclaveData](/windows/win32/api/enclaveapi/nf-enclaveapi-loadenclavedata) | Loads data into an uninitialized enclave that you created by calling [CreateEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-createenclave). |
| [LoadEnclaveImage](/windows/win32/api/Enclaveapi/nf-enclaveapi-loadenclaveimagew) | Loads an image and all of its imports into an enclave. |
| [TerminateEnclave](/windows/win32/api/Enclaveapi/nf-enclaveapi-terminateenclave) | Ends the execution of the threads that are running within an enclave. |

## See also

- [Enclave Enumerations](enclaves-enumerations.md)
- [Enclave Structures](enclaves-structures.md)
