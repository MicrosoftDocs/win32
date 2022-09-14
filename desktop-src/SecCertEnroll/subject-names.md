---
description: The subject field of a PKCS \#10 certificate request contains the distinguished name of the entity requesting the certificate.
ms.assetid: 6c35ce42-07be-4d47-a14e-ed5a361dbe33
title: Subject Names
ms.topic: article
ms.date: 05/31/2018
---

# Subject Names

The **subject** field of a PKCS \#10 certificate request contains the distinguished name of the entity requesting the certificate.

``` syntax
CertificationRequestInfo ::= SEQUENCE 
{
   version                 CertificationRequestInfoVersion,
   subject                 Name,
   subjectPublicKeyInfo    SubjectPublicKeyInfo,
   attributes              [0] IMPLICIT Attributes
}
```

The distinguished name consists of a sequence of relative distinguished names (RDNs). Each RDN consists of a set of attributes, and each attribute consists of an object identifier and a value. The data type of the value is identified by the **DirectoryString** structure.

``` syntax
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeValue

AttributeTypeValue ::= SEQUENCE 
{
   type       EncodedObjectID,
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

For more information, see the following topics:

-   [Creating a Subject Name](creating-a-subject-name.md)
-   [Encoding a Subject Name](encoding-a-subject-name.md)

## Related topics

<dl> <dt>

[Requests](/windows/desktop/SecCrypto/requests)
</dt> </dl>

 

 
