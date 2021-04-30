---
description: An X.509 version 3 certificate contains the fields defined in version 1 and version 2 and adds certificate extensions. The ASN.1 syntax of certificate extensions is shown in the following example.
ms.assetid: ca8df7a4-caa4-4fe7-81a8-8fce372454f4
title: Version 3 Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Version 3 Extensions

An X.509 version 3 certificate contains the fields defined in version 1 and version 2 and adds certificate extensions. The ASN.1 syntax of certificate extensions is shown in the following example.

``` syntax
---------------------------------------------------------------------
-- Extensions (beginning with version 3).
---------------------------------------------------------------------
Extensions ::= SEQUENCE OF Extension

Extension ::= SEQUENCE 
{
  Id                  OBJECT IDENTIFIER,
  critical            BOOLEAN DEFAULT FALSE,
  extnValue           OCTET STRING
}
```

The standard version 3 extensions and their object identifiers (OIDs) are listed in the following table. 
Microsoft supports these and includes additional custom extensions. 
For more information, see [Extensions](extensions.md).

| Extension                                         | Description                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Authority Key Identifier(2.5.29.19)<br/>    | Identifies the certification authority (CA) public key that corresponds to the CA private key used to sign the certificate.                                                                              |
| Basic Constraints(2.5.29.35)<br/>           | Specifies whether the entity can be used as a CA and, if so, the number of subordinate CAs that can exist beneath it in the certificate chain.                                                           |
| Certificate Policies(2.5.29.32)<br/>        | Specifies the policies under which the certificate has been issued and the purposes for which it can be used.                                                                                            |
| CRL Distribution Points(2.5.29.31)<br/>     | Contains the URI of the base [*certificate revocation list*](/windows/desktop/SecGloss/c-gly) (CRL).                                  |
| Enhanced Key Usage(2.5.29.46)<br/>          | Specifies the manner in which the public key contained in the certificate can be used.                                                                                                                   |
| Issuer Alternative Name(2.5.29.8)<br/>      | Specifies one or more alternative name forms for the issuer of the certificate request.                                                                                                                  |
| Key Usage(2.5.29.15)<br/>                   | Specifies restrictions on the operations that can be performed by the public key contained in the certificate.                                                                                           |
| Name Constraints(2.5.29.30)<br/>            | Specifies the namespace within which all subject names in a certificate hierarchy must be located. The extension is used only in a CA certificate.                                                       |
| Policy Constraints(2.5.29.36)<br/>          | Constrains path validation by prohibiting policy mapping or by requiring that each certificate in the hierarchy contain an acceptable policy identifier. The extension is used only in a CA certificate. |
| Policy Mappings(2.5.29.33)<br/>             | Specifies the policies in a subordinate CA that correspond to policies in the issuing CA.                                                                                                                |
| Private Key Usage Period(2.5.29.16)<br/>    | Specifies a different validity period for the private key than for the certificate with which the private key is associated.                                                                             |
| Subject Alternative Name(2.5.29.17)<br/>    | Specifies one or more alternative name forms for the subject of the certificate request. Example alternative forms include email addresses, DNS names, IP addresses, and URIs.                           |
| Subject Directory Attributes(2.5.29.9)<br/> | Conveys identification attributes such as the nationality of the certificate subject. The extension value is a sequence of OID-value pairs.                                                              |
| Subject Key Identifier(2.5.29.14)<br/>      | Differentiates between multiple public keys held by the certificate subject. The extension value is typically a SHA-1 hash of the key.                                                                   |



 

## Related topics

<dl> <dt>

[Basic Fields](about-basic-fields.md)
</dt> <dt>

[Version 2 Fields](about-version-2-fields.md)
</dt> <dt>

[X.509 Public Key Certificates](about-x-509-public-key-certificates.md)
</dt> </dl>

 

