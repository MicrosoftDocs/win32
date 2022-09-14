---
description: Asymmetric keys, also known as public/private key pairs, are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt session keys and digital signatures. Asymmetric encryption uses public key encryption algorithms.
ms.assetid: f75e5e6c-0a84-47ac-97db-5063327f7931
title: Asymmetric Keys
ms.topic: article
ms.date: 05/31/2018
---

# Asymmetric Keys

[*Asymmetric keys*](../secgloss/a-gly.md), also known as [*public/private key pairs*](../secgloss/p-gly.md), are used for asymmetric encryption. Asymmetric encryption is used mainly to encrypt and decrypt [*session keys*](../secgloss/s-gly.md) and [*digital signatures*](../secgloss/d-gly.md). Asymmetric encryption uses [*public key encryption*](../secgloss/p-gly.md) algorithms.

Public key algorithms use two different keys: a [*public key*](../secgloss/p-gly.md) and a [*private key*](../secgloss/p-gly.md). The private key member of the pair must be kept private and secure. The public key, however, can be distributed to anyone who requests it. The public key of a key pair is often distributed by means of a [*digital certificate*](../secgloss/c-gly.md). When one key of a key pair is used to encrypt a message, the other key from that pair is required to decrypt the message. Thus if user A's public key is used to encrypt data, only user A (or someone who has access to user A's private key) can decrypt the data. If user A's private key is used to encrypt a piece of data, only user A's public key will decrypt the data, thus indicating that user A (or someone with access to user A's private key) did the encryption.

If the private key is used to sign a message, the public key from that pair must be used to validate the signature. For example, if Alice wants to send someone a digitally signed message, she would sign the message with her private key, and the other person could verify her signature by using her public key. Because presumably only Alice has access to her private key, the fact that the signature can be verified with Alice's public key indicates that Alice created the signature.

Unfortunately, public key algorithms are very slow, roughly 1,000 times slower than symmetric algorithms. It is impractical to use them to encrypt large amounts of data. In practice, public key algorithms are used to encrypt [*session keys*](../secgloss/s-gly.md). [*Symmetric algorithms*](../secgloss/s-gly.md) are used for encryption/decryption of most data.

Similarly, because signing a message, in effect, encrypts the message, it is not practical to use public key signature algorithms to sign large messages. Instead, a fixed-length [*hash*](../secgloss/h-gly.md) is made of the message and the hash value is signed. For more information, see [Hashes and Digital Signatures](hashes-and-digital-signatures.md).

Each user generally has two [*public/private key pairs*](../secgloss/p-gly.md). One key pair is used to encrypt session keys and the other to create [*digital signatures*](../secgloss/d-gly.md). These are known as the [*key exchange key pair*](../secgloss/k-gly.md) and the [*signature key pair*](../secgloss/s-gly.md), respectively.

Note that although key containers created by most [*cryptographic service providers*](../secgloss/c-gly.md) (CSPs) contain two key pairs, this is not required. Some CSPs do not store any [*key pairs*](../secgloss/k-gly.md) while other CSPs store more than two pairs.

All keys in CryptoAPI are stored within CSPs. CSPs are also responsible for creating the keys, destroying them, and using them to perform a variety of cryptographic operations. Exporting keys out of the CSP so that they can be sent to other users is discussed in [Cryptographic Key Storage and Exchange](cryptographic-key-storage-and-exchange.md).

 

 
