---
Description: 'A file marked encrypted is encrypted by the NTFS file system by using the current encryption driver.'
ms.assetid: '166bfb8c-b97d-4cc7-bf6b-399837cb8ad0'
title: Handling Encrypted Files and Directories
---

# Handling Encrypted Files and Directories

A programmer or user may mark a directory or file as encrypted. A file marked encrypted is encrypted by the NTFS file system by using the current encryption driver. If at a later date the file is marked as not encrypted, it is decrypted and left in a plain text (unsecured) state.

Directories are not themselves encrypted. Rather, by default, in an "encrypted" directory all new files in the directory are encrypted at creation. A user must specifically change the status of a new file to decrypted if the user does not want the file to be encrypted. An encrypted directory is visible. To make a directory inaccessible to other users, use the standard methods of access control.

The encryption functions cannot be used with the [Backup API](https://msdn.microsoft.com/library/windows/desktop/aa362508).

To encrypt a new file, use the [**CreateFile**](createfile.md) function with the **FILE\_ATTRIBUTE\_ENCRYPTED** flag. To encrypt an existing file, use the [**EncryptFile**](encryptfile.md) function. All data streams in the file are encrypted. If the file is already encrypted, **EncryptFile** does nothing but returns a nonzero value, which indicates success. If the file is compressed, **EncryptFile** decompresses the file before encrypting it.

To decrypt an encrypted file, use the [**DecryptFile**](decryptfile.md) function. If the file is not encrypted, **DecryptFile** does nothing but returns a nonzero value indicating success.

The [**EncryptionDisable**](encryptiondisable.md) function disables or enables the encryption of the indicated directory and the files in it. It does not affect the encryption of subdirectories below the indicated directory.

To retrieve the encryption status of a file, use the [**FileEncryptionStatus**](fileencryptionstatus.md) function. Alternatively, call the [**GetFileAttributes**](getfileattributes.md) function and examine the **FILE\_ATTRIBUTE\_ENCRYPTED** flag in the return value.

[**CopyFile**](copyfile.md) and [**CopyFileEx**](copyfileex.md) attempt to encrypt the destination file with the keys used in the encryption of the source file. If this cannot be done, both functions attempt to encrypt the destination file with default keys. If both of these methods cannot be done, **CopyFile** and **CopyFileEx** fail with an **ERROR\_ENCRYPTION\_FAILED** error. If you want **CopyFileEx** to complete the copy operation even when the destination file cannot be encrypted, include the **COPY\_FILE\_ALLOW\_DECRYPTED\_DESTINATION** flag in the value of the *dwCopyFlags* parameter in your call to **CopyFileEx**.

 

 



