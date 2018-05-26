---
Description: Explains the CryptoAPI system architecture.
ms.assetid: 244329bb-fc71-4ab9-8831-a9478108ffa3
title: CryptoAPI System Architecture
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CryptoAPI System Architecture

The CryptoAPI system architecture is composed of five major functional areas:

-   [Base Cryptographic Functions](#base-cryptographic-functions)
-   [Certificate Encode/Decode Functions](#certificate-encodedecode-functions)
-   [Certificate Store Functions](#certificate-store-functions)
-   [Simplified Message Functions](#simplified-message-functions)
-   [Low-level Message Functions](#low-level-message-functions)

## Base Cryptographic Functions

-   *Context functions* used to connect to a CSP. These functions enable applications to choose a specific CSP by name or to choose a specific CSP that can provide a needed class of functionality.
-   [*Key generation functions*](security.k_gly#-security-key-generation-functions-gly) used to generate and store [*cryptographic keys*](security.c_gly#-security-cryptographic-key-gly). Full support is included for changing [*chaining modes*](security.c_gly#-security-chaining-mode-gly), [*initialization vectors*](security.i_gly#-security-initialization-vector-gly), and other encryption features. For more information, see [Key Generation and Exchange Functions](cryptography-functions.md#key-generation-and-exchange-functions).
-   *Key exchange functions* used to exchange or transmit keys. For more information, see [Cryptographic Key Storage and Exchange](cryptographic-key-storage-and-exchange.md) and [Key Generation and Exchange Functions](cryptography-functions.md#key-generation-and-exchange-functions).

## Certificate Encode/Decode Functions

-   Functions used to encrypt or decrypt data. Support is also included for [*hashing*](security.h_gly#-security-hash-gly) data. For more information, see [Data Encryption and Decryption Functions](cryptography-functions.md#data-encryption-and-decryption-functions) and [Data Encryption and Decryption](data-encryption-and-decryption.md).

## Certificate Store Functions

-   Functions used to manage collections of digital certificates. For more information, see [Digital Certificates](digital-certificates.md) and [Certificate Store Functions](cryptography-functions.md#certificate-and-certificate-store-functions).

## Simplified Message Functions

-   Functions used to encrypt and decrypt messages and data.
-   Functions used to sign messages and data.
-   Functions used to verify the authenticity of signatures on received messages and related data.

For more information, see [Simplified Messages](simplified-messages.md) and [Simplified Message Functions](cryptography-functions.md#simplified-message-functions).

## Low-level Message Functions

-   Functions used to perform all of the tasks performed by the simplified message functions. The low-level message functions provide more flexibility than the simplified message functions but require more function calls. For more information, see [Low-level Messages](low-level-messages.md) and [Low-level Message Functions](cryptography-functions.md#low-level-message-functions).

![cryptoapi architecture](images/cryparch.png)

Each of the functional areas has a key word in its function name that indicates its functional area.



| Functional area              | Function name convention |
|------------------------------|--------------------------|
| Base cryptographic functions | Crypt                    |
| Encoding/decoding functions  | Crypt                    |
| Certificate store functions  | Store                    |
| Simplified message functions | Message                  |
| Low-level message functions  | Msg                      |



 

Applications use functions in all of these areas. These functions, taken together, make up CryptoAPI. The [*base cryptographic functions*](security.b_gly#-security-base-cryptographic-functions-gly) use the CSPs for the necessary cryptographic algorithms and for the generation and secure storage of [cryptographic keys](cryptographic-keys.md).

Two different kinds of cryptographic keys are used: [*session keys*](security.s_gly#-security-session-key-gly), which are used for a single encryption/decryption, and [*public/private key pairs*](security.p_gly#-security-public-private-key-pair-gly), which are used on a more permanent basis.

> [!Note]  
> Although an application can communicate directly with any of the five functional areas, it cannot communicate directly with a CSP. All application-to-CSP communications occur through the [*base cryptographic functions*](security.b_gly#-security-base-cryptographic-functions-gly). Base cryptographic functions have a parameter that specifies which CSP to use. This parameter can be set to **NULL** to select a default CSP.

 

 

 



