---
description: Creates a PKCS \#7 request from an existing certificate by inheriting the public and private keys and the certificate template.
ms.assetid: e7df1a2e-5674-4cc6-874b-45bcc7e25127
title: enrollPKCS7
ms.topic: article
ms.date: 05/31/2018
---

# enrollPKCS7

The enrollPKCS7 sample creates a PKCS \#7 request from an existing certificate by inheriting the public and private keys and the certificate template. The existing certificate is used to sign the request. This sample enrolls the user in a certificate hierarchy and installs the certificate response. The sample uses an existing certificate to enroll and install a new one. For more information about renewing an existing certificate, see [enrollRenewalPKCS7](enrollrenewalpkcs7.md).

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollPKCS7 folder.

## Discussion

The enrollPKCS7 sample:

1.  Processes the command line arguments. The command line should contain the name of the certificate template used to find an existing certificate.
2.  Retrieves an existing certificate by using the name of the template specified on the command line or, if a certificate cannot be found, attempts to enroll a new one created by using the template. The findCertByTemplate and enrollCertByTemplate functions are defined in enrollCommon.cpp.
3.  Verifies the certificate chain and converts the certificate to a **BSTR**.
4.  Creates an [**IX509CertificateRequestPkcs7**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7) object and initializes it by using the existing certificate. The new PKCS \#7 request object inherits the private and public keys and template from the existing certificate.
5.  Creates an [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate) object, initializes it by using the existing certificate, and adds it to the PKCS \#7 request object.
6.  Creates an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object, initializes it by using the PKCS \#7 request object, attempts to enroll it with the CA and monitors the status of the enrollment process. The checkEnrollStatus function is defined in enrollCommon.cpp.

## Related topics

<dl> <dt>

[CMC Request](cmc-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



