---
Description: The following interfaces can be used to enroll a user or a computer in a certificate hierarchy.
ms.assetid: 653bc971-8bda-4e23-a56a-dbeb36eeaf6d
title: Certificate Enrollment Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Enrollment Interfaces

The following interfaces can be used to enroll a user or a computer in a certificate hierarchy.



| Interface                                              | Description                                                                                                                                                                         |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master)             | Enrolls a computer or user in a certificate hierarchy.                                                                                                                              |
| [**IX509Enrollment2**](/windows/win32/Certenroll/nn-certenroll-ix509enrollment2?branch=master)           | Extends the [**IX509Enrollment**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollment?branch=master) interface to enable initialization from a template.                                                                          |
| [**IX509EnrollmentHelper**](/windows/win32/Certenroll/nn-certenroll-ix509enrollmenthelper?branch=master) | Defines methods that enable a web application to enroll a certificate, store policy server credentials in the credential cache, and register policy servers and enrollment servers. |
| [**IX509EnrollmentStatus**](/windows/win32/CertEnroll/nn-certenroll-ix509enrollmentstatus?branch=master) | Retrieves detailed error information about a certificate enrollment transaction.                                                                                                    |
| [**IX509SCEPEnrollment**](/windows/win32/Certenroll/nn-certenroll-ix509scepenrollment?branch=master)     | X.509 Simple Computer Enrollment Protocol Interface<br/>                                                                                                                      |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 




