---
description: A Windows public key infrastructure (PKI) saves certificates on the server that hosts the certification authority (CA) and on the local computer or device.
ms.assetid: b6aaafeb-30d1-453e-a70c-dcaa01fea1cf
title: Certificate Directory
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Directory

A Windows public key infrastructure (PKI) saves certificates on the server that hosts the certification authority (CA) and on the local computer or device. CA storage is typically referred to as the certificate database, and local storage is known as the certificate store.

## Certificate Database

When you add Certificate Services on a Windows server and configure a CA, a certificate database is created. By default, the database is contained in the *%SystemRoot%*\\System32\\Certlog folder, and the name is based on the CA name with an .edb extension. The database can contain:

-   Issued certificates
-   Revoked certificates
-   Archived private keys
-   Certificate requests

You cannot use the Certificate Enrollment API to manipulate the database. The enrollment process automatically creates the necessary entries.

## Certificate Stores

Microsoft Certificate Services copies issued certificates and pending or rejected requests to local computers and devices. The storage location is called the certificate store and consists of the following logical stores.

| Logical store                                         | Description                                                                                                            |
|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Personal<br/>                                   | Contains certificates associated with a private key controlled by the user or computer.<br/>                     |
| Trusted Root Certification Authorities<br/>     | Contains certificates from implicitly trusted certification authorities (CAs).<br/>                              |
| Enterprise Trust<br/>                           | Contains certificate trust lists typically used to trust self-signed certificates from other organizations.<br/> |
| Intermediate Certification Authorities<br/>     | Contains certificates issued to subordinate CAs in the certification hierarchy.<br/>                             |
| Active Directory User Object<br/>               | Contains the user object certificate or certificates published in Active Directory.<br/>                         |
| Trusted Publishers<br/>                         | Contains certificates from trusted CAs.<br/>                                                                     |
| Untrusted Certificates<br/>                     | Contains certificates that have been explicitly identified as untrusted.<br/>                                    |
| Third-Party Root Certification Authorities<br/> | Contains trusted root certificates from CAs outside the internal certificate hierarchy.<br/>                     |
| Trusted People<br/>                             | Contains certificates issued to users or entities that have been explicitly trusted.<br/>                        |
| Other People<br/>                               | Contains certificates issued to users or entities that have been implicitly trusted.<br/>                        |
| Certificate Enrollment Requests<br/>            | Contains pending or rejected certificate requests.<br/>                                                          |



 

You cannot use the Certificate Enrollment API to specify or retrieve store properties or copy certificates to specific stores.

## Related topics

<dl> <dt>

[PKI Elements](about-pki-components.md)
</dt> </dl>

 

 




