---
description: Contains definitions of security terms that begin with the letter B.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 2e570727-7da0-4e17-bf5d-6fe0e6aef65b
title: B (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# B (Security Glossary)

[A](a-gly.md) B [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_backup_authority_gly"></span><span id="_SECURITY_BACKUP_AUTHORITY_GLY"></span>**backup authority**
</dt> <dd>

A trusted application running on a secure computer that provides secondary storage for the session keys of its clients. The backup authority stores session keys as key BLOBs that are encrypted with the backup authority's public key.

</dd> <dt>

<span id="_security_base_content_type_gly"></span><span id="_SECURITY_BASE_CONTENT_TYPE_GLY"></span>**base content type**
</dt> <dd>

A type of data contained in a PKCS \#7 message. Base content types only contain data, no cryptographic enhancements such as hashes or signatures. Currently, the only base content type is the Data content type.

</dd> <dt>

<span id="_security_base_cryptographic_functions_gly"></span><span id="_SECURITY_BASE_CRYPTOGRAPHIC_FUNCTIONS_GLY"></span>**base cryptographic functions**
</dt> <dd>

The lowest level of functions in the CryptoAPI architecture. They are used by applications and other high-level CryptoAPI functions to provide access to CSP-provided cryptographic algorithms, secure key generation, and secure storage of secrets.

See also [*cryptographic service providers*](c-gly.md).

</dd> <dt>

<span id="_security_basic_encoding_rules_gly"></span><span id="_SECURITY_BASIC_ENCODING_RULES_GLY"></span>**Basic Encoding Rules**
</dt> <dd>

(BER) The set of rules used to encode ASN.1 defined data into a stream of bits (zeros or ones) for external storage or transmission. A single ASN.1 object may have several equivalent BER encodes. BER is defined in CCITT Recommendation X.209. This is one of the two encoding methods currently used by CryptoAPI.

</dd> <dt>

<span id="_security_ber_gly"></span><span id="_SECURITY_BER_GLY"></span>**BER**
</dt> <dd>

See *Basic Encoding Rules*.

</dd> <dt>

<span id="_security_big_endian_gly"></span><span id="_SECURITY_BIG_ENDIAN_GLY"></span>**big-endian**
</dt> <dd>

A memory or data format in which the most significant byte is stored at the lower address or arrives first.

See also [*little-endian*](l-gly.md).

</dd> <dt>

<span id="_security_blob_gly"></span><span id="_SECURITY_BLOB_GLY"></span>**BLOB**
</dt> <dd>

A generic sequence of bits that contain one or more fixed-length header structures plus context specific data.

See also [*key BLOBs*](k-gly.md), [*certificate BLOBs*](c-gly.md), [*certificate name BLOBs*](c-gly.md), and [*attribute BLOBs*](a-gly.md).

</dd> <dt>

<span id="_security_block_cipher_gly"></span><span id="_SECURITY_BLOCK_CIPHER_GLY"></span>**block cipher**
</dt> <dd>

A cipher algorithm that encrypts data in discrete units (called blocks), rather than as a continuous stream of bits. The most common block size is 64 bits. For example, DES is a block cipher.

See also [*stream cipher*](s-gly.md).

</dd> <dt>

<span id="_security_bulk_encryption_key_gly"></span><span id="_SECURITY_BULK_ENCRYPTION_KEY_GLY"></span>**bulk encryption key**
</dt> <dd>

A session key derived from a master key. Bulk encryption keys are used in [*Schannel*](s-gly.md) encryption.

</dd> </dl>

 

 



