---
description: Learn to implement the end-to-end workflow for creating and verifying digital signatures using the ML-DSA algorithm with Microsoft's CNG API.
title: Using ML-DSA with CNG for Digital Signatures
ms.topic: how-to
ms.date: 05/15/2025
# Customer intent: As a Windows developer, I want to understand how to implement the ML-DSA algorithm for digital signatures using CNG.
---

# Using ML-DSA with CNG

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This article provides a guide to implementing the end-to-end workflow for creating and verifying digital signatures using the ML-DSA algorithm with Microsoft's CNG API.

## Sample ML-DSA code using Bcrypt

Learn how to use the ML-DSA algorithm with Microsoft's CNG API for digital signatures. The Bcrypt sample includes functions for signing a message and verifying the signature, as well as exporting the public key. The code is designed to be easy to follow and understand, making it suitable for developers looking to implement post-quantum digital signatures in their applications.

### Signature Generation and Verification with ML-DSA 

This code sample demonstrates the end-to-end workflow for creating and verifying digital signatures using the ML-DSA algorithm with Microsoft's CNG API. It highlights the importance of matching context during signing and verification, as well as careful management of cryptographic handles and memory. Post-quantum digital signature algorithms are equivalent at a high level to the existing digital signature algorithms we use today (RSA-PSS, ECDSA, etc.), where one party generates a public/private key-pair and signs a message (or its hash value) with the private key to produce a signature. The signature can be verified by anyone who has the associated public key. One difference is that PQ digital signature algorithms support pre-hash variants, which hash then sign data similar to traditional signature algorithms, as well as pure variants, which sign any input data of arbitrary length. This example uses the pure ML-DSA variant and describes how to use pre-hash ML-DSA. By following these steps, developers can implement secure, post-quantum digital signatures in their applications. 

### Set up algorithm handles and key pairs

You will follow these steps to set up the algorithm handles and key pairs for ML-DSA:

1. Use [BCryptOpenAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) for the ML-DSA algorithm, choosing either the default Microsoft primitive provider or another HSM provider. This step sets up the cryptographic context for subsequent operations.

   ```cpp
   status = BCryptOpenAlgorithmProvider(
       &hAlg,
       BCRYPT_MLDSA_ALGORITHM,
       MS_PRIMITIVE_PROVIDER,
       NULL);
    
   if (!NT_SUCCESS(status)) {
       goto cleanup;
   }
   ```

1. Use [BCryptGenerateKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair) to create private and public keys for the chosen algorithm.

   ```cpp
   status = BCryptGenerateKeyPair(hAlg, &hKeyPair, 0, NULL);

   if (!NT_SUCCESS(status)) {
       goto cleanup;
   }
   ```

   The parameters are as follows:

   - *hAlg*: The handle for the algorithm provider, which was obtained from BCryptOpenAlgorithmProvider.
   - *hKeyPair*: The handle for the key pair. 
   - `0`: Indicates the default key size for ML-DSA. 
   - `NULL`: No flags are set for this operation.

1. Use [BCryptSetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetproperty) to specify the parameter set to use for ML-DSA, which have tradeoffs for strength and performance. In this example the ML-DSA 44 parameter set it chosen, and other options are ML-DSA 65 and ML-DSA 87.

   ```cpp
   status = BCryptSetProperty(&hKeyPair, BCRYPT_PARAMETER_SET_NAME, (PUCHAR)BCRYPT_MLDSA_PARAMETER_SET_44, sizeof(BCRYPT_MLDSA_PARAMETER_SET_44), 0); 

   if (!NT_SUCCESS(status)) { 
       goto cleanup; 
   }
   ```

   Setting **BCRYPT_PARAMETER_SET_NAME** indicates which parameter set to use (e.g., MLDSA-44). 

1. Use [BCryptFinalizeKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair) so the public and private key are ready to be used.

   ```cpp
   status = BCryptFinalizeKeyPair(hKeyPair, NULL); 
   if (!NT_SUCCESS(status)) { 
       goto cleanup; 
   }

   // Public/Private key pair is generated at this point 
   ```

### Sign the message 

To sign a message with the generated key pair, the code uses [BCryptSignHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsignhash).

1. The code first determines the buffer size needed for the signature by calling **BCryptSignHash** with `NULL` output. It then allocates memory for the signature.

   ```cpp
    // Get the signature size
   status = BCryptSignHash(hKeyPair, NULL, NULL, 0, NULL, 0, &cbSignature, NULL);

   if (!NT_SUCCESS(status)) {
       goto cleanup;
   }

   pbSignature = (PBYTE)LocalAlloc(LMEM_FIXED, cbSignature);

   if (pbSignature == NULL) {
   status = STATUS_NO_MEMORY;
       goto cleanup;
   }
   ```

