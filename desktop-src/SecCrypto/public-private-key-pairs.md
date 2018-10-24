---
Description: Asymmetric keys, also known as public/private key pairs, are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt session keys and digital signatures. Asymmetric encryption uses public key encryption algorithms.
ms.assetid: f75e5e6c-0a84-47ac-97db-5063327f7931
title: Asymmetric Keys
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asymmetric Keys

[*Asymmetric keys*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx), also known as [*public/private key pairs*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx), are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt [*session keys*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) and [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx). Asymmetric encryption uses [*public key encryption*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) algorithms.

Public key algorithms use two different keys: a [*public key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx) and a [*private key*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). The private key member of the pair must be kept private and secure. The public key, however, can be distributed to anyone who requests it. The public key of a key pair is often distributed by means of a [*digital certificate*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx). When one key of a key pair is used to encrypt a message, the other key from that pair is required to decrypt the message. Thus if user A's public key is used to encrypt data, only user A (or someone who has access to user A's private key) can decrypt the data. If user A's private key is used to encrypt a piece of data, only user A's public key will decrypt the data, thus indicating that user A (or someone with access to user A's private key) did the encryption.

If the private key is used to sign a message, the public key from that pair must be used to validate the signature. For example, if Alice wants to send someone a digitally signed message, she would sign the message with her private key, and the other person could verify her signature by using her public key. Because presumably only Alice has access to her private key, the fact that the signature can be verified with Alice's public key indicates that Alice created the signature.

Unfortunately, public key algorithms are very slow, roughly 1,000 times slower than symmetric algorithms. It is impractical to use them to encrypt large amounts of data. In practice, public key algorithms are used to encrypt [*session keys*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). [*Symmetric algorithms*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) are used for encryption/decryption of most data.

Similarly, because signing a message, in effect, encrypts the message, it is not practical to use public key signature algorithms to sign large messages. Instead, a fixed-length [*hash*](https://msdn.microsoft.com/en-us/library/ms721586(v=VS.85).aspx) is made of the message and the hash value is signed. For more information, see [Hashes and Digital Signatures](hashes-and-digital-signatures.md).

Each user generally has two [*public/private key pairs*](https://msdn.microsoft.com/en-us/library/ms721603(v=VS.85).aspx). One key pair is used to encrypt session keys and the other to create [*digital signatures*](https://msdn.microsoft.com/en-us/library/ms721573(v=VS.85).aspx). These are known as the [*key exchange key pair*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) and the [*signature key pair*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx), respectively.

Note that although key containers created by most [*cryptographic service providers*](https://msdn.microsoft.com/en-us/library/ms721572(v=VS.85).aspx) (CSPs) contain two key pairs, this is not required. Some CSPs do not store any [*key pairs*](https://msdn.microsoft.com/en-us/library/ms721590(v=VS.85).aspx) while other CSPs store more than two pairs.

All keys in CryptoAPI are stored within CSPs. CSPs are also responsible for creating the keys, destroying them, and using them to perform a variety of cryptographic operations. Exporting keys out of the CSP so that they can be sent to other users is discussed in [Cryptographic Key Storage and Exchange](cryptographic-key-storage-and-exchange.md).

 

 



