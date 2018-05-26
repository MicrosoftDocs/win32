---
Description: The following interfaces can be used to create a certificate property.
ms.assetid: c64fca58-fb2f-412f-b7c0-5db1979d051b
title: Certificate Property Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Property Interfaces

The following interfaces can be used to create a certificate property.



| Interface                                                                          | Description                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertProperties**](/windows/win32/CertEnroll/nn-certenroll-icertproperties?branch=master)                                         | Manage a collection of [**ICertProperty**](/windows/win32/CertEnroll/nn-certenroll-icertproperty?branch=master) objects.                                                                                                                                                                                    |
| [**ICertProperty**](/windows/win32/CertEnroll/nn-certenroll-icertproperty?branch=master)                                             | Associates an external property with a certificate.                                                                                                                                                                                                       |
| [**ICertPropertyArchived**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyarchived?branch=master)                             | Represents a certificate property that identifies whether a certificate has been archived.                                                                                                                                                                |
| [**ICertPropertyArchivedKeyHash**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyarchivedkeyhash?branch=master)               | Represents a SHA-1 hash of an encrypted private key submitted to a certification authority for archival.                                                                                                                                                  |
| [**ICertPropertyAutoEnroll**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyautoenroll?branch=master)                         | Represents a certificate property that identifies a template that has been configured to enable autoenrollment of the certificate.                                                                                                                        |
| [**ICertPropertyBackedUp**](/windows/win32/CertEnroll/nn-certenroll-icertpropertybackedup?branch=master)                             | Represents a certificate property that identifies whether a certificate has been backed up and, if so, the date and time that it was saved.                                                                                                               |
| [**ICertPropertyDescription**](/windows/win32/CertEnroll/nn-certenroll-icertpropertydescription?branch=master)                       | Enables you to specify and retrieve a string that contains descriptive information for a certificate.                                                                                                                                                     |
| [**ICertPropertyEnrollment**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyenrollment?branch=master)                         | Represents a certificate property that contains certificate and certification authority information created when the client calls the [**Enroll**](/windows/win32/CertEnroll/nf-certenroll-ix509enrollment-enroll?branch=master) method on the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) interface. |
| [**ICertPropertyEnrollmentPolicyServer**](/windows/win32/Certenroll/nn-certenroll-icertpropertyenrollmentpolicyserver?branch=master) | Represents an external certificate property that contains information about a certificate enrollment policy (CEP) server and a certificate enrollment server (CES).                                                                                       |
| [**ICertPropertyFriendlyName**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyfriendlyname?branch=master)                     | Enables you to specify and retrieve a string that contains the display name of a certificate.                                                                                                                                                             |
| [**ICertPropertyKeyProvInfo**](/windows/win32/CertEnroll/nn-certenroll-icertpropertykeyprovinfo?branch=master)                       | Represents a certificate property that contains information about a private key.                                                                                                                                                                          |
| [**ICertPropertyRenewal**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyrenewal?branch=master)                               | Represents a certificate property that contains a SHA-1 hash of the new certificate created when an existing certificate is renewed.                                                                                                                      |
| [**ICertPropertyRequestOriginator**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyrequestoriginator?branch=master)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |
| [**ICertPropertyRequestOriginator**](/windows/win32/CertEnroll/nn-certenroll-icertpropertyrequestoriginator?branch=master)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



