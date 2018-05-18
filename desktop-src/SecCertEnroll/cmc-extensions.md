---
Description: 'Extensions are included in a CMC request by adding them to the TaggedAttributes structure shown in the following ASN.1 syntax example. For more information, see the Attributes topic.'
ms.assetid: '3aa9175b-f889-4d5d-8eb2-a8a42f9fe750'
title: CMC Extensions
---

# CMC Extensions

Extensions are included in a CMC request by adding them to the **TaggedAttributes** structure shown in the following ASN.1 syntax example. For more information, see the [Attributes](attributes.md) topic.

``` syntax
CmcData ::= SEQUENCE 
{
   controlSequence         ControlSequence,
   reqSequence             ReqSequence,
   cmsSequence             CmsSequence,
   otherMsgSequence        OtherMsgSequence
}


ControlSequence  ::=    SEQUENCE OF TaggedAttribute

TaggedAttribute ::= SEQUENCE 
{
   bodyPartID              BodyPartID,
   type                    EncodedObjectID,
   values                  AttributeSetValue
}

BodyPartID ::= INTEGER (0..4294967295)
EncodedObjectID ::= OBJECT IDENTIFIER
AttributeSetValue ::= SET OF ANY
```

Each structure in the **TaggedAttributes** collection contains an integer ID, an ASN.1 object identifier (OID), and a set of values. Extensions are incorporated into a request by adding a **CmcAddExtensions** structure to the **values** field. The ASN.1 structure syntax is shown in the following example. The object identifier is **XCN\_OID\_CMC\_ADD\_EXTENSIONS** (1.3.6.1.5.5.7.7.8).

``` syntax
CmcAddExtensions ::= SEQUENCE 
{
   pkiDataReference        BodyPartID,
   certReferences          BodyPartIDSequence,
   extensions              Extensions
}

Extensions ::= SEQUENCE OF Extension

Extension ::= SEQUENCE 
{
   extnId              EncodedObjectID,
   critical            BOOLEAN DEFAULT FALSE,
   extnValue           OCTETSTRING
}
```

The following procedure discusses how to use the Certificate Enrollment API to add extensions to a CMC certificate request.

**To use the Certificate Enrollment API to add extensions to a CMC certificate request**

1.  Create an extension by using any of the available interfaces that derive from the [**IX509Extension**](ix509extension.md) interface or use the **IX509Extension** object directly to create custom extensions.
2.  Call the [**X509Extensions**](ix509certificaterequestcmc-x509extensions-property.md) property on the [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object to retrieve an [**IX509Extensions**](ix509extensions.md) collection.
3.  Add the extensions created in step 1 to the [**IX509Extensions**](ix509extensions.md) collection.
4.  Call [**Enroll**](ix509enrollment-enroll-method.md) to automatically perform the following actions:
    -   Retrieve an [**ICryptAttributes**](icryptattributes.md) object from the [**IX509CertificateRequestCmc**](ix509certificaterequestcmc.md) object.
    -   Create and initialize an [**IX509AttributeExtensions**](ix509attributeextensions.md) object by using the [**IX509Extensions**](ix509extensions.md) collection retrieved in step 2.
    -   Create an [**IX509Attributes**](ix509attributes.md) collection and add the [**IX509AttributeExtensions**](ix509attributeextensions.md) object to it.
    -   Use the [**IX509Attributes**](ix509attributes.md) collection to initialize an [**ICryptAttribute**](icryptattribute.md) object.
    -   Add the [**ICryptAttribute**](icryptattribute.md) object to the [**ICryptAttributes**](icryptattributes.md) collection.

## Related topics

<dl> <dt>

[Attributes](attributes.md)
</dt> <dt>

[Attribute Architecture](attribute-architecture.md)
</dt> <dt>

[CMC Attributes](cmc-attributes.md)
</dt> <dt>

[Extensions](extensions.md)
</dt> </dl>

 

 



