---
description: An X.509 standard certificate, contains version, serial number, algorithm identifier, issuer name, valid date range, subject name, algorithm, and subject public key information, and optionally, issuer unique ID, subject unique ID, and extensions.
ms.assetid: 91425185-2a06-4040-b83d-c42ee080d55f
title: Certificates and CryptoAPI
ms.topic: article
ms.date: 05/31/2018
---

# Certificates and CryptoAPI

[*CryptoAPI*](../secgloss/c-gly.md) supports using X.509 certificates as defined in [IETF RFC 3280](https://www.ietf.org/rfc/rfc3280.txt). This documentation assumes the use of an X.509 or comparable [*digital certificate*](../secgloss/c-gly.md).

An X.509 standard certificate contains the following information.



| Field                | Description                                                                                                                                                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version              | Version number of the certificate.                                                                                                                                                                                         |
| Serial Number        | Serial number of the certificate.                                                                                                                                                                                          |
| Algorithm Identifier | Signature algorithm used by the certificate signer.                                                                                                                                                                        |
| Issuer Name          | Name of the issuer of the certificate.                                                                                                                                                                                     |
| Not Before           | Date before which the certificate is not valid.                                                                                                                                                                            |
| Not After            | Date after which the certificate is not valid.                                                                                                                                                                             |
| Subject Name         | Name of the person or entity to whom the certificate is being issued.                                                                                                                                                      |
| Algorithm            | Algorithm used for the public key.                                                                                                                                                                                         |
| Subject Public Key   | Actual public key (a bit string).                                                                                                                                                                                          |
| Issuer Unique ID     | Optional Field. If present, version must be version 2.                                                                                                                                                                     |
| Subject Unique ID    | Optional Field. If present, version must be version 2.                                                                                                                                                                     |
| Extensions           | Optional field. Represents additional data that an issuer can want to add to a certificate, such as email address or authorization to issue certificates. If extensions are present, version must be version 3.<br/> |



 

 

 
