---
description: The following example shows typical Diffie-Hellman/Schannel client-side code for creating a master key.
ms.assetid: 37b35cd6-b3c9-4a75-83a9-129bcf7a84a3
title: Diffie-Hellman Client Code for Creating the Master Key
ms.topic: article
ms.date: 05/31/2018
---

# Diffie-Hellman Client Code for Creating the Master Key

The following example shows typical [*Diffie-Hellman*](../secgloss/d-gly.md)/Schannel client-side code for creating a [*master key*](../secgloss/m-gly.md).


```C++
//--------------------------------------------------------------------
//   Define and initialize local variables.

HCRYPTPROV hProv      = <protocol engine's key container>;
HCRYPTKEY  hClientDHKey;  // handle to the client's DH key
HCRYPTKEY  hMasterKey;
ALG_ID     Algid;
PBYTE      pbServerPub = <pointer to Server Public Key>;
DWORD      cbServerPub = <size of Server Public Key>;
BYTE       rgbServerBlob[<max BLOB size>];
DWORD      cbServerBlob;
PBYTE      pbG = <pointer to generator G from Server>;
DWORD      cbG = <size of generator G from Server>;
PBYTE      pbP = <pointer to prime P from Server>;
DWORD      cbP = <size of prime P from Server>;
CRYPT_DATA_BLOB Data;
BYTE       rgbClientPubBlob[size of the client public key BLOB];
DWORD      cbClientPubBlob;

//--------------------------------------------------------------------
// Generate and set the parameters on the client DH key
// Schannel specifies the key size and [regen flag when generating
// a client DH key.

CryptGenKey(
      hProv, 
      CALG_DH_EPHEM, 
      ((cbP * 8) << 16)|CRYPT_PREGEN, 
      &hClientDHKey);

Data.pbData = pbP;
Data.cbData = cbP;
CryptSetKeyParam(
         hClientDHKey, 
         KP_P, 
         (BYTE*)&Data, 
         0);

Data.pbData = pbG;
Data.cbData = cbG;
CryptSetKeyParam(
          hClientDHKey, 
          KP_G, 
          (BYTE*)&Data, 
          0);

//--------------------------------------------------------------------
// Create the client private DH key

CryptSetKeyParam(
     hClientDHKey, 
     KP_X, 
     NULL, 
     0);

//--------------------------------------------------------------------
// Build PUBLICKEYBLOB around the server's public key
{
     BLOBHEADER *pBlobHeader = (BLOBHEADER *)rgbServerBlob;
     DHPUBKEY   *pDHPubKey   = (DHPUBKEY *)(pBlobHeader + 1);
     BYTE       *pData       = (BYTE *)(pDHPubKey + 1);

     pBlobHeader->bType    = PUBLICKEYBLOB;
     pBlobHeader->bVersion = CUR_BLOB_VERSION;
     pBlobHeader->reserved = 0;
     pBlobHeader->aiKeyAlg = CALG_DH_EPHEM;

     pDHPubKey->magic = 0x31484400;
     pDHPubKey->bitlen = dwServerPub * 8;

     ReverseMemCopy(pData, pbServerPub, cbServerPub);
     cbServerBlob = sizeof(BLOBHEADER) + sizeof(DHPUBKEY) + 
       cbServerPub;
}

//--------------------------------------------------------------------
// Import the server's public key and get an agreed key

CryptImportKey(
        hProv, 
        rgbServerBlob, 
        cbServerBlob, 
        hClientDHKey, 
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

//--------------------------------------------------------------------
// Export the client Diffie-Hellman public key.

cbClientPubBlob = sizeof(rgbClientPubBlob);
CryptExportKey(
           hClientDHKey, 
           0, 
           PUBLICKEYBLOB,
           0, 
           rgbClientPubBlob, 
           & cbClientPubBlob);

CryptDestroyKey(hClientDHKey);
```



 

 
