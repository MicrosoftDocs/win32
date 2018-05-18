---
title: CERT\_CAPABILITY
description: The following constants indicate the capabilities, algorithms, and cryptography supported by the certificate silo.
ms.assetid: '304d0632-630a-4eea-903b-e0636c5cb12e'
topic_type:
- apiref
api_name:
- CERT_CAPABILITY_HASH_ALG
- CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY
- CERT_CAPABILITY_SIGNATURE_ALG
- CERT_CAPABILITY_CERTIFICATE_SUPPORT
- CERT_CAPABILITY_OPTIONAL_FEATURES
- CERT_MAX_CAPABILITY
- CERT_RSA_1024_OID
- CERT_RSA_2048_OID
- CERT_RSA_3072_OID
- CERT_RSASSA_PSS_SHA1_OID
- CERT_RSASSA_PSS_SHA256_OID
- CERT_RSASSA_PSS_SHA384_OID
- CERT_RSASSA_PSS_SHA512_OID
api_location:
- EhStorExtensions.h
api_type:
- HeaderDef
---

# CERT\_CAPABILITY

The following constants indicate the capabilities, algorithms, and cryptography supported by the certificate silo.

<dl> <dt>

<span id="CERT_CAPABILITY_HASH_ALG"></span><span id="cert_capability_hash_alg"></span>**CERT\_CAPABILITY\_HASH\_ALG**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



Hashing algorithms supported (e.g. SHA-1, SHA-256, etc).


</dt> </dl> </dd> <dt>

<span id="CERT_CAPABILITY_ASYMMETRIC_KEY_CRYPTOGRAPHY"></span><span id="cert_capability_asymmetric_key_cryptography"></span>**CERT\_CAPABILITY\_ASYMMETRIC\_KEY\_CRYPTOGRAPHY**
</dt> <dd> <dl> <dt>

0x2
</dt> <dt>



Asymmetric key cryptography supported (e.g. RSA 1024 bit key).


</dt> </dl> </dd> <dt>

<span id="CERT_CAPABILITY_SIGNATURE_ALG"></span><span id="cert_capability_signature_alg"></span>**CERT\_CAPABILITY\_SIGNATURE\_ALG**
</dt> <dd> <dl> <dt>

0x3
</dt> <dt>



Signature algorithms supported (e.g. RSASSA PSS-SHA1 RSASSA PKCS v1.5 SHA-1).


</dt> </dl> </dd> <dt>

<span id="CERT_CAPABILITY_CERTIFICATE_SUPPORT"></span><span id="cert_capability_certificate_support"></span>**CERT\_CAPABILITY\_CERTIFICATE\_SUPPORT**
</dt> <dd> <dl> <dt>

0x4
</dt> <dt>



Certificate support provided in the certificate silo. Currently, only certificate extension field parsing is supported.


</dt> </dl> </dd> <dt>

<span id="CERT_CAPABILITY_OPTIONAL_FEATURES"></span><span id="cert_capability_optional_features"></span>**CERT\_CAPABILITY\_OPTIONAL\_FEATURES**
</dt> <dd> <dl> <dt>

0x5
</dt> <dt>



Optional features supported by the certificate silo.


</dt> </dl> </dd> <dt>

<span id="CERT_MAX_CAPABILITY"></span><span id="cert_max_capability"></span>**CERT\_MAX\_CAPABILITY**
</dt> <dd> <dl> <dt>

0xFF
</dt> <dt>



This is used to indicate the first reserved value.


</dt> </dl> </dd> <dt>

<span id="CERT_RSA_1024_OID"></span><span id="cert_rsa_1024_oid"></span>**CERT\_RSA\_1024\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.1,1024"
</dt> <dt>



Identifier used to communicate support for RSA 1024 bit keys.


</dt> </dl> </dd> <dt>

<span id="CERT_RSA_2048_OID"></span><span id="cert_rsa_2048_oid"></span>**CERT\_RSA\_2048\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.1,2048"
</dt> <dt>



Identifier used to communicate support for RSA 2048 bit keys.


</dt> </dl> </dd> <dt>

<span id="CERT_RSA_3072_OID"></span><span id="cert_rsa_3072_oid"></span>**CERT\_RSA\_3072\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.1,3072"
</dt> <dt>



Identifier used to communicate support for RSA 3072 bit keys.


</dt> </dl> </dd> <dt>

<span id="CERT_RSASSA_PSS_SHA1_OID"></span><span id="cert_rsassa_pss_sha1_oid"></span>**CERT\_RSASSA\_PSS\_SHA1\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.10,1.3.14.3.2.26"
</dt> <dt>



Identifier used to communicate support for RSASSA PSS-SHA-1 signature algorithm.


</dt> </dl> </dd> <dt>

<span id="CERT_RSASSA_PSS_SHA256_OID"></span><span id="cert_rsassa_pss_sha256_oid"></span>**CERT\_RSASSA\_PSS\_SHA256\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.1"
</dt> <dt>



Identifier used to communicate support for RSASSA PSS-SHA-256 signature algorithm.


</dt> </dl> </dd> <dt>

<span id="CERT_RSASSA_PSS_SHA384_OID"></span><span id="cert_rsassa_pss_sha384_oid"></span>**CERT\_RSASSA\_PSS\_SHA384\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.2"
</dt> <dt>



Identifier used to communicate support for RSASSA PSS-SHA-384 signature algorithm.


</dt> </dl> </dd> <dt>

<span id="CERT_RSASSA_PSS_SHA512_OID"></span><span id="cert_rsassa_pss_sha512_oid"></span>**CERT\_RSASSA\_PSS\_SHA512\_OID**
</dt> <dd> <dl> <dt>

"1.2.840.113549.1.1.10,2.16.840.1.101.3.4.2.3"
</dt> <dt>



Identifier used to communicate support for RSASSA PSS-SHA-512 signature algorithm.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2 \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>EhStorExtensions.h</dt> </dl> |



 

 





