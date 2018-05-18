---
Description: 'To verify a signature, create a hash object using CryptCreateHash. This hash object accumulates the data to be verified. The data is then added to the hash object with the CryptHashData function.'
ms.assetid: '3779f83b-0d87-4f47-949b-9eb39690adfb'
title: Verifying a Signature
---

# Verifying a Signature

To verify a signature, create a [*hash object*](security.h_gly#-security-hash-object-gly) using [**CryptCreateHash**](cryptcreatehash.md). This hash object accumulates the data to be verified. The data is then added to the hash object with the [**CryptHashData**](crypthashdata.md) function.

After the last block of data is added to the hash, use [**CryptVerifySignature**](cryptverifysignature.md) to verify the signature. The address of the signature data, a handle to the hash object, and the handle of the public keys are passed to **CryptVerifySignature**.

After the signature has been verified (or has failed the verification), destroy the hash object using the [**CryptDestroyHash**](cryptdestroyhash.md) function.

 

 