1. Next, it configures a **BCRYPT_PQDSA_PADDING_INFO** structure:

   ```cpp
   // Sign with pure ML-DSA
   //
   // Pure variants sign arbitrary length messages whereas
   // the pre-hash variants sign a hash value of the input.
   // To sign with pure ML-DSA or pure SLH-DSA, pszPrehashAlgId must be set
   // to NULL if BCRYPT_PQDSA_PADDING_INFO is provided to the sign/verify
   // functions.
    
   // For pre-hash signing, the hash algorithm used in creating
   // the hash of the input must be specified using the pszPrehashAlgId
   // field of BCRYPT_PQDSA_PADDING_INFO. This hash algorithm information
   // is required in generating and verifying the signature as the OID of
   // the hash algorithm becomes a prefix of the input to be signed.
   //
    
   padinfo.pbCtx = (PUCHAR)ctx;
   padinfo.cbCtx = sizeof(ctx);
   padinfo.pszPrehashAlgId = NULL;
   ```

   The **BCRYPT_PQDSA_PADDING_INFO** structure contains the following fields:

   - *pbCtx* and *cbCtx*: A pointer and size for an optional context string (additional authenticated data).
   - *pszPrehashAlgId*: Set to `NULL` for "pure" signing (the message is signed directly, not a hash).

1. Finally, the actual signature is generated with another call to [BCryptSignHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsignhash). The key handle, padding info, message, and allocated signature buffer are passed to the call. The **BCRYPT_PAD_PQDSA** flag specifies PQDSA padding.

   ```cpp
   status = BCryptSignHash(
       hKeyPair,
       &padinfo,
       (PUCHAR)msg,
       sizeof(msg),
       pbSignature,
       cbSignature,
       &cbWritten,
       BCRYPT_PAD_PQDSA); 
    
   if (!NT_SUCCESS(status)) {
       goto cleanup;
   } 
   ```

### Export the public key 

In this section, the public key is exported so others can verify the signatures.

1. [BCryptExportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) is first called with `NULL` parameters and the **BCRYPT_PQDSA_PUBLIC_BLOB** format to get the required buffer size:

   ```cpp
   // Get the public key blob size
   status = BCryptExportKey(
       hKeyPair,
       NULL,
       BCRYPT_PQDSA_PUBLIC_BLOB,
       NULL,
       0,
       &cbPublicKeyBlob,
       NULL);
    
   if (!NT_SUCCESS(status)) {
       goto cleanup;
   }
   ```

1. The buffer is allocatied and **BCryptExportKey** is called again to export the public key:

   ```cpp
   pbPublicKeyBlob = (PBYTE)LocalAlloc(LMEM_FIXED, cbPublicKeyBlob);
    
   if (pbPublicKeyBlob == NULL) {
   status = STATUS_NO_MEMORY;
       goto cleanup;
   }
    
   // Export the public key
   status = BCryptExportKey(
       hKeyPair,
       NULL,
       BCRYPT_PQDSA_PUBLIC_BLOB,
       pbPublicKeyBlob,
       cbPublicKeyBlob,
       &cbWritten,
       NULL);
    
   if (!NT_SUCCESS(status)) {
       goto cleanup;
   }
   ```

The exported key is in the **BCRYPT_PQDSA_PUBLIC_BLOB** format. 

### Clean up resources

In the clean up step, allocated resources such as buffers and handles are released, ensuring no memory leaks or dangling handles.

```cpp
cleanup: 

if (pbPublicKeyBlob)
{
    LocalFree(pbPublicKeyBlob);
}

if (pbSignature)
{
    LocalFree(pbSignature);
} 

if (hKeyPair != NULL)
{
    BCryptDestroyKey(hKeyPair);
}

if (hAlg != NULL)
{
    BCryptCloseAlgorithmProvider(hAlg, NULL);
}
```

### Verify the signature 

To verify a signature, the code uses [BCryptVerifySignature](/windows/win32/api/bcrypt/nf-bcrypt-bcryptverifysignature).

