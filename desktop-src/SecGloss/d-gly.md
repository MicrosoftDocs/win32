---
description: Contains definitions of security terms that begin with the letter D.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: d007cbb9-b547-4dc7-bc22-b526f650f7c2
title: D (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# D (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) D [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_dac_gly"></span><span id="_SECURITY_DAC_GLY"></span>**DAC**
</dt> <dd>

See *dynamic access control*.

</dd> <dt>

<span id="_security_dacl_gly"></span><span id="_SECURITY_DACL_GLY"></span>**DACL**
</dt> <dd>

See *discretionary access control list*.

</dd> <dt>

<span id="_security_data_content_type_gly"></span><span id="_SECURITY_DATA_CONTENT_TYPE_GLY"></span>**data content type**
</dt> <dd>

A base content type defined by PKCS \#7. Data content is simply an octet (byte) string.

</dd> <dt>

<span id="_security_data_encryption_gly"></span><span id="_SECURITY_DATA_ENCRYPTION_GLY"></span>**data encryption**
</dt> <dd>

See [*encryption*](e-gly.md).

</dd> <dt>

<span id="_security_data_encryption_function_gly"></span><span id="_SECURITY_DATA_ENCRYPTION_FUNCTION_GLY"></span>**data encryption function**
</dt> <dd>

See [*encryption and decryption functions*](e-gly.md).

</dd> <dt>

<span id="_security_data_encryption_standard_gly"></span><span id="_SECURITY_DATA_ENCRYPTION_STANDARD_GLY"></span>**Data Encryption Standard**
</dt> <dd>

(DES) A block cipher that encrypts data in 64-bit blocks. DES is a symmetric algorithm that uses the same algorithm and key for encryption and decryption.

Developed in the early 1970s, DES is also known as the DEA (Data Encryption Algorithm) by ANSI and the DEA-1 by ISO.

</dd> <dt>

<span id="_security_datagram_gly"></span><span id="_SECURITY_DATAGRAM_GLY"></span>**datagram**
</dt> <dd>

A communication channel that uses information routed through a packet-switching network. This information includes separate packets of information and the delivery information associated with those packets, such as the destination address. In a packet-switching network, data packets are routed independently of one another and may follow different routes. They may also arrive in a different order from the one in which they were sent.

</dd> <dt>

<span id="_security_decoding_gly"></span><span id="_SECURITY_DECODING_GLY"></span>**decoding**
</dt> <dd>

The process of translating an encoded object (such as a certificate) or data back to its original format.

In general terms, data is decoded by the Encoding/Decoding layer of the communication protocol. Certificates are decoded by a call to the **CryptDecodeObject** function.

</dd> <dt>

<span id="_security_decryption_gly"></span><span id="_SECURITY_DECRYPTION_GLY"></span>**decryption**
</dt> <dd>

The process of converting ciphertext to plaintext. Decryption is the opposite of encryption.

</dd> <dt>

<span id="_security_default_mode_gly"></span><span id="_SECURITY_DEFAULT_MODE_GLY"></span>**default mode**
</dt> <dd>

Default settings, such as the block encryption cipher mode or the block encryption padding method.

</dd> <dt>

<span id="_security_der_gly"></span><span id="_SECURITY_DER_GLY"></span>**DER**
</dt> <dd>

See *Distinguished Encoding Rules*.

</dd> <dt>

<span id="_security_derived_key_gly"></span><span id="_SECURITY_DERIVED_KEY_GLY"></span>**derived key**
</dt> <dd>

A cryptographic key created by a call to the **CryptDeriveKey** function. A derived key can be created from a password, or any other user data. Derived keys allow applications to create session keys as needed, eliminating the need to store a particular key.

</dd> <dt>

<span id="_security_des_gly"></span><span id="_SECURITY_DES_GLY"></span>**DES**
</dt> <dd>

See *Data Encryption Standard*.

</dd> <dt>

<span id="_security_dh_gly"></span><span id="_SECURITY_DH_GLY"></span>**DH**
</dt> <dd>

See *Diffie-Hellman algorithm*.

</dd> <dt>

<span id="_security_dh_keyx_gly"></span><span id="_SECURITY_DH_KEYX_GLY"></span>**DH\_KEYX**
</dt> <dd>

The CryptoAPI algorithm name for the Diffie-Hellman key-exchange algorithm.

See also *Diffie-Hellman algorithm*.

</dd> <dt>

<span id="_security_diffie_hellman_algorithm_gly"></span><span id="_SECURITY_DIFFIE_HELLMAN_ALGORITHM_GLY"></span>**Diffie-Hellman algorithm**
</dt> <dd>

(DH) A public key algorithm used for secure key exchange. Diffie-Hellman cannot be used for data encryption. This algorithm is specified as the key exchange algorithm for PROV\_DSS\_DH provider types.

See also *Diffie-Hellman (store and forward) key-exchange algorithm* and *Diffie-Hellman (ephemeral) key-exchange algorithm*.

</dd> <dt>

<span id="_security_diffie_hellman_store_and_forward_key_exchange_algorithm_gly"></span><span id="_SECURITY_DIFFIE_HELLMAN_STORE_AND_FORWARD_KEY_EXCHANGE_ALGORITHM_GLY"></span>**Diffie-Hellman (store and forward) key-exchange algorithm**
</dt> <dd>

A Diffie-Hellman algorithm where the exchange key values are retained (in the CSP) after the key handle has been destroyed.

See also *Diffie-Hellman (ephemeral) key-exchange algorithm*.

</dd> <dt>

<span id="_security_diffie_hellman_ephemeral_key_exchange_algorithm_gly"></span><span id="_SECURITY_DIFFIE_HELLMAN_EPHEMERAL_KEY_EXCHANGE_ALGORITHM_GLY"></span>**Diffie-Hellman (ephemeral) key-exchange algorithm**
</dt> <dd>

A Diffie-Hellman algorithm where the exchange key value is deleted from the CSP when the key handle is destroyed.

See also *Diffie-Hellman (store and forward) key-exchange algorithm*.

</dd> <dt>

<span id="_security_digested_data_gly"></span><span id="_SECURITY_DIGESTED_DATA_GLY"></span>**digested data**
</dt> <dd>

A data content type defined by PKCS \#7 that consists of any type of data plus a message hash (digest) of the content.

</dd> <dt>

<span id="_security_digital_certificate_gly"></span><span id="_SECURITY_DIGITAL_CERTIFICATE_GLY"></span>**digital certificate**
</dt> <dd>

See [*certificate*](c-gly.md).

</dd> <dt>

<span id="_security_digital_envelope_gly"></span><span id="_SECURITY_DIGITAL_ENVELOPE_GLY"></span>**digital envelope**
</dt> <dd>

Private messages encrypted using the recipient's public key. Enveloped messages can only be decrypted by using the recipient's private key, allowing only the recipient to understand the message.

</dd> <dt>

<span id="_security_digital_signature_gly"></span><span id="_SECURITY_DIGITAL_SIGNATURE_GLY"></span>**digital signature**
</dt> <dd>

Data that binds a sender's identity to the information being sent. A digital signature may be bundled with any message, file, or other digitally encoded information, or transmitted separately. Digital signatures are used in public key environments and provide authentication and integrity services.

</dd> <dt>

<span id="_security_digital_signature_algorithm_gly"></span><span id="_SECURITY_DIGITAL_SIGNATURE_ALGORITHM_GLY"></span>**Digital Signature Algorithm**
</dt> <dd>

(DSA) A public key algorithm specified by Digital Signature Standard (DSS). DSA is only used to generate digital signatures. It cannot be used for data encryption.

</dd> <dt>

<span id="_security_digital_signature_key_pair_gly"></span><span id="_SECURITY_DIGITAL_SIGNATURE_KEY_PAIR_GLY"></span>**digital signature key pair**
</dt> <dd>

See [*signature key pair*](s-gly.md).

</dd> <dt>

<span id="_security_digital_signature_standard_gly"></span><span id="_SECURITY_DIGITAL_SIGNATURE_STANDARD_GLY"></span>**Digital Signature Standard**
</dt> <dd>

(DSS) A standard that specifies the Digital Signature Algorithm (DSA) for its signature algorithm and SHA-1 as its message hash algorithm. DSA is a public key cipher that is only used to generate digital signatures and cannot be used for data encryption. DSS is specified by PROV\_DSS, PROV\_DSS\_DH, and PROV\_FORTEZZA provider types.

</dd> <dt>

<span id="_security_discretionary_access_control_list_gly"></span><span id="_SECURITY_DISCRETIONARY_ACCESS_CONTROL_LIST_GLY"></span>**discretionary access control list**
</dt> <dd>

(DACL) An access control list that is controlled by the owner of an object and that specifies the access particular users or groups can have to the object.

See also [*access control list*](a-gly.md) and [*system access control list*](s-gly.md).

</dd> <dt>

<span id="_security_distinguished_encoding_rules_gly"></span><span id="_SECURITY_DISTINGUISHED_ENCODING_RULES_GLY"></span>**Distinguished Encoding Rules**
</dt> <dd>

(DER) A set of rules for encoding ASN.1 defined data as a stream of bits for external storage or transmission. Every ASN.1 object has exactly one corresponding DER encoding. DER is defined in CCITT Recommendation X.509, Section 8.7. This is one of two encoding methods currently used by CryptoAPI.

</dd> <dt>

<span id="_security_dll_gly"></span><span id="_SECURITY_DLL_GLY"></span>**DLL**
</dt> <dd>

See *dynamic-link library*.

</dd> <dt>

<span id="_security_dsa_gly"></span><span id="_SECURITY_DSA_GLY"></span>**DSA**
</dt> <dd>

See *Digital Signature Algorithm*.

</dd> <dt>

<span id="_security_dss_gly"></span><span id="_SECURITY_DSS_GLY"></span>**DSS**
</dt> <dd>

See *Digital Signature Standard*.

</dd> <dt>

<span id="_security_dynamic_access_control_gly"></span><span id="_SECURITY_DYNAMIC_ACCESS_CONTROL_GLY"></span>**Dynamic Access Control**
</dt> <dd>

(DAC) The ability to specify access control policies based on user, device, and resource claims. This makes for more flexible authentication for applications while maintaining security and compliance requirements.

</dd> <dt>

<span id="_security_dynamic_link_library_gly"></span><span id="_SECURITY_DYNAMIC_LINK_LIBRARY_GLY"></span>**dynamic-link library**
</dt> <dd>

(DLL) A file that contains executable routines that can be called from other applications.

</dd> </dl>

 

 



