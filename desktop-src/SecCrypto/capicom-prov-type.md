---
Description: Specifies the type of cryptographic service provider (CSP).
ms.assetid: faf2390d-bf78-4943-91f3-1db9939fedfb
title: CAPICOM\_PROV\_TYPE enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CAPICOM\_PROV\_TYPE enumeration

The **CAPICOM\_PROV\_TYPE** enumeration specifies the type of [*cryptographic service provider*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSP).

## Members



| Member                             | Description                                                                                                                                                                                                                                                                                                                                                                        | Value |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_PROV\_RSA\_FULL**       | The full [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) CSP. This provider type supports both [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and data [*encryption*](https://msdn.microsoft.com/f1caccd2-3453-448e-b194-bf899eff8091).<br/>                                                            | 1     |
| **CAPICOM\_PROV\_RSA\_SIG**        | The subset of the RSA CSP that supports only those functions and algorithms that are required for hashes and digital signatures.<br/>                                                                                                                                                                                                                                        | 2     |
| **CAPICOM\_PROV\_DSS**             | The [*Digital Signature Standard*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DSS) CSP. This provider type supports only hashes and digital signatures. DSS uses the [*Digital Signature Algorithm*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DSA).<br/> | 3     |
| **CAPICOM\_PROV\_FORTEZZA**        | The CSP that contains the cryptographic protocols and algorithms owned by the [*National Institute of Standards and Technology*](https://msdn.microsoft.com/28d229ef-53ce-4d17-aba0-3bbf51e3ff0c) (NIST).<br/>                                                                                      | 4     |
| **CAPICOM\_PROV\_MS\_EXCHANGE**    | The CSP that was designed for the cryptographic needs of Exchange and other applications that are compatible with Microsoft Mail.<br/>                                                                                                                                                                                                                                       | 5     |
| **CAPICOM\_PROV\_SSL**             | The CSP that supports the [*Secure Sockets Layer*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SSL) protocol.<br/>                                                                                                                                                                                              | 6     |
| **CAPICOM\_PROV\_RSA\_SCHANNEL**   | The CSP that supports both [*RSA*](https://msdn.microsoft.com/ce589e18-02ac-42c2-b76b-776deb686bbd) and [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) protocols.<br/>                                                                                                                                                                                        | 12    |
| **CAPICOM\_PROV\_DSS\_DH**         | The CSP that supports both DSS and [*Diffie-Hellman*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) protocols.<br/>                                                                                                                                                                                                          | 13    |
| **CAPICOM\_PROV\_EC\_ECDSA\_SIG**  | The CSP that supports the Elliptic Curve Digital Signature Algorithm (ECDSA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                  | 14    |
| **CAPICOM\_PROV\_EC\_ECNRA\_SIG**  | The CSP that supports the Elliptic Curve Nyberg-Rueppel Analog (ECNRA) functions and algorithms required for digital signatures.<br/>                                                                                                                                                                                                                                        | 15    |
| **CAPICOM\_PROV\_EC\_ECDSA\_FULL** | The CSP that supports the full ECDSA.<br/>                                                                                                                                                                                                                                                                                                                                   | 16    |
| **CAPICOM\_PROV\_EC\_ECNRA\_FULL** | The CSP that supports the full ECNRA.<br/>                                                                                                                                                                                                                                                                                                                                   | 17    |
| **CAPICOM\_PROV\_DH\_SCHANNEL**    | The CSP that supports both [*Diffie-Hellman*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and [*Schannel*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) protocols.<br/>                                                                                                                                   | 18    |
| **CAPICOM\_PROV\_SPYRUS\_LYNKS**   | The CSP that supports the SPYRUS LYNKS Card device.<br/>                                                                                                                                                                                                                                                                                                                     | 20    |
| **CAPICOM\_PROV\_RNG**             | The CSP that handles random number generation.<br/>                                                                                                                                                                                                                                                                                                                          | 21    |
| **CAPICOM\_PROV\_INTEL\_SEC**      | The CSP that provides Intel security.<br/>                                                                                                                                                                                                                                                                                                                                   | 22    |
| **CAPICOM\_PROV\_REPLACE\_OWF**    | The CSP that supports replacement of the manner in which one-way formats are generated from passwords.<br/>                                                                                                                                                                                                                                                                  | 23    |
| **CAPICOM\_PROV\_RSA\_AES**        | The CSP that supports both digital signatures and data encryption using the Advanced Encryption Standard ([*AES*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02)) algorithm.<br/>                                                                                                                                                                                       | 24    |



## Remarks

The **CAPICOM\_PROV\_TYPE** enumeration is used by the following methods and properties:

-   [**PrivateKey.ProviderType**](privatekey-providertype.md) property.
-   [**PrivateKey.Open**](privatekey-open.md) method.

## Requirements



|                            |                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




