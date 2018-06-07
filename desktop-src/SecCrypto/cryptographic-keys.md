---
Description: Cryptographic keys are central to cryptographic operations.
ms.assetid: dda7b527-1522-4b43-8d8e-44ce7983a9aa
title: Cryptographic Keys
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Keys

[*Cryptographic keys*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) are central to cryptographic operations. Many cryptographic schemes consist of pairs of operations, such as encryption and decryption, or signing and verification. A *key* is a piece of variable data that is fed as input into a cryptographic algorithm to perform one such operation. In a well-designed cryptographic scheme, the security of the scheme depends only on the security of the keys used.

Cryptographic keys can be classified based on their usage within a cryptographic scheme, as [Symmetric Keys](symmetric-keys.md) or [Asymmetric Keys](public-private-key-pairs.md). A [*symmetric key*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) is a single key that is used for both operations in a cryptographic scheme (for example, to both [*encrypt*](https://msdn.microsoft.com/f1caccd2-3453-448e-b194-bf899eff8091) and to [*decrypt*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) your data). Usually, the security of the scheme depends on ensuring that the key is only known to the authorized participants. Asymmetric keys, on the other hand, are used in cryptographic schemes where different keys are needed for each operation. Common examples of such schemes are those using [*public/private key pairs*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a), where the security of the scheme depends on ensuring that the [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) is only known to one party. For example, public/private key encryption systems use two keys, a [*public key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) that anyone can use to encrypt data and a [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) that only the authorized recipient possesses and that can be used to decrypt the data.

Cryptographic keys can be further classified by the purpose for which they are used. These uses include digital signature generation, digital signature verification, message authentication, data encryption and decryption, key wrapping, and key transport. For a full list of key types as defined by the [*National Institute of Standards and Technology*](https://msdn.microsoft.com/28d229ef-53ce-4d17-aba0-3bbf51e3ff0c) (NIST), see section 5 GENERAL KEY MANAGEMENT GUIDANCE of [NIST Special Publication 800-57: Recommendation for Key Management – Part 1: General (Revised)](http://go.microsoft.com/fwlink/p/?linkid=180812).

 

 



