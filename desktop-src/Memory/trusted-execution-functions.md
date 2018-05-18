---
Description: 'The following functions are used when working with enclaves that are used to create trusted execution environments:'
ms.assetid: 'DF6CDEE1-CAAA-429C-9939-DDC844302027'
title: Trusted Execution Functions
---

# Trusted Execution Functions

The following functions are used when working with enclaves that are used to create trusted execution environments:

## In this section



| Topic                                                                               | Description                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallEnclave**](callenclave.md)<br/>                                       | Calls a function within an enclave. <br/>                                                                                                                                                                                |
| [**CreateEnclave**](createenclave.md)<br/>                                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave.<br/> |
| [**DeleteEnclave**](deleteenclave.md)<br/>                                   | Deletes the specified enclave.<br/>                                                                                                                                                                                      |
| [**EnclaveGetAttestationReport**](enclavegetattestationreport.md)<br/>       | Gets an enclave attestation report that describes the current enclave and is signed by the authority that is responsible for the type of the enclave. <br/>                                                              |
| [**EnclaveGetEnclaveInformation**](enclavegetenclaveinformation.md)<br/>     | Gets information about the currently executing enclave.<br/>                                                                                                                                                             |
| [**EnclaveSealData**](enclavesealdata.md)<br/>                               | Generates an encrypted binary large object (blob) from unencypted data.<br/>                                                                                                                                             |
| [**EnclaveUnsealData**](enclaveunsealdata.md)<br/>                           | Decrypts an encrypted binary large object (blob).<br/>                                                                                                                                                                   |
| [**EnclaveVerifyAttestationReport**](enclaveverifyattestationreport.md)<br/> | Verifies an attestation report that was generated on the current system. <br/>                                                                                                                                           |
| [**InitializeEnclave**](initializeenclave.md)<br/>                           | Initializes an enclave that you created and loaded with data.<br/>                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](isenclavetypesupported.md)<br/>                 | Retrieves whether the specified type of enclave is supported.<br/>                                                                                                                                                       |
| [**LoadEnclaveData**](loadenclavedata.md)<br/>                               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](createenclave.md).<br/>                                                                                                        |
| [**LoadEnclaveImage**](loadenclaveimage.md)<br/>                             | Loads an image and all of its imports into an enclave.<br/>                                                                                                                                                              |
| [**TerminateEnclave**](terminateenclave.md)<br/>                             | Ends the execution of the threads that are running within an enclave.<br/>                                                                                                                                               |



 

 

 




