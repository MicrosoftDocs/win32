---
description: Contains definitions of security terms that begin with the letter H.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 4165b820-30fc-477e-a690-81109f161323
title: H (Security Glossary)
ms.topic: article
ms.date: 05/31/2018
---

# H (Security Glossary)

[A](a-gly.md) [B](b-gly.md) [C](c-gly.md) [D](d-gly.md) [E](e-gly.md) F [G](g-gly.md) H [I](i-gly.md) J [K](k-gly.md) [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) [X](x-gly.md) Y Z

<dl> <dt>

<span id="_security_handle_gly"></span><span id="_SECURITY_HANDLE_GLY"></span>**handle**
</dt> <dd>

A token used to identify or access an object, such as the handle to a cryptographic provider, certificate store, message, or key pair.

</dd> <dt>

<span id="_security_hash_gly"></span><span id="_SECURITY_HASH_GLY"></span>**hash**
</dt> <dd>

A fixed-size result obtained by applying a mathematical function (the *hashing algorithm*) to an arbitrary amount of data. (Also known as "message digest.")

See also *hashing functions*.

</dd> <dt>

<span id="_security_hash_object_gly"></span><span id="_SECURITY_HASH_OBJECT_GLY"></span>**hash object**
</dt> <dd>

An object used to hash messages or session keys. The hash object is created by a call to **CryptCreateHash**. The definition of the object is defined by the CSP specified in the call.

</dd> <dt>

<span id="_security_hashing_algorithm_gly"></span><span id="_SECURITY_HASHING_ALGORITHM_GLY"></span>**hashing algorithm**
</dt> <dd>

An algorithm used to produce a hash value of some piece of data, such as a message or session key. Typical hashing algorithms include MD2, MD4, MD5, and SHA-1.

</dd> <dt>

<span id="_security_hashing_functions_gly"></span><span id="_SECURITY_HASHING_FUNCTIONS_GLY"></span>**hashing functions**
</dt> <dd>

A set of functions used to create and destroy hash objects, get or set the parameters of a hash object, and hash data and session keys.

</dd> <dt>

<span id="_security_hash_based_message_authentication_code_gly"></span><span id="_SECURITY_HASH_BASED_MESSAGE_AUTHENTICATION_CODE_GLY"></span>**Hash-Based Message Authentication Code**
</dt> <dd>

(HMAC) A symmetric keyed hashing algorithm implemented by Microsoft cryptographic service providers. An HMAC is used to verify the integrity of data to help ensure it has not been modified while in storage or transit. It can be used with any iterated cryptographic hash algorithm, such as MD5 or SHA-1. CryptoAPI references this algorithm by its algorithm identifier (CALG\_HMAC) and class (ALG\_CLASS\_HASH).

See also [*Message Authentication Code*](m-gly.md).

</dd> <dt>

<span id="_security_hcsbc_gly"></span><span id="_SECURITY_HCSBC_GLY"></span>**HCSBC**
</dt> <dd>

Data type which serves as a handle to a Certificate Services backup context. Its role is to maintain context state between the server and the backup APIs when a backup is being performed.

</dd> <dt>

<span id="_security_hmac_gly"></span><span id="_SECURITY_HMAC_GLY"></span>**HMAC**
</dt> <dd>

See *Hash-Based Message Authentication Code*.

</dd> </dl>

 

 



