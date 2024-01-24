---
description: The Base Provider creates 40-bit symmetric keys created with eleven bytes of zero-value salt, eleven bytes of nonzero salt if CRYPT\_CREATE\_SALT is specified, or no salt value.
ms.assetid: f1af0af7-c64e-435a-aef0-7c4ed7bd1199
title: Salt Value Functionality
ms.topic: article
ms.date: 05/31/2018
---

# Salt Value Functionality

The Base Provider creates 40-bit [*symmetric keys*](../secgloss/s-gly.md) created with eleven bytes of zero-value [*salt*](../secgloss/s-gly.md), eleven bytes of nonzero salt if CRYPT\_CREATE\_SALT is specified, or no salt value. A 40-bit symmetric key with zero-value salt, however, is not equivalent to a 40-bit symmetric key without salt. For interoperability, keys must be created without salt. This problem results from a default condition that occurs only with keys of exactly 40 bits. All other [*key lengths*](../secgloss/k-gly.md) do not have salt allocated by default.

Both the Base Providers and the Extended Provider can use the CRYPT\_NO\_SALT flag to specify that no salt value is allocated for a 40-bit symmetric key. The functions that accept this flag are [**CryptGenKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey), [**CryptDeriveKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptderivekey), and [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey). By default, these functions provide backward compatibility for the 40-bit symmetric key case by continuing the use of the eleven-byte-long zero-value salt.

 

 
