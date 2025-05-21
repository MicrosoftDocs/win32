---
description: Learn to implement the end-to-end workflow for creating and verifying digital signatures using the Module-Lattice Key Encapsulation Mechanism (ML-KEM) algorithm with Microsoft's CNG API.
title: Using ML-KEM with CNG for Digital Signatures
ms.topic: how-to
ms.date: 05/16/2025
# Customer intent: As a Windows developer, I want to understand how to implement the ML-KEM algorithm for digital signatures using CNG.
---

# Using ML-KEM with CNG

> [!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this topic is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This article provides a guide to implementing the end-to-end workflow for performing a key exchange using the Module-Lattice Key Encapsulation Mechanism (ML-KEM) algorithm with Microsoft's CNG API.

## Sample ML-KEM Key Encapsulation and Decapsulation code using Bcrypt

ML-KEM is a post-quantum algorithm used for key exchange, and is standardized in FIPS 203. Key exchange is an important part of security protocols such as TLS, whereby a client and a server negotiate a connection and create and share key material to encrypt and decrypt messages sent over the internet. In KEM, the keys produced in key-pair generation process are called Encapsulation Key and Decapsulation Key. Encapsulation Key is public and can be used by anyone to perform a Key Encapsulation operation which produces a secret key (for the party who performs this operation) and a ciphertext. The ciphertext is provided as an input to the Key Decapsulation operation by the private key owner to recover the same shared secret key the encapsulating party has obtained during the Key Encapsulation process. This example demonstrates how a hypothetical TLS client and server application would consume the new ML-KEM APIs in Bcrypt to perform a key exchange.

### Setup and Key Pair Generation

The following steps outline the process of setting up the ML-KEM key pair generation and encapsulation:

1. Use [BCryptGenerateKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair) with **BCRYPT_MLKEM_ALG_HANDLE** to create a new key pair for key encapsulation. The length and flags fields are both `0`, since the key lengths are defined by the ML-KEM parameter set.

   ```cpp
   // Generate the key pair for key exchange
   unique_bcrypt_key hKeyPair;
   THROW_IF_NTSTATUS_FAILED(
      BCryptGenerateKeyPair(
        BCRYPT_MLKEM_ALG_HANDLE,
        &hKeyPair,
        0, // dwLength
        0)); // dwFlags
   ```

1. Call [BCryptSetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetproperty) on the key pair to set the **BCRYPT_PARAMETER_SET_NAME** to **BCRYPT_MLKEM_PARAMETER_SET_768**, specifying the parameter set for the ML-KEM operation. ML-KEM also supports the 512 and 1024 parameter sets defined by NIST.

   ```cpp
   THROW_IF_NTSTATUS_FAILED(
      BCryptSetProperty(
          &hKeyPair,
          BCRYPT_PARAMETER_SET_NAME,
         (PUCHAR) BCRYPT_MLKEM_PARAMETER_SET_768,
          sizeof(BCRYPT_MLKEM_PARAMETER_SET_768),
          0)); // dwFlags
   ```

1. Call [BCryptFinalizeKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair) to make the key pair ready for use in subsequent operations.

   ```cpp
   THROW_IF_NTSTATUS_FAILED(
       BCryptFinalizeKeyPair(
           hKeyPair.get(),
           0)); // dwFlags
   ```

### Public Key Export and Exchange

1. Call [BCryptExportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) with a `NULL` output buffer to query the required size for exporting the **BCRYPT_MLKEM_ENCAPSULATION_BLOB**.

   ```cpp
   ULONG cbEncapsulationKeyBlob = 0;

   THROW_IF_NTSTATUS_FAILED(
       BCryptExportKey(
           hKeyPair.get(),
           NULL,
           BCRYPT_MLKEM_ENCAPSULATION_BLOB,
           NULL, // pbOutput
           0, // cbOutput
           &cbEncapsulationKeyBlob,
           0)); // dwFlags
   ```

1. Allocate a buffer based on the previously retrieved size, then export the encapsulation (public) key using **BCryptExportKey**. This blob will be sent to the key exchange partner (e.g., the server in a client-server scenario). 

   ```cpp
   vector<BYTE> encapsulationKeyBlob(cbEncapsulationKeyBlob);
   THROW_IF_NTSTATUS_FAILED(
       BCryptExportKey(
           hKeyPair.get(),
           NULL,
           BCRYPT_MLKEM_ENCAPSULATION_BLOB,
           encapsulationKeyBlob.data(),
           static_cast<ULONG>(encapsulationKeyBlob.size()),
           &cbEncapsulationKeyBlob,
           0));
   ```

1. Ensure the **BCRYPT_MLKEM_KEY_BLOB** has the correct public magic and 768 parameter set. 

   ```cpp
   BCRYPT_MLKEM_KEY_BLOB* pEncapsulationKeyBlob = 
       reinterpret_cast<BCRYPT_MLKEM_KEY_BLOB *>(encapsulationKeyBlob.data());
   ASSERT(pEncapsulationKeyBlob->dwMagic == BCRYPT_MLKEM_PUBLIC_MAGIC);
   ASSERT(pEncapsulationKeyBlob->cbParameterSet == sizeof(BCRYPT_MLKEM_PARAMETER_SET_768));

   if (wcscmp(BCRYPT_MLKEM_PARAMETER_SET_768, reinterpret_cast<WCHAR *>(pEncapsulationKeyBlob + 1)) != 0)
   {
       return;
   }
   ```

1. Send the encapsulation key to the server in the client key exchange message. 

   ```cpp
   PBYTE pbEncapsulationKey = reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768);
   ULONG cbEncapsulationKey = pEncapsulationKeyBlob->cbKey;
   SendToServer(pbEncapsulationKey, cbEncapsulationKey);
   ```

### Encapsulation and Decapsulation

The following steps outline the process of encapsulating and decapsulating the shared secret key:

1. The server receives the client’s key exchange message and retrieves the bytes of the encapsulation key. 

   ```cpp
   // Server receives the client's key_exchange message and retrieves the
   // encapsulation key bytes.
   vector<BYTE> encapsulationKey = GetClientKeyExchange();
   ULONG cbEncapsulationKey = static_cast<ULONG>(encapsulationKey.size());
   ```

1. The server puts the key into a **BCRYPT_KEY_BLOB** using the 768 parameter set and public magic, and imports the encapsulation key. 

   ```cpp
   // Put the Key in a BCRYPT_KEY_BLOB and import it.
   ULONG cbEncapsulationKeyBlob = sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768) + cbEncapsulationKey;
   vector<BYTE> encapsulationKeyBlob(cbEncapsulationKeyBlob);
   BCRYPT_MLKEM_KEY_BLOB* pEncapsulationKeyBlob = 
       reinterpret_cast<BCRYPT_MLKEM_KEY_BLOB *>(encapsulationKeyBlob.data());
   pEncapsulationKeyBlob->dwMagic = BCRYPT_MLKEM_PUBLIC_MAGIC;
   pEncapsulationKeyBlob->cbParameterSet = sizeof(BCRYPT_MLKEM_PARAMETER_SET_768);
   pEncapsulationKeyBlob->cbKey = cbEncapsulationKey;

   CopyMemory(
       reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB),
       BCRYPT_MLKEM_PARAMETER_SET_768,
       sizeof(BCRYPT_MLKEM_PARAMETER_SET_768));

   CopyMemory(
       reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768),
       encapsulationKey.data(),
       encapsulationKey.size());

   unique_bcrypt_key hKeyPair;

   // The server knows the ML-KEM parameter set from the client's
   // key_exchange, which denotes the parameter set associated with the
   // encapsulation key it sent. In this case, we know it's
   // BCRYPT_MLKEM_PARAMETER_SET_768.
   THROW_IF_NTSTATUS_FAILED(
       BCryptImportKeyPair(
           BCRYPT_MLKEM_ALG_HANDLE,
           NULL, // hImportKey
           BCRYPT_MLKEM_ENCAPSULATION_BLOB,
           &hKeyPair,
           encapsulationKeyBlob.data(),
           static_cast<ULONG>(encapsulationKeyBlob.size()),
           0)); // dwFlags

   // Get the secret key length and ciphertext length. These values are static
   // and can be cached for the algorithm handle.
   ULONG cbSecretKey = 0;
   ULONG cbProperty = sizeof(cbSecretKey);
   ```

1. The server uses [BCryptGetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetproperty) to get the secret key length and ciphertext length and allocate the required buffers for both. 

   ```cpp
   THROW_IF_NTSTATUS_FAILED(
       BCryptGetProperty(
           &hKeyPair,
           BCRYPT_KEM_SHARED_SECRET_LENGTH,
           reinterpret_cast<PUCHAR>(&cbSecretKey),
           cbProperty,
           &cbProperty,
           0)); // dwFlags

   ULONG cbCipherText = 0; 
   cbProperty = sizeof(cbCipherText);

   THROW_IF_NTSTATUS_FAILED(
       BCryptGetProperty(
           &hKeyPair,
           BCRYPT_KEM_CIPHERTEXT_LENGTH,
           reinterpret_cast<PUCHAR>(&cbCipherText),
           cbProperty,
           &cbProperty,
           0)); // dwFlags

   // Then allocate the required buffers.
   vector<BYTE> secretKey(cbSecretKey);
   vector<BYTE> cipherText(cbCipherText);
   ```

1. The server performs [BCryptEncapsulate](./bcrypt/nf-bcrypt-bcryptencapsulate.md) and sends the ciphertext to the client in the server key exchange message. 

   ```cpp
   // Perform the encapsulate operation.
   THROW_IF_NTSTATUS_FAILED(
       BCryptEncapsulate(
           hKeyPair.get(),
           secretKey.data(),
           static_cast<ULONG>(secretKey.size()),
           &cbSecretKey,
           cipherText.data(),
           static_cast<ULONG>(cipherText.size()),
           &cbCipherText,
           0)); // dwFlags

   // cipherText is sent to the client in the server's key_exchange message.
   SendToClient(cipherText.data(), cipherText.size());
   ```

1. The client uses the received server key exchange to generate a ciphertext that encapsulates a shared secret. 

   ```cpp
   // pbEncapsulationKey is sent on the wire in the client's key_exchange
   // message.
   // ...
   // < It's now the server's turn. It will use the encapsulation key to
   // generate the a CipherText encapsulating the shared secret key and send
   // it as a response to the client's key_exchange message. Sample_Server()
   // demonstrates how a hypothetical server may do this.>
   // ...
   // When the ServerKeyExchange message is received from the TLS server,
   // get the ML-KEM CipherText from the ServerKeyExchange message.
   vector<BYTE> cipherText = GetServerKeyExchange(); 
   ```

1. The client calls [BCryptGetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetproperty) to get the secret key length and allocate the appropriate buffer.

   ```cpp
   // Get the secret key length. This value is static and can be cached for
   // the algorithm handle.
   ULONG cbSecretKey = 0;
   ULONG cbProperty = sizeof(cbSecretKey);
   THROW_IF_NTSTATUS_FAILED(
       BCryptGetProperty(
           &hKeyPair,
           BCRYPT_KEM_SHARED_SECRET_LENGTH,
           reinterpret_cast<PUCHAR>(&cbSecretKey),
           cbProperty,
           &cbProperty,
           0)); // dwFlags
   ```

1. The client constructs the shared secret key by creating a key blob and calling [BCryptDecapsulate](./bcrypt/nf-bcrypt-bcryptdecapsulate.md) with the cipher text and secret length. 

   ```cpp
   vector<BYTE> secretKey(cbSecretKey);

   THROW_IF_NTSTATUS_FAILED(
       BCryptDecapsulate(
           hKeyPair.get(),
           cipherText.data(),
           static_cast<ULONG>(cipherText.size()),
           secretKey.data(),
           static_cast<ULONG>(secretKey.size()),
           &cbSecretKey,
           0)); // dwFlags
   ```

### Deriving Session Keys 

Both client and server now have the same shared secret, which can be passed to a key derivation function such as **DeriveSessionKeys** to generate session keys for secure communication.

```cpp
    // secretKey contains the shared secret key which plugs into the TLS key
    // schedule.
    DeriveSessionKeys(secretKey);
```

### Review the full code sample

You can review the full code sample below:

```cpp
void Sample_Client()
{
    // Generate the key pair for key exchange
    unique_bcrypt_key hKeyPair;
    THROW_IF_NTSTATUS_FAILED(
        BCryptGenerateKeyPair(
            BCRYPT_MLKEM_ALG_HANDLE,
            &hKeyPair,
            0, // dwLength
            0)); // dwFlags

   THROW_IF_NTSTATUS_FAILED(
        BCryptSetProperty(
            &hKeyPair,
            BCRYPT_PARAMETER_SET_NAME,
            (PUCHAR) BCRYPT_MLKEM_PARAMETER_SET_768,
            sizeof(BCRYPT_MLKEM_PARAMETER_SET_768),
            0)); // dwFlags

    THROW_IF_NTSTATUS_FAILED(
        BCryptFinalizeKeyPair(
            hKeyPair.get(),
            0)); // dwFlags

    ULONG cbEncapsulationKeyBlob = 0;

    THROW_IF_NTSTATUS_FAILED(
        BCryptExportKey(
            hKeyPair.get(),
            NULL,
            BCRYPT_MLKEM_ENCAPSULATION_BLOB,
            NULL, // pbOutput
            0, // cbOutput
            &cbEncapsulationKeyBlob,
            0)); // dwFlags

    vector<BYTE> encapsulationKeyBlob(cbEncapsulationKeyBlob);
    THROW_IF_NTSTATUS_FAILED(
        BCryptExportKey(
            hKeyPair.get(),
            NULL,
            BCRYPT_MLKEM_ENCAPSULATION_BLOB,
            encapsulationKeyBlob.data(),
            static_cast<ULONG>(encapsulationKeyBlob.size()),
            &cbEncapsulationKeyBlob,
            0));

    BCRYPT_MLKEM_KEY_BLOB* pEncapsulationKeyBlob = 
        reinterpret_cast<BCRYPT_MLKEM_KEY_BLOB *>(encapsulationKeyBlob.data());
    ASSERT(pEncapsulationKeyBlob->dwMagic == BCRYPT_MLKEM_PUBLIC_MAGIC);
    ASSERT(pEncapsulationKeyBlob->cbParameterSet == sizeof(BCRYPT_MLKEM_PARAMETER_SET_768));

    if (wcscmp(BCRYPT_MLKEM_PARAMETER_SET_768, reinterpret_cast<WCHAR *>(pEncapsulationKeyBlob + 1)) != 0)
    {
        return;
    }

    PBYTE pbEncapsulationKey = reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768);
    ULONG cbEncapsulationKey = pEncapsulationKeyBlob->cbKey;
    SendToServer(pbEncapsulationKey, cbEncapsulationKey);

    // pbEncapsulationKey is sent on the wire in the client's key_exchange
    // message.
    // ...
    // < It's now the server's turn. It will use the encapsulation key to
    // generate the a CipherText encapsulating the shared secret key and send
    // it as a response to the client's key_exchange message. Sample_Server()
    // demonstrates how a hypothetical server may do this.>
    // ...
    // When the ServerKeyExchange message is received from the TLS server,
    // get the ML-KEM CipherText from the ServerKeyExchange message.
    vector<BYTE> cipherText = GetServerKeyExchange(); 

    // Get the secret key length. This value is static and can be cached for
    // the algorithm handle.
    ULONG cbSecretKey = 0;
    ULONG cbProperty = sizeof(cbSecretKey);
    THROW_IF_NTSTATUS_FAILED(
        BCryptGetProperty(
            &hKeyPair,
            BCRYPT_KEM_SHARED_SECRET_LENGTH,
            reinterpret_cast<PUCHAR>(&cbSecretKey),
            cbProperty,
            &cbProperty,
            0)); // dwFlags

    vector<BYTE> secretKey(cbSecretKey);

    THROW_IF_NTSTATUS_FAILED(
        BCryptDecapsulate(
            hKeyPair.get(),
            cipherText.data(),
            static_cast<ULONG>(cipherText.size()),
            secretKey.data(),
            static_cast<ULONG>(secretKey.size()),
            &cbSecretKey,
            0)); // dwFlags

    // secretKey is the shared secret key which plugs into the TLS key
    // schedule.
   DeriveSessionKeys(secretKey);
}

void Sample_Server()
{
    // Server receives the client's key_exchange message and retrieves the
    // encapsulation key bytes.
    vector<BYTE> encapsulationKey = GetClientKeyExchange();
    ULONG cbEncapsulationKey = static_cast<ULONG>(encapsulationKey.size());

    // Put the Key in a BCRYPT_KEY_BLOB and import it.
    ULONG cbEncapsulationKeyBlob = sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768) + cbEncapsulationKey;
    vector<BYTE> encapsulationKeyBlob(cbEncapsulationKeyBlob);
    BCRYPT_MLKEM_KEY_BLOB* pEncapsulationKeyBlob = 
        reinterpret_cast<BCRYPT_MLKEM_KEY_BLOB *>(encapsulationKeyBlob.data());
    pEncapsulationKeyBlob->dwMagic = BCRYPT_MLKEM_PUBLIC_MAGIC;
    pEncapsulationKeyBlob->cbParameterSet = sizeof(BCRYPT_MLKEM_PARAMETER_SET_768);
    pEncapsulationKeyBlob->cbKey = cbEncapsulationKey;

    CopyMemory(
        reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB),
        BCRYPT_MLKEM_PARAMETER_SET_768,
        sizeof(BCRYPT_MLKEM_PARAMETER_SET_768));

    CopyMemory(
        reinterpret_cast<PBYTE>(pEncapsulationKeyBlob) + sizeof(BCRYPT_MLKEM_KEY_BLOB) + sizeof(BCRYPT_MLKEM_PARAMETER_SET_768),
        encapsulationKey.data(),
        encapsulationKey.size());

    unique_bcrypt_key hKeyPair;

    // The server knows the ML-KEM parameter set from the client's
    // key_exchange, which denotes the parameter set associated with the
    // encapsulation key it sent. In this case, we know it's
    // BCRYPT_MLKEM_PARAMETER_SET_768.
    THROW_IF_NTSTATUS_FAILED(
        BCryptImportKeyPair(
            BCRYPT_MLKEM_ALG_HANDLE,
            NULL, // hImportKey
            BCRYPT_MLKEM_ENCAPSULATION_BLOB,
            &hKeyPair,
            encapsulationKeyBlob.data(),
            static_cast<ULONG>(encapsulationKeyBlob.size()),
            0)); // dwFlags

    // Get the secret key length and ciphertext length. These values are static
    // and can be cached for the algorithm handle.
    ULONG cbSecretKey = 0;
    ULONG cbProperty = sizeof(cbSecretKey);

    THROW_IF_NTSTATUS_FAILED(
        BCryptGetProperty(
            &hKeyPair,
            BCRYPT_KEM_SHARED_SECRET_LENGTH,
            reinterpret_cast<PUCHAR>(&cbSecretKey),
            cbProperty,
            &cbProperty,
            0)); // dwFlags

    ULONG cbCipherText = 0; 
    cbProperty = sizeof(cbCipherText);

    THROW_IF_NTSTATUS_FAILED(
        BCryptGetProperty(
            &hKeyPair,
            BCRYPT_KEM_CIPHERTEXT_LENGTH,
            reinterpret_cast<PUCHAR>(&cbCipherText),
            cbProperty,
            &cbProperty,
            0)); // dwFlags

    // Then allocate the required buffers.
    vector<BYTE> secretKey(cbSecretKey);
    vector<BYTE> cipherText(cbCipherText);

    // Perform the encapsulate operation.
    THROW_IF_NTSTATUS_FAILED(
        BCryptEncapsulate(
            hKeyPair.get(),
            secretKey.data(),
            static_cast<ULONG>(secretKey.size()),
            &cbSecretKey,
            cipherText.data(),
            static_cast<ULONG>(cipherText.size()),
            &cbCipherText,
            0)); // dwFlags

    // cipherText is sent to the client in the server's key_exchange message.
    SendToClient(cipherText.data(), cipherText.size());

    // secretKey contains the shared secret key which plugs into the TLS key
    // schedule.
    DeriveSessionKeys(secretKey);
}
```

## Related content

- [Using ML-DSA with CNG](cng-mldsa-examples.md)
- [Overview of typical CNG programming](typical-cng-programming.md)
- [CNG Key Storage Functions](cng-key-storage-functions.md)
