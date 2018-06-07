---
Description: The Base Provider, Strong Provider, and Enhanced Provider use the same key BLOBs.
ms.assetid: f1bd347b-33bd-40bc-9a9b-c06f264f1af4
title: Enhanced Provider Key BLOBs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Provider Key BLOBs

The Base Provider, Strong Provider, and Enhanced Provider use the same [*key BLOBs*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)
-   [Simple Key BLOBs](#simple-key-blobs)

## Public Key BLOBs

[*Public key BLOBs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a), type **PUBLICKEYBLOB**, are used to store [*public keys*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) outside a [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP). Extended provider public key BLOBs have the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
RSAPUBKEY rsapubkey;
BYTE modulus[rsapubkey.bitlen/8];
```

The following table describes each public key component. All values are in [*little-endian*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) format.



| Field          | Description                                                                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| modulus        | The public key modulus data is located directly after the [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-_rsapubkey) structure. The size of this data will vary, depending on the size of the public key. The number of bytes can be determined by dividing the value of the **RSAPUBKEY bitlen** field by eight. |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                                                                                                 |
| rsapubkey      | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-_rsapubkey) structure. The **magic** member must be set to 0x31415352. This hexadecimal value is the [*ASCII*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) encoding of RSA1.                                                                         |



 

> [!Note]  
> Public key BLOBs are not encrypted. They contain public keys in [*plaintext*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) form.

 

## Private Key BLOBs

[*Private key BLOBs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a), type **PRIVATEKEYBLOB**, are used to store [*private keys*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) outside a CSP. Extended provider private key BLOBs have the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
RSAPUBKEY rsapubkey;
BYTE modulus[rsapubkey.bitlen/8];
BYTE prime1[rsapubkey.bitlen/16];
BYTE prime2[rsapubkey.bitlen/16];
BYTE exponent1[rsapubkey.bitlen/16];
BYTE exponent2[rsapubkey.bitlen/16];
BYTE coefficient[rsapubkey.bitlen/16];
BYTE privateExponent[rsapubkey.bitlen/8];
```

The following table describes the private key BLOB component.

> [!Note]  
> These fields correspond to the fields described in section 7.2 of [*Public Key Cryptography Standards*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) (PKCS) \#1 with minor differences.

 



| Field           | Description                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| coefficient     | Coefficient. This has a numeric value of (inverse of q) mod p.                                                                                                                                                |
| exponent1       | Exponent 1. This has a numeric value of d mod (p – 1).                                                                                                                                                        |
| exponent2       | Exponent 2. This has a numeric value of d mod (q – 1).                                                                                                                                                        |
| Modulus         | The modulus. This has a value of *Prime1*×*Prime2* and is often known as n.                                                                                                                                   |
| prime1          | Prime number 1, often known as p.                                                                                                                                                                             |
| prime2          | Prime number 2, often known as q.                                                                                                                                                                             |
| privateExponent | Private exponent, often known as d.                                                                                                                                                                           |
| publickeystruc  | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                         |
| rsapubkey       | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-_rsapubkey) structure. The **magic** member must be set to 0x32415352. This hexadecimal value is the [*ASCII*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02) encoding of RSA2. |



 

> [!Note]  
> Private key BLOBs are not encrypted. They contain private keys in plaintext form.

 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> \[!Caution\]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

## Simple Key BLOBs

[*Simple key BLOBs*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50), type **SIMPLEBLOB**, are used to store and transport session keys outside a CSP. Extended provider simple key BLOBs are always encrypted with a [*key exchange public key*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33). The **pbData** member of the **SIMPLEBLOB** is a sequence of bytes in the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
ALG_ID algid;
BYTE encryptedkey[rsapubkey.bitlen/8];
```

The following table describes each component of the **pbData** member of the **SIMPLEBLOB**.



| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algid          | An [**ALG\_ID**](alg-id.md) structure that specifies the encryption algorithm used to encrypt the session key data. This typically has a value of CALG\_RSA\_KEYX, which indicates that the session key data was encrypted with a key exchange public key using the [*RSA Public Key algorithm*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd).                                                                                                                           |
| encryptedkey   | A **BYTE** sequence that represents the encrypted session key data in the form of a PKCS \#1, type 2 encryption block. For information about this data format, see the Public Key Cryptography Standards (PKCS) \#1, published by RSA Data Security, Inc. This data is always the same size as the modulus of the public key. For example, public keys generated by the Microsoft RSA Base Provider can be 512 bits (64 bytes) in length, so the encrypted session key data is also always 512 bits (64 bytes).<br/> |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-_publickeystruc) structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

For information about the Base Provider and Extended Provider key BLOBs, see [Base Provider Key BLOBs](base-provider-key-blobs.md).

 

 




