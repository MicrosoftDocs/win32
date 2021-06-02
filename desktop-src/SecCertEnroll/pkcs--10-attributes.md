---
description: Attributes are included in a PKCS \#10 certificate request by adding them to the CertificationRequestInfo structure shown in the following ASN.1 syntax example.
ms.assetid: 5f00f638-9edb-474b-a7e4-f6f7b62c89a4
title: PKCS \#10 Attributes
ms.topic: article
ms.date: 05/31/2018
---

# PKCS \#10 Attributes

Attributes are included in a PKCS \#10 certificate request by adding them to the **CertificationRequestInfo** structure shown in the following ASN.1 syntax example. For more information about how you can add attributes to a request, see the [Attribute Architecture](attribute-architecture.md) topic.

``` syntax
CertificationRequestInfo ::= SEQUENCE 
{
   version                 CertificationRequestInfoVersion,
   subject                 ANY,
   subjectPublicKeyInfo    SubjectPublicKeyInfo,
   attributes              [0] IMPLICIT Attributes
}

Attributes ::= SET OF Attribute

Attribute ::= SEQUENCE 
{
   type       EncodedObjectID,
   values     AttributeSetValue
}
```

The attribute most commonly added to a PKCS \#10 request is a collection of version 3 extensions defined by an [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions) object. Because a PKCS \#10 request does not contain a field to which the extensions can be directly added, they must be added as an attribute. The **ClientId**, **CspProvider**, **OSVersion**, and **RenewalCertificate** attributes can also be added to a PKCS ) topic.

## Related topics

<dl> <dt>

[Supported Attributes](supported-attributes.md)
</dt> </dl>

 

 



