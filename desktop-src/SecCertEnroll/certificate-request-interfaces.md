---
Description: The following interfaces can be used to create certificate requests.
ms.assetid: 6021db79-ac90-4e0c-afbd-0f926abcab78
title: Certificate Request Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Request Interfaces

The following interfaces can be used to create certificate requests.



| Interface                                                                          | Description                                                                                                                                                   |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IX509CertificateRequest**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequest?branch=master)                         | Represents the abstract top-level interface for a certificate request.                                                                                        |
| [**IX509CertificateRequestCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcertificate?branch=master)   | Enables you to create certificates directly without going through a registration or certification authority.                                                  |
| [**IX509CertificateRequestCertificate2**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestcertificate2?branch=master) | Extends the [**IX509CertificateRequestCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcertificate?branch=master) interface to enable initialization from a template.              |
| [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master)                   | Represents a CMC request.                                                                                                                                     |
| [**IX509CertificateRequestCmc2**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestcmc2?branch=master)                 | Extends the [**IX509CertificateRequestCmc**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestcmc?branch=master) interface to enable initialization from a template.                              |
| [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master)             | Represents a PKCS \#10 request.                                                                                                                               |
| [**IX509CertificateRequestPkcs10V2**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestpkcs10v2?branch=master)         | Extends the [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) interface to enable initialization from a template.                        |
| [**IX509CertificateRequestPkcs10V3**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestpkcs10v3?branch=master)         | Extends the the [**IX509CertificateRequestPkcs10**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10?branch=master) interface and adds properties that enable TPM certificate attestation. |
| [**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master)               | Represents a PKCS \#7 request.                                                                                                                                |
| [**IX509CertificateRequestPkcs7V2**](/windows/win32/Certenroll/nn-certenroll-ix509certificaterequestpkcs7v2?branch=master)           | Extends the [**IX509CertificateRequestPkcs7**](/windows/win32/CertEnroll/nn-certenroll-ix509certificaterequestpkcs7?branch=master) interface to enable initialization from a template.                          |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



