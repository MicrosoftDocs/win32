---
description: CNG provides pre-defined algorithm handles for many algorithms. You can use these handles in any situation that requires an algorithm handle.
ms.assetid: AF58F393-895C-4241-B423-BBADA9B1AE41
title: CNG Algorithm Pseudo-handles
ms.topic: reference
ms.date: 05/27/2025
---

# CNG Algorithm Pseudo-handles

Beginning in Windows 10, CNG provides pre-defined algorithm handles for many algorithms. You can use these handles in any situation that requires an algorithm handle.

## Hash and Message Authentication Code (MAC) Algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_MD2_ALG_HANDLE** | A handle for the MD2 hash algorithm. Standard: RFC 1319. |
| **BCRYPT_MD4_ALG_HANDLE** | A handle for the MD4 hash algorithm. Standard: RFC 1320. |
| **BCRYPT_MD5_ALG_HANDLE** | A handle for the MD5 hash algorithm. Standard: RFC 1321. |
| **BCRYPT_SHA1_ALG_HANDLE** | A handle for the 160-bit secure hash algorithm. Standard: FIPS 180-2, FIPS 198. |
| **BCRYPT_SHA256_ALG_HANDLE** | A handle for the 256-bit secure hash algorithm. Standard: FIPS 180-2, FIPS 198. |
| **BCRYPT_SHA384_ALG_HANDLE** | A handle for the 384-bit secure hash algorithm. Standard: FIPS 180-2, FIPS 198. |
| **BCRYPT_SHA512_ALG_HANDLE** | A handle for the 512-bit secure hash algorithm. Standard: FIPS 180-2, FIPS 198. |
| **BCRYPT_SHA3_256_ALG_HANDLE** | A handle for the SHA3 256-bit secure hash algorithm. Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_SHA3_384_ALG_HANDLE** | A handle for the SHA3 384-bit secure hash algorithm. Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_SHA3_512_ALG_HANDLE** | A handle for the SHA3 512-bit secure hash algorithm. Standard: FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_HMAC_MD2_ALG_HANDLE** | A handle for the hash-based message authentication code using the MD2 hash algorithm. Standard: RFC 2104, RFC 1319. |
| **BCRYPT_HMAC_MD4_ALG_HANDLE** | A handle for the hash-based message authentication code using the MD4 hash algorithm. Standard: RFC 2104, RFC 1320. |
| **BCRYPT_HMAC_MD5_ALG_HANDLE** | A handle for the hash-based message authentication code using the MD4 hash algorithm. Standard: RFC 2104, RFC 1321. |
| **BCRYPT_HMAC_SHA1_ALG_HANDLE** | A handle for the hash-based message authentication code using the 160-bit secure hash algorithm. Standard: RFC 2014, FIPS 180-2, FIPS 198. |
| **BCRYPT_HMAC_SHA256_ALG_HANDLE** | A handle for the hash-based message authentication code using the 256-bit secure hash algorithm. Standard: RFC 2014, FIPS 180-2, FIPS 198. |
| **BCRYPT_HMAC_SHA384_ALG_HANDLE** | A handle for the hash-based message authentication code using the 384-bit secure hash algorithm. Standard: RFC 2014, FIPS 180-2, FIPS 198. |
| **BCRYPT_HMAC_SHA512_ALG_HANDLE** | A handle for the hash-based message authentication code using the 512-bit secure hash algorithm. Standard: RFC 2014, FIPS 180-2, FIPS 198. |
| **BCRYPT_HMAC_SHA3_256_ALG_HANDLE** | A handle for the hash-based message authentication code using the SHA3 256-bit secure hash algorithm. Standard: RFC 2014, FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_HMAC_SHA3_384_ALG_HANDLE** | A handle for the hash-based message authentication code using the SHA3 384-bit secure hash algorithm. Standard: RFC 2014, FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_HMAC_SHA3_512_ALG_HANDLE** | A handle for the hash-based message authentication code using the SHA3 512-bit secure hash algorithm. Standard: RFC 2014, FIPS 202.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_KMAC128_ALG_HANDLE** | A handle for the SHA3 derived Keccak message authentication code (KMAC) built on CSHAKE128. Standard: SP800-185.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |
| **BCRYPT_KMAC256_ALG_HANDLE** | A handle for the SHA3 derived Keccak message authentication code (KMAC) built on CSHAKE256. Standard: SP800-185.<br/>**Windows 11, version 24H2:** Support for this algorithm begins. |

