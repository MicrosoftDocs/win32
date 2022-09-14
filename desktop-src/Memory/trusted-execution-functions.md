---
description: 'The following functions are used when working with enclaves that are used to create trusted execution environments:'
ms.assetid: DF6CDEE1-CAAA-429C-9939-DDC844302027
title: Trusted Execution Functions
ms.topic: article
ms.date: 05/31/2018
---

# Trusted Execution Functions

The following functions are used when working with enclaves that are used to create trusted execution environments:

## In this section



| Topic                                                                               | Description                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallEnclave**](/windows/desktop/api/Enclaveapi/nf-enclaveapi-callenclave)<br/>                                       | Calls a function within an enclave. <br/>                                                                                                                                                                                |
| [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave)<br/>                                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave.<br/> |
| [**DeleteEnclave**](/windows/desktop/api/Enclaveapi/nf-enclaveapi-deleteenclave)<br/>                                   | Deletes the specified enclave.<br/>                                                                                                                                                                                      |
| [**EnclaveGetAttestationReport**](/windows/desktop/api/winenclaveapi/nf-winenclaveapi-enclavegetattestationreport)<br/>       | Gets an enclave attestation report that describes the current enclave and is signed by the authority that is responsible for the type of the enclave. <br/>                                                              |
| [**EnclaveGetEnclaveInformation**](/windows/desktop/api/winenclaveapi/nf-winenclaveapi-enclavegetenclaveinformation)<br/>     | Gets information about the currently executing enclave.<br/>                                                                                                                                                             |
| [**EnclaveSealData**](/windows/desktop/api/winenclaveapi/nf-winenclaveapi-enclavesealdata)<br/>                               | Generates an encrypted binary large object (blob) from unencypted data.<br/>                                                                                                                                             |
| [**EnclaveUnsealData**](/windows/desktop/api/winenclaveapi/nf-winenclaveapi-enclaveunsealdata)<br/>                           | Decrypts an encrypted binary large object (blob).<br/>                                                                                                                                                                   |
| [**EnclaveVerifyAttestationReport**](/windows/desktop/api/winenclaveapi/nf-winenclaveapi-enclaveverifyattestationreport)<br/> | Verifies an attestation report that was generated on the current system. <br/>                                                                                                                                           |
| [**InitializeEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-initializeenclave)<br/>                           | Initializes an enclave that you created and loaded with data.<br/>                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](/windows/desktop/api/enclaveapi/nf-enclaveapi-isenclavetypesupported)<br/>                 | Retrieves whether the specified type of enclave is supported.<br/>                                                                                                                                                       |
| [**LoadEnclaveData**](/windows/desktop/api/enclaveapi/nf-enclaveapi-loadenclavedata)<br/>                               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave).<br/>                                                                                                        |
| [**LoadEnclaveImage**](/windows/desktop/api/Enclaveapi/nf-enclaveapi-loadenclaveimagew)<br/>                             | Loads an image and all of its imports into an enclave.<br/>                                                                                                                                                              |
| [**TerminateEnclave**](/windows/desktop/api/Enclaveapi/nf-enclaveapi-terminateenclave)<br/>                             | Ends the execution of the threads that are running within an enclave.<br/>                                                                                                                                               |



 

 

 




