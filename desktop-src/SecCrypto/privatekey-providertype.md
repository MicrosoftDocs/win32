---
description: Retrieves a value of the CAPICOM\_PROV\_TYPE enumeration that specifies the type of provider.
ms.assetid: bc6a579f-5532-45e3-97f4-adcde2cd29e5
title: PrivateKey.ProviderType property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- PrivateKey.ProviderType
api_type:
- COM
api_location:
- Capicom.dll
---

# PrivateKey.ProviderType property

\[The **ProviderType** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Certificate2.PrivateKey Property**](/dotnet/api/system.security.cryptography.x509certificates.x509certificate2.privatekey?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **ProviderType** property retrieves a value of the [**CAPICOM\_PROV\_TYPE**](capicom-prov-type.md) enumeration that specifies the type of provider.

## Syntax


```VB
PrivateKey.ProviderType As CAPICOM_PROV_TYPE
```



## Property value

A value of the [**CAPICOM\_PROV\_TYPE**](capicom-prov-type.md) enumeration that indicates the type of provider. The following table shows the possible values.



| Value                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CAPICOM_PROV_RSA_FULL"></span><span id="capicom_prov_rsa_full"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_FULL**</dt> </dl>                 | The full [*RSA*](../secgloss/r-gly.md) [*cryptographic service provider*](../secgloss/c-gly.md) (CSP). This provider type supports both [*digital signatures*](../secgloss/d-gly.md) and data [*encryption*](../secgloss/e-gly.md).<br/> |
| <span id="CAPICOM_PROV_RSA_SIG"></span><span id="capicom_prov_rsa_sig"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_SIG**</dt> </dl>                    | The subset of the RSA CSP that supports only those functions and algorithms required for hashes and digital signatures.<br/>                                                                                                                                                                                                                                                                                                                                     |
| <span id="CAPICOM_PROV_DSS"></span><span id="capicom_prov_dss"></span><dl> <dt>**CAPICOM\_PROV\_DSS**</dt> </dl>                                 | The [*Digital Signature Standard*](../secgloss/d-gly.md) (DSS) CSP. This provider type supports only hashes and digital signatures. DSS uses the [*Digital Signature Algorithm*](../secgloss/d-gly.md) (DSA).<br/>                                                                                     |
| <span id="CAPICOM_PROV_FORTEZZA"></span><span id="capicom_prov_fortezza"></span><dl> <dt>**CAPICOM\_PROV\_FORTEZZA**</dt> </dl>                  | The CSP that contains the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST).<br/>                                                                                                                                                                          |
| <span id="CAPICOM_PROV_MS_EXCHANGE"></span><span id="capicom_prov_ms_exchange"></span><dl> <dt>**CAPICOM\_PROV\_MS\_EXCHANGE**</dt> </dl>        | The CSP designed for the cryptographic needs of the Microsoft Exchange mail application and other applications compatible with Microsoft Mail.<br/>                                                                                                                                                                                                                                                                                                              |
| <span id="CAPICOM_PROV_SSL"></span><span id="capicom_prov_ssl"></span><dl> <dt>**CAPICOM\_PROV\_SSL**</dt> </dl>                                 | The CSP that supports the [*Secure Sockets Layer*](../secgloss/s-gly.md) (SSL) protocol.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="CAPICOM_PROV_RSA_SCHANNEL"></span><span id="capicom_prov_rsa_schannel"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_SCHANNEL**</dt> </dl>     | The CSP that supports both RSA and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                                                                                                                                                                                                                    |
| <span id="CAPICOM_PROV_DSS_DH"></span><span id="capicom_prov_dss_dh"></span><dl> <dt>**CAPICOM\_PROV\_DSS\_DH**</dt> </dl>                       | The CSP that supports both [*Digital Signature Standard*](../secgloss/d-gly.md) (DSS) and [*Diffie-Hellman*](../secgloss/d-gly.md) protocols.<br/>                                                                                                                                                           |
| <span id="CAPICOM_PROV_EC_ECDSA_SIG"></span><span id="capicom_prov_ec_ecdsa_sig"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECDSA\_SIG**</dt> </dl>    | The CSP that supports the Elliptic Curve Digital Signature Algorithm (ECDSA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                                                                                                      |
| <span id="CAPICOM_PROV_EC_ECNRA_SIG"></span><span id="capicom_prov_ec_ecnra_sig"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECNRA\_SIG**</dt> </dl>    | The CSP that supports the Elliptic Curve Nyberg-Rueppel Analog (ECNRA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                                                                                                            |
| <span id="CAPICOM_PROV_EC_ECDSA_FULL"></span><span id="capicom_prov_ec_ecdsa_full"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECDSA\_FULL**</dt> </dl> | The CSP that supports the full ECDSA.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_EC_ECNRA_FULL"></span><span id="capicom_prov_ec_ecnra_full"></span><dl> <dt>**CAPICOM\_PROV\_EC\_ECNRA\_FULL**</dt> </dl> | The CSP that supports the full ECNRA.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_DH_SCHANNEL"></span><span id="capicom_prov_dh_schannel"></span><dl> <dt>**CAPICOM\_PROV\_DH\_SCHANNEL**</dt> </dl>        | The CSP that supports both [*Diffie-Hellman*](../secgloss/d-gly.md) and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_SPYRUS_LYNKS"></span><span id="capicom_prov_spyrus_lynks"></span><dl> <dt>**CAPICOM\_PROV\_SPYRUS\_LYNKS**</dt> </dl>     | The CSP that supports the SPYRUS LYNKS Card device.<br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="CAPICOM_PROV_RNG"></span><span id="capicom_prov_rng"></span><dl> <dt>**CAPICOM\_PROV\_RNG**</dt> </dl>                                 | The CSP that handles random number generation.<br/>                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="CAPICOM_PROV_INTEL_SEC"></span><span id="capicom_prov_intel_sec"></span><dl> <dt>**CAPICOM\_PROV\_INTEL\_SEC**</dt> </dl>              | The CSP that provides Intel security.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="CAPICOM_PROV_REPLACE_OWF"></span><span id="capicom_prov_replace_owf"></span><dl> <dt>**CAPICOM\_PROV\_REPLACE\_OWF**</dt> </dl>        | The CSP that supports replacement of the manner in which one-way formats (OWFs) are generated from passwords.<br/>                                                                                                                                                                                                                                                                                                                                               |
| <span id="CAPICOM_PROV_RSA_AES"></span><span id="capicom_prov_rsa_aes"></span><dl> <dt>**CAPICOM\_PROV\_RSA\_AES**</dt> </dl>                    | The CSP that supports both digital signatures and data encryption using the [*Advanced Encryption Standard*](../secgloss/a-gly.md) (AES) algorithm.<br/>                                                                                                                                                                                                                                                                           |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**PrivateKey**](privatekey.md)
</dt> </dl>

 

 
