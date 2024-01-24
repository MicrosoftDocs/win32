---
description: The Certificate Enrollment API includes multiple samples designed to help you create custom applications. Most of the samples are written by using C++, but C# and Visual Basic Scripting Edition (VBScript) samples are also included.
ms.assetid: 70ac7b75-542c-4d79-85ce-4b1bac414879
title: Using the Included Samples
ms.topic: article
ms.date: 05/31/2018
---

# Using the Included Samples

The Certificate Enrollment API includes multiple samples designed to help you create custom applications. Most of the samples are written by using C++, but C# and Visual Basic Scripting Edition (VBScript) samples are also included.

When you install the Microsoft Windows Software Development Kit (SDK), the following samples are installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\ folder.



| Sample                                                                 | Description                                                                                                                                                                                                                                                                                                                                                | Language            |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| [createCNGCustomCMC](createcngcustomcmc.md)                           | Creates a CMC request object from an inner nested PKCS \#10 request.<br/>                                                                                                                                                                                                                                                                            | C++<br/>      |
| [enrollCommon](enrollcommon.md)                                       | Contains the following helper functions and macros used by the included samples.<br/>                                                                                                                                                                                                                                                                | C++<br/>      |
| [enrollCustomCMC](enrollcustomcmc.md)                                 | Creates a CMC certificate request and enrolls a computer in a certificate hierarchy.<br/>                                                                                                                                                                                                                                                            | C++<br/>      |
| [enrollCustomPKCS10](enrollcustompkcs10.md)                           | Creates a custom PKCS \#10 request, submits it to a stand-alone [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA), and installs the issued certificate in the [*certificate store*](/windows/desktop/SecGloss/c-gly).<br/> | C++<br/>      |
| [enrollCustomPKCS10\_2](enrollcustompkcs10-2.md)                      | Creates a custom PKCS \#10 request and attempts to enroll it in an enterprise CA.<br/>                                                                                                                                                                                                                                                               | C++<br/>      |
| [enrollEOBOCMC](enrolleobocmc.md)                                     | Creates a CMC certificate request on behalf of another user and enrolls the user in a certificate hierarchy.<br/>                                                                                                                                                                                                                                    | C++<br/>      |
| [enrollFromPublicKey](enrollfrompublickey.md)                         | Initializes a PKCS \#10 certificate request object, wraps it in a CMC request object, submits the CMC request to an enterprise CA, and saves the certificate returned by the CA in a file.<br/>                                                                                                                                                      | C++<br/>      |
| [enrollKeyArchivalCMC](enrollkeyarchivalcmc.md)                       | Creates a CMC certificate request to archive a [*private key*](/windows/desktop/SecGloss/p-gly) on a CA.<br/>                                                                                                                                                                                                     | C++<br/>      |
| [enrollNestedCMC](enrollnestedcmc.md)                                 | Reads an existing CMC certificate request from a file, wraps it in another CMC request, signs this outer request, submits it to a CA, and saves the certificate response from the CA to a file.<br/>                                                                                                                                                 | C++<br/>      |
| [enrollPKCS7](enrollpkcs7.md)                                         | Creates a [*PKCS \#7*](/windows/desktop/SecGloss/p-gly) request from an existing certificate by inheriting the public and private keys and the certificate template. The sample enrolls the user in a certificate hierarchy and installs the certificate response.<br/>                                   | C++<br/>      |
| [enrollRenewalPKCS7](enrollrenewalpkcs7.md)                           | Creates a PKCS \#7 request object to renew an existing certificate.<br/>                                                                                                                                                                                                                                                                             | C++<br/>      |
| [enrollSimpleMachineCert](enrollsimplemachinecert.md)                 | Enrolls a computer in a certificate hierarchy by using a template, a certificate display name, and the certificate description.<br/>                                                                                                                                                                                                                 | C++, VBS<br/> |
| [enrollSimpleUserCert](enrollsimpleusercert.md)                       | Enrolls an end user with a CA by using a template, the subject name, and the length, in bits, of the key.<br/>                                                                                                                                                                                                                                       | C++, C#<br/> |
| [enrollWithIX509EnrollmentHelper](enrollwithix509enrollmenthelper.md) | Demonstrates how to use the Windows 7 HTTP protocol to enroll a certificate in an enterprise CA.<br/>                                                                                                                                                                                                                                                | C#<br/>      |
| [installResponseFromPFX](installresponsefrompfx.md)                   | Installs an enrolled certificate from a Personal Information Exchange (PFX) file to the certificate store.<br/>                                                                                                                                                                                                                                      | C++<br/>      |



 

## Related topics

<dl> <dt>

[Using the Certificate Enrollment API](about-the-certificate-enrollment-api.md)
</dt> </dl>

 

