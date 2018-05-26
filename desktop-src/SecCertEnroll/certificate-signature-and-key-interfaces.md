---
Description: The following interfaces can be used to manage certificate signatures, and public and private keys.
ms.assetid: 628d6629-3ec3-447e-8b60-a2db5b23e780
title: Certificate Signature and Key Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Signature and Key Interfaces

The following interfaces can be used to manage certificate signatures, and public and private keys.



| Interface                                                      | Description                                                                                       |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**ISignerCertificate**](/windows/win32/CertEnroll/nn-certenroll-isignercertificate?branch=master)               | Represents a signing certificate that enables you to sign a certificate request.                  |
| [**ISignerCertificates**](/windows/win32/CertEnroll/nn-certenroll-isignercertificates?branch=master)             | Manages a collection of [**ISignerCertificate**](/windows/win32/CertEnroll/nn-certenroll-isignercertificate?branch=master) objects.                 |
| [**IX509PrivateKey**](/windows/win32/CertEnroll/nn-certenroll-ix509privatekey?branch=master)                     | Represents an asymmetric private key that can be used for encryption, signing, and key agreement. |
| [**IX509PublicKey**](/windows/win32/CertEnroll/nn-certenroll-ix509publickey?branch=master)                       | Represents a public key in a public/private key pair.                                             |
| [**IX509SignatureInformation**](/windows/win32/CertEnroll/nn-certenroll-ix509signatureinformation?branch=master) | Represents information used to sign a certificate request.                                        |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



