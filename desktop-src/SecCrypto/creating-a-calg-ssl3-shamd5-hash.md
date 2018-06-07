---
Description: Explains how to create a CALG\_SSL3\_SHAMD5 hash.
ms.assetid: dad6fc7f-8abd-4f90-b3e4-8d0169e95087
title: Creating a CALG\_SSL3\_SHAMD5 Hash
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a CALG\_SSL3\_SHAMD5 Hash

**To create a CALG\_SSL3\_SHAMD5 hash**

1.  Using standard CryptoAPI methodology, create both a MD5 and a [*SHA*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) [*hash*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) of the target data.
2.  Concatenate the two hashes, with the MD5 value leftmost and the SHA value rightmost. This results in a 36-byte value (16 bytes + 20 bytes).
3.  Get a handle to a [*hash object*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) by calling [**CryptCreateHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash) with CALG\_SSL3\_SHAMD5 passed in the *Algid* parameter.
4.  Set the hash value with a call to [**CryptSetHashParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsethashparam). The concatenated hash values are passed as a **BYTE**\* in the *pbData* parameter, and the HP\_HASHVAL value must be passed in the *dwParam* parameter. Calling [**CryptHashData**](/windows/desktop/api/Wincrypt/nf-wincrypt-crypthashdata) using the handle returned by [**CryptCreateHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptcreatehash) in step 3 will fail.
5.  Call [**CryptSignHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsignhasha) to generate the signature.
6.  Call [**CryptDestroyHash**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdestroyhash) to destroy the hash object.

 

 



