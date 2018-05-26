---
Description: The following functions are used when working with enclaves that are used to create trusted execution environments
ms.assetid: DF6CDEE1-CAAA-429C-9939-DDC844302027
title: Trusted Execution Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Trusted Execution Functions

The following functions are used when working with enclaves that are used to create trusted execution environments:

## In this section



| Topic                                                                               | Description                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallEnclave**](/windows/win32/Enclaveapi/nf-enclaveapi-callenclave?branch=master)<br/>                                       | Calls a function within an enclave. <br/>                                                                                                                                                                                |
| [**CreateEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-createenclave?branch=master)<br/>                                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave.<br/> |
| [**DeleteEnclave**](/windows/win32/Enclaveapi/nf-enclaveapi-deleteenclave?branch=master)<br/>                                   | Deletes the specified enclave.<br/>                                                                                                                                                                                      |
| [**EnclaveGetAttestationReport**](/windows/win32/winenclaveapi/nf-winenclaveapi-enclavegetattestationreport?branch=master)<br/>       | Gets an enclave attestation report that describes the current enclave and is signed by the authority that is responsible for the type of the enclave. <br/>                                                              |
| [**EnclaveGetEnclaveInformation**](/windows/win32/winenclaveapi/nf-winenclaveapi-enclavegetenclaveinformation?branch=master)<br/>     | Gets information about the currently executing enclave.<br/>                                                                                                                                                             |
| [**EnclaveSealData**](/windows/win32/winenclaveapi/nf-winenclaveapi-enclavesealdata?branch=master)<br/>                               | Generates an encrypted binary large object (blob) from unencypted data.<br/>                                                                                                                                             |
| [**EnclaveUnsealData**](/windows/win32/winenclaveapi/nf-winenclaveapi-enclaveunsealdata?branch=master)<br/>                           | Decrypts an encrypted binary large object (blob).<br/>                                                                                                                                                                   |
| [**EnclaveVerifyAttestationReport**](/windows/win32/winenclaveapi/nf-winenclaveapi-enclaveverifyattestationreport?branch=master)<br/> | Verifies an attestation report that was generated on the current system. <br/>                                                                                                                                           |
| [**InitializeEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-initializeenclave?branch=master)<br/>                           | Initializes an enclave that you created and loaded with data.<br/>                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](/windows/win32/enclaveapi/nf-enclaveapi-isenclavetypesupported?branch=master)<br/>                 | Retrieves whether the specified type of enclave is supported.<br/>                                                                                                                                                       |
| [**LoadEnclaveData**](/windows/win32/enclaveapi/nf-enclaveapi-loadenclavedata?branch=master)<br/>                               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-createenclave?branch=master).<br/>                                                                                                        |
| [**LoadEnclaveImage**](/windows/win32/Enclaveapi/nf-enclaveapi-loadenclaveimagew?branch=master)<br/>                             | Loads an image and all of its imports into an enclave.<br/>                                                                                                                                                              |
| [**TerminateEnclave**](/windows/win32/Enclaveapi/nf-enclaveapi-terminateenclave?branch=master)<br/>                             | Ends the execution of the threads that are running within an enclave.<br/>                                                                                                                                               |



 

 

 