## PQ Digital Signature Algorithms

> [!NOTE]
> The PQDSA handles in this section relate to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this section is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

| Constant | Description |
|----------|-------------|
| **BCRYPT_LMS_ALG_HANDLE** | A handle to the Leighton-Micali Hash-Based Signature (LMS) algorithm. Standard: RFC 8554. |
| **BCRYPT_MLDSA_ALG_HANDLE** | A handle to the Module-Lattice-Based Digital Signature Algorithm (ML-DSA). Standard: FIPS 204. |
| **BCRYPT_SLHDSA_ALG_HANDLE** | A handle to the Stateless Hash-based Digital Signature Algorithm (SLH-DSA). Standard: FIPS 205. |
| **BCRYPT_XMSS_ALG_HANDLE** | A handle to the eXtended Merkle Signature Scheme (XMSS) stateful hash-based algorithm. Standard: RFC 8391. |

## Stream Cipher Algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_RC4_ALG_HANDLE** | A handle for the RC4 stream cipher algorithm. Standard: Various. |

## Random Number Generator Algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_RNG_ALG_HANDLE** | A handle to the random-number generator algorithm.**Note**  Beginning with Windows Vista with SP1 and Windows Server 2008, the random number generator is based on the AES counter mode specified in the NIST SP 800-90 standard.<br/> **Windows Vista:** The random number generator is based on the hash-based random number generator specified in the FIPS 186-2 standard.<br/> **Windows 8:** The RNG algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3. |
| **BCRYPT_RNG_FIPS186_DSA_ALG_HANDLE** | A handle to the random-number generator algorithm suitable for DSA (Digital Signature Algorithm). Standard: FIPS 186-2. |

## Key Derivation Function (KDF) Algorithms

| Constant | Description |
|--------|--------|
| **BCRYPT_CAPI_KDF_ALG_HANDLE** | A handle to the Crypto API (CAPI) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_HKDF_ALG_HANDLE** | A handle to the HMAC-based Extract-and-Expand key derivation function. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions.<br/> **Windows 10:** Support for this algorithm begins. |
| **BCRYPT_PBKDF2_ALG_HANDLE** | A handle to the Password-based key derivation function 2 (PBKDF2) algorithm. Used by the [**BCryptKeyDerivation**](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_SP800108_CTR_HMAC_ALG_HANDLE** | A handle to the Counter mode, hash-based message authentication code (HMAC) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_SP80056A_CONCAT_ALG_HANDLE** | A handle to the SP800-56A key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |

## Key Encapsulation Mechanism (KEM) Algorithms

> [!NOTE]
> The ML-KEM handles in this section relate to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this section is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

| Constant | Description |
|----------|-------------|
| **BCRYPT_MLKEM_ALG_HANDLE** | A handle to the Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) algorithm. Standard: [FIPS 203](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf). |

## Asymmetric Algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_DH_ALG_HANDLE** | A handle to the Diffie-Hellman key exchange algorithm. Standard: PKCS \#3. |
| **BCRYPT_DSA_ALG_HANDLE** | A handle to the Digital Signature Algorithm (DSA) digital signature algorithm. Standard: FIPS 186-2.<br/>**Note:** Beginning with Windows 8, this algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3. |
| **BCRYPT_ECDH_ALG_HANDLE** | A handle to the generic prime elliptic curve Diffie-Hellman key exchange algorithm. Standard: SP800-56A. | 
| **BCRYPT_ECDSA_ALG_HANDLE** | A handle to the generic prime elliptic curve digital signature algorithm. Standard: ANSI X9.62. | 
| **BCRYPT_ECDH_P256_ALG_HANDLE** | A handle to the 256-bit prime elliptic curve Diffie-Hellman key exchange algorithm. Standard: SP800-56A. |
| **BCRYPT_ECDH_P384_ALG_HANDLE** | A handle to the 384-bit prime elliptic curve Diffie-Hellman key exchange algorithm. Standard: SP800-56A. |
| **BCRYPT_ECDH_P521_ALG_HANDLE** | A handle to the 521-bit prime elliptic curve Diffie-Hellman key exchange algorithm. Standard: SP800-56A. |
| **BCRYPT_ECDSA_P256_ALG_HANDLE** | A handle to the 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2). Standard: FIPS 186-2, X9.62. |
| **BCRYPT_ECDSA_P384_ALG_HANDLE** | A handle to the 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2). Standard: FIPS 186-2, X9.62. |
| **BCRYPT_ECDSA_P521_ALG_HANDLE** | A handle to the 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2). Standard: FIPS 186-2, X9.62. |
| **BCRYPT_RSA_ALG_HANDLE** | A handle to the RSA public key algorithm. Standard: PKCS \#1 v1.5 and v2.0. |
| **BCRYPT_RSA_SIGN_ALG_HANDLE** | A handle to the RSA signature algorithm. This algorithm is not currently supported. You can use the **BCRYPT_RSA_ALG_HANDLE** algorithm to perform RSA signing operations. Standard: PKCS \#1 v1.5 and v2.0. |

