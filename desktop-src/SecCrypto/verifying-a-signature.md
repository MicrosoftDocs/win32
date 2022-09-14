---
description: To verify a signature, create a hash object using CryptCreateHash. This hash object accumulates the data to be verified. The data is then added to the hash object with the CryptHashData function.
ms.assetid: 3779f83b-0d87-4f47-949b-9eb39690adfb
title: Verifying a Signature
ms.topic: article
ms.date: 05/31/2018
---

# Verifying a Signature

To verify a signature, create a [*hash object*](../secgloss/h-gly.md) using [**CryptCreateHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash). This hash object accumulates the data to be verified. The data is then added to the hash object with the [**CryptHashData**](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashdata) function.

After the last block of data is added to the hash, use [**CryptVerifySignature**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptverifysignaturea) to verify the signature. The address of the signature data, a handle to the hash object, and the handle of the public keys are passed to **CryptVerifySignature**.

After the signature has been verified (or has failed the verification), destroy the hash object using the [**CryptDestroyHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroyhash) function.

 

 
