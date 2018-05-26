---
Description: Cryptographic keys are central to cryptographic operations.
ms.assetid: dda7b527-1522-4b43-8d8e-44ce7983a9aa
title: Cryptographic Keys
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Cryptographic Keys

[*Cryptographic keys*](security.c_gly#-security-cryptographic-key-gly) are central to cryptographic operations. Many cryptographic schemes consist of pairs of operations, such as encryption and decryption, or signing and verification. A *key* is a piece of variable data that is fed as input into a cryptographic algorithm to perform one such operation. In a well-designed cryptographic scheme, the security of the scheme depends only on the security of the keys used.

Cryptographic keys can be classified based on their usage within a cryptographic scheme, as [Symmetric Keys](symmetric-keys.md) or [Asymmetric Keys](public-private-key-pairs.md). A [*symmetric key*](security.s_gly#-security-symmetric-key-gly) is a single key that is used for both operations in a cryptographic scheme (for example, to both [*encrypt*](security.e_gly#-security-encryption-gly) and to [*decrypt*](security.d_gly#-security-decryption-gly) your data). Usually, the security of the scheme depends on ensuring that the key is only known to the authorized participants. Asymmetric keys, on the other hand, are used in cryptographic schemes where different keys are needed for each operation. Common examples of such schemes are those using [*public/private key pairs*](security.p_gly#-security-public-private-key-pair-gly), where the security of the scheme depends on ensuring that the [*private key*](security.p_gly#-security-private-key-gly) is only known to one party. For example, public/private key encryption systems use two keys, a [*public key*](security.p_gly#-security-public-key-gly) that anyone can use to encrypt data and a [*private key*](security.p_gly#-security-private-key-gly) that only the authorized recipient possesses and that can be used to decrypt the data.

Cryptographic keys can be further classified by the purpose for which they are used. These uses include digital signature generation, digital signature verification, message authentication, data encryption and decryption, key wrapping, and key transport. For a full list of key types as defined by the [*National Institute of Standards and Technology*](security.n_gly#-security-national-institute-of-standards-and-technology-gly) (NIST), see section 5 GENERAL KEY MANAGEMENT GUIDANCE of [NIST Special Publication 800-57: Recommendation for Key Management – Part 1: General (Revised)](http://go.microsoft.com/fwlink/p/?linkid=180812).

 

 



