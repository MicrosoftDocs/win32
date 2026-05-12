---
description: The Encrypted File System (EFS) provides cryptographic protection of individual files on NTFS file system volumes by using a public-key system.
ms.assetid: 5f20109f-727d-44a9-90a1-0adc19b00d28
title: File Encryption
ms.topic: concept-article
ms.date: 07/08/2025
# customer intent: As a Windows app developer, I want to use the Encrypted File System (EFS) to protect sensitive files and directories in my application, so that I can ensure data security even if devices are lost or stolen.
---

# File encryption

The Encrypted File System (EFS) provides an additional level of security for files and directories. It provides cryptographic protection of individual files on NTFS file system volumes using a public-key system.

Typically, the access control to file and directory objects provided by the Windows security model is sufficient to protect unauthorized access to sensitive information. However, if a laptop that contains sensitive data is lost or stolen, the security protection of that data may be compromised. Encrypting the files increases security.

## Working with EFS

To determine whether a file system supports file encryption for files and directories, call the [GetVolumeInformation](/windows/win32/api/FileAPI/nf-fileapi-getvolumeinformationa) function and examine the **FS\_FILE\_ENCRYPTION** bit flag. Note that the following items cannot be encrypted:

- Compressed files
- System files
- System directories
- Root directories
- Transactions

Sparse files can be encrypted.

TxF does not support most operations on Encrypted File System (EFS) files. The only operations TxF supports are read operations, such as [ReadEncryptedFileRaw](/windows/win32/api/WinBase/nf-winbase-readencryptedfileraw).

> [!NOTE]
> When the source file is encrypted, **CopyFile** and **CopyFileEx** rely on the EFS service (hosted in lsass.exe) to create the target file and apply keys used in encryption of the source file. These operations are performed by EFS service while impersonating the caller of **CopyFile** or **CopyFileEx**.

## In this section

The following topics provide information about file encryption:

| Topic | Description |
|-------|-------------|
| [Handling Encrypted Files and Directories](handling-encrypted-files-and-directories.md) | A file marked encrypted is encrypted by the NTFS file system by using the current encryption driver. |
| [Encrypted Files and User Keys](encrypted-files-and-user-keys.md) | Lists the functions to use to create a new key, add a key to an encrypted file, query the keys for an encrypted file, and remove keys from an encrypted file. |
| [Backup and Restore of Encrypted Files](backup-and-restore-of-encrypted-files.md) | The raw encryption functions enable backup of encrypted files. |

For more information about encryption, see [Adding Users to an Encrypted File](adding-users-to-an-encrypted-file.md).

For more information about cryptography, see [Cryptography](/windows/desktop/SecCrypto/cryptography-portal).
