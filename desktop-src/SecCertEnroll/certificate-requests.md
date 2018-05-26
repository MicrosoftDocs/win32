---
Description: The Certificate Enrollment SDK can be used to create PKCS \#10, PKCS \#7, CMC, and self-signed certificate requests.
ms.assetid: 218eafb9-c9c8-49ff-8288-3909ed708ffc
title: Certificate Requests
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Requests

The Certificate Enrollment SDK can be used to create PKCS \#10, PKCS \#7, CMC, and self-signed certificate requests. Each type of request is represented by one of the interfaces listed in the following table. All request interfaces inherit directly or indirectly from the [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) interface. 

| Interface                                                                        | Description                                                                                                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master)           | Represents a PKCS \#10 request. This interface inherits from [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master).                   |
| [**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master)             | Represents a PKCS \#7 request. This interface inherits from [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master).                    |
| [**IX509CertificateRequestCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcertificate?branch=master) | Represents a self-signed certificate. This interface inherits from [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master). |
| [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master)                 | Represents a CMC request. This interface inherits from [**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master).               |



 

The following illustration shows the inheritance structure of the request objects supported by the Certificate Enrollment API. An [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master) object serves, directly or indirectly, as the base class for all of the available request objects.

![inheritance structure for the request interfaces](images/certificate-request-inheritance.png)

Regardless of type, a certificate request contains information about the subject making the request, the subject's public key, a set of attributes, a set of X.509 version 3 extensions (which may be submitted as part of the attributes), and a signature. These issues are addressed by the following topics:

-   [Subject Names](subject-names.md)
-   [Attributes](attributes.md)
-   [Extensions](extensions.md)

## Related topics

<dl> <dt>

[**IX509CertificateRequestCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcertificate?branch=master)
</dt> <dt>

[**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master)
</dt> <dt>

[**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master)
</dt> <dt>

[**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master)
</dt> </dl>

 

 



