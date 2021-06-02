---
description: Certificate Services supports the use of certificates as defined in the ITU-T recommendation X.509 (also, ISO/IEC 9594-8).
ms.assetid: 59f20de0-de24-43c7-a1a2-bdc91ee28059
title: Certificate Properties
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Properties

Certificate Services supports the use of certificates as defined in the ITU-T recommendation [*X.509*](../secgloss/x-gly.md) (also, ISO/IEC 9594-8). The following are properties that are contained in a standard X.509 certificate.



| Field                                       | Description                                                                                                                                                                                                     |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version                                     | Version number of the certificate format.                                                                                                                                                                       |
| Serial Number                               | Serial number of the certificate. This number is assigned by the issuer and is unique within the issuer's list of issued certificates.                                                                          |
| Algorithm Identifier and Parameters         | Signature algorithm and any parameters used by the issuer.                                                                                                                                                      |
| Issuer                                      | Name of the [*certification authority*](../secgloss/c-gly.md) which issued the certificate.                                               |
| Not Before (Date)                           | Certificate not valid before this date.                                                                                                                                                                         |
| Not After (Date)                            | Certificate not valid after this date.                                                                                                                                                                          |
| Subject Name                                | Name of the person or entity to whom the certificate is being issued. This field can also include the certificate recipient's organization, organization unit, locality, state or province, and country/region. |
| Subject Public Key Algorithm and Parameters | The algorithm and any parameters used for the subject's [*public key*](../secgloss/p-gly.md).                                                                       |
| Subject Public Key                          | The actual public key (a bit string).                                                                                                                                                                           |
| Signature                                   | Signature as provided by the issuer.                                                                                                                                                                            |



 

A certificate can contain the following items, depending on the [*X.509*](../secgloss/x-gly.md) version of the certificate.



| Optional field    | Description                                                                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Issuer Unique ID  | Used to make the issuer name unambiguous if it has been used by more than one entity. Present only in versions [*X.509*](../secgloss/x-gly.md) 2.0 or later.<br/> |
| Subject unique ID | Used to make the subject name unambiguous if it has been used by more than one entity. Present only in X.509 2.0 or later.<br/>                                                                     |
| Extensions        | For specifying any desired custom properties. Any number of extension fields can be included in the certificate. Present only in version X.509 3.0.<br/>                                            |



 

> [!Note]  
> Microsoft Certificate Services issues X.509 version 3 certificates.

 

## Related topics

<dl> <dt>

[Name Properties](name-properties.md)
</dt> </dl>

 

 
