---
description: Specifies the type of cryptographic service provider (CSP).
ms.assetid: faf2390d-bf78-4943-91f3-1db9939fedfb
title: CAPICOM_PROV_TYPE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_PROV_TYPE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_PROV\_TYPE enumeration

The **CAPICOM\_PROV\_TYPE** enumeration specifies the type of [*cryptographic service provider*](../secgloss/c-gly.md) (CSP).

## Members



| Member                             | Description                                                                                                                                                                                                                                                                                                                                                                        | Value |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_PROV\_RSA\_FULL**       | The full [*RSA*](../secgloss/r-gly.md) CSP. This provider type supports both [*digital signatures*](../secgloss/d-gly.md) and data [*encryption*](../secgloss/e-gly.md).<br/>                                                            | 1     |
| **CAPICOM\_PROV\_RSA\_SIG**        | The subset of the RSA CSP that supports only those functions and algorithms that are required for hashes and digital signatures.<br/>                                                                                                                                                                                                                                        | 2     |
| **CAPICOM\_PROV\_DSS**             | The [*Digital Signature Standard*](../secgloss/d-gly.md) (DSS) CSP. This provider type supports only hashes and digital signatures. DSS uses the [*Digital Signature Algorithm*](../secgloss/d-gly.md) (DSA).<br/> | 3     |
| **CAPICOM\_PROV\_FORTEZZA**        | The CSP that contains the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST).<br/>                                                                                      | 4     |
| **CAPICOM\_PROV\_MS\_EXCHANGE**    | The CSP that was designed for the cryptographic needs of Exchange and other applications that are compatible with Microsoft Mail.<br/>                                                                                                                                                                                                                                       | 5     |
| **CAPICOM\_PROV\_SSL**             | The CSP that supports the [*Secure Sockets Layer*](../secgloss/s-gly.md) (SSL) protocol.<br/>                                                                                                                                                                                              | 6     |
| **CAPICOM\_PROV\_RSA\_SCHANNEL**   | The CSP that supports both [*RSA*](../secgloss/r-gly.md) and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                                                                        | 12    |
| **CAPICOM\_PROV\_DSS\_DH**         | The CSP that supports both DSS and [*Diffie-Hellman*](../secgloss/d-gly.md) protocols.<br/>                                                                                                                                                                                                          | 13    |
| **CAPICOM\_PROV\_EC\_ECDSA\_SIG**  | The CSP that supports the Elliptic Curve Digital Signature Algorithm (ECDSA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                  | 14    |
| **CAPICOM\_PROV\_EC\_ECNRA\_SIG**  | The CSP that supports the Elliptic Curve Nyberg-Rueppel Analog (ECNRA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                        | 15    |
| **CAPICOM\_PROV\_EC\_ECDSA\_FULL** | The CSP that supports the full ECDSA.<br/>                                                                                                                                                                                                                                                                                                                                   | 16    |
| **CAPICOM\_PROV\_EC\_ECNRA\_FULL** | The CSP that supports the full ECNRA.<br/>                                                                                                                                                                                                                                                                                                                                   | 17    |
| **CAPICOM\_PROV\_DH\_SCHANNEL**    | The CSP that supports both [*Diffie-Hellman*](../secgloss/d-gly.md) and [*Schannel*](../secgloss/s-gly.md) protocols.<br/>                                                                                                                                   | 18    |
| **CAPICOM\_PROV\_SPYRUS\_LYNKS**   | The CSP that supports the SPYRUS LYNKS Card device.<br/>                                                                                                                                                                                                                                                                                                                     | 20    |
| **CAPICOM\_PROV\_RNG**             | The CSP that handles random number generation.<br/>                                                                                                                                                                                                                                                                                                                          | 21    |
| **CAPICOM\_PROV\_INTEL\_SEC**      | The CSP that provides Intel security.<br/>                                                                                                                                                                                                                                                                                                                                   | 22    |
| **CAPICOM\_PROV\_REPLACE\_OWF**    | The CSP that supports replacement of the manner in which one-way formats are generated from passwords.<br/>                                                                                                                                                                                                                                                                  | 23    |
| **CAPICOM\_PROV\_RSA\_AES**        | The CSP that supports both digital signatures and data encryption using the Advanced Encryption Standard ([*AES*](../secgloss/a-gly.md)) algorithm.<br/>                                                                                                                                                                                       | 24    |



## Remarks

The **CAPICOM\_PROV\_TYPE** enumeration is used by the following methods and properties:

-   [**PrivateKey.ProviderType**](privatekey-providertype.md) property.
-   [**PrivateKey.Open**](privatekey-open.md) method.

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
