---
description: Diffie-Hellman version 3 Public Key BLOBs (type PUBLICKEYBLOB) are used to export and import information about a DH public key.
ms.assetid: ba29a71a-7509-49c7-93d2-f0a699532706
title: Diffie-Hellman Version 3 Public Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# Diffie-Hellman Version 3 Public Key BLOBs

Diffie-Hellman version 3 [*Public Key BLOBs*](../secgloss/p-gly.md) (type PUBLICKEYBLOB) are used to export and import information about a DH public key. They have the following format:


```C++
BLOBHEADER blobheader; 
                 // As explained under "Data Structures"
DHPUBKEY_VER3 dhpubkeyver3;
BYTE p[dhpubkeyver3.bitlenP/8]; 
                 // Where P is the prime modulus
BYTE q[dhpubkeyver3.bitlenQ/8]; 
                 // Where Q is a large factor of P-1
BYTE g[dhpubkeyver3.bitlenP/8]; 
                 // Where G is the generator parameter
BYTE j[dhpubkeyver3.bitlenJ/8]; 
                 // Where J is (P-1)/Q
BYTE y[dhpubkeyver3.bitlenP/8]; 
                 // Where Y is (G^X) mod P
```



This BLOB format is exported when the CRYPT\_BLOB\_VER3 flag is used with [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey). Because the version is in the BLOB, there is no need to specify a flag when using this [*BLOB*](../secgloss/b-gly.md) with [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey).

In addition, this BLOB format is used with the [**CryptSetKeyParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam) function when the *dwParam* value KP\_PUB\_PARAMS is used to set key parameters on a DH key. This is done when the CRYPT\_PREGEN flag has been used to generate the key. When used in this situation, the y value is ignored and therefore should not be included in the BLOB.

The following table describes each component of the key BLOB.



| Field        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| blobheader   | A [**BLOBHEADER**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure. The **bType** member must have a value of PUBLICKEYBLOB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| dhpubkeyver3 | A [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) structure. The **magic** member should be set to 0x33484400 for public keys. Notice that the hexadecimal value is just an [*ASCII*](../secgloss/a-gly.md) encoding of "DH3".                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| P            | The P value is located directly after the [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) structure and should always be the length, in bytes, of the **DHPUBKEY\_VER3** **bitlenP** field (bit length of P) divided by eight ([*little-endian*](../secgloss/l-gly.md) format).                                                                                                                                                                                                                                                                                                                                                                                           |
| Q            | The Q value is located directly after the P value and should always be the length in bytes of the [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) **bitlenQ** field divided by eight ([*little-endian*](../secgloss/l-gly.md) format). If the bitlenQ value is 0, then the value is absent from the BLOB.                                                                                                                                                                                                                                                                                                                                                                 |
| G            | The G value is located directly after the Q value and should always be the length, in bytes, of the [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) **bitlenP** field (bit length of P) divided by eight. If the length of the data is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](../secgloss/l-gly.md) format).                                                                                                                                                                                                                              |
| J            | The J value is located directly after the G value and should always be the length in bytes of the [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) **bitlenJ** field divided by eight ([*little-endian*](../secgloss/l-gly.md) format). If the bitlenQ value is 0, then the value is absent from the BLOB.                                                                                                                                                                                                                                                                                                                                                                 |
| Y            | The Y value, (G^X) mod P, is located directly after the J value and should always be the length in bytes of the [**DHPUBKEY\_VER3**](/windows/win32/api/wincrypt/ns-wincrypt-dhpubkey_ver3) **bitlenP** field (bit length of P) divided by eight. If the length of the data that results from the calculation of (G^X) mod P is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](../secgloss/l-gly.md) format). When this structure is used with [**CryptSetKeyParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptsetkeyparam) with the *dwParam* value KP\_PUB\_PARAMS, this value is not included in the BLOB. |



 

> [!Note]  
> Public key BLOBs are not encrypted, but contain public keys in plaintext form.

 

 

 
