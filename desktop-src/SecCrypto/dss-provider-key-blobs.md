---
Description: Used with the Digital Signature Standard (DSS) provider to export keys from, and import keys into, the cryptographic service provider (CSP).
ms.assetid: a0a266ef-0830-4a3f-9bf6-6b64c95c3d03
title: DSS Provider Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# DSS Provider Key BLOBs

[*BLOBs*](https://msdn.microsoft.com/en-us/library/ms721569(v=VS.85).aspx) are used with the [*Digital Signature Standard*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx) (DSS) provider to export keys from, and import keys into, the [*cryptographic service provider*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)

## Public Key BLOBs

A DSS [*public key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) is exported and imported as a BLOB, a sequence of bytes structured as follows.

``` syntax
PUBLICKEYSTRUC    publickeystruc;
DSSPUBKEY         dsspubkey;
BYTE              p[dsspubkey.bitlen/8];
BYTE              q[20];
BYTE              g[dsspubkey.bitlen/8];
BYTE              y[dsspubkey.bitlen/8];
DSSSEED           seedstruct;
```

The following table describes these components. All values are in [*little-endian*](https://msdn.microsoft.com/en-us/library/ms721592(v=VS.85).aspx) format.



| Field          | Description                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dsspubkey      | A [**DSSPUBKEY**](https://msdn.microsoft.com/en-us/library/Aa381982(v=VS.85).aspx) structure. The **magic** member must have a value of 0x31535344. This hexadecimal number is the [*ASCII*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) encoding of DSS1. |
| g              | A **BYTE** sequence. The generator, g. Must be the same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                      |
| p              | A **BYTE** sequence. The prime modulus, p. The most significant bit of the most significant byte must be set to one.                                                                                                 |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                                |
| q              | A **BYTE** sequence. The prime, q, 20 bytes in length. The most significant bit of the most significant byte must be set to one.                                                                                     |
| seedstruct     | A [**DSSSEED**](/windows/desktop/api/Wincrypt/ns-wincrypt-_dssseed) structure. Seed and counter values for verifying primes.                                                                                                                                |
| y              | A **BYTE** sequence. The public key, y. Must be same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                         |



 

> [!Note]  
> [*Public key BLOBs*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) are not encrypted. They contain public keys in [*plaintext*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) form.

 

## Private Key BLOBs

A DSS [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) is exported and imported as a sequence of bytes structured as follows.

``` syntax
PUBLICKEYSTRUC    publickeystruc;
DSSPUBKEY         dsspubkey;
BYTE              p[dsspubkey.bitlen/8];
BYTE              q[20];
BYTE              g[dsspubkey.bitlen/8];
BYTE              x[20];
DSSSEED           seedstruct;
```

The following table describes each component. All values are in [*little-endian*](https://msdn.microsoft.com/en-us/library/ms721592(v=VS.85).aspx) format.



| Field          | Description                                                                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dsspubkey      | A [**DSSPUBKEY**](https://msdn.microsoft.com/en-us/library/Aa381982(v=VS.85).aspx) structure. The **magic** member must be set to 0x32535344. This hexadecimal number is the [*ASCII*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) encoding of DSS2. |
| g              | A **BYTE** sequence. The generator, g. Must be the same length as p. If it is not the same length as p, then it must be padded with 0x00 bytes.                                                                |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                          |
| p              | A **BYTE** sequence. The prime modulus, p. The most significant bit of the most significant byte must be set to one.                                                                                           |
| q              | A **BYTE** sequence. The prime, q. q is 20 bytes in length. The most significant bit of the most significant byte must be set to one.                                                                          |
| seedstruct     | A [**DSSSEED**](/windows/desktop/api/Wincrypt/ns-wincrypt-_dssseed) structure. Seed and counter values for verifying primes.                                                                                                                          |
| x              | A **BYTE** sequence. The secret exponent, x. Must always be 20 bytes in length. If x is smaller than 20 bytes in length, then it must be padded with 0x00.                                                     |



 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> [!Caution]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

 

 



