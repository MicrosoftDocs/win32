---
description: Contains definitions of security terms that begin with the letter A.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 0baaa937-f635-4500-8dcd-9dbbd6f4cd02
title: A (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# A (Security Glossary)

A [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_absolute_security_descriptor_gly"></span><span id="_SECURITY_ABSOLUTE_SECURITY_DESCRIPTOR_GLY"></span>**absolute security descriptor**
</dt> <dd>

A security descriptor structure that contains pointers to the security information associated with an object.

See also [*security descriptor*](s-gly.md) and [*self-relative security descriptor*](s-gly.md).

</dd> <dt>

<span id="_security_abstract_syntax_notation_one_gly"></span><span id="_SECURITY_ABSTRACT_SYNTAX_NOTATION_ONE_GLY"></span>**Abstract Syntax Notation One**
</dt> <dd>

(ASN.1) A method used to specify abstract objects that are intended for serial transmission.

</dd> <dt>

<span id="_security_access_block_gly"></span><span id="_SECURITY_ACCESS_BLOCK_GLY"></span>**access block**
</dt> <dd>

A key BLOB that contains the key of the symmetric cipher used to encrypt a file or message. The access block can only be opened with a private key.

</dd> <dt>

<span id="_security_access_control_entry_gly"></span><span id="_SECURITY_ACCESS_CONTROL_ENTRY_GLY"></span>**access control entry**
</dt> <dd>

(ACE) An entry in an access control list (ACL). An ACE contains a set of access rights and a security identifier (SID) that identifies a trustee for whom the rights are allowed, denied, or audited.

See also *access control list*, [*security identifier*](s-gly.md), and [*trustee*](t-gly.md).

</dd> <dt>

<span id="_security_access_control_list_gly"></span><span id="_SECURITY_ACCESS_CONTROL_LIST_GLY"></span>**access control list**
</dt> <dd>

(ACL) A list of security protections that applies to an object. (An object can be a file, process, event, or anything else having a security descriptor.) An entry in an access control list (ACL) is an access control entry (ACE). There are two types of access control list, discretionary and system.

See also *access control entry*, [*discretionary access control list*](d-gly.md), [*security descriptor*](s-gly.md), and [*system access control list*](s-gly.md).

</dd> <dt>

<span id="_security_access_mask_gly"></span><span id="_SECURITY_ACCESS_MASK_GLY"></span>**access mask**
</dt> <dd>

A 32-bit value that specifies the rights that are allowed or denied in an access control entry (ACE). An access mask is also used to request access rights when an object is opened.

See also *access control entry*.

</dd> <dt>

<span id="_security_access_token_gly"></span><span id="_SECURITY_ACCESS_TOKEN_GLY"></span>**access token**
</dt> <dd>

An access token contains the security information for a logon session. The system creates an access token when a user logs on, and every process executed on behalf of the user has a copy of the token. The token identifies the user, the user's groups, and the user's privileges. The system uses the token to control access to securable objects and to control the ability of the user to perform various system-related operations on the local computer. There are two kinds of access token, primary and impersonation.

See also [*impersonation token*](i-gly.md), [*primary token*](p-gly.md), [*privilege*](p-gly.md), [*process*](p-gly.md), and [*security identifier*](s-gly.md).

</dd> <dt>

<span id="_security_ace_gly"></span><span id="_SECURITY_ACE_GLY"></span>**ACE**
</dt> <dd>

See *access control entry*.

</dd> <dt>

<span id="_security_acl_gly"></span><span id="_SECURITY_ACL_GLY"></span>**ACL**
</dt> <dd>

See *access control list*.

</dd> <dt>

<span id="_security_aes_gly"></span><span id="_SECURITY_AES_GLY"></span>**Advanced Encryption Standard**
</dt> <dd>

(AES) A cryptographic algorithm specified by the National Institute of Standards and Technology (NIST) to protect sensitive information.

</dd> <dt>

<span id="_security_alg_class_data_encrypt_gly"></span><span id="_SECURITY_ALG_CLASS_DATA_ENCRYPT_GLY"></span>**ALG\_CLASS\_DATA\_ENCRYPT**
</dt> <dd>

The CryptoAPI algorithm class for data encryption algorithms. Typical data encryption algorithms include RC2 and RC4.

</dd> <dt>

<span id="_security_alg_class_hash_gly"></span><span id="_SECURITY_ALG_CLASS_HASH_GLY"></span>**ALG\_CLASS\_HASH**
</dt> <dd>

The CryptoAPI algorithm class for hashing algorithms. Typical hashing algorithms include MD2, MD5, SHA-1, and MAC.

</dd> <dt>

<span id="_security_alg_class_key_exchange_gly"></span><span id="_SECURITY_ALG_CLASS_KEY_EXCHANGE_GLY"></span>**ALG\_CLASS\_KEY\_EXCHANGE**
</dt> <dd>

The CryptoAPI algorithm class for key exchange algorithms. A typical key exchange algorithm is RSA\_KEYX.

</dd> <dt>

<span id="_security_alg_class_signature_gly"></span><span id="_SECURITY_ALG_CLASS_SIGNATURE_GLY"></span>**ALG\_CLASS\_SIGNATURE**
</dt> <dd>

The CryptoAPI algorithm class for signature algorithms. A typical digital signature algorithm is RSA\_SIGN.

</dd> <dt>

<span id="_security_apdu_gly"></span><span id="_SECURITY_APDU_GLY"></span>**APDU**
</dt> <dd>

See *application protocol data unit*.

</dd> <dt>

<span id="_security_application_protocol_data_unit_gly"></span><span id="_SECURITY_APPLICATION_PROTOCOL_DATA_UNIT_GLY"></span>**application protocol data unit**
</dt> <dd>

(APDU) A command sequence (an Application Protocol Data Unit) that can be sent by the smart card or returned by the application.

See also [*reply APDU*](r-gly.md).

</dd> <dt>

<span id="_security_application_protocol_gly"></span><span id="_SECURITY_APPLICATION_PROTOCOL_GLY"></span>**application protocol**
</dt> <dd>

A protocol that normally resides on top of the transport layer. For example, HTTP, TELNET, FTP, and SMTP are all application protocols.

</dd> <dt>

<span id="_security_asn.1_gly"></span><span id="_SECURITY_ASN.1_GLY"></span>**ASN.1**
</dt> <dd>

See *Abstract Syntax Notation One*.

</dd> <dt>

<span id="_security_ascii_gly"></span><span id="_SECURITY_ASCII_GLY"></span>**ASCII**
</dt> <dd>

American Standard Code for Information Interchange. A coding scheme that assigns numeric values to letters, numbers, punctuation marks, and certain other characters.

</dd> <dt>

<span id="_security_asymmetric_algorithm_gly"></span><span id="_SECURITY_ASYMMETRIC_ALGORITHM_GLY"></span>**asymmetric algorithm**
</dt> <dd>

See [*public key algorithm*](p-gly.md).

</dd> <dt>

<span id="_security_asymmetric_key_gly"></span><span id="_SECURITY_ASYMMETRIC_KEY_GLY"></span>**asymmetric key**
</dt> <dd>

One of a pair of keys used with an asymmetric cryptographic algorithm. Such an algorithm uses two cryptographic keys: a "public key" for encryption and a "private key" for decryption. In signature and verification, the roles are reversed: the public key is used for verification, and the private key is used for signature generation. The most important feature of such algorithms is that their security does not depend on keeping the public key secret (though it may require some assurance of authenticity of public keys, for example, that they be obtained from a trusted source). Secrecy of the private key is required. Examples of public key algorithms are [*Digital Signature Algorithm (DSA)*](d-gly.md), Elliptic Curve Digital Signature Algorithm (ECDSA), and the Rivest-Shamir-Adleman (RSA) family of algorithms.

</dd> <dt>

<span id="_security_atr_string_gly"></span><span id="_SECURITY_ATR_STRING_GLY"></span>**ATR string**
</dt> <dd>

A sequence of bytes returned from a smart card when it is turned on. These bytes are used to identify the card to the system.

</dd> <dt>

<span id="_security_attribute_gly"></span><span id="_SECURITY_ATTRIBUTE_GLY"></span>**attribute**
</dt> <dd>

An element of a relative distinguished name (RDN). Some typical attributes include common name, surname, email address, postal address, and country/region name.

</dd> <dt>

<span id="_security_attribute_blob_gly"></span><span id="_SECURITY_ATTRIBUTE_BLOB_GLY"></span>**attribute BLOB**
</dt> <dd>

An encoded representation of the attribute information stored in a certificate request.

</dd> <dt>

<span id="_security_audit_security_object_gly"></span><span id="_SECURITY_AUDIT_SECURITY_OBJECT_GLY"></span>**Audit security object**
</dt> <dd>

A security descriptor that controls access to the audit policy subsystem.

</dd> <dt>

<span id="_security_authentication_gly"></span><span id="_SECURITY_AUTHENTICATION_GLY"></span>**authentication**
</dt> <dd>

The process for verifying that a user, computer, service, or process is who or what it claims to be.

</dd> <dt>

<span id="_security_authentication_package_gly"></span><span id="_SECURITY_AUTHENTICATION_PACKAGE_GLY"></span>**authentication package**
</dt> <dd>

A DLL that encapsulates the authentication logic used to determine whether to permit a user to log on. LSA authenticates a user logon by sending the request to an authentication package. The authentication package then examines the logon information and either authenticates or rejects the user logon attempt.

</dd> <dt>

<span id="_security_authenticode_gly"></span><span id="_SECURITY_AUTHENTICODE_GLY"></span>**Authenticode**
</dt> <dd>

A security feature of Internet Explorer. Authenticode allows vendors of downloadable executable code (plug-ins or ActiveX controls, for example) to attach digital certificates to their products to assure end users that the code is from the original developer and has not been altered. Authenticode lets end users decide for themselves whether to accept or reject software components posted on the Internet before downloading begins.

</dd> </dl>

 

 



