---
description: BLOBs are used with the RSA/Schannel provider to export keys from, and import keys into, the cryptographic service provider (CSP).
ms.assetid: 97d5ee6d-4687-4cd2-b122-36f8ea3c93ca
title: RSA/Schannel Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# RSA/Schannel Key BLOBs

[*BLOBs*](../secgloss/b-gly.md) are used with the [*RSA*](../secgloss/r-gly.md)/[*Schannel*](../secgloss/s-gly.md) provider to export keys from, and import keys into, the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)
-   [Simple Key BLOBs](#simple-key-blobs)

## Public Key BLOBs

[*Public key BLOBs*](../secgloss/p-gly.md), type **PUBLICKEYBLOB**, are used to store [*public keys*](../secgloss/p-gly.md). These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc ;
RSAPUBKEY       rsapubkey;
BYTE            modulus[rsapubkey.bitlen/8];
```

The following table describes each public key component. All values are in [*little-endian*](../secgloss/l-gly.md) format.



| Field          | Description                                                                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| modulus        | A **BYTE** sequence. The public key modulus data is located directly after the **RSAPUBKEY** structure. The length of this data varies, depending on the length of the public key. The number of bytes can be determined by dividing the value of the **bitlen** member of **RSAPUBKEY** by eight. |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                                                                                                              |
| rsapubkey      | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-rsapubkey) structure. The **magic** member must be set to 0x31415352. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of RSA1.                                                                                      |



 

> [!Note]  
> Public key BLOBs are not encrypted. They contain public keys in [*plaintext*](../secgloss/p-gly.md) form.

 

## Private Key BLOBs

[*Private key BLOBs*](../secgloss/p-gly.md), type **PRIVATEKEYBLOB**, are used to store [*public/private key pairs*](../secgloss/p-gly.md). These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc ;
RSAPUBKEY       rsapubkey;
BYTE            modulus[rsapubkey.bitlen/8];
BYTE            prime1[rsapubkey.bitlen/16];
BYTE            prime2[rsapubkey.bitlen/16];
BYTE            exponent1[rsapubkey.bitlen/16];
BYTE            exponent2[rsapubkey.bitlen/16];
BYTE            coefficient[rsapubkey.bitlen/16];
BYTE            privateExponent[rsapubkey.bitlen/8];
```

If the [*key BLOB*](../secgloss/k-gly.md) is encrypted, then everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. It is the responsibility of the application to manage this information.

 

The following table describes each private key BLOB component.

> [!Note]  
> These fields correspond to the fields described in section 7.2 of [*Public Key Cryptography Standards*](../secgloss/p-gly.md) (PKCS) \#1 with minor differences.

 



| Field           | Description                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| exponent1       | A **BYTE** sequence. The first exponent. This has a numeric value of d mod (p – 1).                                                                                                                           |
| exponent2       | A **BYTE** sequence. The second exponent. This has a numeric value of d mod (q – 1).                                                                                                                          |
| coefficient     | A **BYTE** sequence. Coefficient. This has a numeric value of (inverse of q) mod p.                                                                                                                           |
| Modulus         | A **BYTE** sequence. The modulus. This has a string that contains *Prime1* \* *Prime2*. It is often known as n.                                                                                               |
| prime1          | A **BYTE** sequence. Prime number 1, often known as p.                                                                                                                                                        |
| prime2          | A **BYTE** sequence. Prime number 2, often known as q.                                                                                                                                                        |
| publickeystruc  | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                         |
| privateExponent | A **BYTE** sequence. The private exponent, often known as d.                                                                                                                                                  |
| rsapubkey       | A [**RSAPUBKEY**](/windows/desktop/api/Wincrypt/ns-wincrypt-rsapubkey) structure. The **magic** member must be set to 0x32415352. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of RSA2. |



 

> [!Note]  
> Private key BLOBs are not encrypted. They contain private keys in plaintext form.

 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> [!Caution]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

## Simple Key BLOBs

[*Simple key BLOBs*](../secgloss/s-gly.md), type **SIMPLEBLOB**, are used to store and transport session keys. These are always encrypted with a [*key exchange public key*](../secgloss/k-gly.md). These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc ;
ALG_ID          algid;
BYTE            encryptedkey[rsapubkey.bitlen/8];
```

The following table describes each simple BLOB component.



| Field          | Description                                                                                                                                                                                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algid          | An [**ALG\_ID**](alg-id.md) structure. This typically specifies the CALG\_RSA\_KEYX algorithm, which indicates that the session key data was encrypted with a key exchange public key, using the [*RSA Public Key algorithm*](../secgloss/r-gly.md). |
| encryptedkey   | A **BYTE** sequence. The encrypted session key data is in the form of a PKCS \#1, type 2 encryption block. For information about this data format, see the Public Key Cryptography Standards (PKCS), published by RSA Data Security, Inc.                                                                                     |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                                                                                                                                         |



 

This data is always the same size as the modulus of the public key. For example, public keys generated by the Microsoft Base Cryptographic Provider are always 512 bits (64 bytes) in length, so the encrypted session key data is also always 64 bytes.

 

 
