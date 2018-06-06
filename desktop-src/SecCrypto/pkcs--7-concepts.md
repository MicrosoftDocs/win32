---
Description: The CryptoAPI message functions adhere to PKCS \#7 Cryptographic Message Syntax (CMS) Standard. Developers need to be familiar with this specification to most effectively use the low-level message functions. A few of its definitions are highlighted here.
ms.assetid: 99b633fe-9898-4570-ba8b-16ee78d351da
title: PKCS \#7 Cryptographic Messaging Syntax Concepts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PKCS \#7 Cryptographic Messaging Syntax Concepts

The CryptoAPI message functions adhere to [*PKCS \#7*](security.p_gly#-security-pkcs-7-standard-gly) [Cryptographic Message Syntax (CMS) Standard](http://go.microsoft.com/fwlink/p/?linkid=98036). Developers need to be familiar with this specification to most effectively use the [*low-level message functions*](security.l_gly#-security-low-level-message-functions-gly). A few of its definitions are highlighted here.

The PKCS \#7 standard describes a general syntax for data that may have [*cryptography*](security.c_gly#-security-cryptography-gly) applied to it, such as [*digital signatures*](security.d_gly#-security-digital-signature-gly) and [*digital envelopes*](security.d_gly#-security-digital-envelope-gly). The syntax admits recursion, so that, for example, one envelope can be nested inside another, or one party can sign digital data that has already been put into an envelope. It also allows arbitrary attributes, such as signing time, to be authenticated along with the content of a message. Further, it provides for other attributes, such as [*countersignatures*](security.c_gly#-security-countersignature-gly), to be associated with a signature.

The type of data contained in a PKCS \#7 message is called its content type. There are two classes of content types: Base and Enhanced.

-   Base content types contain only data with no cryptographic enhancements. Presently there is only one content type in this class, the [*data content type*](security.d_gly#-security-data-content-type-gly).
-   [*Enhanced content types*](security.e_gly#-security-enhanced-content-type-gly) contain data of some type (possibly encrypted), and other cryptographic enhancements (such as hashes or signatures).

The content in the Enhanced class employs encapsulation, giving rise to the terms [*outer content*](security.o_gly#-security-outer-content-gly) (the one containing the enhancements) and [*inner content*](security.i_gly#-security-inner-content-gly) (the one being enhanced). For example, an Enhanced class might contain the [*data content type*](security.d_gly#-security-data-content-type-gly) (Base class) that has a signature included with it. In this case, the data content type is the *inner content* and the combination of the data content type and the signature forms the outer content.

The content types defined in the PKCS \#7 standard are as follows.



| Content type              | Description                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data                      | An octet (**BYTE**) string.                                                                                                                                                                                                                                                                                           |
| Signed Data               | Content of any type and encrypted message [*hashes*](security.h_gly#-security-hash-gly) ([*digests*](security.m_gly#-security-message-digest-gly)) of the content for zero or more signers.                                                                           |
| Enveloped Data            | Encrypted content of any type and encrypted content-encryption keys for one or more recipients. The combination of encrypted content and encrypted content-encryption key for a recipient is a [*digital envelope*](security.d_gly#-security-digital-envelope-gly) for that recipient. |
| Signed-and-Enveloped Data | Encrypted content of any type, encrypted content-encryption keys for one or more recipients, and doubly encrypted message digests for one or more signers. The double encryption consists of an encryption with a signer's private key followed by an encryption with the content-encryption key.                     |
| Digested Data             | Content of any type and a message [*hash*](security.h_gly#-security-hash-gly) (digest) of the content.                                                                                                                                                                                             |
| Encrypted Data            | Encrypted content of any type. Unlike the enveloped-[*data content type*](security.d_gly#-security-data-content-type-gly), the encrypted-data content type has neither recipients nor encrypted content-encryption keys. Keys are assumed to be managed by other means.               |



 

> [!Note]  
> Throughout the PKCS \#7 specification, the terms *digest* and [*digested*](security.d_gly#-security-digested-data-gly) refer to the value produced from applying a [*hashing algorithm*](security.h_gly#-security-hashing-algorithm-gly) to data. This documentation uses the terms [*hash*](security.h_gly#-security-hash-gly) and *hashed* for the same purpose. For example, the data type used with the [*low-level message functions*](security.l_gly#-security-low-level-message-functions-gly) is called hashed rather than digested. For the purposes of this documentation, the two sets of terms may be used interchangeably.

 

 

 



