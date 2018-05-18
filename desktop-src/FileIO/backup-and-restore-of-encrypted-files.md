---
Description: 'The raw encryption functions enable backup of encrypted files.'
ms.assetid: '00f9b00e-305d-4554-8b43-7061228c92c3'
title: Backup and Restore of Encrypted Files
---

# Backup and Restore of Encrypted Files

The Encrypting File System (EFS) filters the opening of an encrypted file in such a way that the application that opened the file gets access to the unencrypted information, provided of course it has the proper credentials to access the file and get the key necessary to decrypt the file. Subsequent read operations on this file will yield unencrypted text. This is very desirable for typical access to encrypted files, and keeps the encryption and decryption of the files transparent. However, it hinders backup of encrypted files, because if backup is attempted with the standard file I/O calls like [**CreateFile**](createfile.md), [**ReadFile**](readfile.md), and [**WriteFile**](writefile.md), the files backed up will be the plain text version.

The raw encryption functions are provided to solve this problem. Backup applications are a primary intended user for these functions. Raw encryption functions differ from other file system functions in that open, read, and write functions allow access to the raw encrypted data streams and also allow reading/writing of the $EFS stream. Therefore, the caller of the raw encryption functions does not need access to the cryptographic keys that decrypt the file. The following raw encryption APIs are available for use with backup and restore applications: 

| Raw Encryption API                                     | Description                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OpenEncryptedFileRaw**](openencryptedfileraw.md)   | Open an encrypted file with access to data in encrypted format. If the caller does not have access to the key for the file, the caller needs [SeBackupPrivilege](https://msdn.microsoft.com/library/windows/desktop/aa375728) to export encrypted files or SeRestorePrivilege to import encrypted files. |
| [**CloseEncryptedFileRaw**](closeencryptedfileraw.md) | Close an encrypted file opened with [**OpenEncryptedFileRaw**](openencryptedfileraw.md)                                                                                                                                                                                      |
| [**ReadEncryptedFileRaw**](readencryptedfileraw.md)   | Read an encrypted file leaving its data in encrypted format                                                                                                                                                                                                                   |
| [**WriteEncryptedFileRaw**](writeencryptedfileraw.md) | Write an encrypted file leaving its data in encrypted format                                                                                                                                                                                                                  |
| [**ImportCallback**](importcallback.md)               | Application-defined callback for use with [**WriteEncryptedFileRaw**](writeencryptedfileraw.md)                                                                                                                                                                              |
| [**ExportCallback**](exportcallback.md)               | Application-defined callback for use with [**ReadEncryptedFileRaw**](readencryptedfileraw.md)                                                                                                                                                                                |



 

 

 



