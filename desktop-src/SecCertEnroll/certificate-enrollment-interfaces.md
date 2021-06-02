---
description: The following interfaces can be used to enroll a user or a computer in a certificate hierarchy.
ms.assetid: 653bc971-8bda-4e23-a56a-dbeb36eeaf6d
title: Certificate Enrollment Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Enrollment Interfaces

The following interfaces can be used to enroll a user or a computer in a certificate hierarchy.



| Interface                                              | Description                                                                                                                                                                         |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment)             | Enrolls a computer or user in a certificate hierarchy.                                                                                                                              |
| [**IX509Enrollment2**](/windows/desktop/api/Certenroll/nn-certenroll-ix509enrollment2)           | Extends the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) interface to enable initialization from a template.                                                                          |
| [**IX509EnrollmentHelper**](/windows/desktop/api/Certenroll/nn-certenroll-ix509enrollmenthelper) | Defines methods that enable a web application to enroll a certificate, store policy server credentials in the credential cache, and register policy servers and enrollment servers. |
| [**IX509EnrollmentStatus**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollmentstatus) | Retrieves detailed error information about a certificate enrollment transaction.                                                                                                    |
| [**IX509SCEPEnrollment**](/windows/desktop/api/Certenroll/nn-certenroll-ix509scepenrollment)     | X.509 Simple Computer Enrollment Protocol Interface<br/>                                                                                                                      |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 




