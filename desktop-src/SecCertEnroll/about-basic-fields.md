---
description: An X.509 version 1 certificate contains the following fields. Version 2 fields are discussed in Version 2 Fields. Version 3 fields are discussed in Version 3 Extensions.
ms.assetid: d614130c-cf1b-4580-8903-064982ed738e
title: Basic Fields
ms.topic: article
ms.date: 05/31/2018
---

# Basic Fields

An X.509 version 1 certificate contains the following fields. Version 2 fields are discussed in [Version 2 Fields](about-version-2-fields.md). Version 3 fields are discussed in [Version 3 Extensions](about-version-3-extensions.md).

## Version

Specifies the version number of the encoded certificate. Currently, the possible values of this field are 0, 1, or 2, but this may be expanded in the future.

``` syntax
---------------------------------------------------------------------
-- Version number. Currently, this can be 0, 1, or 2.
---------------------------------------------------------------------
CertificateVersion ::= INTEGER {v1(0), v2(1), v3(2)}
```

## Serial Number

Contains a positive, unique integer assigned by the certification authority (CA) to the certificate.

``` syntax
---------------------------------------------------------------------
-- Certificate serial number
---------------------------------------------------------------------
CertificateSerialNumber ::= INTEGER
```

## Signature Algorithm

Contains an [*object identifier*](/windows/desktop/SecGloss/o-gly) (OID) that specifies the algorithm used by the CA to sign the certificate. 
For example, 1.2.840.113549.1.1.5 specifies a SHA-1 hashing algorithm combined with the RSA encryption algorithm from RSA Laboratories.

``` syntax
---------------------------------------------------------------------
-- Signature OID
---------------------------------------------------------------------
signature ::= AlgorithmIdentifier

AlgorithmIdentifier ::= SEQUENCE 
{
  algorithm           OBJECT IDENTIFIER,
  parameters          ANY OPTIONAL    
}
```

## Issuer

Contains the [*X.500*](/windows/desktop/SecGloss/x-gly) distinguished name (DN) of the CA that created and signed the certificate.

``` syntax
---------------------------------------------------------------------
-- Issuer name 
---------------------------------------------------------------------
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
  type       OBJECT IDENTIFIER,
  value      ANY 
}
```

## Validity

Specifies the time interval during which the certificate is valid. 
Dates through the end of 2049 use the Coordinated Universal Time (Greenwich Mean Time) format (*yymmddhhmmssz*). 
Dates beginning with January 1st, 2050 use the generalized time format (*yyyymmddhhmmssz*).

``` syntax
---------------------------------------------------------------------
-- Validity period 
---------------------------------------------------------------------
Validity ::= SEQUENCE 
{
  notBefore           ChoiceOfTime,
  notAfter            ChoiceOfTime
}

ChoiceOfTime ::= CHOICE 
{
  utcTime                 UTCTime,
  generalTime             GeneralizedTime
}
```

## Subject

Contains an X.500 distinguished name of the entity associated with the public key contained in the certificate.

``` syntax
---------------------------------------------------------------------
-- Subject name 
---------------------------------------------------------------------
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
  type       OBJECT IDENTIFIER,
  value      ANY 
}
```

## Public Key

Contains the public key and associated algorithm information.

``` syntax
---------------------------------------------------------------------
--  Subject public key information
---------------------------------------------------------------------
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
```

## Related topics

<dl> <dt>

[Version 2 Fields](about-version-2-fields.md)
</dt> <dt>

[Version 3 Extensions](about-version-3-extensions.md)
</dt> <dt>

[X.509 Public Key Certificates](about-x-509-public-key-certificates.md)
</dt> </dl>

 

 
