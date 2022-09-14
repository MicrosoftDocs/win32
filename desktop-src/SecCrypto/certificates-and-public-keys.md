---
description: Certificate Services is one foundation for the Public Key Infrastructure (PKI) that provides the means for safeguarding and authenticating information.
ms.assetid: c18f46ca-e805-4b33-8014-79dc34c18531
title: Certificates and Public Keys
ms.topic: article
ms.date: 05/31/2018
---

# Certificates and Public Keys

Certificate Services is one foundation for the Public Key Infrastructure (PKI) that provides the means for safeguarding and authenticating information. The relationship between a certificate holder, the certificate holder's identity, and the certificate holder's [*public key*](../secgloss/p-gly.md) is a critical portion of PKI. This infrastructure is made up of the following parts:

-   [The Public/Private Key Pair](#the-publicprivate-key-pair)
-   [The Certificate Request](#the-certificate-request)
-   [The Certification Authority](#the-certification-authority)
-   [The Certificate](#the-certificate-request)
-   [The Certificate Revocation List](#the-certificate-revocation-list)
-   [Your Public Key Used for Encryption](#your-public-key-used-for-encryption)
-   [Your Public Key Used for Signature Verification](#your-public-key-used-for-signature-verification)
-   [Microsoft Certificate Services Role](#microsoft-certificate-services-role)

## The Public/Private Key Pair

PKI requires the use of [*public/private key pairs*](../secgloss/p-gly.md). The mathematics of public/private key pairs is beyond the scope of this documentation, but it is important to note the functional relationship between a public and a private key. PKI [*cryptographic algorithms*](../secgloss/c-gly.md) use the [*public key*](../secgloss/p-gly.md) of the receiver of an encrypted message to encrypt data, and the related [*private key*](../secgloss/p-gly.md) and only the related private key to decrypt the encrypted message.

Similarly, a [*digital signature*](../secgloss/d-gly.md) of the content, described in greater detail below, is created with the signer's private key. The corresponding public key, which is available to everyone, is used to verify this signature. The secrecy of the private key must be maintained because the framework falls apart after the private key is compromised.

Given enough time and resources, a public/private key pair can be compromised, that is, the private key can be discovered. The longer the key, the more difficult it is to use brute force to discover the private key. In practice, sufficiently strong keys can be used to make it unfeasible to determine the private key in a timely manner, making the Public Key Infrastructure a viable security mechanism.

A private key can be stored, in protected format, on a disk, in which case it can only be used with that specific computer unless it is physically moved to another computer. An alternative is to have a key on a smart card that can be used on a different computer provided it has a smart card reader and supporting software.

The public key, but not the private key, of the subject of a digital certificate is included as part of the [*certificate request*](../secgloss/c-gly.md). (Hence, a public/private key pair must exist before making the certificate request.) That public key becomes part of the issued certificate.

## The Certificate Request

Before a certificate is issued, a [*certificate request*](../secgloss/c-gly.md) must be generated. This request applies to one entity, for example, an end-user, a computer, or an application. For discussion, assume that the entity is yourself. Details of your identity are included in the certificate request. After the request is generated, it is submitted to a [*certification authority*](../secgloss/c-gly.md) (CA). The CA then uses your identity information to determine whether the request meets the CA's criteria for issuing a certificate. If the CA approves the request, it issues a certificate to you, as the entity named in the request.

## The Certification Authority

Before issuing your certificate, the CA verifies your identity. When the certificate is issued, your identity is bound to the certificate, which contains your public key. Your certificate also contains the CA's digital signature (which can be verified by anyone who receives your certificate).

Because your certificate contains the identity of the issuing CA, an interested party that trusts this CA can extend that trust to your certificate. The issuance of a certificate does not establish trust, but transfers trust. If the certificate consumer does not trust the issuing CA, it will not (or at least should not) trust your certificate.

A chain of signed certificates allows trust to be transferred to other CAs as well. This allows parties who use different CAs to still be able to trust certificates (provided there is a common CA in the chain, that is, a CA that is trusted by both parties).

## The Certificate

In addition to your public key and the identity of the issuing CA, the issued certificate contains information about the purposes of your key and certificate. Furthermore, it includes the path to the CA's list of revoked certificates, and it specifies the certificate validity period (beginning and ending dates).

Assuming the certificate consumer trusts the issuing CA for your certificate, the certificate consumer must determine whether the certificate is still valid by comparing the certificate's beginning and ending dates with the current time and by checking that your certificate in not on the CA's list of revoked certificates.

## The Certificate Revocation List

Assuming the certificate is being used in a valid time period and the certificate consumer trusts the issuing CA, there is one more item for the certificate consumer to check before using the certificate: the [*certificate revocation list*](../secgloss/c-gly.md) (CRL). The certificate consumer checks the CA's CRL (the path to which is included as an extension in your certificate) to ensure your certificate is not on the list of certificates that have been revoked. CRLs exist because there are times when a certificate has not expired, but it can no longer be trusted. Periodically, the CA will publish an updated CRL. Certificate consumers are responsible for comparing certificates to the current CRL before considering the certificate trustworthy.

## Your Public Key Used for Encryption

If a sender wants to encrypt a message before sending it to you, the sender first retrieves your certificate. After the sender determines that the CA is trusted and your certificate is valid and not revoked, the sender uses your public key (recall it is part of the certificate) with cryptographic algorithms to encrypt the [*plaintext*](../secgloss/p-gly.md) message into [*ciphertext*](../secgloss/c-gly.md). When you receive the ciphertext, you use your private key to decrypt the ciphertext.

If a third party intercepts the ciphertext email message, the third party will not be able to decrypt it without access to your [*private key*](../secgloss/p-gly.md).

Note that the bulk of the activities listed here are handled by software, not directly by the user.

## Your Public Key Used for Signature Verification

A [*digital signature*](../secgloss/d-gly.md) is used as confirmation that a message has not been altered and as confirmation of the message sender's identity. This digital signature is dependent on your private key and the message contents. Using the message as input and your private key, cryptographic algorithms create the digital signature. The contents of the message are not changed by the signing process. A recipient can use your public key (after checking your certificate's validity, issuing CA, and revocation status) to determine whether the signature corresponds to the message contents and to determine whether the message was sent by you.

If a third party intercepts the intended message, alters it (even slightly), and forwards it and the original signature to the recipient, the recipient, upon examination of the message and signature, will be able to determine that the message is suspect. Similarly, if a third party creates a message and sends it with a bogus digital signature under the guise that it originated from you, the recipient will be able to use your public key to determine that the message and signature do not correspond to each other.

[*Nonrepudiation*](../secgloss/n-gly.md) is also supported by digital signatures. If the sender of a signed message denies sending the message, the recipient can use the signature to refute that claim.

Note that the bulk of the activities listed here are also handled by software, not directly by the user.

## Microsoft Certificate Services Role

Microsoft Certificate Services has the role of issuing certificates or denying requests for certificates, as directed by policy modules, which are responsible for ensuring the identity of the certificate requester. Certificate Services also provides the ability to revoke a certificate, as well as publish the CRL. Certificate Services can also centrally distribute (for example, to a directory service) issued certificates. The ability to issue, distribute, revoke, and manage certificates, along with the publication of CRLs, provides the necessary capabilities for public key infrastructure.

 

 
