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




| Identifier | Value | Description | 
|------------|-------|-------------|
| CALG_3DES | 0x00006603 | <a href="/windows/desktop/SecGloss/t-gly"><em>Triple DES</em></a> encryption algorithm. | 
| CALG_3DES_112 | 0x00006609 | Two-key <a href="/windows/desktop/SecGloss/t-gly"><em>triple DES</em></a> encryption with effective key length equal to 112 bits. | 
| CALG_AES | 0x00006611 | Advanced Encryption Standard (AES). This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>. | 
| CALG_AES_128 | 0x0000660e | 128 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>. | 
| CALG_AES_192 | 0x0000660f | 192 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>. | 
| CALG_AES_256 | 0x00006610 | 256 bit AES. This algorithm is supported by the <a href="microsoft-aes-cryptographic-provider.md">Microsoft AES Cryptographic Provider</a>. | 
| CALG_AGREEDKEY_ANY | 0x0000aa03 | Temporary algorithm identifier for handles of Diffie-Hellman–agreed keys. | 
| CALG_CYLINK_MEK | 0x0000660c | An algorithm to create a 40-bit DES key that has parity bits and zeroed key bits to make its key length 64 bits. This algorithm is supported by the <a href=""></a><a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_DES | 0x00006601 | DES encryption algorithm. | 
| CALG_DESX | 0x00006604 | DESX encryption algorithm. | 
| CALG_DH_EPHEM | 0x0000aa02 | Diffie-Hellman ephemeral key exchange algorithm. | 
| CALG_DH_SF | 0x0000aa01 | Diffie-Hellman store and forward key exchange algorithm. | 
| CALG_DSS_SIGN | 0x00002200 | DSA <a href="/windows/desktop/SecGloss/p-gly"><em>public key</em></a> signature algorithm. | 
| CALG_ECDH | 0x0000aa05 | Elliptic curve Diffie-Hellman key exchange algorithm.<blockquote>[!Note]<br />This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.</blockquote><br /><strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_ECDH_EPHEM | 0x0000ae06 | Ephemeral elliptic curve Diffie-Hellman key exchange algorithm.<blockquote>[!Note]<br />This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.</blockquote><br /><strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_ECDSA | 0x00002203 | Elliptic curve digital signature algorithm.<blockquote>[!Note]<br />This algorithm is supported only through <a href="/windows/desktop/SecCNG/cng-portal">Cryptography API: Next Generation</a>.</blockquote><br /><strong>Windows Server 2003 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_ECMQV | 0x0000a001 | Elliptic curve Menezes, Qu, and Vanstone (MQV) key exchange algorithm. This algorithm is not supported. | 
| CALG_HASH_REPLACE_OWF | 0x0000800b | One way function hashing algorithm. | 
| CALG_HUGHES_MD5 | 0x0000a003 | Hughes MD5 hashing algorithm. | 
| CALG_HMAC | 0x00008009 | HMAC keyed hash algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_KEA_KEYX | 0x0000aa04 | KEA key exchange algorithm (FORTEZZA). This algorithm is not supported. | 
| CALG_MAC | 0x00008005 | <a href="/windows/desktop/SecGloss/m-gly"><em>MAC</em></a> keyed hash algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_MD2 | 0x00008001 | MD2 hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_MD4 | 0x00008002 | MD4 hashing algorithm. | 
| CALG_MD5 | 0x00008003 | MD5 hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_NO_SIGN | 0x00002000 | No signature algorithm. | 
| CALG_OID_INFO_CNG_ONLY | 0xffffffff | The algorithm is only implemented in CNG. The macro, IS_SPECIAL_OID_INFO_ALGID, can be used to determine whether a cryptography algorithm is only supported by using the CNG functions. | 
| CALG_OID_INFO_PARAMETERS | 0xfffffffe | The algorithm is defined in the encoded parameters. The algorithm is only supported by using CNG. The macro, IS_SPECIAL_OID_INFO_ALGID, can be used to determine whether a cryptography algorithm is only supported by using the CNG functions. | 
| CALG_PCT1_MASTER | 0x00004c04 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_RC2 | 0x00006602 | RC2 block encryption algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_RC4 | 0x00006801 | RC4 stream encryption algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_RC5 | 0x0000660d | RC5 block encryption algorithm. | 
| CALG_RSA_KEYX | 0x0000a400 | RSA public key exchange algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_RSA_SIGN | 0x00002400 | RSA public key signature algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_SCHANNEL_ENC_KEY | 0x00004c07 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_SCHANNEL_MAC_KEY | 0x00004c03 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_SCHANNEL_MASTER_HASH | 0x00004c02 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_SEAL | 0x00006802 | SEAL encryption algorithm. This algorithm is not supported. | 
| CALG_SHA | 0x00008004 | SHA hashing algorithm. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_SHA1 | 0x00008004 | Same as <strong>CALG_SHA</strong>. This algorithm is supported by the <a href="microsoft-base-cryptographic-provider.md">Microsoft Base Cryptographic Provider</a>. | 
| CALG_SHA_256 | 0x0000800c | 256 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider..<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br /><strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_SHA_384 | 0x0000800d | 384 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider.<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br /><strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_SHA_512 | 0x0000800e | 512 bit SHA hashing algorithm. This algorithm is supported by Microsoft Enhanced RSA and AES Cryptographic Provider.<strong>Windows XP with SP3:</strong> This algorithm is supported by the Microsoft Enhanced RSA and AES Cryptographic Provider (Prototype).<br /><strong>Windows XP with SP2, Windows XP with SP1 and Windows XP:</strong> This algorithm is not supported.<br /> | 
| CALG_SKIPJACK | 0x0000660a | Skipjack block encryption algorithm (FORTEZZA). This algorithm is not supported. | 
| CALG_SSL2_MASTER | 0x00004c05 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_SSL3_MASTER | 0x00004c01 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_SSL3_SHAMD5 | 0x00008008 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_TEK | 0x0000660b | TEK (FORTEZZA). This algorithm is not supported. | 
| CALG_TLS1_MASTER | 0x00004c06 | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 
| CALG_TLS1PRF | 0x0000800a | Used by the Schannel.dll operations system. This <strong>ALG_ID</strong> should not be used by applications. | 




 

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

 

 
