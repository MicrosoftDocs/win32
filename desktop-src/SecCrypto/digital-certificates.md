---
description: How digital certificates provide secure communications and how to use CryptoAPI to use and manage those certificates.
ms.assetid: e523b335-0156-4f47-b55c-b80495587c4f
title: Digital Certificates
ms.topic: article
ms.date: 05/31/2018
---

# Digital Certificates

Authentication is crucial to secure communications. Users must be able to prove their identity to those with whom they communicate and must be able to verify the identity of others. Authentication of identity on a network is complex because the communicating parties do not physically meet as they communicate. This can allow an unethical person to intercept messages or to impersonate another person or entity. A method must be worked out to maintain the necessary level of trust within the communication process.

The [*digital certificate*](../secgloss/c-gly.md) is a common credential that provides a means to verify identity. This section provides an overview of how certificates provide secure communications and how to use CryptoAPI to use and manage those certificates.

A certificate is a set of data that identifies an entity. A trusted organization assigns a certificate to an individual or an entity that associates a public key with the individual. The individual or entity to whom a certificate is issued is called the subject of that certificate. The trusted organization that issues the certificate is a [*certification authority*](../secgloss/c-gly.md) (CA) and is known as the certificate's issuer. A trustworthy CA will only issue a certificate after verifying the identity of the certificate's subject.

Certificates use cryptographic techniques to address the problem of the lack of physical contact between those communicating. Using these techniques limits the possibility of an unethical person intercepting, altering, or counterfeiting messages. These cryptographic techniques make certificates difficult to modify. Thus, it is difficult for an entity to impersonate someone else.

The data in a certificate includes the public cryptographic key from the certificate subject's [*public/private key pair*](../secgloss/p-gly.md). A message signed with its sender's private key can only be retrieved by the message's recipient using the sender's public key. This key can be found on a copy of the sender's certificate. Retrieving a signature with a [*public key*](../secgloss/p-gly.md) from a certificate proves that the signature was produced using the certificate subject's [*private key*](../secgloss/p-gly.md). If the sender has been vigilant and has kept the private key secret, the receiver can be confident in the identity of the message sender.

On a network, there is often a trusted application known as a [*certificate server*](../secgloss/c-gly.md). A CA running on a secure computer manages the certificate server. This application has access to the public key of all its clients. Certificate servers dispense messages known as certificates, each of which contains the public key of one of its client users. Each certificate is signed with the CA's private key. Thus the receiver of such a certificate can verify that a specified CA sent it.

Digital certificates also include extensions and extended properties that provide additional information about the certificate's subject such as the subject's email address and the activities that the certificate's subject can perform.

 

 
