---
description: BLOBs are used with the Diffie-Hellman/Schannel provider to export keys from, and import keys into, the cryptographic service provider (CSP).
ms.assetid: ebb85b7c-204d-4b1c-86dc-5a03c8eda47b
title: Diffie-Hellman/Schannel Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# Diffie-Hellman/Schannel Key BLOBs

[*BLOBs*](../secgloss/b-gly.md) are used with the [*Diffie-Hellman*](../secgloss/d-gly.md)/[*Schannel*](../secgloss/s-gly.md) provider to export keys from, and import keys into, the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

-   [Public Key BLOBs](#public-key-blobs)
-   [Private Key BLOBs](#private-key-blobs)

## Public Key BLOBs

Diffie-Hellman [*public key BLOBs*](../secgloss/p-gly.md), type **PUBLICKEYBLOB**, are used to exchange the (G^X) mod P value in a Diffie-Hellman key exchange. These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
DHPUBKEY        dhpubkey;
BYTE            y[dhpubkey.bitlen/8]; // Where y = (G^X) mod P
```

The following table describes each component of the [*key BLOB*](../secgloss/k-gly.md).



| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dhpubkey       | A [**DHPUBKEY**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey) structure. The **magic** member must be set to 0x31484400. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of DH1.                                                                                                                                                                                                                                                                                                                                                      |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| y              | A **BYTE** sequence. The y value, (G^X) mod P, is located directly after the [**DHPUBKEY**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey) structure. The length, in bytes, of the sequence is the **bitlen** member of **DHPUBKEY** divided by eight. If the length of the data that results from the calculation of (G^X) mod P is one or more bytes shorter than P divided by eight, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](../secgloss/l-gly.md) format). |



 

## Private Key BLOBs

D-H [*private key BLOBs*](../secgloss/p-gly.md), type **PRIVATEKEYBLOB**, are used to export and import private information of a D-H key. These keys are exported and imported as a sequence of bytes with the following format.

``` syntax
PUBLICKEYSTRUC  publickeystruc;
DHPUBKEY        dhpubkey;
BYTE            prime[dhpubkey.bitlen/8];
BYTE            generator[dhpubkey.bitlen/8];
BYTE            secret[dhpubkey.bitlen/8];
```

The following table describes each component of the key BLOB.



| Field          | Description                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dhpubkey       | A [**DHPUBKEY**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey) structure. The **magic** member must be set to 0x32484400. This hexadecimal value is the [*ASCII*](../secgloss/a-gly.md) encoding of DH2. |
| generator      | A **BYTE** sequence. The generator G.                                                                                                                                                                      |
| publickeystruc | A [**PUBLICKEYSTRUC**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure.                                                                                                                                                      |
| prime          | A **BYTE** sequence. The prime modulus, P. This data must always have the most significant bit of the most significant byte set to one.                                                                    |
| secret         | A **BYTE** sequence. The secret exponent X.                                                                                                                                                                |



 

> [!Note]  
> The prime, generator, and secret values must always have the same length, in bytes. If any value is one byte or more shorter than the others, it must be padded with the necessary number of zero bytes to make them the same. The prime, generator, and secret are in [*little-endian*](../secgloss/l-gly.md) format.

 

 

 
