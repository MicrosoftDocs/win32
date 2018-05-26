---
Description: A finish message is sent immediately after a change cipher spec message to verify the success of key exchange and authentication processes.
ms.assetid: 1ae92223-3729-48be-af42-146c9cbae6a5
title: Finish Messages in the TLS 1.0 Protocol
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Finish Messages in the TLS 1.0 Protocol

A finish message is sent immediately after a change cipher spec message to verify the success of key exchange and authentication processes. The finish messages in the TLS 1.0 protocol are calculated using [*Pseudo-Random Function*](security.p_gly#-security-pseudo-random-function-gly) (PRF) with the [*master key*](security.m_gly#-security-master-key-gly), a label, and a seed as input. PRF produces an output of arbitrary length. The following method is used to generate the PRF output used in TLS 1.0 finish messages.

A PRF [*hash*](security.h_gly#-security-hash-gly) handle is generated using [**CryptCreateHash**](/windows/win32/Wincrypt/nf-wincrypt-cryptcreatehash?branch=master) with the **ALG\_ID** value set to CALG\_TLS1PRF and the handle to the master key passed in the *hKey* parameter. The label and seed values are set on the hash handle using the values HP\_TLS1PRF\_LABEL and HP\_TLS1PRF\_SEED, respectively, in the *dwParam* parameter with the [**CryptSetHashParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptsethashparam?branch=master) function. Finally, the protocol engine calls the function [**CryptGetHashParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptgethashparam?branch=master) with the value HP\_HASHVAL in the *dwParam* parameter to retrieve the PRF data to be included in the finish message. When making the call to **CryptGetHashParam**, the protocol engine must specify how many bytes of data PRF will produce. This is done in the *pdwDataLen* parameter, and the resulting data is placed in the buffer pointed to by the *pbData* parameter.

The following is typical source code for this protocol engine:


```C++
CRYPT_DATA_BLOB Data;
HCRYPTHASH hFinishHash;
BYTE rgbFinishPRF[12];
BYTE rgbCliHashOfHandshakes[36];

//------------------------------------------------------------
// get client finish message

CryptCreateHash(
         hProv, 
         CALG_TLS1PRF, 
         hMasterKey, 
         0, 
         &amp;hFinishHash);

Data.pbData = (BYTE*)"client finished";
Data.cbData = 15;
CryptSetHashParam(
         hFinishHash, 
         HP_TLS1PRF_LABEL, 
         (BYTE*)&amp;Data, 
         0);

Data.pbData = rgbCliHashOfHandshakes;
Data.cbData = sizeof(rgbCliHashOfHandshakes);
CryptSetHashParam(
          hFinishHash, 
          HP_TLS1PRF_SEED, 
          (BYTE*)&amp;Data, 
          0);

cbFinishPRF = sizeof(rgbFinishPRF);
CryptGetHashParam(
          hFinishHash, 
          HP_HASHVAL, 
          rgbFinishPRF, 
          &amp;cbFinishPRF, 
          0);

CryptDestroyHash(hFinishHash);
```



 

 