## Block Cipher and Cipher-based Message Authentication Code Algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_3DES_CBC_ALG_HANDLE** | A handle for the triple Data Encryption Standard algorithm using Cipher Block Chaining mode (CBC). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_ECB_ALG_HANDLE** | A handle for the triple Data Encryption Standard algorithm using Electronic Cookbook mode (ECB). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_CFB_ALG_HANDLE** | A handle for the triple Data Encryption Standard algorithm using Cipher Feedback mode (CFB). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_112_CBC_ALG_HANDLE** | A handle for the 112-bit triple Data Encryption Standard algorithm using Cipher Block Chaining mode (CBC). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_112_CBC_ALG_HANDLE** | A handle for the 112-bit triple Data Encryption Standard algorithm using Cipher Block Chaining mode (CBC). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_112_ECB_ALG_HANDLE** | A handle for the 112-bit triple Data Encryption Standard algorithm using Electronic Cookbook mode (ECB). Standard: SP800-67, SP800-38A. |
| **BCRYPT_3DES_112_CFB_ALG_HANDLE** | A handle for the 112-bit triple Data Encryption Standard algorithm using Cipher Feedback mode (CFB). Standard: SP800-67, SP800-38A. |
| **BCRYPT_AES_CMAC_ALG_HANDLE** | A handle for the Advanced Encryption standard (AES) cipher-based message authentication code (CMAC) algorithm. Standard: SP800-38B. |
| **BCRYPT_AES_CBC_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) algorithm using Cipher Block Chaining Mode (CBC). Standard: FIPS 197. |
| **BCRYPT_AES_ECB_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) algorithm using Electronic Cookbook Mode (ECB). Standard: FIPS 197. |
| **BCRYPT_AES_CFB_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) algorithm using Cipher Feedback Mode (CFB). Standard: FIPS 197. |
| **BCRYPT_AES_CCM_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) algorithm using Counter with CBC-MAC Mode (CCM). Standard: FIPS 197. |
| **BCRYPT_AES_GCM_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) algorithm using Galois Counter Mode (GCM). Standard: FIPS 197. |
| **BCRYPT_DES_CBC_ALG_HANDLE** | A handle for the Data Encryption Standard (DES) algorithm using Cipher Block Chaining Mode (GCM). Standard: FIPS 46-3, FIPS 81. |
| **BCRYPT_DES_ECB_ALG_HANDLE** | A handle for the Data Encryption Standard (DES) algorithm using Electronic Cookbook Mode (ECB). Standard: FIPS 46-3, FIPS 81. |
| **BCRYPT_DES_CFB_ALG_HANDLE** | A handle for the Data Encryption Standard (DES) algorithm using Cipher Feedback Mode (CFB). Standard: FIPS 46-3, FIPS 81. |
| **BCRYPT_AES_CMAC_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) cipher based message authentication code (CMAC) symmetric encryption algorithm. Standard: SP 800-38B. |
| **BCRYPT_AES_GMAC_ALG_HANDLE** | A handle for the Advanced Encryption Standard (AES) Galois message authentication code (GMAC) symmetric encryption algorithm. Standard: SP800-38D. |
| **BCRYPT_RC4_ALG_HANDLE** | A handle to the RC4 symmetric encryption algorithm. Standard: Various. |

## Remarks

Beginning in Windows 10, CNG provides pre-defined algorithm handles for many algorithms. You can use these handles in any situation that requires an algorithm handle. However, any call to [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty) fails as the algorithm handle is shared and cannot be modified. In addition, these handles cannot be used at `IRQL=DISPATCH` in kernel mode.

## Related topics

[BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)

[NCryptCreatePersistedKey](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey)
