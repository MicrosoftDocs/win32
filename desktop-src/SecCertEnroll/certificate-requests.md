---
Description: 'The Certificate Enrollment SDK can be used to create PKCS \#10, PKCS \#7, CMC, and self-signed certificate requests.'
ms.assetid: '218eafb9-c9c8-49ff-8288-3909ed708ffc'
title: Certificate Requests
---

# Certificate Requests

The Certificate Enrollment SDK can be used to create PKCS \#10, PKCS \#7, CMC, and self-signed certificate requests. Each type of request is represented by one of the interfaces listed in the following table. All request interfaces inherit directly or indirectly from the [**IX509CertificateRequest**](ix509certificaterequest.md) interface. 

| Interface                                                                        | Description                                                                                                                                |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md)           | Represents a PKCS \#10 request. This interface inherits from [**IX509CertificateRequest**](ix509certificaterequest.md).                   |
| [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)             | Represents a PKCS \#7 request. This interface inherits from [**IX509CertificateRequest**](ix509certificaterequest.md).                    |
| [**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md) | Represents a self-signed certificate. This interface inherits from [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md). |
| [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)                 | Represents a CMC request. This interface inherits from [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md).               |



 

The following illustration shows the inheritance structure of the request objects supported by the Certificate Enrollment API. An [**IX509CertificateRequest**](ix509certificaterequest.md) object serves, directly or indirectly, as the base class for all of the available request objects.

![inheritance structure for the request interfaces](images/certificate-request-inheritance.png)

Regardless of type, a certificate request contains information about the subject making the request, the subject's public key, a set of attributes, a set of X.509 version 3 extensions (which may be submitted as part of the attributes), and a signature. These issues are addressed by the following topics:

-   [Subject Names](subject-names.md)
-   [Attributes](attributes.md)
-   [Extensions](extensions.md)

## Related topics

<dl> <dt>

[**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md)
</dt> <dt>

[**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)
</dt> <dt>

[**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)
</dt> <dt>

[**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md)
</dt> </dl>

 

 



