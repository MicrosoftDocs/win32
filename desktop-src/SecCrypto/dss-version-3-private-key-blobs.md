---
description: Describes the format of an exported DSS version 3 private key.
ms.assetid: 650532fd-919b-495a-9fb9-981790447d3d
title: DSS Version 3 Private Key BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# DSS Version 3 Private Key BLOBs

When a version 3 [*DSS*](../secgloss/d-gly.md) [*private key*](../secgloss/p-gly.md) is exported, it is in a format as follows:


```C++
BLOBHEADER        blobheader; 
DSSPRIVKEY_VER3   dssprivkeyver3;
BYTE p[dssprivkeyver3.bitlenP/8]; 
                    // Where P is the prime modulus
BYTE q[dssprivkeyver3.bitlenQ/8]; 
                    // Where Q is a large factor of P-1
BYTE g[dssprivkeyver3.bitlenP/8]; 
                    // Where G is the generator parameter
BYTE j[dssprivkeyver3.bitlenJ/8]; 
                    // Where J is (P-1)/Q
BYTE y[dssprivkeyver3.bitlenP/8]; 
                    // Where Y is (G^X) mod P
BYTE x[dssprivkeyver3.bitlenX/8]; 
                    // Where X is the private exponent
```



This [*BLOB*](../secgloss/b-gly.md) format is exported when the CRYPT\_BLOB\_VER3 flag is used with [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey). Because the version is in the BLOB, there is no need to specify a flag when using this BLOB with [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey).

The following table describes each component of the [*key BLOB*](../secgloss/k-gly.md).



| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blobheader     | A [**BLOBHEADER**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) structure. The **bType** member must have a value of PUBLICKEYBLOB.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Dssprivkeyver3 | A **DSSPRIVKEY\_VER3** structure. The **magic** member should be set to "DSS4" (0x34535344) for private keys. Notice that the hexadecimal value is just an [*ASCII*](../secgloss/a-gly.md) encoding of "DSS4."<br/>                                                                                                                                                                                                                                                                     |
| P              | The P value is located directly after the **DSSPRIVKEY\_VER3** structure, and should always be the length, in bytes, of the **DSSPRIVKEY\_VER3 bitlenP** field (bit length of P) divided by eight ([*little-endian*](../secgloss/l-gly.md) format).                                                                                                                                                                                                                           |
| Q              | The Q value is located directly after the P value and should always be the length, in bytes, of the **DSSPRIVKEY\_VER3 bitlenQ** field divided by eight ([*little-endian*](../secgloss/l-gly.md) format).                                                                                                                                                                                                                                                                     |
| G              | The G value is located directly after the Q value and should always be the length, in bytes, of the **DSSPRIVKEY\_VER3 bitlenP** field (bit length of P) divided by eight. If the length of the data is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](../secgloss/l-gly.md) format).                                                                 |
| J              | The J value is located directly after the G value and should always be the length, in bytes, of the **DSSPRIVKEY\_VER3 bitlenJ** field divided by eight ([*little-endian*](../secgloss/l-gly.md) format). If the bitlenJ value is 0 then the value is absent from the BLOB.                                                                                                                                                                                                   |
| Y              | The Y value, (G^X) mod P, is located directly after the J value, and should always be the length, in bytes, of the **DSSPRIVKEY\_VER3 bitlenP** field (bit length of P) divided by eight. If the length of the data that results from the calculation of (G^X) mod P is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([*little-endian*](../secgloss/l-gly.md) format). |
| X              | The X value is a random large integer such that the public portion of the DH key pair, Y, is equal to: Y = (G^X) mod P<br/>                                                                                                                                                                                                                                                                                                                                                                                               |



 

When calling [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey), the developer can choose whether to encrypt the key. The key is encrypted if the *hExpKey* parameter contains a valid handle to a session key. Everything but the [**BLOBHEADER**](/windows/desktop/api/Wincrypt/ns-wincrypt-publickeystruc) portion of the BLOB is encrypted. Note that the encryption algorithm and encryption key parameters are not stored along with the [*private key BLOB*](../secgloss/p-gly.md). The application must manage and store this information. If zero is passed for *hExpKey*, the private key will be exported without encryption.

> [!IMPORTANT]
> It is dangerous to export private keys without encryption because they are then vulnerable to interception and use by unauthorized entities.

 

 

 
