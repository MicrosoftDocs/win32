---
description: An application using a backup authority to store session keys typically follows these steps.
ms.assetid: 859310ed-6000-44c8-92f7-974326ce0fc9
title: Storing Session Keys Using a Backup Authority
ms.topic: article
ms.date: 05/31/2018
---

# Storing Session Keys Using a Backup Authority

An application using a [*backup authority*](../secgloss/b-gly.md) to store session keys typically follows these steps.

**To use a backup authority**

1.  Encrypt the file as usual.
2.  Export the [*session key*](../secgloss/s-gly.md) used to encrypt the file into a [*simple key BLOB*](../secgloss/s-gly.md), specifying that your own [*key exchange public key*](../secgloss/k-gly.md) be used to encrypt the key BLOB. Store this key BLOB with the encrypted file.
3.  Export the session key again, this time specifying that the backup authority's public key be used to encrypt the key BLOB. Send this key BLOB to the backup authority, along with the key's description, serial number, and so on.

If a [*key pair*](../secgloss/k-gly.md) is lost, the keys can be retrieved from the [*backup authority*](../secgloss/b-gly.md) if the identity of the keys' owner can be established. The procedure for establishing identity is determined by the policy of the particular backup authority and does not involve CryptoAPI.

For the code needed to create a session key and export that key to a [*simple key BLOB*](../secgloss/s-gly.md) that can be written to a disk file, see [Example C Program: Exporting a Session Key](example-c-program-exporting-a-session-key.md).

 

 
