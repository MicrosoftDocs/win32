---
description: The Certificate Enrollment API uses Abstract Syntax Notation One (ASN.1) to define, encode, and decode the certificate requests and certificates that it transfers between client computers and certification authorities.
ms.assetid: 970a246f-a4c3-489b-b6a4-7d3103f388cf
title: Introduction to ASN.1 Syntax and Encoding
ms.topic: article
ms.date: 05/31/2018
---

# Introduction to ASN.1 Syntax and Encoding

The Certificate Enrollment API uses Abstract Syntax Notation One (ASN.1) to define, encode, and decode the certificate requests and certificates that it transfers between client computers and certification authorities. ASN.1 can be conceptually divided into a set of syntax rules and a set of encoding rules as shown by the following examples.

## ASN.1 Syntax Example

A certificate request contains, among other things, the name of the entity that is making the request or for which the request is being made. The name is a sequence of X.500 relative distinguished names (RDNs). Each RDN in the sequence consists of an object identifier (OID) and a value. The ASN.1 syntax for a subject name is shown in the following example.

``` syntax
---------------------------------------------------------------------
-- Subject name
---------------------------------------------------------------------
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
   type               OBJECT IDENTIFIER,
   value              ANY 
}
```

## ASN.1 Encoding Example

The Certificate Enrollment API uses [*Distinguished Encoding Rules*](/windows/desktop/SecGloss/d-gly) (DER) to encode the preceding subject name. DER requires that each item in the name be represented by a TLV triplet where T contains the tag number of the ASN.1 type, L contains the length, and V contains the associated value. The following example shows how the subject name TestCN.TestOrg is encoded.

``` syntax
1.     30 23            ; SEQUENCE (0x23 = 35 Bytes)
2.     |  |  31 0f            ; SET (f Bytes)
3.     |  |  |  30 0d            ; SEQUENCE (d Bytes)
4.     |  |  |     06 03         ; OBJECT_ID (3 Bytes)
5.     |  |  |     |  55 04 03
6.     |  |  |     |     ; 2.5.4.3 Common Name (CN)
7.     |  |  |     13 06         ; PRINTABLE_STRING (6 Bytes)
8.     |  |  |        54 65 73 74 43 4e                    ; TestCN
9.     |  |  |           ; "TestCN"
10.    |  |  31 10            ; SET (10 Bytes)
11.    |  |     30 0e            ; SEQUENCE (e Bytes)
12.    |  |        06 03         ; OBJECT_ID (3 Bytes)
13.    |  |        |  55 04 0a
14.    |  |        |     ; 2.5.4.10 Organization (O)
15.    |  |        13 07         ; PRINTABLE_STRING (7 Bytes)
16.    |  |           54 65 73 74 4f 72 67                 ; TestOrg
17.    |  |              ; "TestOrg"
```

Note the following points:

-   Line 1:<dl> The name is a sequence of relative distinguished names.  
    The tag number for the **SEQUENCE** type is 0x30.  
    The subject name of TestCN.TestOrg requires 35 (0x23) bytes.  
    </dl>
-   Line 2:<dl> The Common Name, TestCN, is a single set of **AttributeTypeValue** structures.  
    The tag number for a **SET** is 0x31.  
    </dl>
-   Line 3:<dl> The **AttributeTypeValue** structure is a sequence.  
    The tag number for the **SEQUENCE** type is 0x30.  
    The structure requires 13 (0xD) bytes.  
    </dl>
-   Lines 4 to 6:<dl> The object identifier (OID) for the Common Name is 2.5.4.3.  
    The OID is a three byte **OBJECT\_ID** type.  
    The tag number for the **OBJECT\_ID** type is 0x06.  
    </dl>
-   Lines 7 to 9:<dl> The Common Name, TestCN, is a string value.  
    The string is a six byte **PRINTABLE\_STRING** type.  
    The tag number for the **PRINTABLE\_STRING** type is 0x13.  
    </dl>

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[Certificate Request Encoding](about-certificate-request-encoding.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> </dl>

 

 
