---
Description: Explains how to create an HMAC.
ms.assetid: b1747b7e-a505-4b23-93bc-cef4e77bf825
title: Creating an HMAC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating an HMAC

**To compute an HMAC**

1.  Get a pointer to the Microsoft [*Cryptographic Service Provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP) by calling [**CryptAcquireContext**](/windows/win32/Wincrypt/nf-wincrypt-cryptacquirecontexta?branch=master).
2.  Create a handle to an [*HMAC*](security.h_gly#-security-hmac-gly)[*hash object*](security.h_gly#-security-hash-object-gly) by calling [**CryptCreateHash**](/windows/win32/Wincrypt/nf-wincrypt-cryptcreatehash?branch=master). Pass CALG\_HMAC in the *Algid* parameter. Pass the handle of a [*symmetric key*](security.s_gly#-security-symmetric-key-gly) in the *hKey* parameter. This symmetric key is the key used to compute the HMAC.
3.  Specify the type of hash to be used by calling [**CryptSetHashParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptsethashparam?branch=master) with the *dwParam* parameter set to the value HP\_HMAC\_INFO. The *pbData* parameter must point to an initialized [**HMAC\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_hmac_info?branch=master) structure.
4.  Call [**CryptHashData**](/windows/win32/Wincrypt/nf-wincrypt-crypthashdata?branch=master) to begin computing the HMAC of the data. The first call to **CryptHashData** causes the key value to be combined using the XOR operator with the inner string and the data. The result of the XOR operation is hashed, and then the target data for the HMAC (pointed to by the *pbData* parameter passed in the call to **CryptHashData**) is hashed. If necessary, subsequent calls to **CryptHashData** may then be made to finish the hashing of the target data.
5.  Call [**CryptGetHashParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptgethashparam?branch=master) with the *dwParam* parameter set to HP\_HASHVAL. This call causes the inner hash to be finished and the outer string to be combined using XOR with the key. The result of the XOR operation is hashed, and then the result of the inner hash (completed in the previous step) is hashed. The outer hash is then finished and returned in the *pbData* parameter and the length in the *dwDataLen* parameter.

> [!Note]  
> Do not use the same [*symmetric*](security.s_gly#-security-symmetric-key-gly) ([*session*](security.s_gly#-security-session-key-gly)) key for both message encryption and [*Message Authentication Code*](security.m_gly#-security-message-authentication-code-gly) (MAC) generation. Using the same key for both greatly increases the risk of messages being decoded by attackers.

 

 

 



