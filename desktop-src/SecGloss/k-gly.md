---
description: Contains definitions of security terms that begin with the letter K.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: f17042c3-ba1a-408f-af55-5f171b0dee33
title: K (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# K (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_kca_gly"></span><span id="_SECURITY_KCA_GLY"></span>**KCA**
</dt> <dd>

See *key certification authority*.

</dd> <dt>

<span id="_security_kdc_gly"></span><span id="_SECURITY_KDC_GLY"></span>**KDC**
</dt> <dd>

See *Key Distribution Center*.

</dd> <dt>

<span id="_security_kea_gly"></span><span id="_SECURITY_KEA_GLY"></span>**KEA**
</dt> <dd>

See *key exchange algorithm*.

</dd> <dt>

<span id="_security_kerberos_protocol_gly"></span><span id="_SECURITY_KERBEROS_PROTOCOL_GLY"></span>**Kerberos protocol**
</dt> <dd>

A protocol that defines how clients interact with a network authentication service. Clients obtain tickets from the Kerberos Key Distribution Center (KDC), and they present these tickets to servers when connections are established. Kerberos tickets represent the client's network credentials.

</dd> <dt>

<span id="_security_key_blob_gly"></span><span id="_SECURITY_KEY_BLOB_GLY"></span>**key BLOB**
</dt> <dd>

A BLOB containing an encrypted private key. Key BLOBs provide a way to store keys outside the CSP. Key BLOBs are created by exporting an existing key from the CSP by calling the **CryptExportKey** function. Later, the key BLOB can be imported into a provider (often a different CSP on a different computer) by calling the **CryptImportKey** function. This creates a key in the CSP that is a duplicate of the one that was exported.

See also [*simple key BLOB*](s-gly.md), [*public key BLOB*](p-gly.md), and [*private key BLOB*](p-gly.md).

</dd> <dt>

<span id="_security_key_blob_format_gly"></span><span id="_SECURITY_KEY_BLOB_FORMAT_GLY"></span>**key BLOB format**
</dt> <dd>

The format of the key BLOB when a public or session key is exported from a CSP. The format is specified by the provider type of the exporting CSP. A key BLOB is created by calling **CryptExportKey**.

See also [*public key BLOB*](p-gly.md) and [*simple key BLOB*](s-gly.md).

</dd> <dt>

<span id="_security_key_certification_authority_gly"></span><span id="_SECURITY_KEY_CERTIFICATION_AUTHORITY_GLY"></span>**key certification authority**
</dt> <dd>

(KCA) A trusted entity that typically keeps a secure database of compound messages signed with the KCA's private key. In practical implementations, the compound messages consist of the user's name, the user's public key, and any other important information about the user. When the receiving application gets a signed message from a user, the application can then verify the public key received with the message by comparing it to the public key stored in the KCA database.

</dd> <dt>

<span id="_security_key_container_gly"></span><span id="_SECURITY_KEY_CONTAINER_GLY"></span>**key container**
</dt> <dd>

A part of the key database that contains all the key pairs (exchange and signature key pairs) belonging to a specific user. Each container has a unique name that is used when calling the **CryptAcquireContext** function to get a handle to the container.

</dd> <dt>

<span id="_security_key_database_gly"></span><span id="_SECURITY_KEY_DATABASE_GLY"></span>**key database**
</dt> <dd>

A database that contains the persistent cryptographic keys for a specific CSP. The database contains one or more key containers, which individually store all the cryptographic key pairs for a specific user.

See also *key container*.

</dd> <dt>

<span id="_security_key_distribution_center_gly"></span><span id="_SECURITY_KEY_DISTRIBUTION_CENTER_GLY"></span>**Key Distribution Center**
</dt> <dd>

(KDC) A network service that supplies session tickets and temporary session keys used in the Kerberos V5 authentication protocol. The KDC runs as a privileged process on all domain controllers.

See also *Kerberos protocol*.

</dd> <dt>

<span id="_security_key_exchange_algorithm_gly"></span><span id="_SECURITY_KEY_EXCHANGE_ALGORITHM_GLY"></span>**key exchange algorithm**
</dt> <dd>

An algorithm used to encrypt and decrypt exchange keys (symmetric session keys). Some common key exchange algorithms include Diffie-Hellman and KEA, the key exchange algorithm specified by a PROV\_FORTEZZA provider type. The KEA algorithm is an improved version of the Diffie-Hellman algorithm. Each provider type can specify only one key exchange algorithm.

</dd> <dt>

<span id="_security_key_exchange_algorithm_name_gly"></span><span id="_SECURITY_KEY_EXCHANGE_ALGORITHM_NAME_GLY"></span>**Key Exchange Algorithm**
</dt> <dd>

(KEA) The key exchange algorithm specified by a PROV\_FORTEZZA provider type. This algorithm is an improved version of the Diffie-Hellman algorithm.

</dd> <dt>

<span id="_security_key_exchange_certificate_gly"></span><span id="_SECURITY_KEY_EXCHANGE_CERTIFICATE_GLY"></span>**key exchange certificate**
</dt> <dd>

A certificate used to encrypt information sent to another party. The certification authority (CA) key exchange certificate can be used by a client to encrypt information sent to the CA.

</dd> <dt>

<span id="_security_key_exchange_functions_gly"></span><span id="_SECURITY_KEY_EXCHANGE_FUNCTIONS_GLY"></span>**key exchange functions**
</dt> <dd>

A set of functions used to exchange or transmit keys. Key exchange functions can also be used to implement fully authenticated three-phase key exchanges.

</dd> <dt>

<span id="_security_key_exchange_key_pair_gly"></span><span id="_SECURITY_KEY_EXCHANGE_KEY_PAIR_GLY"></span>**key-exchange key pair**
</dt> <dd>

See [*exchange key pair*](e-gly.md).

</dd> <dt>

<span id="_security_key_exchange_private_key_gly"></span><span id="_SECURITY_KEY_EXCHANGE_PRIVATE_KEY_GLY"></span>**key exchange private key**
</dt> <dd>

The private key of an exchange key pair.

See also [*exchange key pair*](e-gly.md).

</dd> <dt>

<span id="_security_key_exchange_protocol_gly"></span><span id="_SECURITY_KEY_EXCHANGE_PROTOCOL_GLY"></span>**key exchange protocol**
</dt> <dd>

A protocol by which two parties exchange information to establish a shared secret. The shared secret is then typically used as a symmetric encryption key.

</dd> <dt>

<span id="_security_key_exchange_public_key_gly"></span><span id="_SECURITY_KEY_EXCHANGE_PUBLIC_KEY_GLY"></span>**key exchange public key**
</dt> <dd>

The public key of an exchange key pair.

See also [*exchange key pair*](e-gly.md).

</dd> <dt>

<span id="_security_key_generation_functions_gly"></span><span id="_SECURITY_KEY_GENERATION_FUNCTIONS_GLY"></span>**key generation functions**
</dt> <dd>

A set of functions used by applications to generate and customize cryptographic keys. These functions include full support for changing chaining modes, initialization vectors, and other encryption features.

</dd> <dt>

<span id="_security_key_length_gly"></span><span id="_SECURITY_KEY_LENGTH_GLY"></span>**key length**
</dt> <dd>

Values specified by some providers that indicate the length of the public/private key pairs and session keys used with that provider.

</dd> <dt>

<span id="_security_key_pair_gly"></span><span id="_SECURITY_KEY_PAIR_GLY"></span>**key pair**
</dt> <dd>

A private key and its related public key.

</dd> <dt>

<span id="_security_key_storage_provider_gly"></span><span id="_SECURITY_KEY_STORAGE_PROVIDER_GLY"></span>**key storage provider**
</dt> <dd>

(KSP) An independent software module that implements functionality to create, manage, store, and retrieve [*private keys*](p-gly.md).

</dd> <dt>

<span id="_security_ksp_gly"></span><span id="_SECURITY_KSP_GLY"></span>**KSP**
</dt> <dd>

See *key storage provider*.

</dd> </dl>

 

 



