---
description: Used to identify standard encryption algorithms in various CNG functions and structures, such as the CRYPT\_INTERFACE\_REG structure.
ms.assetid: a05ae7e6-d882-4287-9990-23e4cd340b05
title: CNG Algorithm Identifiers (Bcrypt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CNG Algorithm Identifiers

The following identifiers are used to identify standard encryption algorithms in various CNG functions and structures, such as the [**CRYPT\_INTERFACE\_REG**](/windows/desktop/api/Bcrypt/ns-bcrypt-crypt_interface_reg) structure. Third party providers may have additional algorithms that they support.




| Constant/value | Description | 
|----------------|-------------|
| <span id="BCRYPT_3DES_ALGORITHM"></span><span id="bcrypt_3des_algorithm"></span><dl><dt><strong>BCRYPT_3DES_ALGORITHM</strong></dt><dt>"3DES"</dt></dl> | The triple data encryption standard symmetric encryption algorithm.<br /> Standard: SP800-67, SP800-38A<br /> | 
| <span id="BCRYPT_3DES_112_ALGORITHM"></span><span id="bcrypt_3des_112_algorithm"></span><dl><dt><strong>BCRYPT_3DES_112_ALGORITHM</strong></dt><dt>"3DES_112"</dt></dl> | The 112-bit triple data encryption standard symmetric encryption algorithm.<br /> Standard: SP800-67, SP800-38A<br /> | 
| <span id="BCRYPT_AES_ALGORITHM"></span><span id="bcrypt_aes_algorithm"></span><dl><dt><strong>BCRYPT_AES_ALGORITHM</strong></dt><dt>"AES"</dt></dl> | The advanced encryption standard symmetric encryption algorithm.<br /> Standard: FIPS 197<br /> | 
| <span id="BCRYPT_AES_CMAC_ALGORITHM"></span><span id="bcrypt_aes_cmac_algorithm"></span><dl><dt><strong>BCRYPT_AES_CMAC_ALGORITHM</strong></dt><dt>"AES-CMAC"</dt></dl> | The advanced encryption standard (AES) cipher based message authentication code (CMAC) symmetric encryption algorithm.<br /> Standard: SP 800-38B<br /><strong>Windows 8:</strong> Support for this algorithm begins.<br /><br /> | 
| <span id="BCRYPT_AES_GMAC_ALGORITHM"></span><span id="bcrypt_aes_gmac_algorithm"></span><dl><dt><strong>BCRYPT_AES_GMAC_ALGORITHM</strong></dt><dt>"AES-GMAC"</dt></dl> | The advanced encryption standard (AES) Galois message authentication code (GMAC) symmetric encryption algorithm.<br /> Standard: SP800-38D<br /><strong>Windows Vista:</strong> This algorithm is supported beginning with Windows Vista with SP1.<br /> | 
| <span id="BCRYPT_CAPI_KDF_ALGORITHM"></span><span id="bcrypt_capi_kdf_algorithm"></span><dl><dt><strong>BCRYPT_CAPI_KDF_ALGORITHM</strong></dt><dt>L"CAPI_KDF"</dt></dl> | Crypto API (CAPI) key derivation function algorithm. Used by the <a href="/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptkeyderivation"><strong>BCryptKeyDerivation</strong></a> and <a href="/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptkeyderivation"><strong>NCryptKeyDerivation</strong></a> functions.<br /> | 
| <span id="BCRYPT_DES_ALGORITHM"></span><span id="bcrypt_des_algorithm"></span><dl><dt><strong>BCRYPT_DES_ALGORITHM</strong></dt><dt>"DES"</dt></dl> | The data encryption standard symmetric encryption algorithm.<br /> Standard: FIPS 46-3, FIPS 81<br /> | 
| <span id="BCRYPT_DESX_ALGORITHM"></span><span id="bcrypt_desx_algorithm"></span><dl><dt><strong>BCRYPT_DESX_ALGORITHM</strong></dt><dt>"DESX"</dt></dl> | The extended data encryption standard symmetric encryption algorithm.<br /> Standard: None<br /> | 
| <span id="BCRYPT_DH_ALGORITHM"></span><span id="bcrypt_dh_algorithm"></span><dl><dt><strong>BCRYPT_DH_ALGORITHM</strong></dt><dt>"DH"</dt></dl> | The Diffie-Hellman key exchange algorithm.<br /> Standard: PKCS #3<br /> | 
| <span id="BCRYPT_DSA_ALGORITHM"></span><span id="bcrypt_dsa_algorithm"></span><dl><dt><strong>BCRYPT_DSA_ALGORITHM</strong></dt><dt>"DSA"</dt></dl> | The digital signature algorithm.<br /> Standard: FIPS 186-2<br /><strong>Windows 8:</strong> Beginning with Windows 8, this algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3.<br /> | 
| <span id="BCRYPT_ECDH_P256_ALGORITHM"></span><span id="bcrypt_ecdh_p256_algorithm"></span><dl><dt><strong>BCRYPT_ECDH_P256_ALGORITHM</strong></dt><dt>"ECDH_P256"</dt></dl> | The 256-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br /> Standard: SP800-56A<br /> | 
| <span id="BCRYPT_ECDH_P384_ALGORITHM"></span><span id="bcrypt_ecdh_p384_algorithm"></span><dl><dt><strong>BCRYPT_ECDH_P384_ALGORITHM</strong></dt><dt>"ECDH_P384"</dt></dl> | The 384-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br /> Standard: SP800-56A<br /> | 
| <span id="BCRYPT_ECDH_P521_ALGORITHM"></span><span id="bcrypt_ecdh_p521_algorithm"></span><dl><dt><strong>BCRYPT_ECDH_P521_ALGORITHM</strong></dt><dt>"ECDH_P521"</dt></dl> | The 521-bit prime elliptic curve Diffie-Hellman key exchange algorithm.<br /> Standard: SP800-56A<br /> | 
| <span id="BCRYPT_ECDSA_P256_ALGORITHM"></span><span id="bcrypt_ecdsa_p256_algorithm"></span><dl><dt><strong>BCRYPT_ECDSA_P256_ALGORITHM</strong></dt><dt>"ECDSA_P256"</dt></dl> | The 256-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br /> Standard: FIPS 186-2, X9.62<br /> | 
| <span id="BCRYPT_ECDSA_P384_ALGORITHM"></span><span id="bcrypt_ecdsa_p384_algorithm"></span><dl><dt><strong>BCRYPT_ECDSA_P384_ALGORITHM</strong></dt><dt>"ECDSA_P384"</dt></dl> | The 384-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br /> Standard: FIPS 186-2, X9.62<br /> | 
| <span id="BCRYPT_ECDSA_P521_ALGORITHM"></span><span id="bcrypt_ecdsa_p521_algorithm"></span><dl><dt><strong>BCRYPT_ECDSA_P521_ALGORITHM</strong></dt><dt>"ECDSA_P521"</dt></dl> | The 521-bit prime elliptic curve digital signature algorithm (FIPS 186-2).<br /> Standard: FIPS 186-2, X9.62<br /> | 
| <span id="BCRYPT_MD2_ALGORITHM"></span><span id="bcrypt_md2_algorithm"></span><dl><dt><strong>BCRYPT_MD2_ALGORITHM</strong></dt><dt>"MD2"</dt></dl> | The MD2 hash algorithm.<br /> Standard: RFC 1319<br /> | 
| <span id="BCRYPT_MD4_ALGORITHM"></span><span id="bcrypt_md4_algorithm"></span><dl><dt><strong>BCRYPT_MD4_ALGORITHM</strong></dt><dt>"MD4"</dt></dl> | The MD4 hash algorithm.<br /> Standard: RFC 1320<br /> | 
| <span id="BCRYPT_MD5_ALGORITHM"></span><span id="bcrypt_md5_algorithm"></span><dl><dt><strong>BCRYPT_MD5_ALGORITHM</strong></dt><dt>"MD5"</dt></dl> | The MD5 hash algorithm.<br /> Standard: RFC 1321<br /> | 
| <span id="BCRYPT_RC2_ALGORITHM"></span><span id="bcrypt_rc2_algorithm"></span><dl><dt><strong>BCRYPT_RC2_ALGORITHM</strong></dt><dt>"RC2"</dt></dl> | The RC2 block symmetric encryption algorithm.<br /> Standard: RFC 2268<br /> | 
| <span id="BCRYPT_RC4_ALGORITHM"></span><span id="bcrypt_rc4_algorithm"></span><dl><dt><strong>BCRYPT_RC4_ALGORITHM</strong></dt><dt>"RC4"</dt></dl> | The RC4 symmetric encryption algorithm.<br /> Standard: Various<br /> | 
| <span id="BCRYPT_RNG_ALGORITHM"></span><span id="bcrypt_rng_algorithm"></span><dl><dt><strong>BCRYPT_RNG_ALGORITHM</strong></dt><dt>"RNG"</dt></dl> | The random-number generator algorithm.<br /> Standard: FIPS 186-2, FIPS 140-2, NIST SP 800-90<br /><blockquote>[!Note]<br />Beginning with Windows Vista with SP1 and Windows Server 2008, the random number generator is based on the AES counter mode specified in the NIST SP 800-90 standard.</blockquote><br /><strong>Windows Vista:</strong> The random number generator is based on the hash-based random number generator specified in the FIPS 186-2 standard.<br /><strong>Windows 8:</strong> Beginning with Windows 8, the RNG algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3.<br /> | 
| <span id="BCRYPT_RNG_DUAL_EC_ALGORITHM"></span><span id="bcrypt_rng_dual_ec_algorithm"></span><dl><dt><strong>BCRYPT_RNG_DUAL_EC_ALGORITHM</strong></dt><dt>"DUALECRNG"</dt></dl> | The dual elliptic curve random-number generator algorithm. <br /> Standard: SP800-90.<br /><strong>Windows 8:</strong> Beginning with Windows 8, the EC RNG algorithm supports FIPS 186-3. Keys less than or equal to 1024 bits adhere to FIPS 186-2 and keys greater than 1024 to FIPS 186-3.<br /><strong>Windows 10:</strong> Beginning with Windows 10, the dual elliptic curve random number generator algorithm has been removed. Existing uses of this algorithm will continue to work; however, the random number generator is based on the AES counter mode specified in the NIST SP 800-90 standard. New code should use <strong>BCRYPT_RNG_ALGORITHM</strong>, and it is recommended that existing code be changed to use <strong>BCRYPT_RNG_ALGORITHM</strong>. <br /> | 
| <span id="BCRYPT_RNG_FIPS186_DSA_ALGORITHM"></span><span id="bcrypt_rng_fips186_dsa_algorithm"></span><dl><dt><strong>BCRYPT_RNG_FIPS186_DSA_ALGORITHM</strong></dt><dt>"FIPS186DSARNG"</dt></dl> | The random-number generator algorithm suitable for DSA (Digital Signature Algorithm). <br /> Standard: FIPS 186-2.<br /><strong>Windows 8:</strong> Support for FIPS 186-3 begins.<br /> | 
| <span id="BCRYPT_RSA_ALGORITHM"></span><span id="bcrypt_rsa_algorithm"></span><dl><dt><strong>BCRYPT_RSA_ALGORITHM</strong></dt><dt>"RSA"</dt></dl> | The RSA public key algorithm. <br /> Standard: PKCS #1 v1.5 and v2.0.<br /> | 
| <span id="BCRYPT_RSA_SIGN_ALGORITHM"></span><span id="bcrypt_rsa_sign_algorithm"></span><dl><dt><strong>BCRYPT_RSA_SIGN_ALGORITHM</strong></dt><dt>"RSA_SIGN"</dt></dl> | The RSA signature algorithm. This algorithm is not currently supported. You can use the <strong>BCRYPT_RSA_ALGORITHM</strong> algorithm to perform RSA signing operations. <br /> Standard: PKCS #1 v1.5 and v2.0.<br /> | 
| <span id="BCRYPT_SHA1_ALGORITHM"></span><span id="bcrypt_sha1_algorithm"></span><dl><dt><strong>BCRYPT_SHA1_ALGORITHM</strong></dt><dt>"SHA1"</dt></dl> | The 160-bit secure hash algorithm. <br /> Standard: FIPS 180-2, FIPS 198.<br /> | 
| <span id="BCRYPT_SHA256_ALGORITHM"></span><span id="bcrypt_sha256_algorithm"></span><dl><dt><strong>BCRYPT_SHA256_ALGORITHM</strong></dt><dt>"SHA256"</dt></dl> | The 256-bit secure hash algorithm.<br /> Standard: FIPS 180-2, FIPS 198.<br /> | 
| <span id="BCRYPT_SHA384_ALGORITHM"></span><span id="bcrypt_sha384_algorithm"></span><dl><dt><strong>BCRYPT_SHA384_ALGORITHM</strong></dt><dt>"SHA384"</dt></dl> | The 384-bit secure hash algorithm. <br /> Standard: FIPS 180-2, FIPS 198.<br /> | 
| <span id="BCRYPT_SHA512_ALGORITHM"></span><span id="bcrypt_sha512_algorithm"></span><dl><dt><strong>BCRYPT_SHA512_ALGORITHM</strong></dt><dt>"SHA512"</dt></dl> | The 512-bit secure hash algorithm. <br /> Standard: FIPS 180-2, FIPS 198.<br /> | 
| <span id="BCRYPT_SP800108_CTR_HMAC_ALGORITHM"></span><span id="bcrypt_sp800108_ctr_hmac_algorithm"></span><dl><dt><strong>BCRYPT_SP800108_CTR_HMAC_ALGORITHM</strong></dt><dt>L"SP800_108_CTR_HMAC"</dt></dl> | Counter mode, hash-based message authentication code (HMAC) key derivation function algorithm. Used by the <a href="/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptkeyderivation"><strong>BCryptKeyDerivation</strong></a> and <a href="/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptkeyderivation"><strong>NCryptKeyDerivation</strong></a> functions.<br /> | 
| <span id="BCRYPT_SP80056A_CONCAT_ALGORITHM"></span><span id="bcrypt_sp80056a_concat_algorithm"></span><dl><dt><strong>BCRYPT_SP80056A_CONCAT_ALGORITHM</strong></dt><dt>L"SP800_56A_CONCAT"</dt></dl> | SP800-56A key derivation function algorithm. Used by the <a href="/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptkeyderivation"><strong>BCryptKeyDerivation</strong></a> and <a href="/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptkeyderivation"><strong>NCryptKeyDerivation</strong></a> functions.<br /> | 
| <span id="_BCRYPT_PBKDF2_ALGORITHM"></span><span id="_bcrypt_pbkdf2_algorithm"></span><dl><dt><strong>BCRYPT_PBKDF2_ALGORITHM</strong></dt><dt>L"PBKDF2"</dt></dl> | Password-based key derivation function 2 (PBKDF2) algorithm. Used by the <a href="/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptkeyderivation"><strong>BCryptKeyDerivation</strong></a> and <a href="/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptkeyderivation"><strong>NCryptKeyDerivation</strong></a> functions.<br /> | 
| <span id="BCRYPT_ECDSA_ALGORITHM"></span><span id="bcrypt_ecdsa_algorithm"></span><dl><dt><strong>BCRYPT_ECDSA_ALGORITHM</strong></dt><dt>"ECDSA"</dt></dl> | Generic prime elliptic curve digital signature algorithm (see <strong>Remarks</strong> for more information). <br /> Standard: ANSI X9.62.<br /> | 
| <span id="BCRYPT_ECDH_ALGORITHM"></span><span id="bcrypt_ecdh_algorithm"></span><dl><dt><strong>BCRYPT_ECDH_ALGORITHM</strong></dt><dt>"ECDH"</dt></dl> | Generic prime elliptic curve Diffie-Hellman key exchange algorithm (see <strong>Remarks</strong> for more information). <br /> Standard: SP800-56A.<br /> | 
| <span id="BCRYPT_XTS_AES_ALGORITHM"></span><span id="bcrypt_xts_aes_algorithm"></span><dl><dt><strong>BCRYPT_XTS_AES_ALGORITHM</strong></dt><dt>"XTS-AES"</dt></dl> | The advanced encryption standard symmetric encryption algorithm in XTS mode. <br /> Standard: SP-800-38E, IEEE Std 1619-2007.<br /><strong>Windows 10:</strong> Support for this algorithm begins.<br /> | 




## Remarks

To use **BCRYPT\_ECDSA\_ALGORITM**or **BCRYPT\_ECDH\_ALGORITHM**, call [**BCryptOpenAlgorithmProvider**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) with either **BCRYPT\_ECDSA\_ALGORITHM** or **BCRYPT\_ECDH\_ALGORITHM** as the *pszAlgId*. Then use [**BCryptSetProperty**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptsetproperty) to set the **BCRYPT\_ECC\_CURVE\_NAME** property to a named algorithm listed in CNG Named Curves.

To provider user-defined elliptic curve parameters directly, use [**BCryptSetProperty**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptsetproperty) to set the **BCRYPT\_ECC\_PARAMETERS** property. Download the [Windows 10 Cryptographic Provider Developer Kit (CPDK)](https://www.microsoft.com/download/details.aspx?id=30688) for more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Bcrypt.h</dt> </dl> |



## See also

<dl> <dt>

[**BCryptOpenAlgorithmProvider**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptopenalgorithmprovider)
</dt> <dt>

[**NCryptCreatePersistedKey**](/windows/desktop/api/Ncrypt/nf-ncrypt-ncryptcreatepersistedkey)
</dt> </dl>

 

 




