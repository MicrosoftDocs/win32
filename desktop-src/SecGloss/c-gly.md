---
description: Contains definitions of security terms that begin with the letter C.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: db46def4-bfdc-4801-a57d-d568e94a2dbb
title: C (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# C (Security Glossary)

[A](a-gly.md) [B](b-gly.md) C [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_ca_gly"></span><span id="_SECURITY_CA_GLY"></span>**CA**
</dt> <dd>

See *certification authority*.

</dd> <dt>

<span id="_security_ca_certificate_gly"></span><span id="_SECURITY_CA_CERTIFICATE_GLY"></span>**CA certificate**
</dt> <dd>

Identifies the certification authority (CA) that issues server and client authentication certificates to the servers and clients that request these certificates. Because it contains a public key used in digital signatures, it is also referred to as a signature certificate. If the CA is a root authority, the CA certificate may be referred to as a root certificate. Also sometimes known as a site certificate.

</dd> <dt>

<span id="_security_ca_hierarchy_gly"></span><span id="_SECURITY_CA_HIERARCHY_GLY"></span>**CA hierarchy**
</dt> <dd>

A certification authority (CA) hierarchy contains multiple CAs. It is organized such that each CA is certified by another CA in a higher level of the hierarchy until the top of the hierarchy, also known as the root authority, is reached.

</dd> <dt>

<span id="_security_calg_dh_ephem_gly"></span><span id="_SECURITY_CALG_DH_EPHEM_GLY"></span>**CALG\_DH\_EPHEM**
</dt> <dd>

The CryptoAPI algorithm identifier for the Diffie-Hellman key-exchange algorithm when used for the generation of ephemeral keys.

See also [*Diffie-Hellman (ephemeral) key-exchange algorithm*](d-gly.md).

</dd> <dt>

<span id="_security_calg_dh_sf_gly"></span><span id="_SECURITY_CALG_DH_SF_GLY"></span>**CALG\_DH\_SF**
</dt> <dd>

The CryptoAPI algorithm identifier for the Diffie-Hellman key-exchange algorithm when used for the generation of store-and-forward keys.

See also [*Diffie-Hellman (store and forward) key-exchange algorithm*](d-gly.md).

</dd> <dt>

<span id="_security_calg_hmac_gly"></span><span id="_SECURITY_CALG_HMAC_GLY"></span>**CALG\_HMAC**
</dt> <dd>

The CryptoAPI algorithm identifier for the hash-based Message Authentication Code algorithm.

See also [*Hash-Based Message Authentication Code*](h-gly.md).

</dd> <dt>

<span id="_security_calg_mac_gly"></span><span id="_SECURITY_CALG_MAC_GLY"></span>**CALG\_MAC**
</dt> <dd>

The CryptoAPI algorithm identifier for the Message Authentication Code algorithm.

See also [*Message Authentication Code*](m-gly.md).

</dd> <dt>

<span id="_security_calg_md2_gly"></span><span id="_SECURITY_CALG_MD2_GLY"></span>**CALG\_MD2**
</dt> <dd>

The CryptoAPI algorithm identifier for the MD2 hash algorithm.

See also [*MD2 algorithm*](m-gly.md).

</dd> <dt>

<span id="_security_calg_md5_gly"></span><span id="_SECURITY_CALG_MD5_GLY"></span>**CALG\_MD5**
</dt> <dd>

The CryptoAPI algorithm identifier for the MD5 hash algorithm.

See also [*MD5 algorithm*](m-gly.md).

</dd> <dt>

<span id="_security_calg_rc2_gly"></span><span id="_SECURITY_CALG_RC2_GLY"></span>**CALG\_RC2**
</dt> <dd>

The CryptoAPI algorithm identifier for the RC2 block cipher algorithm.

See also [*RC2 block algorithm*](r-gly.md).

</dd> <dt>

<span id="_security_calg_rc4_gly"></span><span id="_SECURITY_CALG_RC4_GLY"></span>**CALG\_RC4**
</dt> <dd>

The CryptoAPI algorithm identifier for the RC4 stream cipher algorithm.

See also [*RC4 stream algorithm*](r-gly.md).

</dd> <dt>

<span id="_security_calg_rsa_keyx_gly"></span><span id="_SECURITY_CALG_RSA_KEYX_GLY"></span>**CALG\_RSA\_KEYX**
</dt> <dd>

The CryptoAPI algorithm identifier for the RSA public key algorithm when used for key exchange.

See also [*RSA public key algorithm*](r-gly.md).

</dd> <dt>

<span id="_security_calg_rsa_sign_gly"></span><span id="_SECURITY_CALG_RSA_SIGN_GLY"></span>**CALG\_RSA\_SIGN**
</dt> <dd>

The CryptoAPI algorithm identifier for the RSA public key algorithm when used to generate digital signatures.

See also [*RSA public key algorithm*](r-gly.md).

</dd> <dt>

<span id="_security_calg_sha_gly"></span><span id="_SECURITY_CALG_SHA_GLY"></span>**CALG\_SHA**
</dt> <dd>

The CryptoAPI algorithm identifier for the Secure Hash Algorithm (SHA-1).

See also [*Secure Hash Algorithm*](s-gly.md).

</dd> <dt>

<span id="_security_cast_gly"></span><span id="_SECURITY_CAST_GLY"></span>**CAST**
</dt> <dd>

A group of DES-like symmetric block ciphers developed by C. M. Adams and S. E. Tavares. PROV\_MS\_EXCHANGE provider types specify a particular CAST algorithm that uses a 64-bit block size.

</dd> <dt>

<span id="_security_cbc_gly"></span><span id="_SECURITY_CBC_GLY"></span>**CBC**
</dt> <dd>

See *Cipher Block Chaining*.

</dd> <dt>

<span id="_security_certificate_gly"></span><span id="_SECURITY_CERTIFICATE_GLY"></span>**certificate**
</dt> <dd>

A digitally signed statement that contains information about an entity and the entity's public key, thus binding these two pieces of information together. A certificate is issued by a trusted organization (or entity) called a *certification authority* (CA) after the CA has verified that the entity is who it says it is.

Certificates can contain different types of data. For example, an X.509 certificate includes the format of the certificate, the serial number of the certificate, the algorithm used to sign the certificate, the name of the CA that issued the certificate, the name and public key of the entity requesting the certificate, and the CA's signature.

</dd> <dt>

<span id="_security_certificate_blob_gly"></span><span id="_SECURITY_CERTIFICATE_BLOB_GLY"></span>**certificate BLOB**
</dt> <dd>

A BLOB that contains the certificate data.

A certificate BLOB is created by calls to **CryptEncodeObject**. The process is complete when the output of the call contains all the certificate data.

</dd> <dt>

<span id="_security_certificate_context_gly"></span><span id="_SECURITY_CERTIFICATE_CONTEXT_GLY"></span>**certificate context**
</dt> <dd>

A CERT\_CONTEXT structure that contains a handle to a certificate store, a pointer to the original encoded certificate BLOB, a pointer to a CERT\_INFO structure, and an encoding type member. It is the **CERT\_INFO** structure that contains most of the certificate information.

</dd> <dt>

<span id="_security_certificate_encode_decode_functions_gly"></span><span id="_SECURITY_CERTIFICATE_ENCODE_DECODE_FUNCTIONS_GLY"></span>**certificate encode/decode functions**
</dt> <dd>

Functions that manage the translation of certificates and related material into standard, binary formats that can be used in different environments.

</dd> <dt>

<span id="_security_certificate_encoding_type_gly"></span><span id="_SECURITY_CERTIFICATE_ENCODING_TYPE_GLY"></span>**certificate encoding type**
</dt> <dd>

Defines how the certificate is encoded. The certificate encoding type is stored in the low-order word of the encoding type (**DWORD**) structure.

</dd> <dt>

<span id="_security_certificate_management_over_cms_gly"></span><span id="_SECURITY_CERTIFICATE_MANAGEMENT_OVER_CMS_GLY"></span>**Certificate Management over CMS**
</dt> <dd>

CMC. Certificate Management over CMS. CMC is a certificate management protocol that uses Cryptographic Message Syntax (CMS). Microsoft wraps CMC certificate requests in a [*PKCS \#7*](p-gly.md) (CMS) request object before sending the request to an enrollment server.

</dd> <dt>

<span id="_security_certificate_name_blob_gly"></span><span id="_SECURITY_CERTIFICATE_NAME_BLOB_GLY"></span>**certificate name BLOB**
</dt> <dd>

An encoded representation of the name information that is included in certificates. Each name BLOB is mapped to a **CERT\_NAME\_BLOB** structure.

For example, the issuer and subject information referenced by a **CERT\_INFO** structure is stored in two **CERT\_NAME\_BLOB** structures.

</dd> <dt>

<span id="_security_certificate_policy_gly"></span><span id="_SECURITY_CERTIFICATE_POLICY_GLY"></span>**certificate policy**
</dt> <dd>

A named set of rules that indicate the applicability of certificates for a specific class of applications with common security requirements. Such a policy might, for example, limit certain certificates to electronic data interchange transactions within given price limits.

</dd> <dt>

<span id="_security_certificate_request_gly"></span><span id="_SECURITY_CERTIFICATE_REQUEST_GLY"></span>**certificate request**
</dt> <dd>

A specially formatted electronic message (sent to a CA) used to request a certificate. The request must contain the information required by the CA to authenticate the request, plus the public key of the entity requesting the certificate.

All the information necessary to create the request is mapped to a **CERT\_REQUEST\_INFO** structure.

</dd> <dt>

<span id="_security_certificate_revocation_list_gly"></span><span id="_SECURITY_CERTIFICATE_REVOCATION_LIST_GLY"></span>**certificate revocation list**
</dt> <dd>

(CRL) A document maintained and published by a certification authority (CA) that lists certificates issued by the CA that are no longer valid.

</dd> <dt>

<span id="_security_certificate_server_gly"></span><span id="_SECURITY_CERTIFICATE_SERVER_GLY"></span>**certificate server**
</dt> <dd>

A server that issues certificates for a particular CA. The certificate server software provides customizable services for issuing and managing certificates used in security systems that employ public key cryptography.

</dd> <dt>

<span id="_security_certificate_services_gly"></span><span id="_SECURITY_CERTIFICATE_SERVICES_GLY"></span>**Certificate Services**
</dt> <dd>

A software service that issues certificates for a particular *certification authority* (CA). It provides customizable services for issuing and managing certificates for the enterprise. Certificates can be used to provide authentication support, including secure email, web-based authentication, and smart card authentication.

</dd> <dt>

<span id="_security_certificate_store_gly"></span><span id="_SECURITY_CERTIFICATE_STORE_GLY"></span>**certificate store**
</dt> <dd>

Typically, a permanent storage where certificates, certificate revocation lists (CRLs), and certificate trust lists (CTLs) are stored. It is possible, however, to create and open a certificate store solely in memory when working with certificates that do not need to be put in permanent storage.

The certificate store is central to much of the certificate functionality in CryptoAPI.

</dd> <dt>

<span id="_security_certificate_store_functions_gly"></span><span id="_SECURITY_CERTIFICATE_STORE_FUNCTIONS_GLY"></span>**certificate store functions**
</dt> <dd>

Functions that manage the storage and retrieval data such as certificates, certificate revocation lists (CRLs), and certificate trust lists (CTLs). These functions can be separated into common certificate functions, certificate revocation list functions, and certificate trust list functions.

</dd> <dt>

<span id="_security_certificate_template_gly"></span><span id="_SECURITY_CERTIFICATE_TEMPLATE_GLY"></span>**certificate template**
</dt> <dd>

A Windows construct that profiles certificates (that is, it prespecifies the format and content) based on their intended usage. When requesting a [*certificate*](/windows) from a Windows enterprise *certification authority* (CA), certificate requesters are, depending on their access rights, able to select from a variety of certificate types that are based on certificate templates, such as User and Code Signing.

</dd> <dt>

<span id="_security_certificate_trust_list_gly"></span><span id="_SECURITY_CERTIFICATE_TRUST_LIST_GLY"></span>**certificate trust list**
</dt> <dd>

(CTL) A predefined list of items that have been signed by a trusted entity. A CTL can be anything, such as a list of hashes of certificates, or a list of file names. All the items in the list are authenticated (approved) by the signing entity.

</dd> <dt>

<span id="_security_certification_authority_gly"></span><span id="_SECURITY_CERTIFICATION_AUTHORITY_GLY"></span>**certification authority**
</dt> <dd>

(CA) An entity entrusted to issue certificates that assert that the recipient individual, computer, or organization requesting the certificate fulfills the conditions of an established policy.

</dd> <dt>

<span id="_security_cfb_gly"></span><span id="_SECURITY_CFB_GLY"></span>**CFB**
</dt> <dd>

See *Cipher Feedback*.

</dd> <dt>

<span id="_security_chaining_mode_gly"></span><span id="_SECURITY_CHAINING_MODE_GLY"></span>**chaining mode**
</dt> <dd>

A block cipher mode that introduces feedback by combining ciphertext and plaintext.

See also *Cipher Block Chaining*.

</dd> <dt>

<span id="_security_cipher_gly"></span><span id="_SECURITY_CIPHER_GLY"></span>**cipher**
</dt> <dd>

A cryptographic algorithm used to encrypt data; that is, to transform plaintext into ciphertext using a predefined key.

</dd> <dt>

<span id="_security_cipher_block_chaining_gly"></span><span id="_SECURITY_CIPHER_BLOCK_CHAINING_GLY"></span>**Cipher Block Chaining**
</dt> <dd>

(CBC) A method of operating a symmetric block cipher that uses feedback to combine previously generated ciphertext with new plaintext.

Each plaintext block is combined with the ciphertext of the previous block by a bitwise-**XOR** operation before it is encrypted. Combining ciphertext and plaintext ensures that even if the plaintext contains many identical blocks, they will each encrypt to a different ciphertext block.

When the Microsoft Base Cryptographic Provider is used, CBC is the default cipher mode.

</dd> <dt>

<span id="_security_cipher_block_chaining_mac_gly"></span><span id="_SECURITY_CIPHER_BLOCK_CHAINING_MAC_GLY"></span>**Cipher Block Chaining MAC**
</dt> <dd>

A block cipher method that encrypts the base data with a block cipher and then uses the last encrypted block as the hash value. The encryption algorithm used to build the [*Message Authentication Code*](m-gly.md) (MAC) is the one that was specified when the session key was created.

</dd> <dt>

<span id="_security_cipher_feedback_gly"></span><span id="_SECURITY_CIPHER_FEEDBACK_GLY"></span>**Cipher Feedback**
</dt> <dd>

(CFB) A block cipher mode that processes small increments of plaintext into ciphertext, instead of processing an entire block at a time.

This mode uses a shift register that is one block size in length and divided into sections. For example, if the block size is 64 bits with eight bits processed at a time, then the shift register would be divided into eight sections.

</dd> <dt>

<span id="_security_cipher_mode_gly"></span><span id="_SECURITY_CIPHER_MODE_GLY"></span>**cipher mode**
</dt> <dd>

A block cipher mode (each block is encrypted individually) that can be specified by using the **CryptSetKeyParam** function. If the application does not explicitly specify one of these modes, then the cipher block chaining (CBC) cipher mode is used.

ECB: A block cipher mode that uses no feedback.

CBC: A block cipher mode that introduces feedback by combining ciphertext and plaintext.

CFB: A block cipher mode that processes small increments of plaintext into ciphertext, instead of processing an entire block at a time.

OFB: A block cipher mode that uses feedback similar to CFB.

</dd> <dt>

<span id="_security_ciphertext_gly"></span><span id="_SECURITY_CIPHERTEXT_GLY"></span>**ciphertext**
</dt> <dd>

A message that has been encrypted.

</dd> <dt>

<span id="_security_cleartext_gly"></span><span id="_SECURITY_CLEARTEXT_GLY"></span>**cleartext**
</dt> <dd>

See [*plaintext*](p-gly.md).

</dd> <dt>

<span id="_security_client_gly"></span><span id="_SECURITY_CLIENT_GLY"></span>**client**
</dt> <dd>

The application, rather than the server application, that initiates a connection to a server.

Compare with [*server*](s-gly.md).

</dd> <dt>

<span id="_security_client_certificate_gly"></span><span id="_SECURITY_CLIENT_CERTIFICATE_GLY"></span>**client certificate**
</dt> <dd>

Refers to a certificate used for client authentication, such as authenticating a web browser on a web server. When a web browser client attempts to access a secured web server, the client sends its certificate to the server to allow it to verify the client's identity.

</dd> <dt>

<span id="_security_cmc_gly"></span><span id="_SECURITY_CMC_GLY"></span>**CMC**
</dt> <dd>

See *Certificate Management over CMS*.

</dd> <dt>

<span id="_security_cng_gly"></span><span id="_SECURITY_CNG_GLY"></span>**CNG**
</dt> <dd>

See *Cryptography API: Next Generation*.

</dd> <dt>

<span id="_security_communication_protocol_gly"></span><span id="_SECURITY_COMMUNICATION_PROTOCOL_GLY"></span>**communication protocol**
</dt> <dd>

The method in which data is serialized (converted to a string of ones and zeros) and deserialized. The protocol is controlled by both software and data-transmission hardware.

Typically discussed in terms of layers, a simplified communication protocol might consist of an application layer, encode/decode layer, and hardware layer.

</dd> <dt>

<span id="_security_constrained_delegation_gly"></span><span id="_SECURITY_CONSTRAINED_DELEGATION_GLY"></span>**constrained delegation**
</dt> <dd>

Behavior that allows the server to forward requests on behalf of the client only to a specified list of services.

**Windows XP:** Constrained delegation is not supported.

</dd> <dt>

<span id="_security_context_gly"></span><span id="_SECURITY_CONTEXT_GLY"></span>**context**
</dt> <dd>

The security data relevant to a connection. A context contains information such as a session key and duration of the session.

</dd> <dt>

<span id="_security_context_function_gly"></span><span id="_SECURITY_CONTEXT_FUNCTION_GLY"></span>**context function**
</dt> <dd>

Functions used to connect to a cryptographic service provider (CSP). These functions enable applications to choose a specific CSP by name or get one with a needed class of functionality.

</dd> <dt>

<span id="_security_countersignature_gly"></span><span id="_SECURITY_COUNTERSIGNATURE_GLY"></span>**countersignature**
</dt> <dd>

A signature of an existing signature and message or a signature of an existing signature. A countersignature is used to sign the encrypted hash of an existing signature or to time stamp a message.

</dd> <dt>

<span id="_security_credentials_gly"></span><span id="_SECURITY_CREDENTIALS_GLY"></span>**credentials**
</dt> <dd>

Previously authenticated logon data used by a [*security principal*](s-gly.md) to establish its own identity, such as a password, or a Kerberos protocol ticket.

</dd> <dt>

<span id="_security_crl_gly"></span><span id="_SECURITY_CRL_GLY"></span>**CRL**
</dt> <dd>

See *certificate revocation list*.

</dd> <dt>

<span id="_security_crypt_asn_encoding_gly"></span><span id="_SECURITY_CRYPT_ASN_ENCODING_GLY"></span>**CRYPT\_ASN\_ENCODING**
</dt> <dd>

Encoding type that specifies certificate encoding. Certificate encoding types are stored in the low-order word of a **DWORD** (value is: 0x00000001). This encoding type is functionally the same as the X509\_ASN\_ENCODING encoding type.

</dd> <dt>

<span id="_security_cryptoanalysis_gly"></span><span id="_SECURITY_CRYPTOANALYSIS_GLY"></span>**cryptanalysis**
</dt> <dd>

Cryptanalysis is the art and science of breaking ciphertext. In contrast, the art and science of keeping messages secure is cryptography.

</dd> <dt>

<span id="_security_cryptoapi_gly"></span><span id="_SECURITY_CRYPTOAPI_GLY"></span>**CryptoAPI**
</dt> <dd>

Application programming interface that enables application developers to add authentication, encoding, and encryption to Windows-based applications.

</dd> <dt>

<span id="_security_cryptographic_algorithm_gly"></span><span id="_SECURITY_CRYPTOGRAPHIC_ALGORITHM_GLY"></span>**cryptographic algorithm**
</dt> <dd>

A mathematical function used for encryption and decryption. Most cryptographic algorithms are based on a substitution cipher, a transposition cipher, or a combination of both.

</dd> <dt>

<span id="_security_cryptographic_digest_gly"></span><span id="_SECURITY_CRYPTOGRAPHIC_DIGEST_GLY"></span>**Cryptographic Digest**
</dt> <dd>

A one-way hash function that takes a variable-length input string and converts it to a fixed-length output string (called a cryptographic digest.) This fixed-length output string is probabilistically unique for every different input string and thus can act as a fingerprint of a file. When a file with a cryptographic digest is downloaded, the receiver recomputes the digest. If the output string matches the digest contained in the file, the receiver has proof that the received file was not tampered with and is identical to the file originally sent.

</dd> <dt>

<span id="_security_cryptographic_key_gly"></span><span id="_SECURITY_CRYPTOGRAPHIC_KEY_GLY"></span>**cryptographic key**
</dt> <dd>

A cryptographic key is a piece of data that is required to initialize a cryptographic algorithm. Cryptographic systems are generally designed so that their security depends only on the security of their cryptographic keys and not, for example, on keeping their algorithms secret.

There are many different types of cryptographic keys, corresponding to the wide variety of cryptographic algorithms. Keys can be classified according to the type of algorithm they are used with (for example, as symmetric or asymmetric keys). They can also be classified based on their lifetime within a system (for example, as long-lived or session keys).

</dd> <dt>

<span id="_security_cryptographic_service_provider_gly"></span><span id="_SECURITY_CRYPTOGRAPHIC_SERVICE_PROVIDER_GLY"></span>**cryptographic service provider**
</dt> <dd>

(CSP) An independent software module that actually performs cryptography algorithms for authentication, encoding, and encryption.

</dd> <dt>

<span id="_security_cryptography_gly"></span><span id="_SECURITY_CRYPTOGRAPHY_GLY"></span>**cryptography**
</dt> <dd>

The art and science of information security. It includes information confidentiality, data integrity, entity authentication, and data origin authentication.

</dd> <dt>

<span id="_security_cryptography_api_gly"></span><span id="_SECURITY_CRYPTOGRAPHY_API_GLY"></span>**Cryptography API**
</dt> <dd>

See *CryptoAPI*.

</dd> <dt>

<span id="_security_cryptography_api__next_generation_gly"></span><span id="_SECURITY_CRYPTOGRAPHY_API__NEXT_GENERATION_GLY"></span>**Cryptography API: Next Generation**
</dt> <dd>

(CNG) The second generation of the *CryptoAPI*. CNG allows you to replace existing algorithm providers with your own providers and add new algorithms as they become available. CNG also allows the same APIs to be used from user and kernel mode applications.

</dd> <dt>

<span id="_security_cryptology_gly"></span><span id="_SECURITY_CRYPTOLOGY_GLY"></span>**cryptology**
</dt> <dd>

The branch of mathematics that encompasses both cryptography and cryptanalysis.

</dd> <dt>

<span id="_security_cryptospi_gly"></span><span id="_SECURITY_CRYPTOSPI_GLY"></span>**CryptoSPI**
</dt> <dd>

The system program interface used with a *cryptographic service provider* (CSP).

</dd> <dt>

<span id="_security_csp_gly"></span><span id="_SECURITY_CSP_GLY"></span>**CSP**
</dt> <dd>

See *cryptographic service provider*.

</dd> <dt>

<span id="_security_csp_family_gly"></span><span id="_SECURITY_CSP_FAMILY_GLY"></span>**CSP family**
</dt> <dd>

A unique group of CSPs that use the same set of data formats and perform their function in the same way. Even when two CSP families use the same algorithm (for example, the RC2 block cipher), their different padding schemes, keys lengths, or default modes make each group distinct. CryptoAPI has been designed so that each CSP type represents a particular family.

</dd> <dt>

<span id="_security_csp_name_gly"></span><span id="_SECURITY_CSP_NAME_GLY"></span>**CSP name**
</dt> <dd>

The textual name of the CSP. If the CSP has been signed by Microsoft, this name must exactly match the CSP name that was specified in the Export Compliance Certificate (ECC).

</dd> <dt>

<span id="_security_csp_type_gly"></span><span id="_SECURITY_CSP_TYPE_GLY"></span>**CSP type**
</dt> <dd>

Indicates the CSP family associated with a provider. When an application connects to a CSP of a particular type, each of the CryptoAPI functions will, by default, operate in a way prescribed by the family that corresponds to that CSP type.

</dd> <dt>

<span id="_security_ctl_gly"></span><span id="_SECURITY_CTL_GLY"></span>**CTL**
</dt> <dd>

See *certificate trust list*.

</dd> <dt>

<span id="_security_cylink_mek_gly"></span><span id="_SECURITY_CYLINK_MEK_GLY"></span>**CYLINK\_MEK**
</dt> <dd>

An encryption algorithm that uses a 40-bit variant of a DES key where 16 bits of the 56-bit DES key are set to zero. This algorithm is implemented as specified in the IETF Draft specification for 40-bit DES. The draft specification, at the time of this writing can be found at ftp://ftp.ietf.org/internet-drafts/draft-hoffman-des40-02.txt. This algorithm is used with the **ALG\_ID** value CALG\_CYLINK\_MEK.

</dd> </dl>

 

 
