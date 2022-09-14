---
description: The following interfaces can be used to manage certificate signatures, and public and private keys.
ms.assetid: 628d6629-3ec3-447e-8b60-a2db5b23e780
title: Certificate Signature and Key Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Signature and Key Interfaces

The following interfaces can be used to manage certificate signatures, and public and private keys.



| Interface                                                      | Description                                                                                       |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate)               | Represents a signing certificate that enables you to sign a certificate request.                  |
| [**ISignerCertificates**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificates)             | Manages a collection of [**ISignerCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-isignercertificate) objects.                 |
| [**IX509PrivateKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509privatekey)                     | Represents an asymmetric private key that can be used for encryption, signing, and key agreement. |
| [**IX509PublicKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509publickey)                       | Represents a public key in a public/private key pair.                                             |
| [**IX509SignatureInformation**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509signatureinformation) | Represents information used to sign a certificate request.                                        |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



