---
Description: Digital certification involves a process for signing the certificate. This process is described.
ms.assetid: bb0382fd-2924-429f-933b-84ab61debf20
title: X.509 Digital Certification
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# X.509 Digital Certification

A primary task of a [*digital certificate*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) is to provide access to the subject's [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). The certificate also confirms that the certificate's public key belongs to the certificate's subject. For example, a [*certification authority*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CA) can digitally sign a special message (the certificate information) that contains the name of some user, say "Alice," and her public key. This must be done in such a way that anyone can verify that the certificate was issued and signed by no one other than the CA. If the CA is trusted and it can be verified that Alice's certificate was issued by that CA, any receiver of Alice's certificate can trust Alice's public key from that certificate.

The typical implementation of digital certification involves a process for signing the certificate.

The process goes like this:

1.  Alice sends a signed [*certificate request*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) containing her name, her public key, and perhaps some additional information to a CA.
2.  The CA creates a message, *m*, from Alice's request. The CA signs the message with its private key, creating a separate signature message, *sig*. The CA returns the message, *m*, and the signature, *sig*, to Alice. Together, *m* and *sig* form Alice's certificate.
3.  Alice sends both parts of her certificate to Bob to give him access to her public key.
4.  Bob verifies the signature, *sig* using the CA's public key. If the signature proves valid, he accepts the public key in the certificate as Alice's public key.

As with any [*digital signature*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2), any receiver with access to the CA's public key can determine whether a specific CA signed the certificate. This process requires no access to any secret information. The scenario just presented assumes that Bob has access to the CA's public key. Bob would have access to that key if he has a copy of the CA's certificate that contains that public key.

[*X.509*](https://msdn.microsoft.com/28dba6ef-939f-4789-9789-ee6e0fef0177) digital certificates include not only a user's name and public key, but also other information about the user. These certificates are more than stepping stones in a digital hierarchy of trust. They enable the CA to give a certificate's receiver a means of trusting not only the public key of the certificate's subject, but also that other information about the certificate's subject. That other information can include, among other things, an email address, an authorization to sign documents of a given value, or the authorization to become a CA and sign other certificates.

X.509 certificates and many other certificates have a valid time duration. A certificate can expire and no longer be valid. A CA can revoke a certificate for a number of reasons. To handle revocations, a CA maintains and distributes a list of revoked certificates called a [*certificate revocation list*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CRL). Network users access the CRL to determine the validity of a certificate.

 

 



