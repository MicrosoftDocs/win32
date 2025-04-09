---
description: Enclaves are used to create trusted execution environments. These Bcrypt APIs are available to developers in VBS enclaves.
ms.assetid: 11903971-331b-4184-a7f9-635414f62243
title: Bcrypt APIs available in VBS enclaves
titleSuffix: Secure Enclaves
ms.topic: reference
ms.date: 11/20/2024
---

# Bcrypt APIs available in VBS enclaves

[!INCLUDE [enclaves-os-reqs.md](../includes/enclaves-os-reqs.md)]

Enclaves are used to create trusted execution environments. These Bcrypt APIs are available to developers in VBS enclaves.

## List of Bcrypt.h APIs

The following APIs in the [bcrypt.h](/windows/win32/api/bcrypt/) header file are available to be called in VBS enclaves.

| API | Description |
|--------|--------|
| [BCRYPT_INIT_AUTH_MODE_INFO](/windows/win32/api/bcrypt/nf-bcrypt-bcrypt_init_auth_mode_info) | Initializes a **BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO** structure for use in calls to **BCryptEncrypt** and **BCryptDecrypt** functions. |
| [BCryptAddContextFunction](/windows/win32/api/bcrypt/nf-bcrypt-bcryptaddcontextfunction) | Adds a cryptographic function to the list of functions that are supported by an existing CNG context. |
| [BCryptCloseAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptclosealgorithmprovider) | Closes an algorithm provider. |
| [BCryptConfigureContext](/windows/win32/api/bcrypt/nf-bcrypt-bcryptconfigurecontext) | Sets the configuration information for an existing CNG context. |
| [BCryptConfigureContextFunction](/windows/win32/api/bcrypt/nf-bcrypt-bcryptconfigurecontextfunction) | Sets the configuration information for the cryptographic function of an existing CNG context. |
| [BCryptCreateContext](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatecontext) | Creates a new CNG configuration context. |
| [BCryptCreateHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatehash) | Called to create a hash or Message Authentication Code (MAC) object. |
| [BCryptCreateMultiHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatemultihash) | Creates a multi-hash state that allows for the parallel computation of multiple hash operations. |
| [BCryptDecrypt](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdecrypt) | Decrypts a block of data. |
| [BCryptDeleteContext](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdeletecontext) | Deletes an existing CNG configuration context. |
| [BCryptDeriveKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekey) | Derives a key from a secret agreement value. |
| [BCryptDeriveKeyCapi](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeycapi) | Derives a key from a hash value. |
| [BCryptDeriveKeyPBKDF2](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeypbkdf2) | Derives a key from a hash value by using the PBKDF2 key derivation algorithm as defined by RFC 2898. |
| [BCryptDestroyHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroyhash) | Destroys a hash or Message Authentication Code (MAC) object. |
| [BCryptDestroyKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroykey) | Destroys a key. |
| [BCryptDestroySecret](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroysecret) | Destroys a secret agreement handle that was created by using the **BCryptSecretAgreement** function. |
| [BCryptDuplicateHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptduplicatehash) | Duplicates an existing hash or Message Authentication Code (MAC) object. |
| [BCryptDuplicateKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptduplicatekey) | Creates a duplicate of a symmetric key. |
| [BCryptEncrypt](/windows/win32/api/bcrypt/nf-bcrypt-bcryptencrypt) | Encrypts a block of data. |
| [BCryptEnumAlgorithms](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumalgorithms) | Gets a list of the registered algorithm identifiers. |
| [BCryptEnumContextFunctionProviders](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumcontextfunctionproviders) | Obtains the providers for the cryptographic functions for a context in the specified configuration table. |
| [BCryptEnumContextFunctions](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumcontextfunctions) | Obtains the cryptographic functions for a context in the specified configuration table. |
| [BCryptEnumContexts](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumcontexts) | Obtains the identifiers of the contexts in the specified configuration table. |
| [BCryptEnumProviders](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumproviders) | Obtains all of the CNG providers that support a specified algorithm. |
| [BCryptEnumRegisteredProviders](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumregisteredproviders) | Retrieves information about the registered providers. |
| [BCryptExportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) | Exports a key to a memory BLOB that can be persisted for later use. |
| [BCryptFinalizeKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair) | Completes a public/private key pair. |
| [BCryptFinishHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinishhash) | Retrieves the hash or Message Authentication Code (MAC) value for the data accumulated from prior calls to **BCryptHashData**. |
| [BCryptFreeBuffer](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfreebuffer) | Used to free memory that was allocated by one of the CNG functions. |
| [BCryptGenerateKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair) | Creates an empty public/private key pair. |
| [BCryptGenerateSymmetricKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratesymmetrickey) | Creates a key object for use with a symmetrical key encryption algorithm from a supplied key. |
| [BCryptGenRandom](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) | Generates a random number. |
| [BCryptGetFipsAlgorithmMode](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetfipsalgorithmmode) | Determines whether Federal Information Processing Standard (FIPS) compliance is enabled. |
| [BCryptGetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetproperty) | Retrieves the value of a named property for a CNG object. |
| [BCryptHash](/windows/win32/api/bcrypt/nf-bcrypt-bcrypthash) | Performs a single hash computation. This is a convenience function that wraps calls to **BCryptCreateHash**, **BCryptHashData**, **BCryptFinishHash**, and **BCryptDestroyHash**. |
| [BCryptHashData](/windows/win32/api/bcrypt/nf-bcrypt-bcrypthashdata) | Performs a one way hash or Message Authentication Code (MAC) on a data buffer. |
| [BCryptImportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkey) | Imports a symmetric key from a key BLOB. |
| [BCryptImportKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkeypair) | Imports a public/private key pair from a key BLOB. |
| [BCryptKeyDerivation](/windows/win32/api/bcrypt/nf-bcrypt-bcryptkeyderivation) | Derives a key without requiring a secret agreement. |
| [BCryptOpenAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) | Loads and initializes a CNG provider. |
| [BCryptProcessMultiOperations](/windows/win32/api/bcrypt/nf-bcrypt-bcryptprocessmultioperations) | Processes a sequence of operations on a multi-object state. |
| [BCryptQueryContextConfiguration](/windows/win32/api/bcrypt/nf-bcrypt-bcryptquerycontextconfiguration) | Retrieves the current configuration for the specified CNG context. |
| [BCryptQueryContextFunctionConfiguration](/windows/win32/api/bcrypt/nf-bcrypt-bcryptquerycontextfunctionconfiguration) | Obtains the cryptographic function configuration information for an existing CNG context. |
| [BCryptQueryContextFunctionProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptquerycontextfunctionproperty) | Obtains the value of a named property for a cryptographic function in an existing CNG context. |
| [BCryptQueryProviderRegistration](/windows/win32/api/bcrypt/nf-bcrypt-bcryptqueryproviderregistration) | Retrieves information about a CNG provider. |
| [BCryptRegisterConfigChangeNotify](/windows/win32/api/bcrypt/nf-bcrypt-bcryptregisterconfigchangenotify) | Creates a user mode CNG configuration change event handler. |
| [BCryptRegisterConfigChangeNotify](/windows/win32/api/bcrypt/nf-bcrypt-bcryptregisterconfigchangenotify-r1) | Describes how the **BCryptRegisterConfigChangeNotify(PRKEVENT)** function creates kernel mode CNG configuration change event handler. |
| [BCryptRemoveContextFunction](/windows/win32/api/bcrypt/nf-bcrypt-bcryptremovecontextfunction) | Removes a cryptographic function from the list of functions that are supported by an existing CNG context. |
| [BCryptResolveProviders](/windows/win32/api/bcrypt/nf-bcrypt-bcryptresolveproviders) | Obtains a collection of all of the providers that meet the specified criteria. |
| [BCryptSecretAgreement](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsecretagreement) | Creates a secret agreement value from a private and a public key. |
| [BCryptSetContextFunctionProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetcontextfunctionproperty) | Sets the value of a named property for a cryptographic function in an existing CNG context. |
| [BCryptSetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetproperty) | Sets the value of a named property for a CNG object. |
| [BCryptSignHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsignhash) | Creates a signature of a hash value. |
| [BCryptUnregisterConfigChangeNotify](/windows/win32/api/bcrypt/nf-bcrypt-bcryptunregisterconfigchangenotify) | Removes a user mode CNG configuration change event handler that was created by using the **BCryptRegisterConfigChangeNotify(HANDLE\*)** function. |
| [BCryptUnregisterConfigChangeNotify](/windows/win32/api/bcrypt/nf-bcrypt-bcryptunregisterconfigchangenotify-r1) | Removes a user mode CNG configuration change event handler that was created by using the **BCryptRegisterConfigChangeNotify(HANDLE\*)** function. |
| [BCryptVerifySignature](/windows/win32/api/bcrypt/nf-bcrypt-bcryptverifysignature) | Verifies that the specified signature matches the specified hash. |

## See also

- [Secure Enclaves (Trusted Execution)](enclaves.md)
- [UCRT APIs Available in VBS Enclaves](enclaves-available-in-ucrt.md)
- [Vertdll APIs Available in VBS Enclaves](enclaves-available-in-vertdll.md)
- [libvcruntime APIs Available in VBS Enclaves](enclaves-available-in-libvcruntime.md)
