---
Description: 'Creates a custom PKCS \#10 request and attempts to enroll it in an enterprise certification authority (CA).'
ms.assetid: 'ACBD3CE1-6A2A-47EE-9482-7398ABE15F5C'
title: 'enrollCustomPKCS10\_2'
---

# enrollCustomPKCS10\_2

The enrollCustomPKCS10\_2 sample creates a custom PKCS \#10 request and attempts to enroll it in an enterprise [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA).

## Location

When you install the Microsoft Windows Software Development Kit (SDK), the sample is installed by default in the *%ProgramFiles%*\\Microsoft SDKs\\Windows\\v7.0\\Samples\\Security\\X509 Certificate Enrollment\\VC\\enrollCustomPKCS10\_2 folder.

## Discussion

The enrollCustomPKCS10\_2 sample:

1.  Processes the command line arguments. The command line should contain the name of a template and the name of a cryptographic provider.
2.  Creates an [**IX509Enrollment**](ix509enrollment.md) object and initializes it by using the name of the template specified on the command line.
3.  Retrieves the [*certificate request*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-request-gly) from the enrollment object.
4.  Retrieves the innermost PKCS\#10 request from the certificate request object obtained in step 3.
5.  Retrieves a [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly) from the PKCS\#10 request.
6.  Creates an [**ICspInformations**](icspinformations.md) collection and adds the available cryptographic providers to the collection and then retrieves an [**ICspStatus**](icspstatus.md) object for the provider specified on the command line.
7.  Sets the status object on the private key.
8.  Attempts to enroll the [*certificate request*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-request-gly).

## Related topics

<dl> <dt>

[PKCS \#10 Request](pkcs--10-request.md)
</dt> <dt>

[Using the Included Samples](using-the-included-samples.md)
</dt> </dl>

 

 



