---
Description: 'Extensions are included in a PKCS \#10 certificate request by adding them to the attributes field of the CertificationRequestInfo structure shown in the following ASN.1 syntax example. For more information, see the Attributes topic.'
ms.assetid: '26fa8476-a0ad-4114-a1e7-ed3d4fc9d30e'
title: 'PKCS \#10 Extensions'
---

# PKCS \#10 Extensions

Extensions are included in a PKCS \#10 certificate request by adding them to the **attributes** field of the **CertificationRequestInfo** structure shown in the following ASN.1 syntax example. For more information, see the [Attributes](attributes.md) topic.

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

The following procedure discusses how to use the Certificate Enrollment API to add extensions to a PKCS \#10 certificate request:

1.  Retrieve an [**IX509Extensions**](ix509extensions.md) collection by calling the [**X509Extension**](ix509certificaterequestpkcs10-x509extensions-property.md) property on the [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) object.
2.  Create an extension by using any of the available interfaces that derive from the [**IX509Extension**](ix509extension.md) interface.
3.  Add the extensions created in step 2 to the [**IX509Extensions**](ix509extensions.md) collection retrieved in step 1.

## Related topics

<dl> <dt>

[Attributes](attributes.md)
</dt> <dt>

[Attribute Architecture](attribute-architecture.md)
</dt> <dt>

[PKCS \#10 Attributes](pkcs--10-attributes.md)
</dt> <dt>

[Extensions](extensions.md)
</dt> </dl>

 

 



