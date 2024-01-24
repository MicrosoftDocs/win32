---
description: The CNG API implements an extensible provider model that lets you load a provider by specifying the required cryptographic algorithm rather than a particular provider.
ms.assetid: a88a089b-4afe-4201-96f7-97f19bce18a1
title: Typical CNG Programming
ms.topic: article
ms.date: 05/31/2018
---

# Typical CNG Programming

The CNG API implements an extensible provider model that lets you load a provider by specifying the required cryptographic algorithm rather than a particular provider. The advantage is that an algorithm provider can be replaced or upgraded and you will not have to change your code in any way to use the new provider. Also, if some algorithm is determined to be unsafe in the future, a more secure version of that algorithm can be installed without affecting your code. Most of the CNG APIs require a provider or an object created by a provider.

The typical steps involved in using the CNG API for cryptographic primitive operations are as follows:

1.  Opening the Algorithm Provider
2.  Getting or Setting Algorithm Properties
3.  Creating or Importing a Key
4.  Performing Cryptographic Operations
5.  Closing the Algorithm Provider

For more information, see Programming Examples.

## Opening the Algorithm Provider

The [**BCryptOpenAlgorithmProvider**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) function provides you with an algorithm provider handle that is used in subsequent CNG APIs, such as [**BCryptCreateHash**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptcreatehash) or [**BCryptGenerateKeyPair**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptgeneratekeypair).

## Getting or Setting Algorithm Properties

You can use the algorithm provider handle to get implementation details for the algorithm, such as the key size or the current mode of operation. You use the [**BCryptGetProperty**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptgetproperty) function to obtain specific properties.

You can also modify the properties of the algorithm. For example, If you want to use ECB block cipher chaining with AES, you set the **BCRYPT\_CHAINING\_MODE** property of an AES algorithm to **BCRYPT\_CHAIN\_MODE\_ECB**; the property is assigned to all AES keys created using this algorithm handle, without the need to configure each and every AES key. You use the [**BCryptSetProperty**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptsetproperty) function to modify these properties.

## Creating or Importing a Key

Depending on the type of algorithm you use, you may need to create or load a key. For example, the [**BCryptEncrypt**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptencrypt) function takes a key handle for the first parameter. If you want that function to encrypt data with a symmetric encryption algorithm such as AES, you must first obtain a key. How you obtain the key depends on the type of algorithm being used and the source of the key.

You can create ephemeral keys with the [**BCryptGenerateSymmetricKey**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptgeneratesymmetrickey) and [**BCryptGenerateKeyPair**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptgeneratekeypair) functions. You can also import ephemeral keys from a memory BLOB with the [**BCryptImportKey**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptimportkey) and [**BCryptImportKeyPair**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptimportkeypair) functions.

For persisted keys, you use the key storage functions to load a key storage provider, and then create or load the keys. You can also use these functions to create or load ephemeral keys by passing **NULL** for any container names. For more information about the key storage functions, see [CNG Key Storage Functions](cng-key-storage-functions.md).

## Performing Cryptographic Operations

You are now ready to perform the cryptographic operation, such as encrypting or decrypting data by using the [**BCryptEncrypt**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptencrypt) or [**BCryptDecrypt**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptdecrypt) functions, respectively.

## Closing the Algorithm Provider

When the provider is no longer needed, you must pass the handle to the [**BCryptCloseAlgorithmProvider**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptclosealgorithmprovider) function to close the provider. This causes the provider to release any resources that have been allocated for that algorithm provider instance. After a provider handle is closed, it cannot be reused.

Loading a provider can be a relatively time-intensive process. You should therefore cache any provider handles that you will reference multiple times during the lifetime of your application.

## Programming Examples

The following examples describe how to perform specific cryptographic operations using CNG.

-   [Creating a Hash with CNG](creating-a-hash-with-cng.md)
-   [Signing Data with CNG](signing-data-with-cng.md)
-   [Encrypting Data with CNG](encrypting-data-with-cng.md)

 

 



