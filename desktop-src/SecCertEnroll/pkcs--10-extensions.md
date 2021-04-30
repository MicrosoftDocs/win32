---
description: Extensions are included in a PKCS \#10 certificate request by adding them to the attributes field of the CertificationRequestInfo structure shown in the following ASN.1 syntax example. For more information, see the Attributes topic.
ms.assetid: 26fa8476-a0ad-4114-a1e7-ed3d4fc9d30e
title: PKCS \#10 Extensions
ms.topic: article
ms.date: 05/31/2018
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

1.  Retrieve an [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection by calling the [**X509Extension**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestpkcs10-get_x509extensions) property on the [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) object.
2.  Create an extension by using any of the available interfaces that derive from the [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) interface.
3.  Add the extensions created in step 2 to the [**IX509Extensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensions) collection retrieved in step 1.

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

 

 



