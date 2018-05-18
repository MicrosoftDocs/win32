---
Description: 'The Base Provider creates 40-bit symmetric keys created with eleven bytes of zero-value salt, eleven bytes of nonzero salt if CRYPT\_CREATE\_SALT is specified, or no salt value.'
ms.assetid: 'f1af0af7-c64e-435a-aef0-7c4ed7bd1199'
title: Salt Value Functionality
---

# Salt Value Functionality

The Base Provider creates 40-bit [*symmetric keys*](security.s_gly#-security-symmetric-key-gly) created with eleven bytes of zero-value [*salt*](security.s_gly#-security-salt-value-gly), eleven bytes of nonzero salt if CRYPT\_CREATE\_SALT is specified, or no salt value. A 40-bit symmetric key with zero-value salt, however, is not equivalent to a 40-bit symmetric key without salt. For interoperability, keys must be created without salt. This problem results from a default condition that occurs only with keys of exactly 40 bits. All other [*key lengths*](security.k_gly#-security-key-length-gly) do not have salt allocated by default.

Both the Base Providers and the Extended Provider can use the CRYPT\_NO\_SALT flag to specify that no salt value is allocated for a 40-bit symmetric key. The functions that accept this flag are [**CryptGenKey**](cryptgenkey.md), [**CryptDeriveKey**](cryptderivekey.md), and [**CryptImportKey**](cryptimportkey.md). By default, these functions provide backward compatibility for the 40-bit symmetric key case by continuing the use of the eleven-byte-long zero-value salt.

 

 



