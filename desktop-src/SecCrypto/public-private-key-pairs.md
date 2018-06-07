---
Description: Asymmetric keys, also known as public/private key pairs, are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt session keys and digital signatures. Asymmetric encryption uses public key encryption algorithms.
ms.assetid: f75e5e6c-0a84-47ac-97db-5063327f7931
title: Asymmetric Keys
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asymmetric Keys

[*Asymmetric keys*](https://msdn.microsoft.com/0baaa937-f635-4500-8dcd-9dbbd6f4cd02), also known as [*public/private key pairs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a), are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt [*session keys*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) and [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2). Asymmetric encryption uses [*public key encryption*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) algorithms.

Public key algorithms use two different keys: a [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) and a [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). The private key member of the pair must be kept private and secure. The public key, however, can be distributed to anyone who requests it. The public key of a key pair is often distributed by means of a [*digital certificate*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb). When one key of a key pair is used to encrypt a message, the other key from that pair is required to decrypt the message. Thus if user A's public key is used to encrypt data, only user A (or someone who has access to user A's private key) can decrypt the data. If user A's private key is used to encrypt a piece of data, only user A's public key will decrypt the data, thus indicating that user A (or someone with access to user A's private key) did the encryption.

If the private key is used to sign a message, the public key from that pair must be used to validate the signature. For example, if Alice wants to send someone a digitally signed message, she would sign the message with her private key, and the other person could verify her signature by using her public key. Because presumably only Alice has access to her private key, the fact that the signature can be verified with Alice's public key indicates that Alice created the signature.

Unfortunately, public key algorithms are very slow, roughly 1,000 times slower than symmetric algorithms. It is impractical to use them to encrypt large amounts of data. In practice, public key algorithms are used to encrypt [*session keys*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50). [*Symmetric algorithms*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) are used for encryption/decryption of most data.

Similarly, because signing a message, in effect, encrypts the message, it is not practical to use public key signature algorithms to sign large messages. Instead, a fixed-length [*hash*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) is made of the message and the hash value is signed. For more information, see [Hashes and Digital Signatures](hashes-and-digital-signatures.md).

Each user generally has two [*public/private key pairs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a). One key pair is used to encrypt session keys and the other to create [*digital signatures*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2). These are known as the [*key exchange key pair*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) and the [*signature key pair*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50), respectively.

Note that although key containers created by most [*cryptographic service providers*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) (CSPs) contain two key pairs, this is not required. Some CSPs do not store any [*key pairs*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) while other CSPs store more than two pairs.

All keys in CryptoAPI are stored within CSPs. CSPs are also responsible for creating the keys, destroying them, and using them to perform a variety of cryptographic operations. Exporting keys out of the CSP so that they can be sent to other users is discussed in [Cryptographic Key Storage and Exchange](cryptographic-key-storage-and-exchange.md).

 

 