1. The **MLDSAVerifySample** function in the sample code below receives the exported public key blob, the message, context, and the signature. 
1. [BCryptImportKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkeypair) imports the public key blob to create a key handle usable by the API. 
1. Again, **BCRYPT_PQDSA_PADDING_INFO** is prepared with the context (it should match the one used during signing). The following fields are set:
   - *pbCtx*/*cbCtx* (Context): Used to supply additional data, which can help bind signatures to a specific application or use case. Both signing and verifying must use the same context.
   - *pszPrehashAlgId*: Set to `NULL` for "pure" ML-DSA. For pre-hash variants, it specifies the hash algorithm ID.
   - **BCRYPT_PAD_PQDSA**: Specifies the use of PQDSA padding for post-quantum security.
1. [BCryptVerifySignature](/windows/win32/api/bcrypt/nf-bcrypt-bcryptverifysignature) is called with the key handle, padding info, the original message, and the signature. If the function returns success, the signature is valid; otherwise, it is not. 

The steps above are annotated in the code sample below:

```cpp
//
// This function takes as input an ML-DSA-44 public key blob,
// and a signature generated by the same algorithm along with
// the message the signature belongs to. It verifies whether the
// signature is valid or not.
//
// STEP 1: Receive the public key blob, message, context, and signature
NTSTATUS MLDSAVerifySample(
    PCBYTE pbPublicKeyBlob,
    ULONG cbPublicKeyBlob,
    PCBYTE pbMsg,
    ULONG cbMsg,
    PCBYTE pbContext,
    ULONG cbContext,
    PCBYTE pbSignature,
    ULONG cbSignature)
{
    NTSTATUS status = STATUS_SUCCESS;
    BCRYPT_ALG_HANDLE hAlg = NULL;
    BCRYPT_KEY_HANDLE hKey = NULL;
    BCRYPT_PQDSA_PADDING_INFO padinfo = { 0 };

    status = BCryptOpenAlgorithmProvider(
        &hAlg,
        BCRYPT_MLDSA_ALGORITHM,
        MS_PRIMITIVE_PROVIDER,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    // STEP 2: Import the public key
    // Import the public key
    status = BCryptImportKeyPair(
        hAlg,
        NULL,
        BCRYPT_PQDSA_PUBLIC_BLOB,
        &hKey,
        (PUCHAR)pbPublicKeyBlob,
        cbPublicKeyBlob,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    // STEP 3: Prepare the padding info
    // Verify the signature
    // Assuming the signature is generated with pure ML-DSA.
    // Otherwise pszPrehashAlgId must be set to the identifier
    // of the hash algorithm used in pre-hashing the input.
    padinfo.pbCtx = (PUCHAR)pbContext;
    padinfo.cbCtx = cbContext;
    padinfo.pszPrehashAlgId = NULL;

    // STEP 4: Verify the signature
    status = BCryptVerifySignature(
        hKey,
        &padinfo,
        (PUCHAR)pbMsg,      // pbHash
        cbMsg,              // cbHash
        (PUCHAR)pbSignature,
        cbSignature,
        BCRYPT_PAD_PQDSA);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

cleanup:

    if (hKey != NULL)
    {
        BCryptDestroyKey(hKey);
    }

    if (hAlg != NULL)
    {
        BCryptCloseAlgorithmProvider(hAlg, NULL);
    }

    return status;
}
```

In the `cleanup:` block, the code uses [BCryptDestroyKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroykey) to delete the key handle from memory and [BCryptCloseAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptclosealgorithmprovider) to delete the algorithm handle from memory. 

### Review the full code sample

The following code sample demonstrates the complete process of generating and verifying a digital signature using the ML-DSA algorithm with Microsoft's CNG API:

```cpp
//
// Sample ML-DSA code
//
// This function creates an ML-DSA-44 private key, signs
// a message with it, and exports the public-key. The receiver
// can use the public key, message, and the signature to verify
// that they are generated by the same party who owns the private key.
//
#define SAMPLE_MESSAGE "message"
#define SAMPLE_CONTEXT "context"

NTSTATUS MLDSASignSample()
{
    NTSTATUS status = STATUS_SUCCESS;
    BCRYPT_ALG_HANDLE hAlg = NULL;
    BCRYPT_KEY_HANDLE hKeyPair = NULL;
    BCRYPT_PQDSA_PADDING_INFO padinfo = { 0 };
    PBYTE pbSignature = NULL;
    ULONG cbSignature, cbWritten;
    const BYTE msg[] = SAMPLE_MESSAGE;
    const BYTE ctx[] = SAMPLE_CONTEXT;
    PBYTE pbPublicKeyBlob = NULL;
    ULONG cbPublicKeyBlob;

    status = BCryptOpenAlgorithmProvider(
        &hAlg,
        BCRYPT_MLDSA_ALGORITHM,
        MS_PRIMITIVE_PROVIDER,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    status = BCryptGenerateKeyPair(hAlg, &hKeyPair, 0, NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    status = BCryptSetProperty(&hKeyPair, BCRYPT_PARAMETER_SET_NAME, (PUCHAR)BCRYPT_MLDSA_PARAMETER_SET_44, sizeof(BCRYPT_MLDSA_PARAMETER_SET_44), 0);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    status = BCryptFinalizeKeyPair(hKeyPair, NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    // Public/Private key pair is generated at this point

    // Get the signature size
    status = BCryptSignHash(hKeyPair, NULL, NULL, 0, NULL, 0, &cbSignature, NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    pbSignature = (PBYTE)LocalAlloc(LMEM_FIXED, cbSignature);

    if (pbSignature == NULL) {
  status = STATUS_NO_MEMORY;
        goto cleanup;
    }

    //
    // Sign with pure ML-DSA
    //
    // Pure variants sign arbitrary length messages whereas
    // the pre-hash variants sign a hash value of the input.
    // To sign with pure ML-DSA or pure SLH-DSA, pszPrehashAlgId must be set
    // to NULL if BCRYPT_PQDSA_PADDING_INFO is provided to the sign/verify
    // functions.

    // For pre-hash signing, the hash algorithm used in creating
    // the hash of the input must be specified using the pszPrehashAlgId
    // field of BCRYPT_PQDSA_PADDING_INFO. This hash algorithm information
    // is required in generating and verifying the signature as the OID of
    // the hash algorithm becomes a prefix of the input to be signed.
    //

    padinfo.pbCtx = (PUCHAR)ctx;
    padinfo.cbCtx = sizeof(ctx);
    padinfo.pszPrehashAlgId = NULL;

    status = BCryptSignHash(
        hKeyPair,
        &padinfo,
        (PUCHAR)msg,
        sizeof(msg),
        pbSignature,
        cbSignature,
        &cbWritten, 
        BCRYPT_PAD_PQDSA);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    //
    // Export the public key
    //

    // Get the public key blob size
    status = BCryptExportKey(
        hKeyPair,
        NULL,
        BCRYPT_PQDSA_PUBLIC_BLOB,
        NULL,
        0,
        &cbPublicKeyBlob,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    pbPublicKeyBlob = (PBYTE)LocalAlloc(LMEM_FIXED, cbPublicKeyBlob);

    if (pbPublicKeyBlob == NULL) {
  status = STATUS_NO_MEMORY;
        goto cleanup;
    }

    // Export the public key
    status = BCryptExportKey(
        hKeyPair,
        NULL,
        BCRYPT_PQDSA_PUBLIC_BLOB,
        pbPublicKeyBlob,
        cbPublicKeyBlob,
        &cbWritten,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

cleanup:

    if (pbPublicKeyBlob)
    {
        LocalFree(pbPublicKeyBlob);
    }

    if (pbSignature)
    {
        LocalFree(pbSignature);
    }

    if (hKeyPair != NULL)
    {
        BCryptDestroyKey(hKeyPair);
    }

    if (hAlg != NULL)
    {
        BCryptCloseAlgorithmProvider(hAlg, NULL);
    }

    return status;
}

//
// This function takes as input an ML-DSA-44 public key blob,
// and a signature generated by the same algorithm along with
// the message the signature belongs to. It verifies whether the
// signature is valid or not.
//
NTSTATUS MLDSAVerifySample(
    PCBYTE pbPublicKeyBlob,
    ULONG cbPublicKeyBlob,
    PCBYTE pbMsg,
    ULONG cbMsg,
    PCBYTE pbContext,
    ULONG cbContext,
    PCBYTE pbSignature,
    ULONG cbSignature)
{
    NTSTATUS status = STATUS_SUCCESS;
    BCRYPT_ALG_HANDLE hAlg = NULL;
    BCRYPT_KEY_HANDLE hKey = NULL;
    BCRYPT_PQDSA_PADDING_INFO padinfo = { 0 };

    status = BCryptOpenAlgorithmProvider(
        &hAlg,
        BCRYPT_MLDSA_ALGORITHM,
        MS_PRIMITIVE_PROVIDER,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    // Import the public key
    status = BCryptImportKeyPair(
        hAlg,
        NULL,
        BCRYPT_PQDSA_PUBLIC_BLOB,
        &hKey,
        (PUCHAR)pbPublicKeyBlob,
        cbPublicKeyBlob,
        NULL);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

    // Verify the signature
    // Assuming the signature is generated with pure ML-DSA.
    // Otherwise pszPrehashAlgId must be set to the identifier
    // of the hash algorithm used in pre-hashing the input.
    padinfo.pbCtx = (PUCHAR)pbContext;
    padinfo.cbCtx = cbContext;
    padinfo.pszPrehashAlgId = NULL;

    status = BCryptVerifySignature(
        hKey,
        &padinfo,
        (PUCHAR)pbMsg,      // pbHash
        cbMsg,              // cbHash
        (PUCHAR)pbSignature,
        cbSignature,
        BCRYPT_PAD_PQDSA);

    if (!NT_SUCCESS(status)) {
        goto cleanup;
    }

cleanup:

    if (hKey != NULL)
    {
        BCryptDestroyKey(hKey);
    }

    if (hAlg != NULL)
    {
        BCryptCloseAlgorithmProvider(hAlg, NULL);
    }

    return status;
}
```

## Related content

- [Using ML-KEM with CNG](cng-mlkem-examples.md)
- [Overview of typical CNG programming](typical-cng-programming.md)
- [CNG Key Storage Functions](cng-key-storage-functions.md)
