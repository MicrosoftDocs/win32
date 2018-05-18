---
Description: 'The following interfaces can be used to create certificate requests.'
ms.assetid: '6021db79-ac90-4e0c-afbd-0f926abcab78'
title: Certificate Request Interfaces
---

# Certificate Request Interfaces

The following interfaces can be used to create certificate requests.



| Interface                                                                          | Description                                                                                                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequest**](ix509certificaterequest.md)                         | Represents the abstract top-level interface for a certificate request.                                                                                        |
| [**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md)   | Enables you to create certificates directly without going through a registration or certification authority.                                                  |
| [**IX509CertificateRequestCertificate2**](ix509certificaterequestcertificate2.md) | Extends the [**IX509CertificateRequestCertificate**](ix509certificaterequestcertificate.md) interface to enable initialization from a template.              |
| [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md)                   | Represents a CMC request.                                                                                                                                     |
| [**IX509CertificateRequestCmc2**](ix509certificaterequestcmc2.md)                 | Extends the [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) interface to enable initialization from a template.                              |
| [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md)             | Represents a PKCS \#10 request.                                                                                                                               |
| [**IX509CertificateRequestPkcs10V2**](ix509certificaterequestpkcs10v2.md)         | Extends the [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) interface to enable initialization from a template.                        |
| [**IX509CertificateRequestPkcs10V3**](ix509certificaterequestpkcs10v3.md)         | Extends the the [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) interface and adds properties that enable TPM certificate attestation. |
| [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md)               | Represents a PKCS \#7 request.                                                                                                                                |
| [**IX509CertificateRequestPkcs7V2**](ix509certificaterequestpkcs7v2.md)           | Extends the [**IX509CertificateRequestPkcs7**](ix509certificaterequestpkcs7.md) interface to enable initialization from a template.                          |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



