---
description: Specifies an algorithm identifier.
ms.assetid: 557436b4-f7f1-4708-acc7-c6b47e6322ad
title: ALG_ID (Wincrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ALG_ID

The **ALG_ID** data type specifies an algorithm identifier. Parameters of this data type are passed to most of the functions in CryptoAPI.


```C++
typedef unsigned int ALG_ID;
```



The following table lists the algorithm identifiers that are currently defined. Authors of custom [*cryptographic service providers*](../secgloss/c-gly.md) (CSPs) can define new values. Also, the **ALG_ID** used by custom CSPs for the key specifications **AT_KEYEXCHANGE** and **AT_SIGNATURE** are provider dependent. Current mappings follow the table.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Identifier</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CALG_3DES</td>
<td>0x00006603</td>
<td><a href="/windows/desktop/SecGloss/t-gly"><em>Triple DES</em></a> encryption algorithm.</td>
</tr>
<tr class="even">
<td>CALG_3DES_112</td>
<td>0x00006609</td>
<td>Two-key <a href="/windows/desktop/SecGloss/t-gly"><em>triple DES</em></a> encryption with effective key length equal to 112 bits.</td>
</tr>
<tr class="odd">
<td>CALG_AES</td>
<td>0x00006611</td>
<td>Advanced Encryption Standard (AES). This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_AES_128</td>
<td>0x0000660e</td>
<td>128 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_AES_192</td>
<td>0x0000660f</td>
<td>192 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_AES_256</td>
<td>0x00006610</td>
<td>256 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_AGREEDKEY_ANY</td>
<td>0x0000aa03</td>
<td>Temporary algorithm identifier for handles of Diffie-Hellman–agreed keys.</td>
</tr>
<tr class="even">
<td>CALG_CYLINK_MEK</td>
<td>0x0000660c</td>
<td>An algorithm to create a 40-bit DES key that has parity bits and zeroed key bits to make its key length 64 bits. This algorithm is supported by the <a href=""></a><a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_DES</td>
<td>0x00006601</td>
<td>DES encryption algorithm.</td>
</tr>
<tr class="even">
<td>CALG_DESX</td>
<td>0x00006604</td>
<td>DESX encryption algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_DH_EPHEM</td>
<td>0x0000aa02</td>
<td>Diffie-Hellman ephemeral key exchange algorithm.</td>
</tr>
<tr class="even">
<td>CALG_DH_SF</td>
<td>0x0000aa01</td>
<td>Diffie-Hellman store and forward key exchange algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_DSS_SIGN</td>
<td>0x00002200</td>
<td>DSA <a href="/windows/desktop/SecGloss/p-gly"><em>public key</em></a> signature algorithm.</td>
</tr>
<tr class="even">
<td>CALG_ECDH</td>
<td>0x0000aa05</td>
<td>Elliptic curve Diffie-Hellman key exchange algorithm.
<blockquote>
[!Note]<br />
This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.
</blockquote>
<br/> <strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="odd">
<td>CALG_ECDH_EPHEM</td>
<td>0x0000ae06</td>
<td>Ephemeral elliptic curve Diffie-Hellman key exchange algorithm.
<blockquote>
[!Note]<br />
This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.
</blockquote>
<br/> <strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="even">
<td>CALG_ECDSA</td>
<td>0x00002203</td>
<td>Elliptic curve digital signature algorithm.
<blockquote>
[!Note]<br />
This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.
</blockquote>
<br/> <strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="odd">
<td>CALG_ECMQV</td>
<td>0x0000a001</td>
<td>Elliptic curve Menezes, Qu, and Vanstone (MQV) key exchange algorithm. This algorithm is not supported.</td>
</tr>
<tr class="even">
<td>CALG_HASH_REPLACE_OWF</td>
<td>0x0000800b</td>
<td>One way function hashing algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_HUGHES_MD5</td>
<td>0x0000a003</td>
<td>Hughes MD5 hashing algorithm.</td>
</tr>
<tr class="even">
<td>CALG_HMAC</td>
<td>0x00008009</td>
<td>HMAC keyed hash algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_KEA_KEYX</td>
<td>0x0000aa04</td>
<td>KEA key exchange algorithm (FORTEZZA). This algorithm is not supported.</td>
</tr>
<tr class="even">
<td>CALG_MAC</td>
<td>0x00008005</td>
<td><a href="/windows/desktop/SecGloss/m-gly"><em>MAC</em></a> keyed hash algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_MD2</td>
<td>0x00008001</td>
<td>MD2 hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_MD4</td>
<td>0x00008002</td>
<td>MD4 hashing algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_MD5</td>
<td>0x00008003</td>
<td>MD5 hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_NO_SIGN</td>
<td>0x00002000</td>
<td>No signature algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_OID_INFO_CNG_ONLY</td>
<td>0xffffffff</td>
<td>The algorithm is only implemented in CNG. The macro, IS_SPECIAL_OID_INFO_ALGID, can be used to determine whether a cryptography algorithm is only supported by using the CNG functions.</td>
</tr>
<tr class="even">
<td>CALG_OID_INFO_PARAMETERS</td>
<td>0xfffffffe</td>
<td>The algorithm is defined in the encoded parameters. The algorithm is only supported by using CNG. The macro, IS_SPECIAL_OID_INFO_ALGID, can be used to determine whether a cryptography algorithm is only supported by using the CNG functions.</td>
</tr>
<tr class="odd">
<td>CALG_PCT1_MASTER</td>
<td>0x00004c04</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_RC2</td>
<td>0x00006602</td>
<td>RC2 block encryption algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_RC4</td>
<td>0x00006801</td>
<td>RC4 stream encryption algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_RC5</td>
<td>0x0000660d</td>
<td>RC5 block encryption algorithm.</td>
</tr>
<tr class="odd">
<td>CALG_RSA_KEYX</td>
<td>0x0000a400</td>
<td>RSA public key exchange algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_RSA_SIGN</td>
<td>0x00002400</td>
<td>RSA public key signature algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_SCHANNEL_ENC_KEY</td>
<td>0x00004c07</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_SCHANNEL_MAC_KEY</td>
<td>0x00004c03</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="odd">
<td>CALG_SCHANNEL_MASTER_HASH</td>
<td>0x00004c02</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_SEAL</td>
<td>0x00006802</td>
<td>SEAL encryption algorithm. This algorithm is not supported.</td>
</tr>
<tr class="odd">
<td>CALG_SHA</td>
<td>0x00008004</td>
<td>SHA hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="even">
<td>CALG_SHA1</td>
<td>0x00008004</td>
<td>Same as <strong>CALG_SHA</strong>. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>.</td>
</tr>
<tr class="odd">
<td>CALG_SHA_256</td>
<td>0x0000800c</td>
<td>256 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider..<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br/> <strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="even">
<td>CALG_SHA_384</td>
<td>0x0000800d</td>
<td>384 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider.<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br/> <strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="odd">
<td>CALG_SHA_512</td>
<td>0x0000800e</td>
<td>512 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider.<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br/> <strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br/></td>
</tr>
<tr class="even">
<td>CALG_SKIPJACK</td>
<td>0x0000660a</td>
<td>Skipjack block encryption algorithm (FORTEZZA). This algorithm is not supported.</td>
</tr>
<tr class="odd">
<td>CALG_SSL2_MASTER</td>
<td>0x00004c05</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_SSL3_MASTER</td>
<td>0x00004c01</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="odd">
<td>CALG_SSL3_SHAMD5</td>
<td>0x00008008</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_TEK</td>
<td>0x0000660b</td>
<td>TEK (FORTEZZA). This algorithm is not supported.</td>
</tr>
<tr class="odd">
<td>CALG_TLS1_MASTER</td>
<td>0x00004c06</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
<tr class="even">
<td>CALG_TLS1PRF</td>
<td>0x0000800a</td>
<td>Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications.</td>
</tr>
</tbody>
</table>



 

For the [Microsoft Base Cryptographic Provider](microsoft-base-cryptographic-provider.md), the [Microsoft Strong Cryptographic Provider](microsoft-strong-cryptographic-provider.md), and the [Microsoft Enhanced Cryptographic Provider](microsoft-enhanced-cryptographic-provider.md), the **ALG_IDs** used for the key specifications **AT_KEYEXCHANGE** and **AT_SIGNATURE** are as follows:

-   **CALG_RSA_KEYX** is used for **AT_KEYEXCHANGE**.
-   **CALG_RSA_SIGN** is used for **AT_SIGNATURE**.

For the [Microsoft Base DSS and Diffie-Hellman Cryptographic Provider](microsoft-base-dss-and-diffie-hellman-cryptographic-provider.md), the **ALG_IDs** used for the key specifications **AT_KEYEXCHANGE** and **AT_SIGNATURE** are as follows:

-   **CALG_DH_SF** is used for **AT_KEYEXCHANGE**.
-   **CALG_DSS_SIGN** is used for **AT_SIGNATURE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Wincrypt.h</dt> </dl> |



## See also

<dl> <dt>

[Cryptography Functions](cryptography-functions.md)
</dt> <dt>

[**CRYPT_ALGORITHM_IDENTIFIER**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_algorithm_identifier)
</dt> <dt>

[**CryptFindOIDInfo**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptfindoidinfo)
</dt> </dl>

 

 
