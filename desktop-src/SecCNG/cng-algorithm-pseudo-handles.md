---
description: Learn how to use CNG pre-defined algorithm handles for cryptographic operations in Windows. Discover available handles for hash, encryption, digital signature, and key derivation algorithms.
ms.assetid: AF58F393-895C-4241-B423-BBADA9B1AE41
title: CNG Algorithm Pseudo-Handles - Windows Security APIs
ms.topic: reference
ms.date: 10/05/2025
---

# CNG algorithm pseudo-handles

Beginning in Windows 10, CNG (Cryptography API: Next Generation) provides pre-defined algorithm handles for cryptographic operations. These algorithm handles simplify development by eliminating the need to manually create handles for common cryptographic algorithms including hash functions, encryption algorithms, digital signatures, and key derivation functions.

## Hash and Message Authentication Code (MAC) algorithms

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_MD2_ALG_HANDLE**<br/>0x00000001 | A handle for the MD2 hash algorithm. | [RFC 1319](https://datatracker.ietf.org/doc/html/rfc1319) |
| **BCRYPT_MD4_ALG_HANDLE**<br/>0x00000011 | A handle for the MD4 hash algorithm. | [RFC 1320](https://datatracker.ietf.org/doc/html/rfc1320) |
| **BCRYPT_MD5_ALG_HANDLE**<br/>0x00000021 | A handle for the MD5 hash algorithm. | [RFC 1321](https://datatracker.ietf.org/doc/html/rfc1321) |
| **BCRYPT_SHA1_ALG_HANDLE**<br/>0x00000031 | A handle for the 160-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| **BCRYPT_SHA256_ALG_HANDLE**<br/>0x00000041 | A handle for the 256-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| **BCRYPT_SHA384_ALG_HANDLE**<br/>0x00000051 | A handle for the 384-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| **BCRYPT_SHA512_ALG_HANDLE**<br/>0x00000061 | A handle for the 512-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) |
| **BCRYPT_HMAC_SHA1_ALG_HANDLE**<br/>0x000000A1 | A handle for the hash-based message authentication code using the 160-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_SHA256_ALG_HANDLE**<br/>0x000000B1 | A handle for the hash-based message authentication code using the 256-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_SHA384_ALG_HANDLE**<br/>0x000000C1 | A handle for the hash-based message authentication code using the 384-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_SHA512_ALG_HANDLE**<br/>0x000000D1 | A handle for the hash-based message authentication code using the 512-bit secure hash algorithm. | [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_MD2_ALG_HANDLE**<br/>0x00000121 | A handle for the hash-based message authentication code using the MD2 hash algorithm. | [RFC 1319](https://datatracker.ietf.org/doc/html/rfc1319), [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.txt) |
| **BCRYPT_HMAC_MD4_ALG_HANDLE**<br/>0x00000131 | A handle for the hash-based message authentication code using the MD4 hash algorithm. | [RFC 1320](https://datatracker.ietf.org/doc/html/rfc1320), [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.txt) |
| **BCRYPT_HMAC_MD5_ALG_HANDLE**<br/>0x00000091 | A handle for the hash-based message authentication code using the MD4 hash algorithm. | [RFC 1321](https://datatracker.ietf.org/doc/html/rfc1321), [RFC 2104](https://datatracker.ietf.org/doc/html/rfc2104.txt) |
| Available in **Windows 11, version 23H2** |
| **BCRYPT_SHA3_256_ALG_HANDLE**<br/>0x000003B1 | A handle for the SHA3 256-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |
| **BCRYPT_SHA3_384_ALG_HANDLE**<br/>0x000003C1 | A handle for the SHA3 384-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |
| **BCRYPT_SHA3_512_ALG_HANDLE**<br/>0x000003D1 | A handle for the SHA3 512-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final) |
| **BCRYPT_HMAC_SHA3_256_ALG_HANDLE**<br/>0x000003E1 | A handle for the hash-based message authentication code using the SHA3 256-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_SHA3_384_ALG_HANDLE**<br/>0x000003F1 | A handle for the hash-based message authentication code using the SHA3 384-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_HMAC_SHA3_512_ALG_HANDLE**<br/>0x00000401 | A handle for the hash-based message authentication code using the SHA3 512-bit secure hash algorithm. | [FIPS 202](https://csrc.nist.gov/pubs/fips/202/final), [FIPS 198-1](https://csrc.nist.gov/pubs/fips/198-1/final) |
| **BCRYPT_CSHAKE128_ALG_HANDLE**<br/>0x00000411 | A handle for the SHA3 derived cSHAKE 128-bit XOF (extendable-output function) hash algorithm. | [SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |
| **BCRYPT_CSHAKE256_ALG_HANDLE**<br/>0x00000421 | A handle for the SHA3 derived cSHAKE 256-bit XOF (extendable-output function) hash algorithm. | [SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |
| **BCRYPT_KMAC128_ALG_HANDLE**<br/>0x00000431 | A handle for the SHA3 derived Keccak message authentication code (KMAC) built on cSHAKE128. | [SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |
| **BCRYPT_KMAC256_ALG_HANDLE**<br/>0x00000441 | A handle for the SHA3 derived Keccak message authentication code (KMAC) built on cSHAKE256. | [SP 800-185](https://csrc.nist.gov/pubs/sp/800/185/final) |

## PQ digital signature algorithms

> [!NOTE]
> The PQDSA handles in this section relate to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this section is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_LMS_ALG_HANDLE** | A handle to the Leighton-Micali Hash-Based Signature (LMS) algorithm. | [RFC 8554](https://datatracker.ietf.org/doc/html/rfc8554) |
| **BCRYPT_MLDSA_ALG_HANDLE** | A handle to the Module-Lattice-Based Digital Signature Algorithm (ML-DSA). | [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) |
| **BCRYPT_SLHDSA_ALG_HANDLE** | A handle to the Stateless Hash-based Digital Signature Algorithm (SLH-DSA). | [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final) |
| **BCRYPT_XMSS_ALG_HANDLE** | A handle to the eXtended Merkle Signature Scheme (XMSS) stateful hash-based algorithm. | [RFC 8391](https://datatracker.ietf.org/doc/html/rfc8391) |

## Stream cipher algorithms

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_RC4_ALG_HANDLE**<br/>0x00000071 | A handle for the RC4 stream cipher algorithm. | Various |

## Random number generator algorithms

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_RNG_ALG_HANDLE**<br/>0x00000081 | A handle to the random-number generator algorithm. | **Windows 8:** The RNG algorithm supports [FIPS 186-3](https://csrc.nist.gov/pubs/fips/186-3/final). Keys less than or equal to 1024 bits adhere to [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final) and keys greater than 1024 to [FIPS 186-3](https://csrc.nist.gov/pubs/fips/186-3/final).<br/> **Windows Vista with SP1 and Windows Server 2008:** The random number generator is based on the AES counter mode specified in the [NIST SP 800-90](https://csrc.nist.gov/pubs/sp/800/90/r1/final) standard.<br/> **Windows Vista:** The random number generator is based on the hash-based random number generator specified in the [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final) standard. |

## Key derivation function (KDF) algorithms

| Constant | Description |
|----------|-------------|
| **BCRYPT_CAPI_KDF_ALG_HANDLE**<br/>0x00000321 | A handle to the Crypto API (CAPI) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_PBKDF2_ALG_HANDLE**<br/>0x00000331 | A handle to the Password-based key derivation function 2 (PBKDF2) algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_SP800108_CTR_HMAC_ALG_HANDLE**<br/>0x00000341 | A handle to the Counter mode, hash-based message authentication code (HMAC) key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_SP80056A_CONCAT_ALG_HANDLE**<br/>0x00000351 | A handle to the SP800-56A key derivation function algorithm. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |
| **BCRYPT_HKDF_ALG_HANDLE**<br/>0x00000391 | A handle to the HMAC-based Extract-and-Expand key derivation function. Used by the [BCryptKeyDerivation](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptkeyderivation) and [NCryptKeyDerivation](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptkeyderivation) functions. |

## Key encapsulation mechanism (KEM) algorithms

> [!NOTE]
> The ML-KEM handles in this section relate to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here. The feature described in this section is available in pre-release versions of the [Windows Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_MLKEM_ALG_HANDLE** | A handle to the Module-Lattice-Based Key Encapsulation Mechanism (ML-KEM) algorithm. | [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) |

## Asymmetric algorithms

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_DH_ALG_HANDLE**<br/>0x00000281 | A handle to the Diffie-Hellman key exchange algorithm. | PKCS \#3 |
| **BCRYPT_DSA_ALG_HANDLE**<br/>0x000002D1 | A handle to the Digital Signature Algorithm (DSA) digital signature algorithm. | [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final) <br/>**Beginning with Windows 8:** This algorithm supports [FIPS 186-3](https://csrc.nist.gov/pubs/fips/186-3/final). Keys less than or equal to 1024 bits adhere to [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final) and keys greater than 1024 to [FIPS 186-3](https://csrc.nist.gov/pubs/fips/186-3/final). |
| **BCRYPT_ECDH_ALG_HANDLE**<br/>0x00000291 | A handle to the generic prime elliptic curve Diffie-Hellman key exchange algorithm. | [SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) |
| **BCRYPT_ECDH_P256_ALG_HANDLE**<br/>0x000002A1 | A handle to the 256-bit prime elliptic curve Diffie-Hellman key exchange algorithm. | [SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) |
| **BCRYPT_ECDH_P384_ALG_HANDLE**<br/>0x000002B1 | A handle to the 384-bit prime elliptic curve Diffie-Hellman key exchange algorithm. | [SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) |
| **BCRYPT_ECDH_P521_ALG_HANDLE**<br/>0x000002C1 | A handle to the 521-bit prime elliptic curve Diffie-Hellman key exchange algorithm. | [SP 800-56A](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final) |
| **BCRYPT_ECDSA_ALG_HANDLE**<br/>0x000000F1 | A handle to the generic prime elliptic curve digital signature algorithm. | ANSI X9.62 | 
| **BCRYPT_ECDSA_P256_ALG_HANDLE**<br/>0x000002E1 | A handle to the 256-bit prime elliptic curve digital signature algorithm. | [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final), X9.62 |
| **BCRYPT_ECDSA_P384_ALG_HANDLE**<br/>0x000002F1 | A handle to the 384-bit prime elliptic curve digital signature algorithm. | [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final), X9.62 |
| **BCRYPT_ECDSA_P521_ALG_HANDLE**<br/>0x00000301 | A handle to the 521-bit prime elliptic curve digital signature algorithm. | [FIPS 186-2](https://csrc.nist.gov/pubs/fips/186-2/final), X9.62 |
| **BCRYPT_RSA_ALG_HANDLE**<br/>0x000000E1 | A handle to the RSA public key algorithm. | PKCS \#1 v1.5 and v2.0 |
| **BCRYPT_RSA_SIGN_ALG_HANDLE**<br/>0x00000311 | A handle to the RSA signature algorithm. This algorithm is not currently supported. You can use the **BCRYPT_RSA_ALG_HANDLE** algorithm to perform RSA signing operations. | PKCS \#1 v1.5 and v2.0. |

## Block cipher and cipher-based message authentication code algorithms

| Constant | Description | Standards |
|----------|-------------|-----------|
| **BCRYPT_AES_CMAC_ALG_HANDLE**<br/>0x00000101 | A handle for the Advanced Encryption Standard (AES) cipher based message authentication code (CMAC) symmetric encryption algorithm. | [SP 800-38B](https://csrc.nist.gov/pubs/sp/800/38/b/final) |
| **BCRYPT_AES_GMAC_ALG_HANDLE**<br/>0x00000111 | A handle for the Advanced Encryption Standard (AES) Galois message authentication code (GMAC) symmetric encryption algorithm. [SP800-38D](https://csrc.nist.gov/pubs/sp/800/38/d/final) |
| **BCRYPT_3DES_CBC_ALG_HANDLE**<br/>0x00000141 | A handle for the triple Data Encryption Standard algorithm using Cipher Block Chaining mode (CBC). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_3DES_ECB_ALG_HANDLE**<br/>0x00000151 | A handle for the triple Data Encryption Standard algorithm using Electronic Codebook mode (ECB). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_3DES_CFB_ALG_HANDLE**<br/>0x00000161 | A handle for the triple Data Encryption Standard algorithm using Cipher Feedback mode (CFB). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_3DES_112_CBC_ALG_HANDLE**<br/>0x00000171 | A handle for the 112-bit triple Data Encryption Standard algorithm using Cipher Block Chaining mode (CBC). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_3DES_112_ECB_ALG_HANDLE**<br/>0x00000181 | A handle for the 112-bit triple Data Encryption Standard algorithm using Electronic Codebook mode (ECB). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_3DES_112_CFB_ALG_HANDLE**<br/>0x00000191 | A handle for the 112-bit triple Data Encryption Standard algorithm using Cipher Feedback mode (CFB). | [SP 800-67](https://csrc.nist.gov/pubs/sp/800/67/r2/final), [SP 800-38A](https://csrc.nist.gov/pubs/sp/800/38/a/final) |
| **BCRYPT_AES_CBC_ALG_HANDLE**<br/>0x000001A1 | A handle for the Advanced Encryption Standard (AES) algorithm using Cipher Block Chaining Mode (CBC). | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |
| **BCRYPT_AES_ECB_ALG_HANDLE**<br/>0x000001B1 | A handle for the Advanced Encryption Standard (AES) algorithm using Electronic Codebook Mode (ECB). | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |
| **BCRYPT_AES_CFB_ALG_HANDLE**<br/>0x000001C1 | A handle for the Advanced Encryption Standard (AES) algorithm using Cipher Feedback Mode (CFB). | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |
| **BCRYPT_AES_CCM_ALG_HANDLE**<br/>0x000001D1 | A handle for the Advanced Encryption Standard (AES) algorithm using Counter with CBC-MAC Mode (CCM). | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |
| **BCRYPT_AES_GCM_ALG_HANDLE**<br/>0x000001E1 | A handle for the Advanced Encryption Standard (AES) algorithm using Galois Counter Mode (GCM). | [FIPS 197](https://csrc.nist.gov/pubs/fips/197/final) |
| **BCRYPT_DES_CBC_ALG_HANDLE**<br/>0x000001F1 | A handle for the Data Encryption Standard (DES) algorithm using Cipher Block Chaining Mode (GCM). | [FIPS 46-3](https://csrc.nist.gov/pubs/fips/46-3/final), [FIPS 81](https://csrc.nist.gov/pubs/fips/81/final) |
| **BCRYPT_DES_ECB_ALG_HANDLE**<br/>0x00000201 | A handle for the Data Encryption Standard (DES) algorithm using Electronic Codebook Mode (ECB). | [FIPS 46-3](https://csrc.nist.gov/pubs/fips/46-3/final), [FIPS 81](https://csrc.nist.gov/pubs/fips/81/final) |
| **BCRYPT_DES_CFB_ALG_HANDLE**<br/>0x00000211 | A handle for the Data Encryption Standard (DES) algorithm using Cipher Feedback Mode (CFB). | [FIPS 46-3](https://csrc.nist.gov/pubs/fips/46-3/final), [FIPS 81](https://csrc.nist.gov/pubs/fips/81/final) |

## Remarks

You can use these handles in any situation that requires an algorithm handle. However, any call to [BCryptSetProperty](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptsetproperty) fails as the algorithm handle is shared and cannot be modified. In addition, these handles cannot be used at `IRQL=DISPATCH` in kernel mode.

## Related content

- [BCryptOpenAlgorithmProvider](/windows/win32/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)
- [NCryptCreatePersistedKey](/windows/win32/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey)
