---
description: Creates a CMC certificate request on behalf of another user and enrolls the user in a certificate hierarchy.
ms.assetid: 14cc76c9-0e2b-498f-b058-244af6e9111e
title: enrollEOBOCMC
ms.topic: article
ms.date: 05/31/2018
---

# enrollEOBOCMC

The enrollEOBOCMC sample creates a CMC certificate request on behalf of another user and enrolls the user in a certificate hierarchy. Enrollment on behalf of another user requires that the certificate request be signed by using an enrollment agent certificate.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollEOBOCMC folder.

## Discussion

The enrollEOBOCMC sample:

1.  Processes the following command line arguments:
    -   The name of a certificate template.
    -   The name of the user requesting the certificate.
    -   The name of a Personal Information Exchange (PFX) file in which to save the request.
    -   A password to use with the PFX file.
    -   An optional enrollment agent template name. The template is used to create an enrollment agent certificate if none exists in the certificate store.
2.  Creates an [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object and initializes it by using the certificate template specified on the command line.
3.  Adds the name of the requester to the CMC request object.
4.  Retrieves an existing enrollment agent certificate or, if one cannot be found, creates a certificate request from the enrollment agent template specified on the command line and attempts to enroll it.
5.  Verifies the certificate chain that contains the enrollment agent certificate.
6.  Creates an [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate) object, initializes it by using the enrollment agent certificate, retrieves the [**ISignerCertificates**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificates) collection from the CMC request object, and adds the enrollment agent signing certificate object to the collection. The [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object discussed in the next step uses the certificate to sign the CMC request.
7.  Creates an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object, initializes it by using the CMC request, attempts to enroll it, and checks the progress of the enrollment process.
8.  Exports the installed certificate to a PFX file. The file is protected by using the password specified on the command line. The EncodeToFileW function is defined in enrollCommon.cpp.
9.  Deletes the certificate from the certificate store. The functions used in the following code example can be found in the CryptoAPI documentation.
10. Deletes the private key from the computer.

## Related topics

<dl> <dt>

[CMC EOBO Request](cmc-eobo-request.md)
</dt> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



