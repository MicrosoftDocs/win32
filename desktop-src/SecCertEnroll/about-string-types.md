---
description: One of the most common uses of strings in a public key infrastructure (PKI) is to create an X.500 Distinguished Name.
ms.assetid: 01e8749b-a040-4267-bc12-f58f2c300337
title: String Types
ms.topic: article
ms.date: 05/31/2018
---

# String Types

One of the most common uses of strings in a public key infrastructure (PKI) is to create an X.500 Distinguished Name. For example, the subject name of a certificate request is created by combining a sequence of relative distinguished names as shown in the following syntax example.

``` syntax
---------------------------------------------------------------------
-- Breakdown of a subject name in a certificate request.
---------------------------------------------------------------------

CertificationRequestInfo ::= SEQUENCE 
{
   version                 CertificationRequestInfoVersion,
   subject                 Name,
   subjectPublicKeyInfo    SubjectPublicKeyInfo,
   attributes              [0] IMPLICIT Attributes
}

Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
   type       OBJECT IDENTIFIER,
   value      ANY 
}

DirectoryString ::= CHOICE 
{
   teletexString           TeletexString (SIZE (1..MAX)),
   printableString         PrintableString (SIZE (1..MAX)),
   universalString         UniversalString (SIZE (1..MAX)),
   utf8String              UTF8String (SIZE (1..MAX)),
   bmpString               BMPString (SIZE (1..MAX)) 
}
```

The Certificate Enrollment API supports the following ASN.1 string types.

## BMPString

Encoding tag: 0x1E

Certreq.exe name: UNICODE\_STRING

The Basic Multilingual Plane (BMP) is a character encoding that encompasses the first plane of the Universal Character Set (UCS). There are seventeen planes numbered 0 to 16. BMP occupies plane 0 and includes 65,536 code points from 0x0000 to 0xFFFF. This is the section of the Unicode character map where most of the characters assignments have so far been made. It includes Latin, Middle Eastern, Asian, African, and other languages.

## IA5String

Encoding tag: 0x16

Certreq.exe name: IA5\_STRING

The International Alphabet number 5 (IA5) is generally equivalent to the ASCII alphabet, but different versions can include accents or other characters specific to a regional language. The following example shows the **IA5String** type used in the ASN.1 definition of the **AlternativeNames** certificate extension.

``` syntax
---------------------------------------------------------------------
-- AlternativeNames extension
---------------------------------------------------------------------

AltNames ::= SEQUENCE OF GeneralName

GeneralNames ::= AltNames

GeneralName ::= CHOICE 
{
   otherName               [0] IMPLICIT OtherName,
   rfc822Name              [1] IMPLICIT IA5String,
   dNSName                 [2] IMPLICIT IA5String,
   x400Address             [3] IMPLICIT SEQUENCE OF ANY, 
   directoryName           [4] EXPLICIT ANY,    
   ediPartyName            [5] IMPLICIT SEQUENCE OF ANY,
   uniformResourceLocator  [6] IMPLICIT IA5String,
   iPAddress               [7] IMPLICIT OCTET STRING,
   registeredID            [8] IMPLICIT OBJECT IDENTIFIER
}

OtherName ::= SEQUENCE 
{
   type                    OBJECT IDENTIFIER,
   value                   [0] EXPLICIT ANY 
}
```

## PrintableString

Encoding tag: 0x13

Certreq.exe name: PRINTABLE\_STRING

The **PrintableString** data type was originally intended to represent the limited character sets available to mainframe input terminals, but it is still commonly used. It contains the following characters:

-   A-Z
-   a-z
-   0-9
-   ' ( ) + , - . / : = ? \[space\]

## TeletexString

Encoding tag: 0x14

The **TeletexString** and the related **T61String** data types are encoded on 8 bits (or 16 bits for composite characters). They both have a tag number of 0x14. They are not extensively used.

## UTF8String

Encoding tag: 0x0C

Certreq.exe name: UTF8\_STRING

The 8-bit UCS/Unicode Transformation Format (UTF-8) is a variable-length character encoding that can represent any universal character as a Unicode character while allowing initial code points to remain consistent with ASCII. UTF-8 uses one to four bytes. The tag number is 0x0C.

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



