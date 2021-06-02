---
description: The following interfaces can be used to create a certificate property.
ms.assetid: c64fca58-fb2f-412f-b7c0-5db1979d051b
title: Certificate Property Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Property Interfaces

The following interfaces can be used to create a certificate property.



| Interface                                                                          | Description                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertProperties**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperties)                                         | Manage a collection of [**ICertProperty**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperty) objects.                                                                                                                                                                                    |
| [**ICertProperty**](/windows/desktop/api/CertEnroll/nn-certenroll-icertproperty)                                             | Associates an external property with a certificate.                                                                                                                                                                                                       |
| [**ICertPropertyArchived**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyarchived)                             | Represents a certificate property that identifies whether a certificate has been archived.                                                                                                                                                                |
| [**ICertPropertyArchivedKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyarchivedkeyhash)               | Represents a SHA-1 hash of an encrypted private key submitted to a certification authority for archival.                                                                                                                                                  |
| [**ICertPropertyAutoEnroll**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyautoenroll)                         | Represents a certificate property that identifies a template that has been configured to enable autoenrollment of the certificate.                                                                                                                        |
| [**ICertPropertyBackedUp**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertybackedup)                             | Represents a certificate property that identifies whether a certificate has been backed up and, if so, the date and time that it was saved.                                                                                                               |
| [**ICertPropertyDescription**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertydescription)                       | Enables you to specify and retrieve a string that contains descriptive information for a certificate.                                                                                                                                                     |
| [**ICertPropertyEnrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyenrollment)                         | Represents a certificate property that contains certificate and certification authority information created when the client calls the [**Enroll**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-enroll) method on the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) interface. |
| [**ICertPropertyEnrollmentPolicyServer**](/windows/desktop/api/Certenroll/nn-certenroll-icertpropertyenrollmentpolicyserver) | Represents an external certificate property that contains information about a certificate enrollment policy (CEP) server and a certificate enrollment server (CES).                                                                                       |
| [**ICertPropertyFriendlyName**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyfriendlyname)                     | Enables you to specify and retrieve a string that contains the display name of a certificate.                                                                                                                                                             |
| [**ICertPropertyKeyProvInfo**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertykeyprovinfo)                       | Represents a certificate property that contains information about a private key.                                                                                                                                                                          |
| [**ICertPropertyRenewal**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyrenewal)                               | Represents a certificate property that contains a SHA-1 hash of the new certificate created when an existing certificate is renewed.                                                                                                                      |
| [**ICertPropertyRequestOriginator**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyrequestoriginator)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |
| [**ICertPropertyRequestOriginator**](/windows/desktop/api/CertEnroll/nn-certenroll-icertpropertyrequestoriginator)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



