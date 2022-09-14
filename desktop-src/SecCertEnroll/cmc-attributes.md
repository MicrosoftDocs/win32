---
description: In practice, the structure of a CMC request, shown by the following syntax, is relatively complex because it often contains nested requests.
ms.assetid: faeee338-bce4-4b35-9be9-72a6568fa259
title: CMC Attributes
ms.topic: article
ms.date: 05/31/2018
---

# CMC Attributes

In practice, the structure of a CMC request, shown by the following syntax, is relatively complex because it often contains nested requests. For example, a CMC request can contain zero or one PKCS \#10 requests in a **TaggedRequest** sequence, and it can contain zero or one PKCS \#7 messages in a **TaggedContentInfo** sequence. Each nested PKCS \#7 message can contain a CMC request which can, in turn, contain more requests. The number of nesting levels is theoretically unlimited, but the certification authority (CA) is typically configured to limit the size of a request. Attributes can be applied to the top level request or to the nested requests. This is discussed in the following sections.

## CMCData Structure

A CMC request contains sequences of **TaggedAttribute**, **TaggedRequest**, and **TaggedContentInfo** ASN.1 structures.

``` syntax
CmcData ::= SEQUENCE 
{
   controlSequence         ControlSequence,
   reqSequence             ReqSequence,
   cmsSequence             CmsSequence,
   otherMsgSequence        OtherMsgSequence
}


ControlSequence  ::=    SEQUENCE OF TaggedAttribute
ReqSequence      ::=    SEQUENCE OF TaggedRequest
CmsSequence      ::=    SEQUENCE OF TaggedContentInfo

TaggedAttribute ::= SEQUENCE 
{
   bodyPartID              BodyPartID,
   type                    EncodedObjectID,
   values                  AttributeSetValue
}

TaggedRequest ::= CHOICE 
{
   tcr                     [0] IMPLICIT TaggedCertificationRequest
}

TaggedContentInfo ::= SEQUENCE 
{
   bodyPartID              BodyPartID,
   contentInfo             ANY
}

BodyPartID ::= INTEGER (0..4294967295)
EncodedObjectID ::= OBJECT IDENTIFIER
AttributeSetValue ::= SET OF ANY
```

## TaggedAttribute Structure

Attributes are included in a CMC certificate request by adding them to the **TaggedAttribute** collection. Each structure in the collection contains an integer ID, an ASN.1 object identifier (OID), and a set of values. The possible values can be any of the following.

``` syntax
CmcAddAttributes ::= SEQUENCE 
{
   pkiDataReference        BodyPartID,
   certReferences          BodyPartIDSequence,
   attributes              Attributes
}

Attributes ::= SET OF Attribute
Attribute ::= SEQUENCE 
{
   type       EncodedObjectID,
   values     AttributeSetValue
}

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

SenderNonce ::= OCTET STRING

TransactID ::= OCTET STRING

RegInfo ::= OCTET STRING
```

## CMCAddAttributes

If the attributes in this structure apply to a nested PKCS \#10 request, the **certReferences** field will contain the **BodyPartID** that identifies the request. If the attributes apply to a nested CMC request, the **pkiDataReference** field will contain the **BodyPartID** of the request. Currently, only one of these fields can be nonzero. The attributes that can be included are listed in the [Supported Attributes](supported-attributes.md) topic.

## CmcAddExtensions

This structure can contain X.509 version 3 extensions plus extensions defined by Microsoft. This attribute is defined by using the [**IX509AttributeExtensions**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeextensions) interface. If the extensions apply to a nested PKCS \#10 request, the **certReferences** field will contain the **BodyPartID** that identifies the request. If the extensions apply to a nested CMC request, the **pkiDataReference** field will contain the **BodyPartID** of the request. Currently, only one of these fields can be nonzero.

## SenderNonce

A nonce is random or pseudo-random binary data that can be included in a certificate request and response transaction to help ensure that the response or request is not a repeat of a previous message. For more information, see the [**SenderNonce**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_sendernonce) property.

## TransactID

A round trip certificate request and response transaction can be tracked using an identifier. The client generates a transaction ID and retains it until the certificate or registration authority responds with a message that completes the transaction. The response includes the identifier. For more information, see the [**TransactionId**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_transactionid) property.

## RegInfo

This attribute can be used to contain any registration information that the client chooses to put into the CMC request. The attribute value is string that contains concatenated name-value pairs. For more information, see the [**NameValuePairs**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509certificaterequestcmc-get_namevaluepairs) property.

## Related topics

<dl> <dt>

[Supported Attributes](supported-attributes.md)
</dt> </dl>

 

 



