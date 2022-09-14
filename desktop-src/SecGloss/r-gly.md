---
description: Contains definitions of security terms that begin with the letter R.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: ce589e18-02ac-42c2-b76b-776deb686bbd
title: R (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# R (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q R [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_rc2_gly"></span><span id="_SECURITY_RC2_GLY"></span>**RC2**
</dt> <dd>

The [*CryptoAPI*](c-gly.md) algorithm name for the RC2 algorithm.

See also *RC2 block algorithm*.

</dd> <dt>

<span id="_security_rc2_block_algorithm_gly"></span><span id="_SECURITY_RC2_BLOCK_ALGORITHM_GLY"></span>**RC2 block algorithm**
</dt> <dd>

A data [*encryption*](e-gly.md) algorithm based on the RC2 64-bit symmetric block cipher. RC2 is specified by PROV\_RSA\_FULL provider types. [*CryptoAPI*](c-gly.md) references this algorithm by its identifier (CALG\_RC2), name (RC2), and class (ALG\_CLASS\_DATA\_ENCRYPT).

</dd> <dt>

<span id="_security_rc4_gly"></span><span id="_SECURITY_RC4_GLY"></span>**RC4**
</dt> <dd>

The [*CryptoAPI*](c-gly.md) algorithm name for the RC4 algorithm.

See also *RC4 stream algorithm*.

</dd> <dt>

<span id="_security_rc4_stream_algorithm_gly"></span><span id="_SECURITY_RC4_STREAM_ALGORITHM_GLY"></span>**RC4 stream algorithm**
</dt> <dd>

A data [*encryption*](e-gly.md) algorithm based on the RC4 symmetric stream cipher. RC4 is specified by PROV\_RSA\_FULL provider types. [*CryptoAPI*](c-gly.md) references this algorithm by its identifier (CALG\_RC4), name (RC4), and class (ALG\_CLASS\_DATA\_ENCRYPT).

</dd> <dt>

<span id="_security_rdn_gly"></span><span id="_SECURITY_RDN_GLY"></span>**RDN**
</dt> <dd>

See *relative distinguished name*.

</dd> <dt>

<span id="_security_reader_gly"></span><span id="_SECURITY_READER_GLY"></span>**reader**
</dt> <dd>

A standard device within the [*smart card*](s-gly.md) subsystem. An interface device (IFD) that supports bidirectional input/output to a smart card. It may be associated with an entire system, one or more reader groups, or with a specific terminal. The smart card subsystem allows a reader to be dedicated to the terminal to which it is assigned. However, currently only one terminal exists on a computer.

</dd> <dt>

<span id="_security_reader_driver_gly"></span><span id="_SECURITY_READER_DRIVER_GLY"></span>**reader driver**
</dt> <dd>

A specific driver that maps driver services to a specific hardware reader device. It must communicate card insertion and removal events to the [*smart card*](s-gly.md) class driver for forwarding to the smart card resource manager, and it must provide data exchange capabilities to the card by any raw, T=0, T=1, or PTS protocol.

</dd> <dt>

<span id="_security_reader_group_gly"></span><span id="_SECURITY_READER_GROUP_GLY"></span>**reader group**
</dt> <dd>

A logical group of readers. Reader groups can be defined by the system or created by users or administrators. Reader groups are used by smart card functions that can act upon groups of readers. To avoid naming collisions with user-defined groups, Microsoft reserves the use of any name that contains the dollar sign ($).

</dd> <dt>

<span id="_security_reader_helper_driver_gly"></span><span id="_SECURITY_READER_HELPER_DRIVER_GLY"></span>**reader helper driver**
</dt> <dd>

Provides common smart card driver support routines and additional T=0 and T=1 protocol support to specific drivers as needed.

</dd> <dt>

<span id="_security_reference_count_gly"></span><span id="_SECURITY_REFERENCE_COUNT_GLY"></span>**reference count**
</dt> <dd>

An integer value used to keep track of a COM object. When an object is created, its reference count is set to one. Every time an interface is bound to the object, its reference count is incremented; when the interface connection is destroyed, the reference count is decremented. The object is destroyed when the reference count reaches zero. All interfaces to that object are then not valid.

</dd> <dt>

<span id="_security_relative_distinguished_name_gly"></span><span id="_SECURITY_RELATIVE_DISTINGUISHED_NAME_GLY"></span>**relative distinguished name**
</dt> <dd>

(RDN) An entity included as the subject in a request for a certificate. The elements in an RDN are defined by its attributes and do not need to include a name. With respect to [*CryptoAPI*](c-gly.md), an RDN is defined by a CERT\_RDN structure, which in turn points to an array of CERT\_RDN\_ATTR attribute structures. Each attribute structure specifies a single attribute.

</dd> <dt>

<span id="_security_relative_identifier_gly"></span><span id="_SECURITY_RELATIVE_IDENTIFIER_GLY"></span>**relative identifier**
</dt> <dd>

(RID) The portion of a [*security identifier*](s-gly.md) (SID) that identifies a user or group in relation to the authority that issued the SID.

</dd> <dt>

<span id="_security_relocated_store_gly"></span><span id="_SECURITY_RELOCATED_STORE_GLY"></span>**relocated store**
</dt> <dd>

A [*certificate store*](c-gly.md) that has been moved from its default registry location to a different location in the registry.

</dd> <dt>

<span id="_security_remote_store_gly"></span><span id="_SECURITY_REMOTE_STORE_GLY"></span>**remote store**
</dt> <dd>

A [*certificate store*](c-gly.md) located on another computer, such as a file server or some other shared remote computer.

</dd> <dt>

<span id="_security_reply_apdu_gly"></span><span id="_SECURITY_REPLY_APDU_GLY"></span>**reply APDU**
</dt> <dd>

An [*application protocol data unit*](a-gly.md) (APDU) sent in reply to a received APDU.

</dd> <dt>

<span id="_security_repudiation_gly"></span><span id="_SECURITY_REPUDIATION_GLY"></span>**repudiation**
</dt> <dd>

The ability of a user to falsely deny having performed an action while other parties cannot prove otherwise. For example, a user who deleted a file and who can successfully deny having done so.

</dd> <dt>

<span id="_security_resource_manager_gly"></span><span id="_SECURITY_RESOURCE_MANAGER_GLY"></span>**resource manager**
</dt> <dd>

The module of the [*smart card*](s-gly.md) subsystem that manages access to multiple readers and smart cards. The resource manager identifies and tracks resources, allocates readers and resources across multiple applications, and supports transaction primitives for accessing services available on a given card.

</dd> <dt>

<span id="_security_resource_manager_api_gly"></span><span id="_SECURITY_RESOURCE_MANAGER_API_GLY"></span>**resource manager API**
</dt> <dd>

A set of Windows functions that provide direct access to the resource manager's services.

</dd> <dt>

<span id="_security_resource_manager_context_gly"></span><span id="_SECURITY_RESOURCE_MANAGER_CONTEXT_GLY"></span>**resource manager context**
</dt> <dd>

The context used by the resource manager when accessing the smart card database. The resource manager context is primarily used by the query and management functions when accessing the database. The scope of the resource manager context can be the current user or the system.

</dd> <dt>

<span id="_security_revocation_list_gly"></span><span id="_SECURITY_REVOCATION_LIST_GLY"></span>**revocation list**
</dt> <dd>

See [*Certificate Revocation List*](c-gly.md).

</dd> <dt>

<span id="_security_rid_gly"></span><span id="_SECURITY_RID_GLY"></span>**RID**
</dt> <dd>

See *relative identifier*.

</dd> <dt>

<span id="_security_root_authority_gly"></span><span id="_SECURITY_ROOT_AUTHORITY_GLY"></span>**root authority**
</dt> <dd>

The [*certification authority*](c-gly.md) (CA) at the top of a CA hierarchy. The root authority certifies CAs in the next level of the hierarchy.

</dd> <dt>

<span id="_security_root_certificate_gly"></span><span id="_SECURITY_ROOT_CERTIFICATE_GLY"></span>**root certificate**
</dt> <dd>

A self-signed [*certification authority*](c-gly.md) (CA) certificate that identifies a CA. It is called a root certificate because it is the certificate for the root CA. The root CA must sign its own CA certificate because by definition there is no higher certifying authority to sign its CA certificate.

</dd> <dt>

<span id="_security_rsa_gly"></span><span id="_SECURITY_RSA_GLY"></span>**RSA**
</dt> <dd>

RSA Data Security, Inc., a major developer and publisher of [*public key cryptography standards*](p-gly.md) (PKCS). The "RSA" in the name stands for the names of the company's three developers and the owners: Rivest, Shamir, and Adleman.

</dd> <dt>

<span id="_security_rsa_keyx_gly"></span><span id="_SECURITY_RSA_KEYX_GLY"></span>**RSA\_KEYX**
</dt> <dd>

The [*CryptoAPI*](c-gly.md) algorithm name for the RSA key exchange algorithm. CryptoAPI also references this algorithm by its algorithm identifier (CALG\_RSA\_KEYX) and class (ALG\_CLASS\_KEY\_EXCHANGE).

</dd> <dt>

<span id="_security_rsa_sign_gly"></span><span id="_SECURITY_RSA_SIGN_GLY"></span>**RSA\_SIGN**
</dt> <dd>

The CryptoAPI algorithm name for the RSA signature algorithm. CryptoAPI also references this algorithm by its algorithm identifier (CALG\_RSA\_SIGN) and class (ALG\_CLASS\_SIGNATURE).

</dd> <dt>

<span id="_security_rsa_public_key_algorithm_gly"></span><span id="_SECURITY_RSA_PUBLIC_KEY_ALGORITHM_GLY"></span>**RSA Public Key algorithm**
</dt> <dd>

A key exchange and signature algorithm based on the popular RSA Public Key cipher. This algorithm is used by PROV\_RSA\_FULL, PROV\_RSA\_SIG, PROV\_MS\_EXCHANGE, and PROV\_SSL provider types. CryptoAPI references this algorithm by its identifiers (CALG\_RSA\_KEYX and CALG\_RSA\_SIGN), names (RSA\_KEYX and RSA\_SIGN) and class (ALG\_CLASS\_KEY\_EXCHANGE).

</dd> </dl>

 

 



