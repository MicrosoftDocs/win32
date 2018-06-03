---
Description: Explains the CryptoAPI system architecture.
ms.assetid: 244329bb-fc71-4ab9-8831-a9478108ffa3
title: CryptoAPI System Architecture
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
-   [*Key generation functions*](https://www.bing.com/search?q=*Key generation functions*) used to generate and store [*cryptographic keys*](https://www.bing.com/search?q=*cryptographic keys*). Full support is included for changing [*chaining modes*](https://www.bing.com/search?q=*chaining modes*), [*initialization vectors*](https://www.bing.com/search?q=*initialization vectors*), and other encryption features. For more information, see [Key Generation and Exchange Functions](https://www.bing.com/search?q=Key Generation and Exchange Functions).
-   *Key exchange functions* used to exchange or transmit keys. For more information, see [Cryptographic Key Storage and Exchange](cryptographic-key-storage-and-exchange.md) and [Key Generation and Exchange Functions](https://www.bing.com/search?q=Key Generation and Exchange Functions).

## Certificate Encode/Decode Functions

-   Functions used to encrypt or decrypt data. Support is also included for [*hashing*](https://www.bing.com/search?q=*hashing*) data. For more information, see [Data Encryption and Decryption Functions](https://www.bing.com/search?q=Data Encryption and Decryption Functions) and [Data Encryption and Decryption](data-encryption-and-decryption.md).

## Certificate Store Functions

-   Functions used to manage collections of digital certificates. For more information, see [Digital Certificates](digital-certificates.md) and [Certificate Store Functions](https://www.bing.com/search?q=Certificate Store Functions).

## Simplified Message Functions

-   Functions used to encrypt and decrypt messages and data.
-   Functions used to sign messages and data.
-   Functions used to verify the authenticity of signatures on received messages and related data.

For more information, see [Simplified Messages](simplified-messages.md) and [Simplified Message Functions](https://www.bing.com/search?q=Simplified Message Functions).

## Low-level Message Functions

-   Functions used to perform all of the tasks performed by the simplified message functions. The low-level message functions provide more flexibility than the simplified message functions but require more function calls. For more information, see [Low-level Messages](low-level-messages.md) and [Low-level Message Functions](https://www.bing.com/search?q=Low-level Message Functions).

![cryptoapi architecture](images/cryparch.png)

Each of the functional areas has a key word in its function name that indicates its functional area.



| Functional area              | Function name convention |
|------------------------------|--------------------------|
| Base cryptographic functions | Crypt                    |
| Encoding/decoding functions  | Crypt                    |
| Certificate store functions  | Store                    |
| Simplified message functions | Message                  |
| Low-level message functions  | Msg                      |



 

Applications use functions in all of these areas. These functions, taken together, make up CryptoAPI. The [*base cryptographic functions*](https://www.bing.com/search?q=*base cryptographic functions*) use the CSPs for the necessary cryptographic algorithms and for the generation and secure storage of [cryptographic keys](cryptographic-keys.md).

Two different kinds of cryptographic keys are used: [*session keys*](https://www.bing.com/search?q=*session keys*), which are used for a single encryption/decryption, and [*public/private key pairs*](https://www.bing.com/search?q=*public/private key pairs*), which are used on a more permanent basis.

> [!Note]  
> Although an application can communicate directly with any of the five functional areas, it cannot communicate directly with a CSP. All application-to-CSP communications occur through the [*base cryptographic functions*](https://www.bing.com/search?q=*base cryptographic functions*). Base cryptographic functions have a parameter that specifies which CSP to use. This parameter can be set to **NULL** to select a default CSP.

 

 

 



