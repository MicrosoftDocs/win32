---
description: Creates a custom PKCS \#10 request, submits it to a stand-alone certification authority (CA), and installs the issued certificate in the certificate store.
ms.assetid: dcb69d7e-457e-457b-9eea-15676ed710aa
title: enrollCustomPKCS10
ms.topic: article
ms.date: 05/31/2018
---

# enrollCustomPKCS10

The enrollCustomPKCS10 sample creates a custom PKCS \#10 request, submits it to a stand-alone certification authority (CA), and installs the issued certificate in the certificate store. A stand-alone CA does not require Active Directory and does not use templates.

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed, by default, in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollCustomPKCS10 folder.

## Discussion

The enrollCustomPKCS10 sample:

1.  Processes the command line arguments. The command line should contain the X.500 certificate subject name, the email (RFC822) name, and an Enhanced Key Usage (EKU) object identifier (OID). For example, you can specify the following arguments to enroll *user1@example.com*:
    -   Subject name: "*CN=user1,DC=example,DC=com*"
    -   RFC822 name: *user1@example.com*
    -   Client authentication EKU OID: 1.3.6.1.5.5.7.3.2
2.  Creates an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object and initializes it for the end user by specifying the **ContextUser** value of the [**X509CertificateEnrollmentContext**](/windows/desktop/api/CertEnroll/ne-certenroll-x509certificateenrollmentcontext) enumeration.
3.  Creates an [**IX500DistinguishedName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix500distinguishedname) object, uses the object to encode the subject name to a byte array, and adds the array to the PKCS \#10 request object.
4.  Creates an [**IObjectId**](/windows/desktop/api/CertEnroll/nn-certenroll-iobjectid) object, initializes it by using the EKU object identifier (OID) specified on the command line, creates an [**IObjectIds**](/windows/desktop/api/CertEnroll/nn-certenroll-iobjectids) collection, adds the new **IObjectId** (EKU) object to the collection, uses the collection to initialize an [**IX509ExtensionEnhancedKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage) object and adds this object to the request.
5.  Creates an [**IAlternativeName**](/windows/desktop/api/CertEnroll/nn-certenroll-ialternativename) object, initializes it by using the RFC822 name specified on the command line, Creates an [**IAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ialternativenames) collection, adds the new **IAlternativeName** (RFC822 name ) object to the collection, creates an [**IX509ExtensionAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionalternativenames) object and adds this object to the request.
6.  Creates an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object, initializes it by using the [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object, and retrieves a string that contains a base64-encoded request.
7.  Creates an [**ICertConfig**](/windows/desktop/api/certcli/nn-certcli-icertconfig) object and uses it to retrieve a string that contains the CA configuration.
8.  Creates a CryptoAPI [**ICertRequest2**](/windows/desktop/api/certcli/nn-certcli-icertrequest2) object and uses it plus the strings that contain the CA configuration and the certificate request to submit the request to the CA.
9.  Checks the submission status and, if enrollment is successful, installs the certificate to the certificate store.

## Related topics

<dl> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 
