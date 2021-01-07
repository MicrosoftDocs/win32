---
description: The CNG API provides a set of functions that perform basic cryptographic operations such as creating hashes or encrypting and decrypting data. For more information about these functions, see CNG Cryptographic Primitive Functions.
ms.assetid: 925848ae-9f4f-444a-81ff-14a1997434b2
title: Cryptographic Primitives
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Primitives

The CNG API provides a set of functions that perform basic cryptographic operations such as creating hashes or encrypting and decrypting data. For more information about these functions, see [CNG Cryptographic Primitive Functions](cng-cryptographic-primitive-functions.md).

CNG implements numerous cryptographic algorithms. Each algorithm or class of algorithms exposes its own primitive API. Multiple implementations of a given algorithm can be installed at the same time; however, only one implementation will be the default at any given time.

Each algorithm class in CNG is represented by a primitive router. Applications using the CNG primitive functions will link to the router binary file Bcrypt.dll in user mode, or Ksecdd.sys in kernel mode before calling the functions. Various router routines manage all of the algorithm primitives. These routers track each algorithm implementation installed on the system and route each function call to the appropriate primitive provider module.

CNG provides primitives for the following classes of algorithms.



| Algorithm class                                                                                                                                                  | Description                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <span id="Random_number_generator"></span><span id="random_number_generator"></span><span id="RANDOM_NUMBER_GENERATOR"></span>Random number generator<br/> | Pluggable random number generation (RNG).<br/>                                                         |
| <span id="Hashing"></span><span id="hashing"></span><span id="HASHING"></span>Hashing<br/>                                                                 | Algorithms used for hashing, such as SHA1 and SHA2.<br/>                                               |
| <span id="Symmetric_encryption"></span><span id="symmetric_encryption"></span><span id="SYMMETRIC_ENCRYPTION"></span>Symmetric encryption<br/>             | Algorithms used for symmetric encryption, such as AES, 3DES, and RC4.<br/>                             |
| <span id="Asymmetric_encryption"></span><span id="asymmetric_encryption"></span><span id="ASYMMETRIC_ENCRYPTION"></span>Asymmetric encryption<br/>         | Asymmetric (public key) algorithms that support encryption, such as RSA.<br/>                          |
| <span id="Signature"></span><span id="signature"></span><span id="SIGNATURE"></span>Signature<br/>                                                         | Signature algorithms such as DSA and ECDSA. This class can also be used with RSA.<br/>                 |
| <span id="Secret_agreement"></span><span id="secret_agreement"></span><span id="SECRET_AGREEMENT"></span>Secret agreement<br/>                             | Secret agreement algorithms such as Diffie-Hellman (DH) and elliptic curve Diffie-Hellman (ECDH).<br/> |



 

The following illustration shows the design and function of the CNG cryptographic primitives.

![design and function of cng cryptographic primitives](images/ssdk-cng1c.png)

The header file Bcrypt.h defines the **MS\_PRIMITIVE\_PROVIDER** constant as "Microsoft Primitive Provider". To use the Microsoft Primitive Provider, pass this value to [**BCryptOpenAlgorithmProvider**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider).

 

 




