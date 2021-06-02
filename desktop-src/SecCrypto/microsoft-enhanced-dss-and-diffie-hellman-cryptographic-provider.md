---
description: The Microsoft enhanced DSS and Diffie-Hellman Cryptographic Provider supports Diffie-Hellman key exchange, SHA hashing, DSA data signing and verification (FIPS 186-2), and RC4 symmetric encryption algorithms.
ms.assetid: 90eca1e0-960f-4355-aef7-6e923100a6d8
title: Microsoft Enhanced DSS & Diffie-Hellman Cryptographic Provider
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Enhanced DSS & Diffie-Hellman Cryptographic Provider

The Microsoft enhanced DSS and [*Diffie-Hellman*](../secgloss/d-gly.md) Cryptographic Provider supports *Diffie-Hellman* key exchange, SHA hashing, DSA data signing and verification (FIPS 186-2), and RC4 symmetric encryption algorithms.

<dl> Provider type: **PROV\_DSS\_DH**  
Provider name: **MS\_ENH\_DSS\_DH\_PROV**  
</dl>

This cryptographic provider supports the following algorithms.

| Algorithm ID          | Algorithm type  | Default size (bits) | Description                                                                                                                                                |
|-----------------------|-----------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CALG\_CYLINK\_MEK** | Data encryption | 40                  | CYLINK message encryption algorithm.                                                                                                                       |
| **CALG\_RC2**         | Data encryption | 128                 | RSA RC2.                                                                                                                                                   |
| **CALG\_RC4**         | Data encryption | 128                 | RSA RC4.                                                                                                                                                   |
| **CALG\_DES**         | Data encryption | 56                  | Data Encryption Standard (DES).                                                                                                                            |
| **CALG\_3DES\_112**   | Data encryption | 112                 | Two key triple DES.                                                                                                                                        |
| **CALG\_3DES**        | Data encryption | 168                 | Three key triple DES.                                                                                                                                      |
| **CALG\_SHA1**        | Hash            | 160                 | Secure Hash Algorithm 1 (SHA-1).                                                                                                                           |
| **CALG\_MD5**         | Hash            | 128                 | Message Digest 5 (MD5).                                                                                                                                    |
| **CALG\_DSS\_SIGN**   | Signature       | 1024                | Digital Signature Algorithm (DSA).                                                                                                                         |
| **CALG\_DH\_SF**      | Key exchange    | 1024                | Store and forward [*Diffie-Hellman*](../secgloss/d-gly.md) key exchange algorithm. |
| **CALG\_DH\_EPHEM**   | Key exchange    | 1024                | [*Diffie-Hellman*](../secgloss/d-gly.md) ephemeral algorithm.                      |



 

 

 
