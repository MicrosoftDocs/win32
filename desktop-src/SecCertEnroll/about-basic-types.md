---
description: The Certificate Enrollment API supports the following basic ASN.1 types.
ms.assetid: ca247945-ebcf-492e-9cc8-a67a9454fa95
title: Basic Types
ms.topic: article
ms.date: 05/31/2018
---

# Basic Types

The Certificate Enrollment API supports the following basic ASN.1 types.

## BIT STRING

Encoding tag: 0x03

Certreq.exe name: BIT\_STRING

A bit or binary string is an arbitrarily long array of bits. Specific bits can be identified by parenthesized integers and assigned names as in the following example.

``` syntax
Versions ::= BIT STRING{ version-1(0), version-2(1) } 
```

Certificate keys and signatures are often represented as bit strings.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: BIT STRING
-- Tag number: 0x03
---------------------------------------------------------------------
SubjectPublicKeyInfo ::= SEQUENCE 
{
  algorithm           AlgorithmIdentifier,
  subjectPublicKey    BIT STRING
} 
```

## BOOLEAN

Encoding tag: 0x01

Certreq.exe name: BOOLEAN

A Boolean type can contain one of two values, **TRUE** or **FALSE**. The following example shows the ASN.1 structure for a Basic Constraints certificate extension. The **cA** field specifies whether a certificate subject is a certification authority (CA). The default criticality is **FALSE**.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: BOOLEAN
-- Tag number: 0x01
---------------------------------------------------------------------
BasicConstraints ::= SEQUENCE 
{
  cA                  BOOLEAN DEFAULT FALSE,
  pathLenConstraint   INTEGER OPTIONAL
}
```

## INTEGER

Encoding tag: 0x02

Certreq.exe name: INTEGER

An integer can typically be any positive or negative integral value. The following example shows the ASN.1 structure for an RSA public key. Note that the **publicExponent** field is restricted to a positive integer less than 4,294,967,296.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: INTEGER
-- Tag number: 0x02
---------------------------------------------------------------------
HUGEINTEGER ::= INTEGER

RSAPublicKey ::= SEQUENCE 
{ 
  modulus         HUGEINTEGER,    
  publicExponent  INTEGER (0..4294967295) 
} 
```

## NULL

Encoding tag: 0x05

Certreq.exe name: **NULL**

A **NULL** type contains a single byte 0x00. It can be used anywhere that the certificate request must indicate an empty value. For example, an **AlgorithmIdentifier** is a sequence that contains an object identifier (OID) and optional parameters.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: NULL
-- Tag number: 0x05
---------------------------------------------------------------------
AlgorithmIdentifier ::= SEQUENCE 
{
  algorithm           OBJECT IDENTIFIER,
  parameters          ANY OPTIONAL    
}
```

If there are no parameters when the structure is encoded, **NULL** is used to indicate an empty value.

``` syntax
30 0d            ; SEQUENCE (d Bytes)
|  |  |  06 09          ; OBJECT_ID (9 Bytes)
|  |  |  |  2a 86 48 86 f7 0d 01 01  01
|  |  |  |     ; 1.2.840.113549.1.1.1 RSA (RSA_SIGN)
|  |  |  05 00          ; NULL (0 Bytes)
```

## OBJECT IDENTIFIER

Encoding tag: 0x06

Certreq.exe name: OBJECT\_ID

The Certificate Enrollment API uses object identifiers (OIDs) as a type of universal pointer to algorithm identifiers, attributes, and other PKI elements. OIDs are typically presented in a dotted decimal string such as "2.16.840.1.101.3.4.1.42". The individual elements in the string, separated by periods, represent the arcs and leaves in a registration authority tree that uniquely identifies the object and the organization that registered it. For example, the preceding OID can be expanded to joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithms(4) aesAlgs(1) with .42 appended to uniquely identify the 256-bit AES cipher block chaining (CBC) mode algorithm.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: OBJECT IDENTIFIER
-- Tag number: 0x06
---------------------------------------------------------------------
AlgorithmIdentifier ::= SEQUENCE 
{
  algorithm           OBJECT IDENTIFIER,
  parameters          ANY OPTIONAL    
}
```

## OCTET STRING

Encoding tag: 0x04

Certreq.exe name: OCTET\_STRING

An octet string is an arbitrarily large byte array. Unlike the **BIT STRING** type, however, specific bits and bytes in the string cannot be assigned names. The word octet is meant to be a platform independent way to refer to a memory word. Within the context of the Certificate Enrollment API, octet and byte are interchangeable.

``` syntax
---------------------------------------------------------------------
-- ASN.1 type example: OCTET STRING
-- Tag number: 0x04
---------------------------------------------------------------------
AuthorityKeyId ::= SEQUENCE 
{
  keyIdentifier       [0] IMPLICIT OCTET STRING OPTIONAL,
  certIssuer          [1] EXPLICIT NAME
  certSerialNumber    [2] IMPLICIT INTEGER OPTIONAL
}
```

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



