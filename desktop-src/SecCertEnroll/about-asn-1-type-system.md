---
Description: The concept of a data type is fundamental to the Abstract Syntax Notation One (ASN.1) standard.
ms.assetid: 85e88e0b-057b-42c7-a3c8-017a30195d1e
title: ASN.1 Type System
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ASN.1 Type System

The concept of a data type is fundamental to the Abstract Syntax Notation One (ASN.1) standard. Every field of a certificate request structure is associated with a type. Consider, for example, the PKCS \#10 ASN.1 certificate syntax shown in the following example.

## ``` syntax

## -- PKCS #10 Certificate request.

CertificationRequestInfo ::= SEQUENCE 
{
   version                 CertificationRequestInfoVersion,
   subject                 Name,
   subjectPublicKeyInfo    SubjectPublicKeyInfo,
   attributes              [0] IMPLICIT Attributes
}
## 

## -- Version number.

CertificationRequestInfoVersion ::= INTEGER
## 

## -- Subject distinguished name (DN).

Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
   type               OBJECT IDENTIFIER,
   value              ANY 
}
## 

## -- Public key information.

SubjectPublicKeyInfo ::= SEQUENCE 
{
   algorithm           AlgorithmIdentifier,
   subjectPublicKey    BITSTRING
}

AlgorithmIdentifier ::= SEQUENCE 
{
  algorithm           OBJECT IDENTIFIER,
  parameters          ANY OPTIONAL    
} 
## 

## -- Attributes.

Attributes ::= SET OF Attribute

Attribute ::= SEQUENCE 
{
   type               OBJECT IDENTIFIER,
   values             AttributeSetValue
}

AttributeSetValue ::= SET OF ANY
```

The high-level request structure, **CertificationRequestInfo**, is a type that is made up from a sequence of other types. When a type is or contains only basic types, string types, or **ANY**, it cannot be broken down further. For example, the **version** field is a **CertificationRequestInfoVersion** type which is, in turn, an **INTEGER** type, a basic ASN.1 type that is not composed from other types.

A type system enables the syntax of a request to be presented visually in a manner readily understood by developers, and it enables the request to be consistently encoded for transmission across a network. For more information about encoding, see [Distinguished Encoding Rules](distinguished-encoding-rules.md). For more information about ASN.1 types, see the following topics.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Basic Types](about-basic-types.md)</td>
<td>Discusses the following data types:
<ul>
<li><strong>BIT STRING</strong></li>
<li><strong>BOOLEAN</strong></li>
<li><strong>INTEGER</strong></li>
<li><strong>NULL</strong></li>
<li><strong>OBJECT IDENTIFIER</strong></li>
<li><strong>OCTET STRING</strong></li>
</ul></td>
</tr>
<tr class="even">
<td>[String Types](about-string-types.md)</td>
<td>Discusses the following string types:
<ul>
<li><strong>BMPString</strong></li>
<li><strong>IA5String</strong></li>
<li><strong>PrintableString</strong></li>
<li><strong>TeletexString</strong></li>
<li><strong>UTF8String</strong></li>
</ul></td>
</tr>
<tr class="odd">
<td>[Constructed Types](about-constructed-types.md)</td>
<td>Discusses ASN.1 data types that can contain basic types, string types, or other constructed types.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Certificate Request Encoding](about-certificate-request-encoding.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> <dt>

[Introduction to ASN.1 Syntax and Encoding](about-introduction-to-asn-1-syntax-and-encoding.md)
</dt> </dl>

 

 



