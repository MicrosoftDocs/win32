---
Description: An application using a backup authority to store session keys typically follows these steps.
ms.assetid: 859310ed-6000-44c8-92f7-974326ce0fc9
title: Procedure for Storing Session Keys Using a Backup Authority
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Procedure for Storing Session Keys Using a Backup Authority

An application using a [*backup authority*](security.b_gly#-security-backup-authority-gly) to store session keys typically follows these steps.

**To use a backup authority**

1.  Encrypt the file as usual.
2.  Export the [*session key*](security.s_gly#-security-session-key-gly) used to encrypt the file into a [*simple key BLOB*](security.s_gly#-security-simple-key-blob-gly), specifying that your own [*key exchange public key*](security.k_gly#-security-key-exchange-public-key-gly) be used to encrypt the key BLOB. Store this key BLOB with the encrypted file.
3.  Export the session key again, this time specifying that the backup authority's public key be used to encrypt the key BLOB. Send this key BLOB to the backup authority, along with the key's description, serial number, and so on.

If a [*key pair*](security.k_gly#-security-key-pair-gly) is lost, the keys can be retrieved from the [*backup authority*](security.b_gly#-security-backup-authority-gly) if the identity of the keys' owner can be established. The procedure for establishing identity is determined by the policy of the particular backup authority and does not involve CryptoAPI.

For the code needed to create a session key and export that key to a [*simple key BLOB*](security.s_gly#-security-simple-key-blob-gly) that can be written to a disk file, see [Example C Program: Exporting a Session Key](example-c-program-exporting-a-session-key.md).

 

 



