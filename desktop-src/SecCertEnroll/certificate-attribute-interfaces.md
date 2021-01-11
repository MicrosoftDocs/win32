---
description: The following interfaces can be used to create certificate attributes.
ms.assetid: 3701f9b2-0857-45f0-b3ed-4f1b3db4d6d8
title: Certificate Attribute Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Attribute Interfaces

The following interfaces can be used to create certificate attributes.



| Interface                                                                    | Description                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute)                                   | Represents a cryptographic attribute in a certificate request.                                                                              |
| [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)                                 | Manages a collection of [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) objects.                                                                 |
| [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute)                                     | Represents an attribute in a PKCS \#7, PKCS \#10, or CMC certificate request.                                                               |
| [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid)                     | Represents an attribute that can be used to identify the client that generated a certificate request.                                       |
| [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions)                 | Represents the certificate extensions in a certificate request.                                                                             |
| [**IX509AttributeArchiveKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekey)                 | Represents an attribute that contains an encrypted private key to be archived by a certification authority.                                 |
| [**IX509AttributeArchiveKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekeyhash)         | Represents an attribute that contains a SHA-1 hash of the encrypted private key to be archived by a certification authority.                |
| [**IX509AttributeCspProvider**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributecspprovider)               | Represents an attribute that identifies the cryptographic provider used by the entity requesting the certificate.                           |
| [**IX509AttributeOSVersion**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeosversion)                   | Represents an attribute that contains version information about the client operating system on which the certificate request was generated. |
| [**IX509AttributeRenewalCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributerenewalcertificate) | Represents an attribute that contains the certificate being renewed.                                                                        |
| [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes)                                   | Manages a collection of [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute) objects.                                                                   |
| [**IX509NameValuePair**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepair)                             | Represents a generic name-value pair.                                                                                                       |
| [**IX509NameValuePairs**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepairs)                           | Manages a collection of [**IX509NameValuePair**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509namevaluepair) objects.                                                           |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



