---
Description: 'The following interfaces can be used to create a certificate property.'
ms.assetid: 'c64fca58-fb2f-412f-b7c0-5db1979d051b'
title: Certificate Property Interfaces
---

# Certificate Property Interfaces

The following interfaces can be used to create a certificate property.



| Interface                                                                          | Description                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICertProperties**](icertproperties.md)                                         | Manage a collection of [**ICertProperty**](icertproperty.md) objects.                                                                                                                                                                                    |
| [**ICertProperty**](icertproperty.md)                                             | Associates an external property with a certificate.                                                                                                                                                                                                       |
| [**ICertPropertyArchived**](icertpropertyarchived.md)                             | Represents a certificate property that identifies whether a certificate has been archived.                                                                                                                                                                |
| [**ICertPropertyArchivedKeyHash**](icertpropertyarchivedkeyhash.md)               | Represents a SHA-1 hash of an encrypted private key submitted to a certification authority for archival.                                                                                                                                                  |
| [**ICertPropertyAutoEnroll**](icertpropertyautoenroll.md)                         | Represents a certificate property that identifies a template that has been configured to enable autoenrollment of the certificate.                                                                                                                        |
| [**ICertPropertyBackedUp**](icertpropertybackedup.md)                             | Represents a certificate property that identifies whether a certificate has been backed up and, if so, the date and time that it was saved.                                                                                                               |
| [**ICertPropertyDescription**](icertpropertydescription.md)                       | Enables you to specify and retrieve a string that contains descriptive information for a certificate.                                                                                                                                                     |
| [**ICertPropertyEnrollment**](icertpropertyenrollment.md)                         | Represents a certificate property that contains certificate and certification authority information created when the client calls the [**Enroll**](ix509enrollment-enroll-method.md) method on the [**IX509Enrollment**](ix509enrollment.md) interface. |
| [**ICertPropertyEnrollmentPolicyServer**](icertpropertyenrollmentpolicyserver.md) | Represents an external certificate property that contains information about a certificate enrollment policy (CEP) server and a certificate enrollment server (CES).                                                                                       |
| [**ICertPropertyFriendlyName**](icertpropertyfriendlyname.md)                     | Enables you to specify and retrieve a string that contains the display name of a certificate.                                                                                                                                                             |
| [**ICertPropertyKeyProvInfo**](icertpropertykeyprovinfo.md)                       | Represents a certificate property that contains information about a private key.                                                                                                                                                                          |
| [**ICertPropertyRenewal**](icertpropertyrenewal.md)                               | Represents a certificate property that contains a SHA-1 hash of the new certificate created when an existing certificate is renewed.                                                                                                                      |
| [**ICertPropertyRequestOriginator**](icertpropertyrequestoriginator.md)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |
| [**ICertPropertyRequestOriginator**](icertpropertyrequestoriginator.md)           | Represents a certificate property that contains the Domain Naming System (DNS) name of the computer on which the request was created.                                                                                                                     |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



