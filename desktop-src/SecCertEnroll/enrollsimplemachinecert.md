---
description: Enrolls a computer in a certificate hierarchy by using a template, a certificate display name, and the certificate description.
ms.assetid: d9e01767-f6e8-4fd6-a848-8d5acf57407e
title: enrollSimpleMachineCert
ms.topic: article
ms.date: 05/31/2018
---

# enrollSimpleMachineCert

The enrollSimpleMachineCert sample enrolls a computer in a certificate hierarchy by using a template, a certificate display name, and the certificate description.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), a C++ version of the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\EnrollSimpleMachineCert folder. A VBScript version is installed in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VBS\\EnrollSimpleMachineCert folder.

## Discussion

The enrollSimpleMachineCert sample:

1.  Processes the command line arguments. The command line should contain the name of the template, a certificate display name, and a certificate description.
2.  Creates an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object and initializes it by using the template specified on the command line. The ContextAdministratorForceMachine value for the first parameter specifies that the certificate is being requested by an administrator acting on behalf of a computer.
3.  Adds the display name and description to the enrollment object.
4.  Attempts to enroll the certificate request and checks the status of the process. The checkEnrollStatus function is defined in enrollCommon.cpp.

## Related topics

<dl> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



