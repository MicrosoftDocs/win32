---
description: Accesses an existing key container. This method associates the key container to the certificate that corresponds to the private key by adding the CERT\_KEY\_PROV\_INFO\_PROP\_ID property using the specified information.
ms.assetid: e5e19452-bfdc-4427-ac1d-cf8aa349bb89
title: PrivateKey.Open method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey.Open
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey.Open method

\[The **Open** method is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.privatekey?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **Open** method accesses an existing [*key container*](../secgloss/k-gly.md). This method associates the key container to the [*certificate*](../secgloss/c-gly.md) that corresponds to the [*private key*](../secgloss/p-gly.md) by adding the CERT\_KEY\_PROV\_INFO\_PROP\_ID property using the specified information.

## Syntax


```VB
PrivateKey.Open( _
  ByVal ContainerName, _
  [ ByVal ProviderName ], _
  [ ByVal ProviderType ], _
  [ ByVal KeySpec ], _
  [ ByVal StoreLocation ], _
  [ ByVal bCheckExistence ] _
)
```



## Parameters

<dl> <dt>

*ContainerName* \[in\]
</dt> <dd>

A string that contains the name of the key container.

</dd> <dt>

*ProviderName* \[in, optional\]
</dt> <dd>

A string that contains the name of the provider. The default value is CAPICOM\_PROV\_MS\_ENHANCED\_PROV. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                      | Meaning                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <span id="CAPICOM_PROV_MS_DEF_PROV"></span><span id="capicom_prov_ms_def_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_PROV**</dt> </dl>                                          | Microsoft base cryptographic provider.<br/>                            |
| <span id="CAPICOM_PROV_MS_ENHANCED_PROV"></span><span id="capicom_prov_ms_enhanced_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_ENHANCED\_PROV**</dt> </dl>                           | Microsoft enhanced cryptographic provider.<br/>                        |
| <span id="CAPICOM_PROV_MS_STRONG_PROV"></span><span id="capicom_prov_ms_strong_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_STRONG\_PROV**</dt> </dl>                                 | Microsoft strong cryptographic provider.<br/>                          |
| <span id="CAPICOM_PROV_MS_DEF_RSA_SIG_PROV"></span><span id="capicom_prov_ms_def_rsa_sig_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_RSA\_SIG\_PROV**</dt> </dl>                | Microsoft RSA signature cryptographic provider.<br/>                   |
| <span id="CAPICOM_PROV_MS_DEF_RSA_SCHANNEL_PROV"></span><span id="capicom_prov_ms_def_rsa_schannel_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_RSA\_SCHANNEL\_PROV**</dt> </dl> | Microsoft RSA Schannel cryptographic provider.<br/>                    |
| <span id="CAPICOM_PROV_MS_DEF_DSS_PROV"></span><span id="capicom_prov_ms_def_dss_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_DSS\_PROV**</dt> </dl>                             | Microsoft base DSS cryptographic provider.<br/>                        |
| <span id="CAPICOM_PROV_MS_DEF_DSS_DH_PROV"></span><span id="capicom_prov_ms_def_dss_dh_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_DSS\_DH\_PROV**</dt> </dl>                   | Microsoft base DSS and Diffie-Hellman cryptographic provider.<br/>     |
| <span id="CAPICOM_PROV_MS_ENH_DSS_DH_PROV"></span><span id="capicom_prov_ms_enh_dss_dh_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_ENH\_DSS\_DH\_PROV**</dt> </dl>                   | Microsoft enhanced DSS and Diffie-Hellman cryptographic provider.<br/> |
| <span id="CAPICOM_PROV_MS_DEF_DH_SCHANNEL_PROV"></span><span id="capicom_prov_ms_def_dh_schannel_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_DEF\_DH\_SCHANNEL\_PROV**</dt> </dl>    | Microsoft DH Schannel cryptographic provider.<br/>                     |
| <span id="CAPICOM_PROV_MS_SCARD_PROV"></span><span id="capicom_prov_ms_scard_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_SCARD\_PROV**</dt> </dl>                                    | Microsoft base smart card cryptographic provider.<br/>                 |
| <span id="CAPICOM_PROV_MS_ENH_RSA_AES_PROV"></span><span id="capicom_prov_ms_enh_rsa_aes_prov"></span><dl> <dt>**CAPICOM\_PROV\_MS\_ENH\_RSA\_AES\_PROV**</dt> </dl>                | Microsoft enhanced RSA and AES cryptographic provider.<br/>            |



 

</dd> <dt>

*ProviderType* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_PROV\_TYPE**](capicom-prov-type.md) enumeration that specifies a provider type. The default value is CAPICOM\_PROV\_RSA\_FULL. This parameter can be one of the following values.



