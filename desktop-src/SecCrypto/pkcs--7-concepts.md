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

The CryptoAPI message functions adhere to [*PKCS \#7*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) [Cryptographic Message Syntax (CMS) Standard](http://go.microsoft.com/fwlink/p/?linkid=98036). Developers need to be familiar with this specification to most effectively use the [*low-level message functions*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f). A few of its definitions are highlighted here.

The PKCS \#7 standard describes a general syntax for data that may have [*cryptography*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) applied to it, such as [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) and [*digital envelopes*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2). The syntax admits recursion, so that, for example, one envelope can be nested inside another, or one party can sign digital data that has already been put into an envelope. It also allows arbitrary attributes, such as signing time, to be authenticated along with the content of a message. Further, it provides for other attributes, such as [*countersignatures*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb), to be associated with a signature.

The type of data contained in a PKCS \#7 message is called its content type. There are two classes of content types: Base and Enhanced.

-   Base content types contain only data with no cryptographic enhancements. Presently there is only one content type in this class, the [*data content type*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2).
-   [*Enhanced content types*](https://msdn.microsoft.com/f1caccd2-3453-448e-b194-bf899eff8091) contain data of some type (possibly encrypted), and other cryptographic enhancements (such as hashes or signatures).

The content in the Enhanced class employs encapsulation, giving rise to the terms [*outer content*](https://msdn.microsoft.com/e6be8932-015e-4058-b249-1671b3fea521) (the one containing the enhancements) and [*inner content*](https://msdn.microsoft.com/af511aed-88f5-4b12-ad44-317925297f70) (the one being enhanced). For example, an Enhanced class might contain the [*data content type*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (Base class) that has a signature included with it. In this case, the data content type is the *inner content* and the combination of the data content type and the signature forms the outer content.

The content types defined in the PKCS \#7 standard are as follows.



| Content type              | Description                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data                      | An octet (**BYTE**) string.                                                                                                                                                                                                                                                                                           |
| Signed Data               | Content of any type and encrypted message [*hashes*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) ([*digests*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1)) of the content for zero or more signers.                                                                           |
| Enveloped Data            | Encrypted content of any type and encrypted content-encryption keys for one or more recipients. The combination of encrypted content and encrypted content-encryption key for a recipient is a [*digital envelope*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) for that recipient. |
| Signed-and-Enveloped Data | Encrypted content of any type, encrypted content-encryption keys for one or more recipients, and doubly encrypted message digests for one or more signers. The double encryption consists of an encryption with a signer's private key followed by an encryption with the content-encryption key.                     |
| Digested Data             | Content of any type and a message [*hash*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) (digest) of the content.                                                                                                                                                                                             |
| Encrypted Data            | Encrypted content of any type. Unlike the enveloped-[*data content type*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2), the encrypted-data content type has neither recipients nor encrypted content-encryption keys. Keys are assumed to be managed by other means.               |



 

> [!Note]  
> Throughout the PKCS \#7 specification, the terms *digest* and [*digested*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) refer to the value produced from applying a [*hashing algorithm*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) to data. This documentation uses the terms [*hash*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) and *hashed* for the same purpose. For example, the data type used with the [*low-level message functions*](https://msdn.microsoft.com/65dd9a04-fc7c-4179-95ff-dac7dad4668f) is called hashed rather than digested. For the purposes of this documentation, the two sets of terms may be used interchangeably.

 

 

 



