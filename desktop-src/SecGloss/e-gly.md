---
description: Contains definitions of security terms that begin with the letter E.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: f1caccd2-3453-448e-b194-bf899eff8091
title: E (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# E (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) E F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_ecb_gly"></span><span id="_SECURITY_ECB_GLY"></span>**ECB**
</dt> <dd>

See *electronic codebook*.

</dd> <dt>

<span id="_security_ecc_gly"></span><span id="_SECURITY_ECC_GLY"></span>**ECC**
</dt> <dd>

See *elliptic curve cryptography*.

</dd> <dt>

<span id="_security_efs_gly"></span><span id="_SECURITY_EFS_GLY"></span>**EFS**
</dt> <dd>

See *Encrypting File System*.

</dd> <dt>

<span id="_security_eku_gly"></span><span id="_SECURITY_EKU_GLY"></span>**EKU**
</dt> <dd>

See *enhanced key usage*.

</dd> <dt>

<span id="_security_electronic_codebook_gly"></span><span id="_SECURITY_ELECTRONIC_CODEBOOK_GLY"></span>**electronic codebook**
</dt> <dd>

(ECB) A block cipher mode (each block is encrypted individually) that uses no feedback. This means any blocks of plaintext that are identical (either in the same message or in a different message that is encrypted with the same key) is transformed into identical ciphertext blocks. Initialization vectors cannot be used with this cipher mode. If a single bit of the ciphertext block is garbled, then the entire corresponding plaintext block is also garbled.

</dd> <dt>

<span id="_security_elliptic_curve_cryptography_gly"></span><span id="_SECURITY_ELLIPTIC_CURVE_CRYPTOGRAPHY_GLY"></span>**elliptic curve cryptography**
</dt> <dd>

(ECC) An approach to public key cryptography based on properties of elliptic curves. The primary advantage of ECC is efficiency, which becomes important as devices get smaller and security requirements get more demanding. For example, ECC keys between 163 bits and 512 bits are one-sixth to one-thirtieth the size of equivalent security-level RSA keys. As key size increases the relative efficiency of ECC increases.

</dd> <dt>

<span id="_security_encoding_gly"></span><span id="_SECURITY_ENCODING_GLY"></span>**encoding**
</dt> <dd>

The process of turning data into a stream of bits. Encoding is part of the serialization process that converts data into a stream of ones and zeros.

</dd> <dt>

<span id="_security_encoding_type_gly"></span><span id="_SECURITY_ENCODING_TYPE_GLY"></span>**encoding type**
</dt> <dd>

Refers to which type of encoding is used for certificate and message encoding. The encoding types are specified as a **DWORD**, with the type of certificate encoding stored in the low-order word and the type of message encoding stored in the high-order word. Although some functions or structure fields require only one of the encoding types, it is always acceptable to specify both.

</dd> <dt>

<span id="_security_encryption_gly"></span><span id="_SECURITY_ENCRYPTION_GLY"></span>**encryption**
</dt> <dd>

The process of converting plaintext to ciphertext to help prevent it from being read and understood by an unauthorized party. Encryption is the opposite of decryption.

</dd> <dt>

<span id="_security_encrypted_data_gly"></span><span id="_SECURITY_ENCRYPTED_DATA_GLY"></span>**encrypted data**
</dt> <dd>

Data that has been converted from plaintext into ciphertext. Encrypted messages are used to disguise the content of a message when it is sent or stored.

</dd> <dt>

<span id="_security_encrypting_file_system_gly"></span><span id="_SECURITY_ENCRYPTING_FILE_SYSTEM_GLY"></span>**Encrypting File System**
</dt> <dd>

(EFS) A feature in the Windows operating system that enables users to encrypt files and folders on an NTFS volume disk to keep them safe from access by intruders.

</dd> <dt>

<span id="_security_encryption_and_decryption_functions_gly"></span><span id="_SECURITY_ENCRYPTION_AND_DECRYPTION_FUNCTIONS_GLY"></span>**encryption and decryption functions**
</dt> <dd>

Simplified message functions used to encode and encrypt (or decode and decrypt) data. As a set, these functions include support for simultaneously encrypting and decrypting data.

See also [*simplified message functions*](s-gly.md).

</dd> <dt>

<span id="_security_enhanced_content_type_gly"></span><span id="_SECURITY_ENHANCED_CONTENT_TYPE_GLY"></span>**enhanced content type**
</dt> <dd>

A class of data contained in a PKCS \#7 message that contains data (possibly encrypted), plus cryptographic enhancements such as hashes or signatures. Types of enhanced data defined by PKCS \#7 include signed data, enveloped data, signed-and-enveloped data, and digested (hashed) data.

</dd> <dt>

<span id="_security_enhanced_key_usage_gly"></span><span id="_SECURITY_ENHANCED_KEY_USAGE_GLY"></span>**enhanced key usage**
</dt> <dd>

(EKU) Both a certificate extension and a certificate extended property value. An EKU specifies the uses for which a certificate is valid.

</dd> <dt>

<span id="_security_enveloped_data_content_type_gly"></span><span id="_SECURITY_ENVELOPED_DATA_CONTENT_TYPE_GLY"></span>**enveloped data content type**
</dt> <dd>

A PKCS \#7 enhanced content that consists of encrypted content (of any type) and content-encryption keys (for one or more recipients). The combination of encrypted content and encryption key for a recipient is called a *digital envelope* for that recipient. This type of message should be used when you want to keep the contents of the message secret and allow only specified persons or entities to retrieve the contents.

</dd> <dt>

<span id="_security_exchange_key_gly"></span><span id="_SECURITY_EXCHANGE_KEY_GLY"></span>**exchange key**
</dt> <dd>

See *exchange key pair*.

</dd> <dt>

<span id="_security_exchange_key_pair_gly"></span><span id="_SECURITY_EXCHANGE_KEY_PAIR_GLY"></span>**exchange key pair**
</dt> <dd>

A public/private key pair used to encrypt session keys so that they can be safely stored and exchanged with other users. Exchange key pairs are created by calling the **CryptGenKey** function.

Compare [*signature key pair*](s-gly.md).

</dd> <dt>

<span id="_security_external_store_gly"></span><span id="_SECURITY_EXTERNAL_STORE_GLY"></span>**external store**
</dt> <dd>

A certificate store that maintains its certificates, CRLs, and CTLs in a location external to cached memory, such as in a database on a network server. An external store does not read and decode its certificates, CRLs, and CTL when the **CertOpenStore** function is called. Reading and decoding is deferred until an enumeration or find method is called.

</dd> </dl>

 

 



