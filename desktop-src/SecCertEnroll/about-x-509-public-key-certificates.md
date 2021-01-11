---
description: Public key cryptography relies on a public and private key pair to encrypt and decrypt content.
ms.assetid: a85ec2bc-a413-41a6-b3d2-5fa81a9e7bb6
title: X.509 Public Key Certificates
ms.topic: article
ms.date: 05/31/2018
---

# X.509 Public Key Certificates

Public key cryptography relies on a public and private key pair to encrypt and decrypt content. The keys are mathematically related, and content encrypted by using one of the keys can only be decrypted by using the other. The private key is kept secret. The public key is typically embedded in a binary certificate, and the certificate is published to a database that can be reached by all authorized users.

The X.509 public key infrastructure (PKI) standard identifies the requirements for robust public key certificates. A certificate is a signed data structure that binds a public key to a person, computer, or organization. Certificates are issued by [*certification authorities*](/windows/desktop/SecGloss/c-gly) (CAs). All who are party to secure communications that make use of a public key rely on the CA to adequately verify the identities of the individuals, systems, or entities to which it issues certificates. The level of verification typically depends on the level of security required for the transaction. If the CA can suitably verify the identity of the requester, it signs (encrypts), encodes, and issues the certificate.

A certificate is a signed data structure that binds a public key to an entity. The [*Abstract Syntax Notation One*](/windows/desktop/SecGloss/a-gly) (ASN.1) syntax for the version 3 [*X.509*](/windows/desktop/SecGloss/x-gly) certificate is shown in the following example.

``` syntax
-- X.509 signed certificate 

SignedContent ::= SEQUENCE 
{
  certificate         CertificateToBeSigned,
  algorithm           Object Identifier,
  signature           BITSTRING
}
 
-- X.509 certificate to be signed

CertificateToBeSigned ::= SEQUENCE 
{
  version                 [0] CertificateVersion DEFAULT v1,
  serialNumber            CertificateSerialNumber,
  signature               AlgorithmIdentifier,
  issuer                  Name
  validity                Validity,
  subject                 Name
  subjectPublicKeyInfo    SubjectPublicKeyInfo,
  issuerUniqueIdentifier  [1] IMPLICIT UniqueIdentifier OPTIONAL,
  subjectUniqueIdentifier [2] IMPLICIT UniqueIdentifier OPTIONAL,
  extensions              [3] Extensions OPTIONAL
}
```

Since its inception in 1998, three versions of the X.509 public key certificate standard have evolved. As shown by the following illustration, each successive version of the data structure has retained the fields that existed in the previous versions and added more.

![x.509 certificates versions 1, 2, and 3](images/x509certificateversions.png)

The following topics discuss the available fields in more detail:

-   [Basic Fields](about-basic-fields.md)
-   [Version 2 Fields](about-version-2-fields.md)
-   [Version 3 Extensions](about-version-3-extensions.md)

## Related topics

<dl> <dt>

[Public Key Infrastructure](public-key-infrastructure.md)
</dt> </dl>

 

 
