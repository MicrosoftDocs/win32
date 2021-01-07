---
description: A group of high-level functions has been provided to simplify and shorten the amount of code necessary to accomplish the usual message manipulation tasks.
ms.assetid: 7c1a4d6e-9b9d-43c8-b094-3c98b9a68490
title: Simplified Messages
ms.topic: article
ms.date: 05/31/2018
---

# Simplified Messages

A group of high-level functions has been provided to simplify and shorten the amount of code necessary to accomplish the usual message manipulation tasks. These functions are called "simplified message functions." The names of all simplified message functions contain the word "Message."

[*Simplified message functions*](../secgloss/s-gly.md) are at a higher level than the base cryptographic functions or the low-level message functions. They wrap several of the base cryptographic, low-level message, and certificate functions into a single function that performs a specific task in a specific manner, such as encrypting a PKCS \#7 message or signing a message. Simplified message functions provide a quick way to get started using CryptoAPI by reducing the number of function calls needed to accomplish a task.

The following table list sections that contain detailed procedure descriptions or C program examples of using the simplified message functions.



| Section                                                                                                                                         | Contents                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [Simplified Message Functions](cryptography-functions.md)                                                         | Lists the simplified message functions.                                                     |
| [Creating a Signed Message](creating-a-signed-message.md)                                                                                      | Details the process of creating a signed message.                                           |
| [Procedure for Signing Data](procedure-for-signing-data.md)                                                                                    | Provides a procedure for using the simplified message functions to create a signed message. |
| [Verifying A Signed Message](verifying-a-signed-message.md)                                                                                    | Details a process for verifying the signature on a signed message.                          |
| [Encrypting a Message](../secauthn/encrypting-a-message.md)                                                                                           | Details the tasks needed to encrypt and decrypt a message.                                  |
| [Decrypting a Message](../secauthn/decrypting-a-message.md)                                                                                           | Details the tasks needed to decrypt a message.                                              |
| [Example C Program: Using CryptEncryptMessage and CryptDecryptMessage](example-c-program-using-cryptencryptmessage-and-cryptdecryptmessage.md) | Provides a procedure and sample code for encrypting and decrypting a message.               |



 

 

 
