---
Description: Used with the Digital Signature Standard (DSS) provider to export keys from, and import keys into, the cryptographic service provider (CSP).
ms.assetid: a0a266ef-0830-4a3f-9bf6-6b64c95c3d03
title: DSS Provider Key BLOBs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DSS Provider Key BLOBs

[*BLOBs*](https://msdn.microsoft.com/2e570727-7da0-4e17-bf5d-6fe0e6aef65b) are used with the [*Digital Signature Standard*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DSS) provider to export keys from, and import keys into, the [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)

## Public Key BLOBs

A DSS [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) is exported and imported as a BLOB, a sequence of bytes structured as follows.

``` syntax
PUBLICKEYSTRUC    publickeystruc;
DSSPUBKEY         dsspubkey;
BYTE              p[dsspubkey.bitlen/8];
BYTE              q[20];
BYTE              g[dsspubkey.bitlen/8];
BYTE              y[dsspubkey.bitlen/8];
DSSSEED           seedstruct;
```

The following table describes these components. All values are in [*little-endian*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) format.



| Field          | Description                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dsspubkey      | A [**DSSPUBKEY**](/windows/desktop/api/Wincrypt/) structure. The **magic** member must have a value of 0x31535344. This hexadecimal number is the [*ASCII*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) encoding of DSS1. |
| g              | A **BYTE** sequence. The generator, g. Must be the same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                      |
| p              | A **BYTE** sequence. The prime modulus, p. The most significant bit of the most significant byte must be set to one.                                                                                                 |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                                |
| q              | A **BYTE** sequence. The prime, q, 20 bytes in length. The most significant bit of the most significant byte must be set to one.                                                                                     |
| seedstruct     | A [**DSSSEED**](/windows/desktop/api/Wincrypt/ns-wincrypt-_dssseed) structure. Seed and counter values for verifying primes.                                                                                                                                |
| y              | A **BYTE** sequence. The public key, y. Must be same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                         |



 

> [!Note]  
> [*Public key BLOBs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) are not encrypted. They contain public keys in [*plaintext*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) form.

 

## Private Key BLOBs

A DSS [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) is exported and imported as a sequence of bytes structured as follows.

``` syntax
PUBLICKEYSTRUC    publickeystruc;
DSSPUBKEY         dsspubkey;
BYTE              p[dsspubkey.bitlen/8];
BYTE              q[20];
BYTE              g[dsspubkey.bitlen/8];
BYTE              x[20];
DSSSEED           seedstruct;
```

The following table describes each component. All values are in [*little-endian*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) format.



| Field          | Description                                                                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dsspubkey      | A [**DSSPUBKEY**](/windows/desktop/api/Wincrypt/) structure. The **magic** member must be set to 0x32535344. This hexadecimal number is the [*ASCII*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) encoding of DSS2. |
| g              | A **BYTE** sequence. The generator, g. Must be the same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                          |
| p              | A **BYTE** sequence. The prime modulus, p. The most significant bit of the most significant byte must be set to one.                                                                                           |
| q              | A **BYTE** sequence. The prime, q. q is 20 bytes in length. The most significant bit of the most significant byte must be set to one.                                                                          |
| seedstruct     | A [**DSSSEED**](/windows/desktop/api/Wincrypt/ns-wincrypt-_dssseed) structure. Seed and counter values for verifying primes.                                                                                                                          |
| x              | A **BYTE** sequence. The secret exponent, x. Must always be 20 bytes in length. If x is smaller than 20 bytes in length, then it must be padded with 0x00.                                                     |



 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> \[!Caution\]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

 

 



