---
description: Used to add attributes to a certificate request.
ms.assetid: 7007c751-f1a4-4ddc-a66e-d3edefc6ed97
title: Attribute Architecture
ms.topic: article
ms.date: 05/31/2018
---

# Attribute Architecture

The following interfaces are used to add attributes to a certificate request:

-   [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute)
-   [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)
-   [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute)
-   [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes)

The architecture follows that defined in the ASN.1 module of the PKCS \#10 certification request syntax.

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

The [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) collection corresponds to the **attributes** field, and each [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object in the collection corresponds to an ASN.1 **Attribute** structure.

Each **Attribute** consists of an object identifier (OID) and zero or more values associated with the OID. A single OID-value pair is represented by an [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute) interface. You can use an [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection to initialize an [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object, but each attribute in the collection must be associated with the same OID. Typically, an attribute has only one value.

You can use any of the following interfaces, which derive from [**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute), to create a single OID/value attribute pair:

-   [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid)
-   [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions)
-   [**IX509AttributeArchiveKey**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekey)
-   [**IX509AttributeArchiveKeyHash**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributearchivekeyhash)
-   [**IX509AttributeCspProvider**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributecspprovider)
-   [**IX509AttributeOSVersion**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeosversion)
-   [**IX509AttributeRenewalCertificate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributerenewalcertificate)

For example, the following procedure shows how to create a **ClientId** attribute.

**To create a **ClientId** attribute**

1.  Retrieve an [**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes) object from an [**IX509CertificateRequestPkcs10**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestpkcs10) or [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) object.
2.  Create and initialize an [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid) object.
3.  Create an [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection and add the [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid) object.
4.  Use the [**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes) collection to initialize an [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object.
5.  Add the [**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute) object to the collection retrieved in step 1.

The following example shows the ASN.1 output of the **ClientId** attribute. The attribute contains the DNS name of the computer on which the request was generated (test3d.jdomcsc.nttest.microsoft.com), the SAM name of the user (JDOMCSC\\administrator), and the name of the application that generated the request (certreq).

``` syntax
0136: 30 57; SEQUENCE (57 Bytes)
0138: |  06 09                            ; OBJECT_ID (9 Bytes)
013a: |  |  2b 06 01 04 01 82 37 15  14
      |  |     ; 1.3.6.1.4.1.311.21.20 Client Information
0143: |  |  31 4a                         ; SET (4a Bytes)
0145: |  |     30 48                      ; SEQUENCE (48 Bytes)
0147: |  |        02 01                   ; INTEGER (1 Bytes)
0149: |  |        |  09
014a: |  |        0c 23                   ; UTF8_STRING (23 Bytes)
014c: |  |        |  74 65 73 74 33 64 2e 6a  64 6f 6d 63 73 63 2e 6e 
015c: |  |        |  74 74 65 73 74 2e 6d 69  63 72 6f 73 6f 66 74 2e 
016c: |  |        |  63 6f 6d                                         
      |  |        |     ; "test3d.jdomcsc.nttest.microsoft.com"
016f: |  |        0c 15                   ; UTF8_STRING (15 Bytes)
0171: |  |        |  4a 44 4f 4d 43 53 43 5c  61 64 6d 69 6e 69 73 74 
0181: |  |        |  72 61 74 6f 72                                   
      |  |        |     ; "JDOMCSC\administrator"
0186: |  |        0c 07                   ; UTF8_STRING (7 Bytes)
0188: |  |           63 65 72 74 72 65 71                             
      |  |              ; "certreq"
```

## Related topics

<dl> <dt>

[**ICryptAttribute**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattribute)
</dt> <dt>

[**ICryptAttributes**](/windows/desktop/api/CertEnroll/nn-certenroll-icryptattributes)
</dt> <dt>

[**IX509Attribute**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attribute)
</dt> <dt>

[**IX509Attributes**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributes)
</dt> </dl>

 

 



