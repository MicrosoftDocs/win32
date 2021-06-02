---
description: Cryptographic keys are central to cryptographic operations.
ms.assetid: dda7b527-1522-4b43-8d8e-44ce7983a9aa
title: Cryptographic Keys
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Keys

[*Cryptographic keys*](../secgloss/c-gly.md) are central to cryptographic operations. Many cryptographic schemes consist of pairs of operations, such as encryption and decryption, or signing and verification. A *key* is a piece of variable data that is fed as input into a cryptographic algorithm to perform one such operation. In a well-designed cryptographic scheme, the security of the scheme depends only on the security of the keys used.

Cryptographic keys can be classified based on their usage within a cryptographic scheme, as [Symmetric Keys](symmetric-keys.md) or [Asymmetric Keys](public-private-key-pairs.md). A [*symmetric key*](../secgloss/s-gly.md) is a single key that is used for both operations in a cryptographic scheme (for example, to both [*encrypt*](../secgloss/e-gly.md) and to [*decrypt*](../secgloss/d-gly.md) your data). Usually, the security of the scheme depends on ensuring that the key is only known to the authorized participants. Asymmetric keys, on the other hand, are used in cryptographic schemes where different keys are needed for each operation. Common examples of such schemes are those using [*public/private key pairs*](../secgloss/p-gly.md), where the security of the scheme depends on ensuring that the [*private key*](../secgloss/p-gly.md) is only known to one party. For example, public/private key encryption systems use two keys, a [*public key*](../secgloss/p-gly.md) that anyone can use to encrypt data and a [*private key*](../secgloss/p-gly.md) that only the authorized recipient possesses and that can be used to decrypt the data.

Cryptographic keys can be further classified by the purpose for which they are used. These uses include digital signature generation, digital signature verification, message authentication, data encryption and decryption, key wrapping, and key transport. For a full list of key types as defined by the [*National Institute of Standards and Technology*](../secgloss/n-gly.md) (NIST), see section 5 GENERAL KEY MANAGEMENT GUIDANCE of [NIST Special Publication 800-57: Recommendation for Key Management – Part 1: General (Revised)](https://csrc.nist.gov/publications/nistpubs/800-57/sp800-57-Part1-revised2_Mar08-2007.pdf).

 

 
