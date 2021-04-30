---
description: The CryptoAPI message functions adhere to PKCS \#7 Cryptographic Message Syntax (CMS) Standard. Developers need to be familiar with this specification to most effectively use the low-level message functions. A few of its definitions are highlighted here.
ms.assetid: 99b633fe-9898-4570-ba8b-16ee78d351da
title: PKCS \#7 Cryptographic Messaging Syntax Concepts
ms.topic: article
ms.date: 05/31/2018
---

# PKCS \#7 Cryptographic Messaging Syntax Concepts

The CryptoAPI message functions adhere to [*PKCS \#7*](../secgloss/p-gly.md) [Cryptographic Message Syntax (CMS) Standard](https://www.ietf.org/rfc/rfc3369.txt). Developers need to be familiar with this specification to most effectively use the [*low-level message functions*](../secgloss/l-gly.md). A few of its definitions are highlighted here.

The PKCS \#7 standard describes a general syntax for data that may have [*cryptography*](../secgloss/c-gly.md) applied to it, such as [*digital signatures*](../secgloss/d-gly.md) and [*digital envelopes*](../secgloss/d-gly.md). The syntax admits recursion, so that, for example, one envelope can be nested inside another, or one party can sign digital data that has already been put into an envelope. It also allows arbitrary attributes, such as signing time, to be authenticated along with the content of a message. Further, it provides for other attributes, such as [*countersignatures*](../secgloss/c-gly.md), to be associated with a signature.

The type of data contained in a PKCS \#7 message is called its content type. There are two classes of content types: Base and Enhanced.

-   Base content types contain only data with no cryptographic enhancements. Presently there is only one content type in this class, the [*data content type*](../secgloss/d-gly.md).
-   [*Enhanced content types*](../secgloss/e-gly.md) contain data of some type (possibly encrypted), and other cryptographic enhancements (such as hashes or signatures).

The content in the Enhanced class employs encapsulation, giving rise to the terms [*outer content*](../secgloss/o-gly.md) (the one containing the enhancements) and [*inner content*](../secgloss/i-gly.md) (the one being enhanced). For example, an Enhanced class might contain the [*data content type*](../secgloss/d-gly.md) (Base class) that has a signature included with it. In this case, the data content type is the *inner content* and the combination of the data content type and the signature forms the outer content.

The content types defined in the PKCS \#7 standard are as follows.



| Content type              | Description                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data                      | An octet (**BYTE**) string.                                                                                                                                                                                                                                                                                           |
| Signed Data               | Content of any type and encrypted message [*hashes*](../secgloss/h-gly.md) ([*digests*](../secgloss/m-gly.md)) of the content for zero or more signers.                                                                           |
| Enveloped Data            | Encrypted content of any type and encrypted content-encryption keys for one or more recipients. The combination of encrypted content and encrypted content-encryption key for a recipient is a [*digital envelope*](../secgloss/d-gly.md) for that recipient. |
| Signed-and-Enveloped Data | Encrypted content of any type, encrypted content-encryption keys for one or more recipients, and doubly encrypted message digests for one or more signers. The double encryption consists of an encryption with a signer's private key followed by an encryption with the content-encryption key.                     |
| Digested Data             | Content of any type and a message [*hash*](../secgloss/h-gly.md) (digest) of the content.                                                                                                                                                                                             |
| Encrypted Data            | Encrypted content of any type. Unlike the enveloped-[*data content type*](../secgloss/d-gly.md), the encrypted-data content type has neither recipients nor encrypted content-encryption keys. Keys are assumed to be managed by other means.               |



 

> [!Note]  
> Throughout the PKCS \#7 specification, the terms *digest* and [*digested*](../secgloss/d-gly.md) refer to the value produced from applying a [*hashing algorithm*](../secgloss/h-gly.md) to data. This documentation uses the terms [*hash*](../secgloss/h-gly.md) and *hashed* for the same purpose. For example, the data type used with the [*low-level message functions*](../secgloss/l-gly.md) is called hashed rather than digested. For the purposes of this documentation, the two sets of terms may be used interchangeably.

 

 

 
