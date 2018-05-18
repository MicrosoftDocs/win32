---
Description: 'The following interfaces can be used to create certificate attributes.'
ms.assetid: '3701f9b2-0857-45f0-b3ed-4f1b3db4d6d8'
title: Certificate Attribute Interfaces
---

# Certificate Attribute Interfaces

The following interfaces can be used to create certificate attributes.



| Interface                                                                    | Description                                                                                                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICryptAttribute**](icryptattribute.md)                                   | Represents a cryptographic attribute in a certificate request.                                                                              |
| [**ICryptAttributes**](icryptattributes.md)                                 | Manages a collection of [**ICryptAttribute**](icryptattribute.md) objects.                                                                 |
| [**IX509Attribute**](ix509attribute.md)                                     | Represents an attribute in a PKCS \#7, PKCS \#10, or CMC certificate request.                                                               |
| [**IX509AttributeClientId**](ix509attributeclientid.md)                     | Represents an attribute that can be used to identify the client that generated a certificate request.                                       |
| [**IX509AttributeExtensions**](ix509attributeextensions.md)                 | Represents the certificate extensions in a certificate request.                                                                             |
| [**IX509AttributeArchiveKey**](ix509attributearchivekey.md)                 | Represents an attribute that contains an encrypted private key to be archived by a certification authority.                                 |
| [**IX509AttributeArchiveKeyHash**](ix509attributearchivekeyhash.md)         | Represents an attribute that contains a SHA-1 hash of the encrypted private key to be archived by a certification authority.                |
| [**IX509AttributeCspProvider**](ix509attributecspprovider.md)               | Represents an attribute that identifies the cryptographic provider used by the entity requesting the certificate.                           |
| [**IX509AttributeOSVersion**](ix509attributeosversion.md)                   | Represents an attribute that contains version information about the client operating system on which the certificate request was generated. |
| [**IX509AttributeRenewalCertificate**](ix509attributerenewalcertificate.md) | Represents an attribute that contains the certificate being renewed.                                                                        |
| [**IX509Attributes**](ix509attributes.md)                                   | Manages a collection of [**IX509Attribute**](ix509attribute.md) objects.                                                                   |
| [**IX509NameValuePair**](ix509namevaluepair.md)                             | Represents a generic name-value pair.                                                                                                       |
| [**IX509NameValuePairs**](ix509namevaluepairs.md)                           | Manages a collection of [**IX509NameValuePair**](ix509namevaluepair.md) objects.                                                           |



 

## Related topics

<dl> <dt>

[CertEnroll Interfaces](certenroll-interfaces.md)
</dt> </dl>

 

 



