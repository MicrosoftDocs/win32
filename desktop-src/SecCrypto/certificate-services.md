---
description: Certificate Services, a service running on a Windows server operating system, receives requests for new digital certificates over transports such as RPC or HTTP.
ms.assetid: '4c0098be-6b1b-4ce0-b3a0-942c1290b5b4'
title: Certificate Services
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Services

[*Certificate Services*](../secgloss/c-gly.md), a service running on a Windows server operating system, receives requests for new digital certificates over transports such as RPC or HTTP. It checks each request against custom or site-specific policies, sets optional properties for a certificate to be issued, and issues the certificate. Certificate Services allows administrators to add elements to a [*certificate revocation list*](../secgloss/c-gly.md) (CRL), and to publish signed CRLs on a regular basis.

Certificate services include programmable interfaces for creating support for additional transports, policies, and certificate properties and formats.

In Windows Server 2003, Certificate Services 2.0 can be installed from **Control Panel** by clicking **Add or Remove Programs** and then clicking **Add/Remove Windows Components** to install or uninstall Certificate Services.

Certificate Services concepts are detailed in the following sections. The content is intended to help you develop applications that will interact with Certificate Services.



| Content                                                                                                                                                           | Section                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Description of the features of Certificate Services                                                                                                               | [Certificate Services Features](certificate-services-features.md)         |
| Overview of Certificate Services architecture                                                                                                                     | [Certificate Services Architecture](certificate-services-architecture.md) |
| Relationship between a certificate, the certificate's subject, and the subject's [*public key*](../secgloss/p-gly.md) | [Certificates and Public Keys](certificates-and-public-keys.md)           |
| Information about the Certificate Request properties                                                                                                              | [Certificate Request Guidelines](certificate-request-guidelines.md)       |
| Details of how a certificate is processed by Certificate Services                                                                                                 | [About Certificates](about-certificates.md)                               |
| Description of the [*certification authority*](../secgloss/c-gly.md) renewal process        | [Certification Authority Renewal](certification-authority-renewal.md)     |



 

The following additional useful topics are also included.



| Content                                                                                                                                             | Section                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Documentation on Certificate Enrollment Control, which provides services for creating certificate requests including requests for smart card users. | [Certificate Enrollment Control](certificate-enrollment-control.md) |
| Documentation on the Microsoft Cryptographic Application Programming Interface, which provides cryptography-based security services.                | [Cryptography Essentials](cryptography-essentials.md)               |
| Documentation on Smart Card, which provides services for developing and using smart card systems.                                                   | [Smart Card](../secauthn/smart-card-authentication.md)                     |
| Name properties of certificates and certificate requests.                                                                                           | [Name Properties](name-properties.md)                               |
| List and descriptions of [*X.509*](../secgloss/x-gly.md) certificate properties.                                  | [Certificate Properties](certificate-properties.md)                 |



 

 

 
