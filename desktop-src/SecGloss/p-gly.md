---
description: Contains definitions of security terms that begin with the letter P.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a
title: P (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# P (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) P Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_padding_gly"></span><span id="_SECURITY_PADDING_GLY"></span>**padding**
</dt> <dd>

A string, typically added when the last plaintext block is short. For example, if the block length is 64 bits and the last block contains only 40 bits, then 24 bits of padding must be added to the last block. The padding string may contain zeros, alternating zeros and ones, or some other pattern. Applications that use [*CryptoAPI*](c-gly.md) need not add padding to their plaintext before it is encrypted, nor do they have to remove it after decrypting. This is all handled automatically.

</dd> <dt>

<span id="_security_password_filter_gly"></span><span id="_SECURITY_PASSWORD_FILTER_GLY"></span>**password filter**
</dt> <dd>

A DLL that provides password policy enforcement and change notification. The functions implemented by password filters are called by the [*Local Security Authority*](l-gly.md).

</dd> <dt>

<span id="_security_persistent_storage_gly"></span><span id="_SECURITY_PERSISTENT_STORAGE_GLY"></span>**persistent storage**
</dt> <dd>

Any storage medium that remains intact when the power to it is disconnected. Many [*certificate store*](c-gly.md) databases are forms of persistent storage.

</dd> <dt>

<span id="_security_pkcs_gly"></span><span id="_SECURITY_PKCS_GLY"></span>**PKCS**
</dt> <dd>

See *Public Key Cryptography Standards*.

</dd> <dt>

<span id="_security_pkcs_1_standard_gly"></span><span id="_SECURITY_PKCS_1_STANDARD_GLY"></span>**PKCS \#1**
</dt> <dd>

The recommended standards for the implementation of public-key cryptography based on the RSA algorithm as defined in [RFC 3447](https://tools.ietf.org/html/rfc3447).

</dd> <dt>

<span id="_security_pkcs_12_standard_gly"></span><span id="_SECURITY_PKCS_12_STANDARD_GLY"></span>**PKCS \#12**
</dt> <dd>

The Personal Information Exchange Syntax Standard, developed and maintained by RSA Data Security, Inc. This syntax standard specifies a portable format for storing or transporting a user's private keys, certificates, and miscellaneous secrets.

See also [*certificate*](c-gly.md) and *Public Key Cryptography Standards*.

</dd> <dt>

<span id="_security_pkcs_7_signed_data_gly"></span><span id="_SECURITY_PKCS_7_SIGNED_DATA_GLY"></span>**PKCS \#7 Signed Data**
</dt> <dd>

A data object that is signed with the Public Key Cryptography Standard \#7 (PKCS \#7) and that encapsulates the information used to sign a file. Typically, it includes the signer's certificate and the [*root certificate*](r-gly.md).

</dd> <dt>

<span id="_security_pkcs_7_standard_gly"></span><span id="_SECURITY_PKCS_7_STANDARD_GLY"></span>**PKCS \#7**
</dt> <dd>

The Cryptographic Message Syntax Standard. A general syntax for data to which cryptography may be applied, such as digital signatures and encryption. It also provides a syntax for disseminating certificates or certificate revocation lists and other message attributes, such as time stamps, to the message.

</dd> <dt>

<span id="_security_pkcs_7_asn_encoding_gly"></span><span id="_SECURITY_PKCS_7_ASN_ENCODING_GLY"></span>**PKCS\_7\_ASN\_ENCODING**
</dt> <dd>

A [*message encoding type*](m-gly.md). Message encoding types are stored in the high-order word of a **DWORD** (value is: 0x00010000).

</dd> <dt>

<span id="_security_plaintext_gly"></span><span id="_SECURITY_PLAINTEXT_GLY"></span>**plaintext**
</dt> <dd>

A message that is not encrypted. Plaintext messages are sometimes referred to as cleartext messages.

</dd> <dt>

<span id="_security_portable_executable_pe_image_gly"></span><span id="_SECURITY_PORTABLE_EXECUTABLE_PE_IMAGE_GLY"></span>**Portable Executable (PE) Image**
</dt> <dd>

The standard Windows executable format.

</dd> <dt>

<span id="_security_prf_gly"></span><span id="_SECURITY_PRF_GLY"></span>**PRF**
</dt> <dd>

See *Pseudo-Random Function*.

</dd> <dt>

<span id="_security_primary_credentials_gly"></span><span id="_SECURITY_PRIMARY_CREDENTIALS_GLY"></span>**primary credentials**
</dt> <dd>

The MsV1\_0 authentication package defines a primary credential key string value: The primary credentials string holds the credentials provided at initial logon time. It includes the user name and both case-sensitive and case-insensitive forms of the user's password.

See also [*supplemental credentials*](s-gly.md).

</dd> <dt>

<span id="_security_primary_service_provider_gly"></span><span id="_SECURITY_PRIMARY_SERVICE_PROVIDER_GLY"></span>**primary service provider**
</dt> <dd>

The service provider that supplies the control interfaces to the card. Each smart card can register its primary service provider in the smart card database.

</dd> <dt>

<span id="_security_primary_token_gly"></span><span id="_SECURITY_PRIMARY_TOKEN_GLY"></span>**primary token**
</dt> <dd>

An access token that is typically created only by the Windows kernel. It may be assigned to a process to represent the default security information for that process.

See also [*access token*](a-gly.md) and [*impersonation token*](i-gly.md).

</dd> <dt>

<span id="_security_principal_gly"></span><span id="_SECURITY_PRINCIPAL_GLY"></span>**principal**
</dt> <dd>

See [*security principal*](s-gly.md).

</dd> <dt>

<span id="_security_privacy_gly"></span><span id="_SECURITY_PRIVACY_GLY"></span>**privacy**
</dt> <dd>

The condition of being isolated from view or secret. With respect to messages, private messages are encrypted messages whose text is hidden from view. With respect to keys, a private key is a secret key concealed from others.

</dd> <dt>

<span id="_security_private_key_gly"></span><span id="_SECURITY_PRIVATE_KEY_GLY"></span>**private key**
</dt> <dd>

The secret half of a key pair used in a public key algorithm. Private keys are typically used to encrypt a symmetric session key, digitally sign a message, or decrypt a message that has been encrypted with the corresponding public key.

See also *public key*.

</dd> <dt>

<span id="_security_private_key_blob_gly"></span><span id="_SECURITY_PRIVATE_KEY_BLOB_GLY"></span>**private key BLOB**
</dt> <dd>

A key BLOB that contains a complete public/private key pair. Private key BLOBs are used by administrative programs to transport key pairs. As the private key portion of the key pair is extremely confidential, these BLOBs are typically kept encrypted with a symmetric cipher. These key BLOBs can also be used by advanced applications where the key pairs are stored within the application, rather than relying on the CSP's storage mechanism. A key BLOB is created by calling the **CryptExportKey** function.

</dd> <dt>

<span id="_security_privilege_gly"></span><span id="_SECURITY_PRIVILEGE_GLY"></span>**privilege**
</dt> <dd>

The right of a user to perform various system-related operations, such as shutting down the system, loading device drivers, or changing the system time. A user's access token contains a list of the privileges held by either the user or the user's groups.

</dd> <dt>

<span id="_security_process_gly"></span><span id="_SECURITY_PROCESS_GLY"></span>**process**
</dt> <dd>

The security context under which an application runs. Typically, the security context is associated with a user, so all applications running under a given process take on the permissions and privileges of the owning user.

</dd> <dt>

<span id="_security_prov_dss_gly"></span><span id="_SECURITY_PROV_DSS_GLY"></span>**PROV\_DSS**
</dt> <dd>

See *PROV\_DSS provider type*.

</dd> <dt>

<span id="_security_prov_dss_provider_type_gly"></span><span id="_SECURITY_PROV_DSS_PROVIDER_TYPE_GLY"></span>**PROV\_DSS Provider Type**
</dt> <dd>

Predefined provider type that only supports digital signatures and hashes. It specifies the DSA signature algorithm, and the MD5 and SHA-1 hashing algorithms.

</dd> <dt>

<span id="_security_prov_dss_dh_gly"></span><span id="_SECURITY_PROV_DSS_DH_GLY"></span>**PROV\_DSS\_DH**
</dt> <dd>

See *PROV\_DSS\_DH provider type*.

</dd> <dt>

<span id="_security_prov_dss_dh_provider_type_gly"></span><span id="_SECURITY_PROV_DSS_DH_PROVIDER_TYPE_GLY"></span>**PROV\_DSS\_DH provider type**
</dt> <dd>

Predefined provider type that provides key exchange, digital signature, and hashing algorithms. It is similar to the PROV\_DSS provider type.

</dd> <dt>

<span id="_security_prov_fortezza_gly"></span><span id="_SECURITY_PROV_FORTEZZA_GLY"></span>**PROV\_FORTEZZA**
</dt> <dd>

See *PROV\_FORTEZZA provider type*.

</dd> <dt>

<span id="_security_prov_fortezza_provider_type_gly"></span><span id="_SECURITY_PROV_FORTEZZA_PROVIDER_TYPE_GLY"></span>**PROV\_FORTEZZA provider type**
</dt> <dd>

Predefined provider type that provides key exchange, digital signature, encryption, and hashing algorithms. The cryptographic protocols and algorithms specified by this provider type are owned by the National Institute of Standards and Technology (NIST).

</dd> <dt>

<span id="_security_prov_ms_exchange_gly"></span><span id="_SECURITY_PROV_MS_EXCHANGE_GLY"></span>**PROV\_MS\_EXCHANGE**
</dt> <dd>

See *PROV\_MS\_EXCHANGE provider type*.

</dd> <dt>

<span id="_security_prov_ms_exchange_provider_type_gly"></span><span id="_SECURITY_PROV_MS_EXCHANGE_PROVIDER_TYPE_GLY"></span>**PROV\_MS\_EXCHANGE provider type**
</dt> <dd>

Predefined provider type designed for the needs of Microsoft Exchange, as well as other applications that are compatible with Microsoft Mail. It provides key exchange, digital signature, encryption, and hashing algorithms.

</dd> <dt>

<span id="_security_prov_rsa_full_gly"></span><span id="_SECURITY_PROV_RSA_FULL_GLY"></span>**PROV\_RSA\_FULL**
</dt> <dd>

See *PROV\_RSA\_FULL provider type*.

</dd> <dt>

<span id="_security_prov_rsa_full_provider_type_gly"></span><span id="_SECURITY_PROV_RSA_FULL_PROVIDER_TYPE_GLY"></span>**PROV\_RSA\_FULL provider type**
</dt> <dd>

Predefined provider type defined by Microsoft and RSA Data Security, Inc. This general purpose provider type provides key exchange, digital signature, encryption, and hashing algorithms. The key exchange, digital signature, and encryption algorithms are based on RSA public key cryptography.

</dd> <dt>

<span id="_security_prov_rsa_sig_gly"></span><span id="_SECURITY_PROV_RSA_SIG_GLY"></span>**PROV\_RSA\_SIG**
</dt> <dd>

See *PROV\_RSA\_SIG provider type*.

</dd> <dt>

<span id="_security_prov_rsa_sig_provider_type_gly"></span><span id="_SECURITY_PROV_RSA_SIG_PROVIDER_TYPE_GLY"></span>**PROV\_RSA\_SIG provider type**
</dt> <dd>

Predefined provider type defined by Microsoft and RSA Data Security. This provider type is a subset of PROV\_RSA\_FULL that provides only digital signature and hashing algorithms. The digital signature algorithm is an RSA public key algorithm.

</dd> <dt>

<span id="_security_prov_ssl_gly"></span><span id="_SECURITY_PROV_SSL_GLY"></span>**PROV\_SSL**
</dt> <dd>

See *PROV\_SSL provider type*.

</dd> <dt>

<span id="_security_prov_ssl_provider_type_gly"></span><span id="_SECURITY_PROV_SSL_PROVIDER_TYPE_GLY"></span>**PROV\_SSL provider type**
</dt> <dd>

Predefined provider type that supports the Secure Sockets Layer (SSL) protocol. This type provides key encryption, digital signature, encryption, and hashing algorithms. A specification explaining SSL is available from Netscape Communications Corp.

</dd> <dt>

<span id="_security_provider_gly"></span><span id="_SECURITY_PROVIDER_GLY"></span>**provider**
</dt> <dd>

See [*Cryptographic Service Provider*](c-gly.md).

</dd> <dt>

<span id="_security_provider_name_gly"></span><span id="_SECURITY_PROVIDER_NAME_GLY"></span>**provider name**
</dt> <dd>

A name used to identify a CSP. For example, the Microsoft Base Cryptographic Provider version 1.0. The provider name is typically used when calling the **CryptAcquireContext** function to connect to a CSP.

</dd> <dt>

<span id="_security_provider_type_gly"></span><span id="_SECURITY_PROVIDER_TYPE_GLY"></span>**provider type**
</dt> <dd>

A term used to identify a type of cryptographic service provider (CSP). CSPs are grouped into different provider types that represent a specific families of standard data formats and protocols. In contrast to a CSP's unique provider name, provider types are not unique for a given CSP. The provider type is typically used when calling the **CryptAcquireContext** function to connect to a CSP.

</dd> <dt>

<span id="_security_pseudo_random_function_gly"></span><span id="_SECURITY_PSEUDO_RANDOM_FUNCTION_GLY"></span>**pseudo-random function**
</dt> <dd>

(PRF) A function that takes a key, label, and seed as input, then produces an output of arbitrary length.

</dd> <dt>

<span id="_security_public_private_key_pair_gly"></span><span id="_SECURITY_PUBLIC_PRIVATE_KEY_PAIR_GLY"></span>**public/private key pair**
</dt> <dd>

A set of cryptographic keys used for public key cryptography. For each user, a CSP usually maintains two public/private key pairs: an exchange key pair and a digital signature key pair. Both key pairs are maintained from session to session.

See [*exchange key pair*](e-gly.md) and [*signature key pair*](s-gly.md).

</dd> <dt>

<span id="_security_public_key_gly"></span><span id="_SECURITY_PUBLIC_KEY_GLY"></span>**public key**
</dt> <dd>

A cryptographic key typically used when decrypting a session key or a digital signature. The public key can also be used to encrypt a message, guaranteeing that only the person with the corresponding private key can decrypt the message.

See also *private key*.

</dd> <dt>

<span id="_security_public_key_algorithm_gly"></span><span id="_SECURITY_PUBLIC_KEY_ALGORITHM_GLY"></span>**public key algorithm**
</dt> <dd>

An asymmetric cipher that uses two keys, one for encryption, the public key, and the other for decryption, the private key. As implied by the key names, the public key used to encode plaintext can be made available to anyone. However, the private key must remain secret. Only the private key can decrypt the ciphertext. The public key algorithm used in this process is slow (on the order of 1,000 times slower than symmetric algorithms), and is typically used to encrypt session keys or digitally sign a message.

See also *public key* and *private key*.

</dd> <dt>

<span id="_security_public_key_blob_gly"></span><span id="_SECURITY_PUBLIC_KEY_BLOB_GLY"></span>**public key BLOB**
</dt> <dd>

A BLOB used to store the public key portion of a public/private key pair. Public key BLOBs are not encrypted as the public key contained within is not secret. A public key BLOB is created by calling the **CryptExportKey** function.

</dd> <dt>

<span id="_security_public_key_cryptography_standards_gly"></span><span id="_SECURITY_PUBLIC_KEY_CRYPTOGRAPHY_STANDARDS_GLY"></span>**Public Key Cryptography Standards**
</dt> <dd>

(PKCS) A set of syntax standards for public key cryptography covering security functions, including methods for signing data, exchanging keys, requesting certificates, public key encryption and decryption, and other security functions.

</dd> <dt>

<span id="_security_public_key_encryption_gly"></span><span id="_SECURITY_PUBLIC_KEY_ENCRYPTION_GLY"></span>**public key encryption**
</dt> <dd>

Encryption that uses a pair of keys, one key to encrypt data and the other key to decrypt data. In contrast, symmetric encryption algorithms that use the same key for both encryption and decryption. In practice, public key cryptography is typically used to protect the session key used by a symmetric encryption algorithm. In this case, the public key is used to encrypt the session key, which in turn was used to encrypt some data, and the private key is used for decryption. In addition to protecting session keys, public key cryptography may also be used to digitally sign a message (using the private key) and validate the signature (using the public key).

See also *public key algorithm*.

</dd> </dl>

 

 



