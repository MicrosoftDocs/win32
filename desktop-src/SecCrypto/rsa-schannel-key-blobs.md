---
Description: BLOBs are used with the RSA/Schannel provider to export keys from, and import keys into, the cryptographic service provider (CSP).
ms.assetid: 97d5ee6d-4687-4cd2-b122-36f8ea3c93ca
title: RSA/Schannel Key BLOBs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSA/Schannel Key BLOBs

[*BLOBs*](security.b_gly#-security-blob-gly) are used with the [*RSA*](security.r_gly#-security-rsa-gly)/[*Schannel*](security.s_gly#-security-schannel-gly) provider to export keys from, and import keys into, the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)
-   [Simple Key BLOBs](#simple-key-blobs)

## Public Key BLOBs

[*Public key BLOBs*](security.p_gly#-security-public-key-blob-gly), type **PUBLICKEYBLOB**, are used to store [*public keys*](security.p_gly#-security-public-key-gly). These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc ;
RSAPUBKEY       rsapubkey;
BYTE            modulus[rsapubkey.bitlen/8];
```

The following table describes each public key component. All values are in [*little-endian*](security.l_gly#-security-little-endian-gly) format.



| Field          | Description                                                                                                                                                                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| modulus        | A **BYTE** sequence. The public key modulus data is located directly after the **RSAPUBKEY** structure. The length of this data varies, depending on the length of the public key. The number of bytes can be determined by dividing the value of the **bitlen** member of **RSAPUBKEY** by eight. |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) structure.                                                                                                                                                                                                                                              |
| rsapubkey      | A [**RSAPUBKEY**](/windows/win32/Wincrypt/ns-wincrypt-_rsapubkey?branch=master) structure. The **magic** member must be set to 0x31415352. This hexadecimal value is the [*ASCII*](security.a_gly#-security-ascii-gly) encoding of RSA1.                                                                                      |



 

> [!Note]  
> Public key BLOBs are not encrypted. They contain public keys in [*plaintext*](security.p_gly#-security-plaintext-gly) form.

 

## Private Key BLOBs

[*Private key BLOBs*](security.p_gly#-security-private-key-blob-gly), type **PRIVATEKEYBLOB**, are used to store [*public/private key pairs*](security.p_gly#-security-public-private-key-pair-gly). These keys are exported and imported as a sequence of bytes with the following format.

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

If the [*key BLOB*](security.k_gly#-security-key-blob-gly) is encrypted, then everything but the [**PUBLICKEYSTRUC**](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. It is the responsibility of the application to manage this information.

 

The following table describes each private key BLOB component.

> [!Note]  
> These fields correspond to the fields described in section 7.2 of [*Public Key Cryptography Standards*](security.p_gly#-security-public-key-cryptography-standards-gly) (PKCS) \#1 with minor differences.

 



| Field           | Description                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| exponent1       | A **BYTE** sequence. The first exponent. This has a numeric value of d mod (p – 1).                                                                                                                           |
| exponent2       | A **BYTE** sequence. The second exponent. This has a numeric value of d mod (q – 1).                                                                                                                          |
| coefficient     | A **BYTE** sequence. Coefficient. This has a numeric value of (inverse of q) mod p.                                                                                                                           |
| Modulus         | A **BYTE** sequence. The modulus. This has a string that contains *Prime1* \* *Prime2*. It is often known as n.                                                                                               |
| prime1          | A **BYTE** sequence. Prime number 1, often known as p.                                                                                                                                                        |
| prime2          | A **BYTE** sequence. Prime number 2, often known as q.                                                                                                                                                        |
| publickeystruc  | A [**PUBLICKEYSTRUC**](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) structure.                                                                                                                                                         |
| privateExponent | A **BYTE** sequence. The private exponent, often known as d.                                                                                                                                                  |
| rsapubkey       | A [**RSAPUBKEY**](/windows/win32/Wincrypt/ns-wincrypt-_rsapubkey?branch=master) structure. The **magic** member must be set to 0x32415352. This hexadecimal value is the [*ASCII*](security.a_gly#-security-ascii-gly) encoding of RSA2. |



 

> [!Note]  
> Private key BLOBs are not encrypted. They contain private keys in plaintext form.

 

When calling [**CryptExportKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptexportkey?branch=master), the developer can choose whether to encrypt the key. The **PRIVATEKEYBLOB** is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**PUBLICKEYSTRUC**](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) portion of the BLOB is encrypted.

> [!Note]  
> The encryption algorithm and encryption key parameters are not stored along with the private key BLOB. The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

 

> \[!Caution\]  
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

## Simple Key BLOBs

[*Simple key BLOBs*](security.s_gly#-security-simple-key-blob-gly), type **SIMPLEBLOB**, are used to store and transport session keys. These are always encrypted with a [*key exchange public key*](security.k_gly#-security-key-exchange-public-key-gly). These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc ;
ALG_ID          algid;
BYTE            encryptedkey[rsapubkey.bitlen/8];
```

The following table describes each simple BLOB component.



| Field          | Description                                                                                                                                                                                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| algid          | An [**ALG\_ID**](alg-id.md) structure. This typically specifies the CALG\_RSA\_KEYX algorithm, which indicates that the session key data was encrypted with a key exchange public key, using the [*RSA Public Key algorithm*](security.r_gly#-security-rsa-public-key-algorithm-gly). |
| encryptedkey   | A **BYTE** sequence. The encrypted session key data is in the form of a PKCS \#1, type 2 encryption block. For information about this data format, see the Public Key Cryptography Standards (PKCS), published by RSA Data Security, Inc.                                                                                     |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) structure.                                                                                                                                                                                                                                                                         |



 

This data is always the same size as the modulus of the public key. For example, public keys generated by the Microsoft Base Cryptographic Provider are always 512 bits (64 bytes) in length, so the encrypted session key data is also always 64 bytes.

 

 



