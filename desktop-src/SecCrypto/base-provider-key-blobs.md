---
description: The Base Provider and Extended Provider use the same key BLOBs.
ms.assetid: b4592036-0fa3-4b7e-beed-78cf1d2f39a9
title: Base Provider Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# Base Provider Key BLOBs

The Base Provider and Extended Provider use the same [*key BLOBs*](../secgloss/k-gly.md).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)
-   [Simple Key BLOBs](#simple-key-blobs)

## Public Key BLOBs

[*Public key BLOBs*](../secgloss/p-gly.md), type **PUBLICKEYBLOB**, are used to store [*public keys*](../secgloss/p-gly.md) outside a [*cryptographic service provider*](../secgloss/c-gly.md) (CSP). Base provider public key BLOBs have the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
RSAPUBKEY rsapubkey;
BYTE modulus[rsapubkey.bitlen/8];
```

The following table describes each public key component. All values are in [*little-endian*](../secgloss/l-gly.md) format.



| Field          | Description                                                                                                                                                                                                                                                                           |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| modulus        | The public key modulus data is located directly after the [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-rsapubkey) structure. The size of this data will vary, depending on the size of the public key. The number of bytes can be determined by dividing the value of the **RSAPUBKEY bitlen** field by eight. |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                                                                                                 |
| rsapubkey      | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-rsapubkey) structure. The **magic** member must be set to 0x31415352. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of RSA1.                                                                         |



 

> [!Note]  
> Public key BLOBs are not encrypted. They contain public keys in [*plaintext*](../secgloss/p-gly.md) form.

 

## Private Key BLOBs

[*Private key BLOBs*](../secgloss/p-gly.md), type **PRIVATEKEYBLOB**, are used to store [*private keys*](../secgloss/p-gly.md) outside a CSP. Base provider private key BLOBs have the following format.

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
> These fields correspond to the fields described in section 7.2 of [*Public Key Cryptography Standards*](../secgloss/p-gly.md) (PKCS) \#1 with minor differences.

 



| Field           | Description                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| coefficient     | Coefficient. This has a numeric value of (inverse of q) mod p.                                                                                                                                                |
| exponent1       | Exponent 1. This has a numeric value of d mod (p – 1).                                                                                                                                                        |
| exponent2       | Exponent 2. This has a numeric value of d mod (q – 1).                                                                                                                                                        |
| Modulus         | The modulus. This has a value of *Prime1*×*Prime2* and is often known as n.                                                                                                                                   |
| prime1          | Prime number 1, often known as p.                                                                                                                                                                             |
| prime2          | Prime number 2, often known as q.                                                                                                                                                                             |
| privateExponent | Private exponent, often known as d.                                                                                                                                                                           |
| publickeystruc  | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                         |
| rsapubkey       | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-rsapubkey) structure. The **magic** member must be set to 0x32415352. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of RSA2. |



 

> [!Note]  
> Private key BLOBs are not encrypted. They contain private keys in plaintext form.

 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> [!Caution]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

## Simple Key BLOBs

[*Simple key BLOBs*](../secgloss/s-gly.md), type **SIMPLEBLOB**, are used to store and transport session keys outside a CSP. Base provider simple key BLOBs are always encrypted with a [*key exchange public key*](../secgloss/k-gly.md). The **pbData** member of the **SIMPLEBLOB** is a sequence of bytes in the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
ALG_ID algid;
BYTE encryptedkey[rsapubkey.bitlen/8];
```

The following table describes each component of the **pbData** member of the **SIMPLEBLOB**.



| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algid          | An [**ALG\_ID**](alg-id.md) structure that specifies the encryption algorithm used to encrypt the session key data. This typically has a value of CALG\_RSA\_KEYX, which indicates that the session key data was encrypted with a key exchange public key using the [*RSA Public Key algorithm*](../secgloss/r-gly.md).                                                                                                                           |
| encryptedkey   | A **BYTE** sequence that represents the encrypted session key data in the form of a PKCS \#1, type 2 encryption block. For information about this data format, see the Public Key Cryptography Standards (PKCS) \#1, published by RSA Data Security, Inc. This data is always the same size as the modulus of the public key. For example, public keys generated by the Microsoft RSA Base Provider can be 512 bits (64 bytes) in length, so the encrypted session key data is also always 512 bits (64 bytes).<br/> |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

 

 
