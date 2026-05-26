---
description: Used to identify standard encryption algorithms in various CNG functions and structures, such as the CRYPT\_INTERFACE\_REG structure.
ms.assetid: a05ae7e6-d882-4287-9990-23e4cd340b05
title: CNG Algorithm Identifiers (Bcrypt.h)
ms.topic: reference
ms.date: 05/27/2025
---

# CNG Algorithm Identifiers

The following identifiers are used to identify standard encryption algorithms in various CNG functions and structures, such as the [CRYPT\_INTERFACE\_REG](/windows/win32/api/Bcrypt/ns-bcrypt-crypt_interface_reg) structure. Third party providers may have additional algorithms that they support.

| Constant/value | Description | 
|----------------|-------------|
| **BCRYPT_3DES_ALGORITHM**<br/>L"3DES" | The triple data encryption standard symmetric encryption algorithm.<br/> Standard: SP800-67, SP800-38A | 
| **BCRYPT_3DES_112_ALGORITHM**<br/>L"3DES_112" | The 112-bit triple data encryption standard symmetric encryption algorithm.<br/> Standard: SP800-67, SP800-38A | 
| **BCRYPT_AES_ALGORITHM**<br/>L"AES" | The advanced encryption standard (AES) symmetric encryption algorithm.<br/> Standard: FIPS 197 | 
| **BCRYPT_AES_CMAC_ALGORITHM**<br/>L"AES-CMAC" | The advanced encryption standard (AES) cipher based message authentication code (CMAC) symmetric encryption algorithm.<br/> Standard: SP 800-38B<br/>**Note:** This algorithm is supported beginning with Windows 8. | 
| **BCRYPT_AES_GMAC_ALGORITHM**<br/>L"AES-GMAC" | The advanced encryption standard (AES) Galois message authentication code (GMAC) symmetric encryption algorithm.<br/>Standard: SP800-38D<br/>**Note:** This algorithm is supported beginning with Windows Vista with SP1. | 
| **BCRYPT_CAPI_KDF_ALGORITHM**<br/>L"CAPI_KDF" | Crypto API (CAPI) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_CHACHA20_POLY1305_ALGORITHM**<br/>L"CHACHA20_POLY1305" | The ChaCha20-Poly1305 AEAD algorithm.<br/> Standard: RFC 8439<br/>**Note:** Support for this algorithm begins with Windows 10. |
| **BCRYPT_CSHAKE128_ALGORITHM**<br/>L"CSHAKE128" | The SHA3 derived customizable XOF with 128-bit strength.<br/>Standard: SP800-185.<br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2. |
| **BCRYPT_CSHAKE256_ALGORITHM**<br/>L"CSHAKE256" | The SHA3 derived customizable XOF with 256-bit strength.<br/>Standard: SP800-185.<br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2. |
| **BCRYPT_DES_ALGORITHM**<br/>L"DES" | The data encryption standard symmetric encryption algorithm.<br/> Standard: FIPS 46-3, FIPS 81 | 
| **BCRYPT_DESX_ALGORITHM**<br/>L"DESX" | The extended data encryption standard symmetric encryption algorithm.<br/> Standard: None | 
| **BCRYPT_DH_ALGORITHM**<br/>L"DH" | The Diffie-Hellman key exchange algorithm.<br/> Standard: PKCS #3 | 
| **BCRYPT_DSA_ALGORITHM**<br/>L"DSA" | The digital signature algorithm.<br/> Standard: FIPS 186-2<br/>**Note:** Beginning with Windows 8, this algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3. | 
| **BCRYPT_ECDH_ALGORITHM**<br/>L"ECDH" | Generic prime elliptic curve Diffie-Hellman key exchange algorithm (see the [Remarks](#remarks) section for more information).<br/>Standard: SP800-56A. | 
| **BCRYPT_ECDSA_ALGORITHM**<br/>L"ECDSA" | Generic prime elliptic curve digital signature algorithm (see the [Remarks](#remarks) section for more information).<br/>Standard: ANSI X9.62. | 
| **BCRYPT_ECDH_P256_ALGORITHM**<br/>L"ECDH_P256" | The 256-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br/> Standard: SP800-56A | 
| **BCRYPT_ECDH_P384_ALGORITHM**<br/>L"ECDH_P384" | The 384-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br/> Standard: SP800-56A | 
| **BCRYPT_ECDH_P521_ALGORITHM**<br/>L"ECDH_P521" | The 521-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br/> Standard: SP800-56A | 
| **BCRYPT_ECDSA_P256_ALGORITHM**<br/>L"ECDSA_P256" | The 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br/> Standard: FIPS 186-2, X9.62 | 
| **BCRYPT_ECDSA_P384_ALGORITHM**<br/>L"ECDSA_P384" | The 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br/> Standard: FIPS 186-2, X9.62 | 
| **BCRYPT_ECDSA_P521_ALGORITHM**<br/>L"ECDSA_P521" | The 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br/> Standard: FIPS 186-2, X9.62 |
| **BCRYPT_HKDF_ALGORITHM**<br/>L"HKDF" | The HMAC-based Extract-and-Expand key derivation function.<br/> Standard: RFC 5869<br/>**Note:** Support for this algorithm begins with Windows 10. |
| **BCRYPT_KMAC128_ALGORITHM**<br/>L"KMAC128" | The SHA3 derived Keccak message authentication code (KMAC) built on CSHAKE128.<br/>Standard: SP800-185.<br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2. |
| **BCRYPT_KMAC256_ALGORITHM**<br/>L"KMAC256" | The SHA3 derived Keccak message authentication code (KMAC) built on CSHAKE256.<br/>Standard: SP800-185.<br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2. |
| **BCRYPT_LMS_ALGORITHM**<br/>L"LMS" | The Leighton-Micali Hash-Based Signature algorithm. Standard: RFC 8554.<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_MD2_ALGORITHM**<br/>L"MD2" | The MD2 hash algorithm.<br/>Standard: RFC 1319 | 
| **BCRYPT_MD4_ALGORITHM**<br/>L"MD4" | The MD4 hash algorithm.<br/>Standard: RFC 1320 | 
| **BCRYPT_MD5_ALGORITHM**<br/>L"MD5" | The MD5 hash algorithm.<br/>Standard: RFC 1321 |
| **BCRYPT_MLDSA_ALGORITHM**<br/>L"ML-DSA" | The Module-Lattice-Based Digital Signature Algorithm (ML-DSA).<br/>Standard: FIPS 204.<br/><br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2.. |
| **BCRYPT_COMPOSITE_MLDSA_ALGORITHM**<br/>L"Composite-ML-DSA" | Composite algorithm combining Module-Lattice-Based Digital Signature Algorithm (ML-DSA) with a traditional signature algorithm.<br/>Standard: [IETF draft](https://datatracker.ietf.org/doc/html/draft-ietf-lamps-pq-composite-sigs).<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_MLKEM_ALGORITHM**<br/>L"ML-KEM" | The Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) algorithm.<br/>Standard: [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).<br/><br/>**Note:** Support for this algorithm begins with Windows 11, version 24H2. |
| **BCRYPT_COMPOSITE_MLKEM_ALGORITHM**<br/>L"Composite-ML-KEM" | Composite algorithm combining the Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) and a traditional key exchange algorithm.<br/>Standard: [IETF draft](https://datatracker.ietf.org/doc/html/draft-ietf-lamps-pq-composite-sigs).<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_RC2_ALGORITHM**<br/>L"RC2" | The RC2 symmetric encryption algorithm.<br/>Standard: RFC 2268 | 
| **BCRYPT_RC4_ALGORITHM**<br/>L"RC4" | The RC4 symmetric encryption algorithm.<br/>Standard: Various | 
| **BCRYPT_RNG_ALGORITHM**<br/>L"RNG" | The random-number generator algorithm.<br/>Standard: FIPS 186-2, FIPS 140-2, NIST SP 800-90<br/>**Note:** Beginning with Windows Vista with SP1 and Windows Server 2008, the random number generator is based on the AES counter mode specified in the NIST SP 800-90 standard.<br/>**Windows Vista:** The random number generator is based on the hash-based random number generator specified in the FIPS 186-2 standard.<br/>**Note:** Beginning with Windows 8, the RNG algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3. | 
| **BCRYPT_RNG_DUAL_EC_ALGORITHM**<br/>L"DUALECRNG" | The dual elliptic curve random-number generator algorithm.<br/>Standard: SP800-90.<br/>**Windows 8:** Beginning with Windows 8, the EC RNG algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3.<br/>**Windows 10:** Beginning with Windows 10, the dual elliptic curve random number generator algorithm has been removed. Existing uses of this algorithm will continue to work; however, the random number generator is based on the AES counter mode specified in the NIST SP 800-90 standard. New code should use **BCRYPT_RNG_ALGORITHM**, and it is recommended that existing code be changed to use **BCRYPT_RNG_ALGORITHM**. | 
| **BCRYPT_RNG_FIPS186_DSA_ALGORITHM**<br/>L"FIPS186DSARNG" | The random-number generator algorithm suitable for DSA (Digital Signature Algorithm).<br/> Standard: FIPS 186-2.<br/>**Windows 8:** Support for FIPS 186-3 begins. | 
| **BCRYPT_RSA_ALGORITHM**<br/>L"RSA" | The RSA public key algorithm.<br/>Standard: PKCS #1 v1.5 and v2.0. | 
| **BCRYPT_RSA_SIGN_ALGORITHM**<br/>L"RSA_SIGN" | The RSA signature algorithm. This algorithm is not currently supported. You can use the **BCRYPT_RSA_ALGORITHM** algorithm to perform RSA signing operations.<br/>Standard: PKCS #1 v1.5 and v2.0. | 
| **BCRYPT_SHA1_ALGORITHM**<br/>L"SHA1" | The 160-bit secure hash algorithm.<br/>Standard: FIPS 180-2, FIPS 198. | 
| **BCRYPT_SHA256_ALGORITHM**<br/>L"SHA256" | The 256-bit secure hash algorithm.<br/>Standard: FIPS 180-2, FIPS 198. | 
| **BCRYPT_SHA384_ALGORITHM**<br/>L"SHA384" | The 384-bit secure hash algorithm.<br/>Standard: FIPS 180-2, FIPS 198. | 
| **BCRYPT_SHA512_ALGORITHM**<br/>L"SHA512" | The 512-bit secure hash algorithm.<br/>Standard: FIPS 180-2, FIPS 198. |
| **BCRYPT_SHA3_256_ALGORITHM**<br/>L"SHA3-256" | The SHA3 256-bit secure hash algorithm.<br/>Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_SHA3_384_ALGORITHM**<br/>L"SHA3-384" | The SHA3 384-bit secure hash algorithm.<br/>Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_SHA3_512_ALGORITHM**<br/>L"SHA3-512" | The SHA3 512-bit secure hash algorithm.<br/>Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_SHAKE128_ALGORITHM**<br/>L"SHAKE128" | The SHA3 XOF with 128-bit strength.<br/>Standard: FIPS 202.<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_SHAKE256_ALGORITHM**<br/>L"SHAKE256" | The SHA3 XOF with 256-bit strength.<br/>Standard: FIPS 202.<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_SLHDSA_ALGORITHM**<br/>L"SLH-DSA" | The Stateless Hash-based digital signature algorithm (SLH-DSA).<br/>Standard: FIPS 205.<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_SP800108_CTR_HMAC_ALGORITHM**<br/>L"SP800_108_CTR_HMAC" | Counter mode, hash-based message authentication code (HMAC) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. | 
| **BCRYPT_SP80056A_CONCAT_ALGORITHM**<br/>L"SP800_56A_CONCAT" | SP800-56A key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. | 
| **BCRYPT_PBKDF2_ALGORITHM**<br/>L"PBKDF2" | Password-based key derivation function 2 (PBKDF2) algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. | 
| **BCRYPT_XMSS_ALGORITHM**<br/>L"XMSS" | The eXtended Merkle Signature Scheme (XMSS) stateful hash-based signature algorithm. XMSS Standard: RFC 8391.<br/><br/>**Note:** This identifier is part of a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The identifier is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). |
| **BCRYPT_XTS_AES_ALGORITHM**<br/>L"XTS-AES" | The advanced encryption standard (AES) symmetric encryption algorithm in XTS mode.<br/>Standard: SP-800-38E, IEEE Std 1619-2007.<br/>**Windows 10:** Support for this algorithm begins. | 

## Remarks

To use **BCRYPT\_ECDSA\_ALGORITHM** or **BCRYPT\_ECDH\_ALGORITHM**, call [BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) with either **BCRYPT\_ECDSA\_ALGORITHM** or **BCRYPT\_ECDH\_ALGORITHM** as the *pszAlgId*. Then use [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty) to set the **BCRYPT\_ECC\_CURVE\_NAME** property to a named algorithm listed in CNG Named Curves.

To provide user-defined elliptic curve parameters directly, use [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty) to set the **BCRYPT\_ECC\_PARAMETERS** property. Download the [Windows 10 Cryptographic Provider Developer Kit (CPDK)](https://www.microsoft.com/download/details.aspx?id=30688) for more information.

## Requirements

| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Bcrypt.h</dt> </dl> |

## Related content

[BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)

[NCryptCreatePersistedKey](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey)

[CNG Property Identifiers](cng-property-identifiers.md)

[BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty)
