---
description: The following example shows typical Diffie-Hellman/Schannel server-side code for creating a master key.
ms.assetid: 1ef0a2ea-8684-425c-abfe-9f65d8df7bbd
title: Diffie-Hellman Server Code for Creating the Master Key
ms.topic: article
ms.date: 05/31/2018
---

# Diffie-Hellman Server Code for Creating the Master Key

The following example shows typical [*Diffie-Hellman*](../secgloss/d-gly.md)/Schannel server-side code for creating a [*master key*](../secgloss/m-gly.md).


```C++
//--------------------------------------------------------------------
//   Define and initialize local variables.

HCRYPTPROV hProv      = <protocol engine's key container>;
HCRYPTKEY  hServerDHKey;  // handle to the client's DH key
HCRYPTKEY  hMasterKey;    // handle for the master key to be created.
ALG_ID     Algid;
PBYTE      pbClientPub = <pointer to client public key>;
DWORD      cbServerPub = <size of client public key>;
BYTE       rgbClientBlob[<max BLOB size>];
DWORD      cbClientBlob = <size of the client key BLOB>;
CRYPT_DATA_BLOB Data;

//--------------------------------------------------------------------
// Build a PUBLICKEYBLOB around the client's public key
{
     BLOBHEADER *pBlobHeader = (BLOBHEADER *)rgbClientBlob;
     DHPUBKEY   *pDHPubKey   = (DHPUBKEY *)(pBlobHeader + 1);
     BYTE       *pData       = (BYTE *)(pDHPubKey + 1);

     pBlobHeader->bType    = PUBLICKEYBLOB;
     pBlobHeader->bVersion = CUR_BLOB_VERSION;
     pBlobHeader->reserved = 0;
     pBlobHeader->aiKeyAlg = CALG_DH_EPHEM;

     pDHPubKey->magic = 0x31484400;
     pDHPubKey->bitlen = dwClientPub * 8;

     ReverseMemCopy(pData, pbClientPub, cbClientPub);
     cbClientBlob = sizeof(BLOBHEADER) + sizeof(DHPUBKEY) + 
        cbClientPub;
}

//--------------------------------------------------------------------
// Import the client's public key and get an agreed key

CryptImportKey(
      hProv, 
      rgbClientBlob, 
      cbClientBlob, 
      hServerDHKey, 
      0, 
      &hMasterKey);

//--------------------------------------------------------------------
// Select the master key type.

switch(<protocol being used>)
{
    case <SSL 3.0>:
        Algid = CALG_SSL3_MASTER;
        break;

    case <TLS 1.0>:
        Algid = CALG_TLS1_MASTER;
        break;
}

//--------------------------------------------------------------------
// Convert the agreed key to the appropriate master key

CryptSetKeyParam(
         hMasterKey, 
         KP_ALGID, 
         (BYTE*)&Algid, 
         0);
```



 

 
