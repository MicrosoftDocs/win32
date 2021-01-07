---
description: The following example shows typical RSA/Schannel client-side code for creating a master key.
ms.assetid: 9ce4877f-e6e6-4b94-9503-092d2702b31f
title: RSA Client Code for Creating the Master Key
ms.topic: article
ms.date: 05/31/2018
---

# RSA Client Code for Creating the Master Key

The following example shows typical RSA/Schannel client-side code for creating a [*master key*](../secgloss/m-gly.md).


```C++
//--------------------------------------------------------------------
//   Define and initialize local variables.

HCRYPTPROV hProv      = <protocol engine's key container>;
HCRYPTKEY  hPublicKey = <server's public key>;
HCRYPTKEY  hMasterKey;       // handle for master key to be created.
ALG_ID     Algid;
DWORD      dwGenFlags =CRYPT_EXPORTABLE;
DWORD          dwExportFlags =0;
BYTE       rgbBlob[<max BLOB size>];
DWORD      cbBlob;

//--------------------------------------------------------------------
// The method for creating the master key depends upon the protocol 
// in use. Schannel protocols include:
//           PCT 1.0
//           SSL 2.0
//           SSL 3.0
//           TLS 1.0     

//--------------------------------------------------------------------
// Select the master key type.

switch(<protocol being used>)
{
    case <PCT 1.0>:
        Algid = CALG_PCT1_MASTER;
        break;

    case <SSL 2.0>:
        Algid = CALG_SSL2_MASTER;
        dwGenFlags |=,key size. << 16;
        if(<SSL3 or TLS is supported>)
            dwExportFlags |= CRYPT_SSL2_FALLBACK;
        break;

    case <SSL 3.0>:
        Algid = CALG_SSL3_MASTER;
        break;

    case <TLS 1.0>:
        Algid = CALG_TLS1_MASTER;
        break;
}

//--------------------------------------------------------------------
// Generate the master key.

CryptGenKey(
         hProv, 
         Algid, 
         dwGenFlags, 
          &hMasterKey);

//--------------------------------------------------------------------
// Export the master key.

cbBlob = sizeof(rgbBlob);
CryptExportKey(
         hMasterKey, 
         hPublicKey, 
         SIMPLEBLOB,
         dwExportFlags, 
         rgbBlob, 
         &cbBlob);
```



 

 
