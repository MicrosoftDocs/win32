---
title: File API
description: Functions relating to the File API.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 7058AF1C-80C5-4C95-B2C7-4CF5971AF4AF
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File API

Functions relating to the File API.

The functions prefaced with *Ipcf* rather than *Ipc* are a subset of the SDK and are the File API.

> [!Note]  
> For error condition processing, always use a call to [**IpcGetErrorMessageText**](ipcgeterrormessagetext.md) right after an SDK API call fails, so you get complete information about the nature of the error.

 

## In this section

<dl> <dt>

[**IpcfDecryptFile**](ipcfdecryptfile.md)
</dt> <dd>

Decrypts the specified file on disk.

</dd> <dt>

[**IpcfDecryptFileStream**](ipcfdecryptfilestream.md)
</dt> <dd>

Decrypts a file as a byte stream.

</dd> <dt>

[**IpcfEncryptFile**](ipcfencryptfile.md)
</dt> <dd>

Encrypts a file on disk.

</dd> <dt>

[**IpcfEncryptFileStream**](ipcfencryptfilestream.md)
</dt> <dd>

Encrypts a file as a byte stream.

</dd> <dt>

[**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)
</dt> <dd>

Used to encrypt a file as a byte stream and optionally add metadata to the encryption license.

</dd> <dt>

[**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
</dt> <dd>

Used to encrypt a file and optionally add metadata to the file encryption license.

</dd> <dt>

[**IpcfGetDecryptedFilePath**](ipcfgetdecryptedfilepath.md)
</dt> <dd>

Use to get the expected, decrypted, absolute file path.

</dd> <dt>

[**IpcfGetDecryptedFilePathFromStream**](ipcfgetdecryptedfilepathfromstream.md)
</dt> <dd>

Used to get the expected, decrypted, absolute file path.

</dd> <dt>

[**IpcfGetEncryptedFilePath**](ipcfgetencryptedfilepath.md)
</dt> <dd>

Used to get the expected, encrypted, absolute file path.

</dd> <dt>

[**IpcfGetEncryptedFilePathFromStream**](ipcfgetencryptedfilepathfromstream.md)
</dt> <dd>

Used to get the expected, encrypted, absolute file path.

</dd> <dt>

[**IpcfGetFileProperty**](ipcfgetfileproperty.md)
</dt> <dd>

Queries the properties of an **IPCF\_FILE\_HANDLE** or the file represented by it.

</dd> <dt>

[**IpcfGetSerializedLicenseFromFile**](ipcfgetserializedlicensefromfile.md)
</dt> <dd>

Gets the license associated with a file.

</dd> <dt>

[**IpcfGetSerializedLicenseFromFileStream**](ipcfgetserializedlicensefromfilestream.md)
</dt> <dd>

Gets the license associated with a file stream.

</dd> <dt>

[**IpcfIsFileEncrypted**](ipcfisfileencrypted.md)
</dt> <dd>

Determines whether a file on disk is encrypted.

</dd> <dt>

[**IpcfIsFileStreamEncrypted**](ipcfisfilestreamencrypted.md)
</dt> <dd>

Determines whether a file stream is encrypted.

</dd> <dt>

[**IpcfOpenFileOnHandle**](ipcfopenfileonhandle.md)
</dt> <dd>

Gets an **IPCF\_FILE\_HANDLE** associated with an encrypted file which can be used to access and modify that file's data.

</dd> <dt>

[**IpcfOpenFileOnILockBytes**](ipcfopenfileonilockbytes.md)
</dt> <dd>

Gets an **IPCF\_FILE\_HANDLE** associated with an encrypted byte stream which can be used to access and modify that stream's data.

</dd> <dt>

[**IpcfLogicalFileRangeToRawFileRange**](ipcflogicalfilerangetorawfilerange.md)
</dt> <dd>

Gets the raw file range for the given logical file range of the protected file content.

</dd> <dt>

[**IpcfReadFile**](ipcfreadfile.md)
</dt> <dd>

Reads protected content of a protected file given a logical file range.

</dd> <dt>

[**IpcfSetEndOfFile**](ipcfsetendoffile.md)
</dt> <dd>

Truncates a protected file.

</dd> <dt>

[**IpcfSetFileProperty**](ipcfsetfileproperty.md)
</dt> <dd>

Sets the properties on **IPCF\_FILE\_HANDLE** or on the file represented by it.

</dd> <dt>

[**IpcfWriteFile**](ipcfwritefile.md)
</dt> <dd>

Modifies protected content of a protected file to a given logical file range.

</dd> </dl>

 

 




