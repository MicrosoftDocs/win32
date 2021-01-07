---
description: A constructed Abstract Syntax Notation One (ASN.1) type is made up from basic types, string types, or other constructed types. For example, an X.509 certificate extension is composed from three basic ASN.1 types as shown by the following example.
ms.assetid: 90c52d71-5d5b-479c-8e29-06c9f0f6da4a
title: Constructed Types
ms.topic: article
ms.date: 05/31/2018
---

# Constructed Types

A constructed [*Abstract Syntax Notation One*](/windows/desktop/SecGloss/a-gly) (ASN.1) type is made up from basic types, string types, or other constructed types. For example, an X.509 certificate extension is composed from three basic ASN.1 types as shown by the following example.

``` syntax
Extension ::= SEQUENCE 
{
   extnId              OBJECT IDENTIFIER,
   critical            BOOLEAN DEFAULT FALSE,
   extnValue           OCTET STRING
}
```

An extension consists of an [*object identifier*](/windows/desktop/SecGloss/o-gly) (OID), a Boolean value that identifies whether the extension is critical, and a byte array that contains the value. The Certificate Enrollment API supports the following constructed ASN.1 types.

## SEQUENCE and SEQUENCE OF

Encoding tag: 0x30

Contains an ordered series of fields of one or more types. Fields can be marked**OPTIONAL** or **DEFAULT**. Also, to avoid ambiguity when decoding, successive optional fields should differ from one another by use of a unique identifier (a bracketed integer such as \[1\]) and from a following required field as shown by the following example.

``` syntax
SomeValue ::= SEQUENCE 
{
   a     INTEGER,
   b     [0] INTEGER OPTIONAL,
   c     [1] INTEGER DEFAULT 1,
   d     INTEGER
}
```

The difference between **SEQUENCE** and **SEQUENCE OF** is that the elements of a **SEQUENCE OF** construct must be of the same type. See the following example. Both constructs have the same tag value (0x30) when encoded.

``` syntax
PolicyQualifiers ::=  SEQUENCE OF PolicyQualifierInfo

PolicyQualifierInfo ::= SEQUENCE 
{
   policyQualifierId   OBJECT IDENTIFIER,
   qualifier           ANY OPTIONAL
}
```

Another way to look at the difference between **SEQUENCE** and **SEQUENCE OF** is to compare them to their counterparts in the C programming language. That is, **SEQUENCE** is roughly equivalent to a structure and **SEQUENCE OF** is roughly equivalent to an array.

## SET and SET OF

Encoding tag: 0x31

Contains an unordered series of fields of one or more types. This differs from a **SEQUENCE** which contains an ordered list. Specifying an unordered list enables an application to provide the structure fields to the encoder in the most appropriate order. As with **SEQUENCE**, the fields of a **SET** construct can be marked with **OPTIONAL** or **DEFAULT**, and unique identifiers must be used to disambiguate the decoding process. The difference between **SET** and **SET OF** is that the elements of a **SET OF** construct must be of the same type.

``` syntax
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
   type       OBJECT IDENTIFIER,
   value      ANY 
}
```

## CHOICE

Encoding tag: not applicable

Defines a choice between alternatives. Each alternative must be uniquely identified by a bracketed integer to avoid ambiguity when decoding. When encoded, the **CHOICE** construct will have the encoding tag value of the chosen alternative.

``` syntax
AltNames ::= SEQUENCE OF GeneralName

GeneralNames ::= AltNames

GeneralName ::= CHOICE 
{
   otherName               [0] IMPLICIT OtherName,
   rfc822Name              [1] IMPLICIT IA5String,
   dNSName                 [2] IMPLICIT IA5String,
   x400Address             [3] IMPLICIT SeqOfAny,
   directoryName           [4] EXPLICIT Name,
   ediPartyName            [5] IMPLICIT SEQUENCE OF ANY,
   uniformResourceLocator  [6] IMPLICIT IA5String,
   iPAddress               [7] IMPLICIT OCTET STRING,
   registeredID            [8] IMPLICIT OBJECT IDENTIFIER
}
```

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> </dl>

 

 
