---
Description: 'BLOBs are used with the Diffie-Hellman provider to export keys from, and import keys into, the cryptographic service provider (CSP).'
ms.assetid: '052f2108-d402-41a0-b4ac-e93ba6b06b49'
title: 'Diffie-Hellman Key BLOBs'
---

# Diffie-Hellman Key BLOBs

[*BLOBs*](security.b_gly#-security-blob-gly) are used with the [*Diffie-Hellman*](security.d_gly#-security-diffie-hellman-algorithm-gly) provider to export keys from, and import keys into, the [*cryptographic service provider*](security.c_gly#-security-cryptographic-service-provider-gly) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)

## Public Key BLOBs

Diffie-Hellman [*public key BLOBs*](security.p_gly#-security-public-key-blob-gly), type **PUBLICKEYBLOB**, are used to exchange the (G^X) mod P value in a Diffie-Hellman key exchange. These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc; 
DHPUBKEY dhpubkey;
BYTE y[dhpubkey.bitlen/8]; // Where y = (G^X) mod P
```

The following table describes each component of the [*key BLOB*](security.k_gly#-security-key-blob-gly).



| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dhpubkey       | A [**DHPUBKEY**](dhpubkey.md) structure. The **magic** member should be set to 0x31484400. This hexadecimal value is the [*ASCII*](security.a_gly#-security-ascii-gly) encoding of "DH1".                                                                                                                                                                                                                                                                                                                                                                 |
| publickeystruc | A [**PUBLICKEYSTRUC**](publickeystruc.md) structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| y              | A **BYTE** sequence. The Y value, (G^X) mod P, is located directly after the [**DHPUBKEY**](dhpubkey.md) structure, and should always be the length, in bytes, of the **DHPUBKEY bitlen** field (bit length of P) divided by eight. If the length of the data that results from the calculation of (G^X) mod P is one or more bytes shorter than P divided by eight, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](security.l_gly#-security-little-endian-gly) format). |



 

## Private Key BLOBs

Diffie-Hellman [*private key BLOBs*](security.p_gly#-security-private-key-blob-gly), type **PRIVATEKEYBLOB**, are used to store the public/private information of a Diffie-Hellman key. These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc; 
DHPUBKEY        dhpubkey;
BYTE            prime[dhpubkey.bitlen/8];
BYTE            generator[dhpubkey.bitlen/8];
BYTE            secret[dhpubkey.bitlen/8];
```

The following table describes each component of the key BLOB.



| Field          | Description                                                                                                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dhpubkey       | A [**DHPUBKEY**](dhpubkey.md) structure. The **magic** member must be set to 0x32484400. This hexadecimal value is the [*ASCII*](security.a_gly#-security-ascii-gly) encoding of "DH2". |
| generator      | A **BYTE** sequence. The generator, G.                                                                                                                                                                       |
| publickeystruc | A [**PUBLICKEYSTRUC**](publickeystruc.md) structure.                                                                                                                                                        |
| prime          | A **BYTE** sequence. The prime modulus, P. This data must always have the most significant bit of the most significant byte set to one.                                                                      |
| secret         | A **BYTE** sequence. The secret exponent, X.                                                                                                                                                                 |



 

> [!Note]  
> The generator and secret must always have the same length, in bytes. If either is one byte or more shorter than the other, it must be padded with the necessary number of zero value bytes to make them the same. Both the generator and the secret are in [*little-endian*](security.l_gly#-security-little-endian-gly) format.

 

 

 



