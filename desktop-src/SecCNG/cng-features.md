---
description: CNG has the following features.
ms.assetid: 400a2b6e-6bbe-4ba4-abde-a2f625007517
title: CNG Features
ms.topic: article
ms.date: 05/31/2018
---

# CNG Features

CNG has the following features.

-   [Cryptographic Agility](#cryptographic-agility)
-   [Certification and Compliance](#certification-and-compliance)
-   [Suite B Support](#suite-b-support)
-   [Legacy Support](#legacy-support)
-   [Kernel Mode Support](#kernel-mode-support)
-   [Auditing](#auditing)
-   [Replaceable Random Number Generators](#replaceable-random-number-generators)
-   [Thread Safety](#thread-safety)
-   [Mode of Operation](#mode-of-operation)

## Cryptographic Agility

One of the key value propositions of CNG is cryptographic agility, sometimes called cryptographic agnosticism. Converting implementation of protocols like [*Secure Sockets Layer protocol*](/windows/desktop/SecGloss/s-gly) (SSL) or [*transport layer security*](/windows/desktop/SecGloss/t-gly) (TLS), CMS (S/MIME), IPsec, Kerberos, and so on, to CNG, however, was required to make this ability valuable. At the CNG level, it was necessary to provide substitution and discoverability for all the algorithm types (symmetric, asymmetric, hash functions), random number generation, and other utility functions. The protocol-level changes are more significant because in many cases the protocol APIs needed to add algorithm selection and other flexibility options that did not previously exist.

CNG is first available in Windows Vista and is positioned to replace existing uses of [*CryptoAPI*](/windows/desktop/SecGloss/c-gly) throughout the Microsoft software stack. Third-party developers will find lots of new features in CNG, including:

-   A new crypto configuration system, supporting better cryptographic agility.
-   Finer-grained abstraction for key storage (and separation of storage from algorithm operations).
-   Process isolation for operations with long-term keys.
-   Replaceable random number generators.
-   Relief from export signing restrictions.
-   Thread-safety throughout the stack.
-   Kernel-mode cryptographic API.

In addition, CNG includes support for all required Suite B algorithms, including [*elliptic curve cryptography*](/windows/desktop/SecGloss/e-gly) (ECC). Existing CryptoAPI applications will continue to work as CNG becomes available.

## Certification and Compliance

CNG is validated to Federal Information Processing Standards (FIPS) 140-2 and is part of the Target of Evaluation for the Windows Common Criteria certification. CNG was designed to be usable as a component in a FIPS level 2 validated system.

CNG complies with Common Criteria requirements by storing and using long lived keys in a secure process.

## Suite B Support

An important feature of CNG is its support for the Suite B algorithms. In February of 2005, the National Security Agency (NSA) of the United States announced a coordinated set of symmetric encryption, asymmetric secret agreement (also known as key exchange), digital signature and hash functions for future U.S. government use called *Suite B*. The NSA has announced that certified Suite B implementations can and will be used for the protection of information designated as Top Secret, Secret, and private information that, in the past was described as Sensitive-But-Unclassified. Because of this, Suite B support is very important to application software vendors and system integrators as well as to Microsoft.

All Suite B algorithms are publicly known. They have been developed outside the scope of the government secrecy historically associated with cryptographic algorithm development. In this same time frame, some European countries and regions have also proposed the same Suite B requirements for protecting their information.

Suite B cryptography recommends use of elliptic curve Diffie-Hellman (ECDH) in many existing protocols such as the Internet Key Exchange (IKE, mainly used in IPsec), [*transport layer security*](/windows/desktop/SecGloss/t-gly) (TLS), and Secure MIME (S/MIME).

CNG includes support for Suite B that extends to all required algorithms: AES (all key sizes), the SHA-2 family (SHA-256, SHA-384 and SHA-512) of hashing algorithms, ECDH, and elliptic curve DSA (ECDSA) over the NIST-standard prime curves P-256, P-384, and P-521. Binary curves, Koblitz curves, custom prime curves, and elliptic curve Menezes-Qu-Vanstone (ECMQV) are not supported by the Microsoft algorithm providers included with Windows Vista.

## Legacy Support

CNG provides support for the current set of algorithms in [*CryptoAPI*](/windows/desktop/SecGloss/c-gly) 1.0. Every algorithm that is currently supported in *CryptoAPI* 1.0 will continue to be supported in CNG.

## Kernel Mode Support

CNG supports cryptography in kernel mode. The same APIs are used in both kernel and user mode to fully support the cryptography features. Both SSL/TLS and IPsec operate in kernel mode in addition to boot processes that will be using CNG. Not all CNG functions can be called from kernel mode. The reference topic for the functions that cannot be called from kernel mode will explicitly state that the function cannot be called from kernel mode. Otherwise, all CNG functions can be called from kernel mode if the caller is running at **PASSIVE\_LEVEL** [*IRQL*](/windows/desktop/SecGloss/i-gly). In addition, some kernel mode CNG functions may be callable at **DISPATCH\_LEVEL IRQL**, depending on the provider's capabilities.

The Microsoft kernel security support provider interface (Ksecdd.sys) is a general purpose, software-based, cryptographic module residing at the kernel mode level of Windows. Ksecdd.sys runs as a kernel mode export driver, and provides cryptographic services through their documented interfaces to kernel components. The only built-in Microsoft provider algorithm that is not supported by Ksecdd.sys is DSA.

**Windows Server 2008 and Windows Vista:** CNG does not support pluggable algorithms and providers in kernel mode. The only supported cryptographic algorithms available in kernel mode are those implementations provided by Microsoft through the kernel mode CNG APIs.

## Auditing

To comply with some of the Common Criteria requirements in addition to providing comprehensive security, many actions that happen in the CNG layer are audited in the Microsoft software key storage provider (KSP). The Microsoft KSP adheres to the following guidelines to create audit records in the security log:

-   Key and key-pair generation failures, including self-test failures, must be audited.
-   Key import and export must be audited.
-   Key destruction failures must be audited.
-   Persistent keys need to be audited when they are written to and read from files.
-   Pair-wise consistency check failures must be audited.
-   Secret key validation failures, if any, must be audited, for example, parity checks on 3DES keys.
-   Failures in encryption, decryption, hashing, signature, verification, key exchange, and random number generation must be audited.
-   Cryptographic self-tests must be audited.

In general, if a key does not have a name, it is an ephemeral key. An ephemeral key does not persist, and the Microsoft KSP does not generate audit records for ephemeral keys. The Microsoft KSP generates audit records in user mode in the LSA process only. No audit record is generated by kernel mode CNG. Administrators need to configure the audit policy to obtain all KSP audit logs from the security log. An administrator must run the following command line to configure additional audits generated by KSPs:

**auditpol /set /subcategory:"other system events" /success:enable /failure:enable**

## Replaceable Random Number Generators

Another improvement that CNG provides is the ability to replace the default random number generator (RNG). In CryptoAPI, it is possible to provide an alternate RNG as part of a cryptographic service provider (CSP), but it is not possible to redirect the Microsoft Base CSPs to use another RNG. CNG makes it possible to explicitly specify a particular RNG to use within particular calls.

## Thread Safety

Any functions that modify the same area of memory at the same time (critical sections) when being called from separate threads are not thread safe.

## Mode of Operation

CNG supports five modes of operations that can be used with symmetric block ciphers through the encryption APIs. These modes and their supportability are listed in the following table. The mode of operation can be changed by setting the [**BCRYPT\_CHAINING\_MODE**](cng-property-identifiers.md) property for the algorithm provider by using the [**BCryptSetProperty**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptsetproperty) function.



| Mode of operation           | BCRYPT\_CHAINING\_MODE value | Algorithms              | Standard  |
|-----------------------------|------------------------------|-------------------------|-----------|
| ECB (Electronic Codebook)   | **BCRYPT\_CHAIN\_MODE\_ECB** | Symmetric block ciphers | SP800-38A |
| CBC (Cipher Block Chaining) | **BCRYPT\_CHAIN\_MODE\_CBC** | Symmetric block ciphers | SP800-38A |
| CFB (Cipher Feedback)       | **BCRYPT\_CHAIN\_MODE\_CFB** | Symmetric block ciphers | SP800-38A |
| CCM (Counter with CBC)      | **BCRYPT\_CHAIN\_MODE\_CCM** | AES                     | SP800-38C |
| GCM (Galois/Counter Mode)   | **BCRYPT\_CHAIN\_MODE\_GCM** | AES                     | SP800-38D |



 

> [!Note]  
> Only ECB, CBC, and CFB modes of operation are defined in Windows Vista. GCM and CCM require Windows Vista with Service Pack 1 (SP1) or Windows Server 2008.

 

 

 
