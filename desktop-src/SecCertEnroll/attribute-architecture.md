---
Description: 'Used to add attributes to a certificate request.'
ms.assetid: '7007c751-f1a4-4ddc-a66e-d3edefc6ed97'
title: Attribute Architecture
---

# Attribute Architecture

The following interfaces are used to add attributes to a certificate request:

-   [**ICryptAttribute**](icryptattribute.md)
-   [**ICryptAttributes**](icryptattributes.md)
-   [**IX509Attribute**](ix509attribute.md)
-   [**IX509Attributes**](ix509attributes.md)

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

The [**ICryptAttributes**](icryptattributes.md) collection corresponds to the **attributes** field, and each [**ICryptAttribute**](icryptattribute.md) object in the collection corresponds to an ASN.1 **Attribute** structure.

Each **Attribute** consists of an object identifier (OID) and zero or more values associated with the OID. A single OID-value pair is represented by an [**IX509Attribute**](ix509attribute.md) interface. You can use an [**IX509Attributes**](ix509attributes.md) collection to initialize an [**ICryptAttribute**](icryptattribute.md) object, but each attribute in the collection must be associated with the same OID. Typically, an attribute has only one value.

You can use any of the following interfaces, which derive from [**IX509Attribute**](ix509attribute.md), to create a single OID/value attribute pair:

-   [**IX509AttributeClientId**](ix509attributeclientid.md)
-   [**IX509AttributeExtensions**](ix509attributeextensions.md)
-   [**IX509AttributeArchiveKey**](ix509attributearchivekey.md)
-   [**IX509AttributeArchiveKeyHash**](ix509attributearchivekeyhash.md)
-   [**IX509AttributeCspProvider**](ix509attributecspprovider.md)
-   [**IX509AttributeOSVersion**](ix509attributeosversion.md)
-   [**IX509AttributeRenewalCertificate**](ix509attributerenewalcertificate.md)

For example, the following procedure shows how to create a **ClientId** attribute.

**To create a **ClientId** attribute**

1.  Retrieve an [**ICryptAttributes**](icryptattributes.md) object from an [**IX509CertificateRequestPkcs10**](ix509certificaterequestpkcs10.md) or [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object.
2.  Create and initialize an [**IX509AttributeClientId**](ix509attributeclientid.md) object.
3.  Create an [**IX509Attributes**](ix509attributes.md) collection and add the [**IX509AttributeClientId**](ix509attributeclientid.md) object.
4.  Use the [**IX509Attributes**](ix509attributes.md) collection to initialize an [**ICryptAttribute**](icryptattribute.md) object.
5.  Add the [**ICryptAttribute**](icryptattribute.md) object to the collection retrieved in step 1.

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

[**ICryptAttribute**](icryptattribute.md)
</dt> <dt>

[**ICryptAttributes**](icryptattributes.md)
</dt> <dt>

[**IX509Attribute**](ix509attribute.md)
</dt> <dt>

[**IX509Attributes**](ix509attributes.md)
</dt> </dl>

 

 



