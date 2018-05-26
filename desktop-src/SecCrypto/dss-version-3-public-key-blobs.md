---
Description: DSS version 3 Public Key BLOBs of type PUBLICKEYBLOB are used to export and import information about a DH public key.
ms.assetid: 9aac1d61-8b61-4f0f-b037-afe4a60302de
title: DSS Version 3 Public Key BLOBs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DSS Version 3 Public Key BLOBs

DSS version 3 [*Public Key BLOBs*](security.p_gly#-security-public-key-blob-gly) of type PUBLICKEYBLOB are used to export and import information about a DH public key. They have the following format:


```C++
BLOBHEADER blobheader; 
        // As explained under "Data Structures"
DSSPUBKEY_VER3 dsspubkeyver3;
BYTE p[dsspubkeyver3.bitlenP/8]; 
       // Where P is the prime modulus
BYTE q[dsspubkeyver3.bitlenQ/8]; 
       // Where Q is a large factor of P-1
BYTE g[dsspubkeyver3.bitlenP/8]; 
       // Where G is the generator parameter
BYTE j[dsspubkeyver3.bitlenJ/8]; 
       // Where J is (P-1)/Q
BYTE y[dsspubkeyver3.bitlenP/8]; 
       // Where Y is (G^X) mod P
```



This [*BLOB*](security.b_gly#-security-blob-gly) format is exported when the CRYPT\_BLOB\_VER3 flag is used with [**CryptExportKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptexportkey?branch=master). Because the version is in the BLOB, there is no need to specify a flag when using this BLOB with [**CryptImportKey**](/windows/win32/Wincrypt/nf-wincrypt-cryptimportkey?branch=master).

In addition, this BLOB format is used with the [**CryptSetKeyParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyparam?branch=master) function when the *dwParam* value KP\_PUB\_PARAMS is used to set key parameters on a DSS key. This is done when the CRYPT\_PREGEN flag has been used to generate the key. When used in this situation, the y value is ignored and therefore should not be included in the BLOB.

The following table describes each component of the key BLOB.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Blobheader</td>
<td>A [<strong>BLOBHEADER</strong>](/windows/win32/Wincrypt/ns-wincrypt-_publickeystruc?branch=master) structure. The <strong>bType</strong> member must have a value of PUBLICKEYBLOB.</td>
</tr>
<tr class="even">
<td>Dsspubkeyver3</td>
<td>A [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master) structure. The <strong>magic</strong> member should be set to &quot;DSS3&quot; (0x33535344) for public keys. Notice that the hexadecimal value is just an [<em>ASCII</em>](security.a_gly#-security-ascii-gly) encoding of &quot;DSS3.&quot;<br/></td>
</tr>
<tr class="odd">
<td>P</td>
<td>The P value is located directly after the [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master) structure, and should always be the length, in bytes, of the DSSPUBKEY_VER3 <strong>bitlenP</strong> field (bit length of P) divided by eight ([<em>little-endian</em>](security.l_gly#-security-little-endian-gly) format).</td>
</tr>
<tr class="even">
<td>Q</td>
<td>The Q value is located directly after the P value and should always be the length in bytes of the [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master)<strong>bitlenQ</strong> member divided by eight ([<em>little-endian</em>](security.l_gly#-security-little-endian-gly) format).</td>
</tr>
<tr class="odd">
<td>G</td>
<td>The G value is located directly after the Q value and should always be the length, in bytes, of the [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master)<strong>bitlenP</strong> member (bit length of P) divided by eight. If the length of the data is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([<em>little-endian</em>](security.l_gly#-security-little-endian-gly) format).</td>
</tr>
<tr class="even">
<td>J</td>
<td>The J value is located directly after the G value and should always be the length in bytes of the [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master)<strong>bitlenJ</strong> member divided by eight ([<em>little-endian</em>](security.l_gly#-security-little-endian-gly) format). If the bitlenQ value is 0, then the value is absent from the BLOB.</td>
</tr>
<tr class="odd">
<td>Y</td>
<td>The Y value, (G^X) mod P, is located directly after the J value, and should always be the length, in bytes, of the [<strong>DSSPUBKEY_VER3</strong>](/windows/win32/Wincrypt/?branch=master)<strong>bitlenP</strong> member (bit length of P) divided by eight. If the length of the data that results from the calculation of (G^X) mod P is one or more bytes shorter than P divided by 8, the data must be padded with the necessary bytes (of zero value) to make the data the desired length ([<em>little-endian</em>](security.l_gly#-security-little-endian-gly) format).
<blockquote>
[!Note]<br />
When this structure is used with [<strong>CryptSetKeyParam</strong>](/windows/win32/Wincrypt/nf-wincrypt-cryptsetkeyparam?branch=master) with the <em>dwParam</em> value KP_PUB_PARAMS, then this value is not included in the BLOB.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> Public key BLOBs are not encrypted, but contain public keys in plaintext form.

 

 

 




