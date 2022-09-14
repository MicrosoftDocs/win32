---
description: Example programs in the following sections perform operations that require public/private key pairs to be available for encrypting and decrypting files, messages, and signatures.
ms.assetid: b03528ff-0170-4dde-ae35-f5c3951d6b1f
title: Necessary Key Containers, Keys, and Certificates
ms.topic: article
ms.date: 05/31/2018
---

# Necessary Key Containers, Keys, and Certificates

Example programs in the following sections perform operations that require [*public/private key pairs*](../secgloss/p-gly.md) to be available for encrypting and decrypting files, messages, and signatures. Many of these programs will compile, link, and run but fail at run time without the existence of proper [*key containers*](../secgloss/k-gly.md), keys, [*certificate stores*](../secgloss/c-gly.md), and certificates in those stores.

In addition, some of the certificates in the MY store must have some of their extended properties set.

Creating the needed default key container can be done by running the program in [Example C Program: Creating a Key Container and Generating Keys](example-c-program-creating-a-key-container-and-generating-keys.md). Note that the creation of a key container does not automatically generate public/private key pairs. The example program, however, both creates the key container and generates the public/private key pairs.

After public/private key pairs have been generated, test certificates using those keys can be obtained from a [*certification authority*](../secgloss/c-gly.md) (CA).

Several of the programs assume that certificates with specific subject names exist in the MY system store. In particular, several programs look for certificates with the subject names "Full Test Cert" and "Hortense." The subject names for the certificates may be changed in the code to match the subject names of certificates that exist in the MY certificate store.

Running the example program in [Example C Program: Listing the Certificates in a Store](example-c-program-listing-the-certificates-in-a-store.md) will display all of the certificates in a store and all of the extended properties that are set on those certificates.

 

 