| Value                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_PROV_RSA_FULL"></span><span id="capicom_prov_rsa_full"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_FULL**</dt> </dl>                 | The full [*RSA*](../secgloss/r-gly.md) [*cryptographic service provider*](../secgloss/c-gly.md) (CSP). This provider type supports both [*digital signatures*](../secgloss/d-gly.md) and data [*encryption*](../secgloss/e-gly.md).<br/> |
| <span id="CAPICOM_PROV_RSA_SIG"></span><span id="capicom_prov_rsa_sig"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_SIG**</dt> </dl>                    | The subset of the RSA CSP that supports only those functions and algorithms that are required for [*hashes*](../secgloss/h-gly.md) and [*digital signatures*](../secgloss/d-gly.md).<br/>                                                                                                                                                                              |
| <span id="CAPICOM_PROV_DSS"></span><span id="capicom_prov_dss"></span><dl> <dt>**CAPICOM\_PROV\_DSS**</dt> </dl>                                 | The [*Digital Signature Standard*](../secgloss/d-gly.md) (DSS) CSP. This provider type supports only hashes and digital signatures. DSS uses the [*Digital Signature Algorithm*](../secgloss/d-gly.md) (DSA).<br/>                                                                                     |
| <span id="CAPICOM_PROV_FORTEZZA"></span><span id="capicom_prov_fortezza"></span><dl> <dt>**CAPICOM\_PROV\_FORTEZZA**</dt> </dl>                  | The CSP that contains the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST).<br/>                                                                                                                                                                          |
| <span id="CAPICOM_PROV_MS_EXCHANGE"></span><span id="capicom_prov_ms_exchange"></span><dl> <dt>**CAPICOM\_PROV\_MS\_EXCHANGE**</dt> </dl>        | The CSP that supports the Microsoft Exchange mail application and other applications that are compatible with Microsoft Mail.<br/>                                                                                                                                                                                                                                                                                                                               |
| <span id="CAPICOM_PROV_SSL"></span><span id="capicom_prov_ssl"></span><dl> <dt>**CAPICOM\_PROV\_SSL**</dt> </dl>                                 | The CSP that supports the [*Secure Sockets Layer*](../secgloss/s-gly.md) (SSL) protocol.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="CAPICOM_PROV_RSA_SCHANNEL"></span><span id="capicom_prov_rsa_schannel"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_SCHANNEL**</dt> </dl>     | The CSP that supports both RSA and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <span id="CAPICOM_PROV_DSS_DH"></span><span id="capicom_prov_dss_dh"></span><dl> <dt>**CAPICOM\_PROV\_DSS\_DH**</dt> </dl>                       | The CSP that supports both DSS and [*Diffie-Hellman*](../secgloss/d-gly.md) protocols.<br/>                                                                                                                                                                                                                                                                                              |
| <span id="CAPICOM_PROV_EC_ECDSA_SIG"></span><span id="capicom_prov_ec_ecdsa_sig"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECDSA\_SIG**</dt> </dl>    | The CSP that supports the Elliptic Curve Digital Signature Algorithm (ECDSA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                                                                                                      |
| <span id="CAPICOM_PROV_EC_ECNRA_SIG"></span><span id="capicom_prov_ec_ecnra_sig"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECNRA\_SIG**</dt> </dl>    | The CSP that supports the Elliptic Curve Nyberg-Rueppel Analog (ECNRA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                                                                                                            |
| <span id="CAPICOM_PROV_EC_ECDSA_FULL"></span><span id="capicom_prov_ec_ecdsa_full"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECDSA\_FULL**</dt> </dl> | The CSP that supports the full ECDSA.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_EC_ECNRA_FULL"></span><span id="capicom_prov_ec_ecnra_full"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECNRA\_FULL**</dt> </dl> | The CSP that supports the full ECNRA.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_DH_SCHANNEL"></span><span id="capicom_prov_dh_schannel"></span><dl> <dt>**CAPICOM\_PROV\_DH\_SCHANNEL**</dt> </dl>        | The CSP that supports both [*Diffie-Hellman*](../secgloss/d-gly.md) and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_SPYRUS_LYNKS"></span><span id="capicom_prov_spyrus_lynks"></span><dl> <dt>**CAPICOM\_PROV\_SPYRUS\_LYNKS**</dt> </dl>     | The CSP that supports the SPYRUS LYNKS Card device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="CAPICOM_PROV_RNG"></span><span id="capicom_prov_rng"></span><dl> <dt>**CAPICOM\_PROV\_RNG**</dt> </dl>                                 | The CSP that handles random number generation.<br/>                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="CAPICOM_PROV_INTEL_SEC"></span><span id="capicom_prov_intel_sec"></span><dl> <dt>**CAPICOM\_PROV\_INTEL\_SEC**</dt> </dl>              | The CSP that provides Intel security.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_REPLACE_OWF"></span><span id="capicom_prov_replace_owf"></span><dl> <dt>**CAPICOM\_PROV\_REPLACE\_OWF**</dt> </dl>        | The CSP that supports replacement of the manner in which one-way formats are generated from passwords.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <span id="CAPICOM_PROV_RSA_AES"></span><span id="capicom_prov_rsa_aes"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_AES**</dt> </dl>                    | The CSP that supports both digital signatures and data encryption using the Advanced Encryption Standard ([*AES*](../secgloss/a-gly.md)) algorithm.<br/>                                                                                                                                                                                                                                                                           |



 

</dd> <dt>

*KeySpec* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_KEY\_SPEC**](capicom-key-spec.md) enumeration that specifies the type of private key. The default value is CAPICOM\_KEY\_SPEC\_SIGNATURE. This parameter can be one of the following values.



| Value                                                                                                                                                                                                        | Meaning                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="CAPICOM_KEY_SPEC_KEYEXCHANGE"></span><span id="capicom_key_spec_keyexchange"></span><dl> <dt>**CAPICOM\_KEY\_SPEC\_KEYEXCHANGE**</dt> </dl> | The key can be used for encryption and signing.<br/> |
| <span id="CAPICOM_KEY_SPEC_SIGNATURE"></span><span id="capicom_key_spec_signature"></span><dl> <dt>**CAPICOM\_KEY\_SPEC\_SIGNATURE**</dt> </dl>       | The key can be used only for signing.<br/>           |



 

</dd> <dt>

*StoreLocation* \[in, optional\]
</dt> <dd>

A value of the [**CAPICOM\_STORE\_LOCATION**](capicom-store-location.md) enumeration that specifies the location of the store where the key resides. The default value is CAPICOM\_CURRENT\_USER\_STORE. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_MEMORY_STORE"></span><span id="capicom_memory_store"></span><dl> <dt>**CAPICOM\_MEMORY\_STORE**</dt> </dl>                                                | The store is a memory store. Any changes in the contents of the store are not persisted.<br/>                                                                                                                                                                                |
| <span id="CAPICOM_LOCAL_MACHINE_STORE"></span><span id="capicom_local_machine_store"></span><dl> <dt>**CAPICOM\_LOCAL\_MACHINE\_STORE**</dt> </dl>                          | The store is a local computer store. Local computer stores can be read/write stores only if the user has read/write permissions. If the user has read/write permissions and if the store is opened read/write, then changes in the contents of the store are persisted.<br/> |
| <span id="CAPICOM_CURRENT_USER_STORE"></span><span id="capicom_current_user_store"></span><dl> <dt>**CAPICOM\_CURRENT\_USER\_STORE**</dt> </dl>                             | The store is a current user store. A current user store may be a read/write store. If it is, changes in the contents of the store are persisted.<br/>                                                                                                                        |
| <span id="CAPICOM_ACTIVE_DIRECTORY_USER_STORE"></span><span id="capicom_active_directory_user_store"></span><dl> <dt>**CAPICOM\_ACTIVE\_DIRECTORY\_USER\_STORE**</dt> </dl> | The store is an Active Directory store. Active Directory stores can be opened only in read-only mode. Certificates cannot be added to or removed from Active Directory stores.<br/>                                                                                          |
| <span id="CAPICOM_SMART_CARD_USER_STORE"></span><span id="capicom_smart_card_user_store"></span><dl> <dt>**CAPICOM\_SMART\_CARD\_USER\_STORE**</dt> </dl>                   | The store is the group of present smart cards. Introduced in CAPICOM 2.0.<br/>                                                                                                                                                                                               |



 

</dd> <dt>

*bCheckExistence* \[in, optional\]
</dt> <dd>

A Boolean value that indicates whether CAPICOM will attempt to access the key. If **True**, CAPICOM attempts to access the key. If the key is user protected or on a smart card or other device, a dialog box may be generated. The default value is **False**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method returns CAPICOM\_E\_NOT\_ALLOWED when it is scripted from a web-based application.

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey**](privatekey.md)
</dt> <dt>

[**Certificate.HasPrivateKey**](certificate-hasprivatekey.md)
</dt> </dl>

 

 
