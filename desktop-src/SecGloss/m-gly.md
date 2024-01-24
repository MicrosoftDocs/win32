---
description: Contains definitions of security terms that begin with the letter M.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 4c4402e9-7455-4868-978f-3899a8fd86c1
title: M (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# M (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) M [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_mac_gly"></span><span id="_SECURITY_MAC_GLY"></span>**MAC**
</dt> <dd>

See *Message Authentication Code*.

</dd> <dt>

<span id="_security_mac_key_gly"></span><span id="_SECURITY_MAC_KEY_GLY"></span>**MAC key**
</dt> <dd>

A message authentication code key used with [*Schannel*](s-gly.md) protocols.

</dd> <dt>

<span id="_security_master_key_gly"></span><span id="_SECURITY_MASTER_KEY_GLY"></span>**master key**
</dt> <dd>

The key used by the client and server for all session key generation. The master key is used to generate the client-read key, the client-write key, the server-read key, and the server-write key. Master keys can be exported as simple key BLOBs.

</dd> <dt>

<span id="_security_md2_gly"></span><span id="_SECURITY_MD2_GLY"></span>**MD2**
</dt> <dd>

The CryptoAPI algorithm name for the MD2 hash algorithm. Other hashing algorithms include *MD4*, *MD5*, and [*SHA*](s-gly.md).

See also *MD2 algorithm*.

</dd> <dt>

<span id="_security_md2_algorithm_gly"></span><span id="_SECURITY_MD2_ALGORITHM_GLY"></span>**MD2 algorithm**
</dt> <dd>

(MD2) A hashing algorithm that creates a 128-bit hash value. MD2 was optimized for use with 8-bit computers. CryptoAPI references this algorithm by its type (CALG\_MD2), name (MAC), and class (ALG\_CLASS\_HASH). MD2 was developed by RSA Data Security, Inc.

See also *MD4 algorithm*, *MD5 algorithm*.

</dd> <dt>

<span id="_security_md4_gly"></span><span id="_SECURITY_MD4_GLY"></span>**MD4**
</dt> <dd>

The CryptoAPI algorithm name for the MD4 hash algorithm. Other hashing algorithms include *MD2*, *MD5*, and [*SHA*](s-gly.md).

See *MD4 algorithm*.

</dd> <dt>

<span id="_security_md4_algorithm_gly"></span><span id="_SECURITY_MD4_ALGORITHM_GLY"></span>**MD4 algorithm**
</dt> <dd>

(MD4) A hashing algorithm that creates a 128-bit hash value. MD4 was optimized for 32-bit computers. It is now considered broken because collisions can be found too quickly and easily. MD4 was developed by RSA Data Security, Inc.

See also *MD2 algorithm*, *MD5 algorithm*.

</dd> <dt>

<span id="_security_md5_gly"></span><span id="_SECURITY_MD5_GLY"></span>**MD5**
</dt> <dd>

The CryptoAPI algorithm name for the MD5 hash algorithm. Other hashing algorithms include *MD2*, *MD4*, and [*SHA*](s-gly.md).

See also *MD5 algorithm*.

</dd> <dt>

<span id="_security_md5_algorithm_gly"></span><span id="_SECURITY_MD5_ALGORITHM_GLY"></span>**MD5 algorithm**
</dt> <dd>

(MD5) A hashing algorithm that creates a 128-bit hash value. MD5 was optimized for 32-bit computers. CryptoAPI references this algorithm by its algorithm identifier (CALG\_MD5), name (MD5), and class (ALG\_CLASS\_HASH). MD5 was developed by RSA Data Security, Inc. and is specified by PROV\_RSA\_FULL, PROV\_RSA\_SIG, PROV\_DSS, PROV\_DSS\_DH, and PROV\_MS\_EXCHANGE provider types.

See also *MD2 algorithm*, *MD4 algorithm*.

</dd> <dt>

<span id="_security_message_gly"></span><span id="_SECURITY_MESSAGE_GLY"></span>**message**
</dt> <dd>

Any data that has been encoded for transmission to or received from a person or entity. Messages may be encrypted for privacy, digitally signed for authentication purposes, or both.

</dd> <dt>

<span id="_security_message_digest_gly"></span><span id="_SECURITY_MESSAGE_DIGEST_GLY"></span>**message digest**
</dt> <dd>

See [*hash*](h-gly.md).

</dd> <dt>

<span id="_security_message_authentication_code_gly"></span><span id="_SECURITY_MESSAGE_AUTHENTICATION_CODE_GLY"></span>**Message Authentication Code**
</dt> <dd>

(MAC) A keyed hashing algorithm that uses a symmetric session key to help ensure that a block of data has retained its integrity from the time it was sent until the time it was received. When using this type of algorithm, the receiving application must also possess the session key to recompute the hash value so it can verify that the base data has not changed. CryptoAPI references this algorithm by its type (CALG\_MAC), name (MAC), and class (ALG\_CLASS\_HASH).

</dd> <dt>

<span id="_security_message_encoding_type_gly"></span><span id="_SECURITY_MESSAGE_ENCODING_TYPE_GLY"></span>**message encoding type**
</dt> <dd>

Defines how the message is encoded. The message encoding type is stored in the high-order word of the encoding type structure. Current defined encoding types are: CRYPT\_ASN\_ENCODING, X509\_ASN\_ENCODING, and PKCS\_7\_ASN\_ENCODING.

</dd> <dt>

<span id="_security_message_management_functions_gly"></span><span id="_SECURITY_MESSAGE_MANAGEMENT_FUNCTIONS_GLY"></span>**message management functions**
</dt> <dd>

Functions that provide two levels of message management: low-level message functions and simplified message functions. The low-level message functions provide more flexibility than the simplified message functions; however, they require more function calls.

</dd> <dt>

<span id="_security_message_signing_functions_gly"></span><span id="_SECURITY_MESSAGE_SIGNING_FUNCTIONS_GLY"></span>**message signing functions**
</dt> <dd>

Functions used to sign messages and data.

See also [*simplified message functions*](s-gly.md).

</dd> <dt>

<span id="_security_mpr_gly"></span><span id="_SECURITY_MPR_GLY"></span>**MPR**
</dt> <dd>

See *Multiple Provider Router*.

</dd> <dt>

<span id="_security_multiple_provider_router_gly"></span><span id="_SECURITY_MULTIPLE_PROVIDER_ROUTER_GLY"></span>**Multiple Provider Router**
</dt> <dd>

(MPR) A system component that handles communications between the system and all network providers. The MPR calls the network provider functions that are exposed by each network provider.

</dd> </dl>

 

 



