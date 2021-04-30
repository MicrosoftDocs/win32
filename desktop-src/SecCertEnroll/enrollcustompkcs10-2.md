---
description: Creates a custom PKCS \#10 request and attempts to enroll it in an enterprise certification authority (CA).
ms.assetid: ACBD3CE1-6A2A-47EE-9482-7398ABE15F5C
title: enrollCustomPKCS10_2
ms.topic: article
ms.date: 05/31/2018
---

# enrollCustomPKCS10\_2

The enrollCustomPKCS10\_2 sample creates a custom PKCS \#10 request and attempts to enroll it in an enterprise [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA).

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed by default in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollCustomPKCS10\_2 folder.

## Discussion

The enrollCustomPKCS10\_2 sample:

1.  Processes the command line arguments. The command line should contain the name of a template and the name of a cryptographic provider.
2.  Creates an [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object and initializes it by using the name of the template specified on the command line.
3.  Retrieves the [*certificate request*](/windows/desktop/SecGloss/c-gly) from the enrollment object.
4.  Retrieves the innermost PKCS\#10 request from the certificate request object obtained in step 3.
5.  Retrieves a [*private key*](/windows/desktop/SecGloss/p-gly) from the PKCS\#10 request.
6.  Creates an [**ICspInformations**](/windows/desktop/api/CertEnroll/nn-certenroll-icspinformations) collection and adds the available cryptographic providers to the collection and then retrieves an [**ICspStatus**](/windows/desktop/api/CertEnroll/nn-certenroll-icspstatus) object for the provider specified on the command line.
7.  Sets the status object on the private key.
8.  Attempts to enroll the [*certificate request*](/windows/desktop/SecGloss/c-gly).

## Related topics

<dl> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 
