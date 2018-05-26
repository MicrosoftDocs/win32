---
Description: The following interfaces can be used to create certificate attributes.
ms.assetid: 3701f9b2-0857-45f0-b3ed-4f1b3db4d6d8
title: Certificate Attribute Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Certificate Attribute Interfaces

The following interfaces can be used to create certificate attributes.



| Interface                                                                    | Description                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICryptAttribute**](/windows/win32/CertEnroll/nn-certenroll-icryptattribute?branch=master)                                   | Represents a cryptographic attribute in a certificate request.                                                                              |
| [**ICryptAttributes**](/windows/win32/CertEnroll/nn-certenroll-icryptattributes?branch=master)                                 | Manages a collection of [**ICryptAttribute**](/windows/win32/CertEnroll/nn-certenroll-icryptattribute?branch=master) objects.                                                                 |
| [**IX509Attribute**](/windows/win32/CertEnroll/nn-certenroll-ix509attribute?branch=master)                                     | Represents an attribute in a PKCS \#7, PKCS \#10, or CMC certificate request.                                                               |
| [**IX509AttributeClientId**](/windows/win32/CertEnroll/nn-certenroll-ix509attributeclientid?branch=master)                     | Represents an attribute that can be used to identify the client that generated a certificate request.                                       |
| [**IX509AttributeExtensions**](/windows/win32/CertEnroll/nn-certenroll-ix509attributeextensions?branch=master)                 | Represents the certificate extensions in a certificate request.                                                                             |
| [**IX509AttributeArchiveKey**](/windows/win32/CertEnroll/nn-certenroll-ix509attributearchivekey?branch=master)                 | Represents an attribute that contains an encrypted private key to be archived by a certification authority.                                 |
| [**IX509AttributeArchiveKeyHash**](/windows/win32/CertEnroll/nn-certenroll-ix509attributearchivekeyhash?branch=master)         | Represents an attribute that contains a SHA-1 hash of the encrypted private key to be archived by a certification authority.                |
| [**IX509AttributeCspProvider**](/windows/win32/CertEnroll/nn-certenroll-ix509attributecspprovider?branch=master)               | Represents an attribute that identifies the cryptographic provider used by the entity requesting the certificate.                           |
| [**IX509AttributeOSVersion**](/windows/win32/CertEnroll/nn-certenroll-ix509attributeosversion?branch=master)                   | Represents an attribute that contains version information about the client operating system on which the certificate request was generated. |
| [**IX509AttributeRenewalCertificate**](/windows/win32/CertEnroll/nn-certenroll-ix509attributerenewalcertificate?branch=master) | Represents an attribute that contains the certificate being renewed.                                                                        |
| [**IX509Attributes**](/windows/win32/CertEnroll/nn-certenroll-ix509attributes?branch=master)                                   | Manages a collection of [**IX509Attribute**](/windows/win32/CertEnroll/nn-certenroll-ix509attribute?branch=master) objects.                                                                   |
| [**IX509NameValuePair**](/windows/win32/CertEnroll/nn-certenroll-ix509namevaluepair?branch=master)                             | Represents a generic name-value pair.                                                                                                       |
| [**IX509NameValuePairs**](/windows/win32/CertEnroll/nn-certenroll-ix509namevaluepairs?branch=master)                           | Manages a collection of [**IX509NameValuePair**](/windows/win32/CertEnroll/nn-certenroll-ix509namevaluepair?branch=master) objects.                                                           |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



