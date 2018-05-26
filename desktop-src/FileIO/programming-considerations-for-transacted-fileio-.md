---
Description: Describes various programming considerations for Transactional NTFS.
ms.assetid: a1ef1ce1-42f6-4627-ab64-e7f41fa23e94
title: Programming Considerations for Transactional NTFS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Programming Considerations for Transactional NTFS

For a description of various programming considerations for Transactional NTFS, see the following sections:

-   [Which File Changes Are Transacted](#which-file-changes-are-transacted)
-   [Compression](#compression)
-   [Creating a File or Directory](#creating-a-file-or-directory)
-   [Deleting a File](#deleting-a-file)
-   [Deleting a Directory](#deleting-a-directory)
-   [Directory Locking Issues](#directory-locking-issues)
-   [Directory Enumeration](#directory-enumeration)
-   [Memory-Mapped Files](#memory-mapped-files)
-   [Named Streams](#named-streams)
-   [Renaming a File or Directory](#renaming-a-file-or-directory)
-   [Reparse Points](#reparse-points)
-   [Error Codes](#error-codes)
-   [Encrypted File System](#encrypted-file-system)
-   [File I/O Functions and Transactional NTFS](#file-io-functions-and-transactional-ntfs)
    -   [Transacted Functions](#transacted-functions)
    -   [File I/O Functions Changed By TxF](#file-io-functions-changed-by-txf)

## Which File Changes Are Transacted

Most file changes, such as changes to file contents, streams, reparse points, attributes, and the file system namespace, are transacted. When one of these changes is made on a transacted file handle, the change is isolated from other transactions, and the change is undone if the transaction is rolled back.

Changes that do not affect file contents, metadata, or the file system namespace, such as changes to compression or defragmentation, are not transacted. These changes are not isolated from other transactions, and they are not undone if the transaction is rolled back.

## Compression

The compression state of a file opened in a transaction cannot be changed.

## Creating a File or Directory

A file or directory that is created in a transaction is not visible to anything outside the current transaction. Outside this transaction, any attempt to create a file with the same name fails with the error **ERROR\_TRANSACTIONAL\_CONFLICT**, effectively reserving the file name for when the transaction commits or is rolled back.

## Deleting a File

A file or directory that is deleted by calling the [**DeleteFileTransacted**](/windows/win32/WinBase/nf-winbase-deletefiletransacteda?branch=master) function remains visible to all outside readers.

> [!Note]  
> All transacted handles to the file must be closed before the end of the transaction. If the handles are not properly closed, the delete does not occur. All open handles to the file must be closed before performing the commit for the delete operation to be considered part of the transaction. This is because the system does not actually delete a file until the last handle to it is closed, even when the operation is not transacted, as part of the Windows file I/O subsystem.

 

## Deleting a Directory

A directory that is deleted by calling the [**RemoveDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-removedirectorytransacteda?branch=master) function remains visible to all outside readers.

> [!Note]  
> The same constraints exist for open handles on transacted directory operations as on files. For more information, see [Deleting a File](#deleting-a-file).

 

## Directory Locking Issues

If a file is modified in a transaction, all directory components of the path to the file are referred to as *pinned against rename* until the transaction ends. That is, the system prevents you from renaming them until the transaction is committed or rolled back. An attempt to rename a directory that is an ancestor to a file that has been modified in an ongoing transaction will fail with the error **ERROR\_CANT\_BREAK\_TRANSACTIONAL\_DEPENDENCY**.

## Directory Enumeration

The contents of a directory can be changed while an enumeration is in progress as a result of using APIs that enumerate, for example the [**FindFirstFileTransacted**](/windows/win32/WinBase/nf-winbase-findfirstfiletransacteda?branch=master) and [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master) functions.

Changes to a directory outside a transaction are not isolated from the transaction and are immediately visible within the transaction. For example, if a non-transacted writer adds a file to a directory, the new file is immediately visible inside the transaction such that calling the [**FindFirstFileTransacted**](/windows/win32/WinBase/nf-winbase-findfirstfiletransacteda?branch=master) or [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master) function will return the new file.

Changes made to a directory inside a transaction are isolated until the transaction commits. For example, a file created in the directory as part of the transaction. A non-transacted reader calling the [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master) or [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master) function will not see the newly created file until the transaction commits.

## Memory-Mapped Files

The client must call the [**FlushViewOfFile**](https://msdn.microsoft.com/library/windows/desktop/aa366563) function, close the file-mapping object, and close the file handle before committing the associated transaction on a memory-mapped file.

## Named Streams

Named streams are fully transactional, but locking is done at the file level, not the stream level. Writers from outside a transaction that attempt to modify any stream within a locked file receive the error **ERROR\_SHARING\_VIOLATION**.

You cannot rename a secondary stream in a transaction.

## Renaming a File or Directory

To rename a file as a transacted operation, call [**MoveFileTransacted**](/windows/win32/WinBase/nf-winbase-movefiletransacteda?branch=master) to move the file.

## Reparse Points

Changes to reparse points are transacted, which means that if a new reparse point gets assigned to a file in a transaction, it is not visible to the other transactions. Similarly, changes or removal of an existing reparse point are not visible until commit.

## Error Codes

The Kernel Transaction Manager (KTM) uses the system error codes in the range from 6700 through 6799. Transactional NTFS (TxF) uses Windows error codes in the range from 6800 through 6899. For more information, see WinError.h and System Error Codes (6000-8199).

## Encrypted File System

TxF does not support operations on EFS files. You cannot open an EFS-encrypted file for transactions. Calling the [**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master) function on an EFS file will fail with the error **ERROR\_EFS\_NOT\_ALLOWED\_IN\_TRANSACTION**. Similarly, calling the [**EncryptFile**](/windows/win32/WinBase/nf-winbase-encryptfilea?branch=master) function on a file in a transaction will fail with the error **ERROR\_EFS\_NOT\_ALLOWED\_IN\_TRANSACTION**.

## File I/O Functions and Transactional NTFS

TxF provides new transacted functions that take a file name, and changes the behavior of existing file I/O API functions that take a file handle.

### Transacted Functions

If you do not call one of the following transacted functions in place of its non-transacted version, the operation will not be transacted:

-   [**CopyFileTransacted**](/windows/win32/WinBase/nf-winbase-copyfiletransacteda?branch=master)
-   [**CreateDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-createdirectorytransacteda?branch=master)
-   [**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master)
-   [**CreateHardLinkTransacted**](/windows/win32/WinBase/nf-winbase-createhardlinktransacteda?branch=master)
-   [**CreateSymbolicLinkTransacted**](/windows/win32/WinBase/nf-winbase-createsymboliclinktransacteda?branch=master)
-   [**DeleteFileTransacted**](/windows/win32/WinBase/nf-winbase-deletefiletransacteda?branch=master)
-   [**FindFirstFileNameTransactedW**](/windows/win32/WinBase/nf-winbase-findfirstfilenametransactedw?branch=master)
-   [**FindFirstFileTransacted**](/windows/win32/WinBase/nf-winbase-findfirstfiletransacteda?branch=master)
-   [**FindFirstStreamTransactedW**](/windows/win32/WinBase/nf-winbase-findfirststreamtransactedw?branch=master)
-   [**GetCompressedFileSizeTransacted**](/windows/win32/WinBase/nf-winbase-getcompressedfilesizetransacteda?branch=master)
-   [**GetFileAttributesTransacted**](/windows/win32/WinBase/nf-winbase-getfileattributestransacteda?branch=master)
-   [**GetFullPathNameTransacted**](/windows/win32/WinBase/nf-winbase-getfullpathnametransacteda?branch=master)
-   [**GetLongPathNameTransacted**](/windows/win32/WinBase/nf-winbase-getlongpathnametransacteda?branch=master)
-   [**MoveFileTransacted**](/windows/win32/WinBase/nf-winbase-movefiletransacteda?branch=master)
-   [**RemoveDirectoryTransacted**](/windows/win32/WinBase/nf-winbase-removedirectorytransacteda?branch=master)
-   [**SetFileAttributesTransacted**](/windows/win32/WinBase/nf-winbase-setfileattributestransacteda?branch=master)

For example, the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function now has a transacted version: [**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master).

### File I/O Functions Changed By TxF

The following table lists the functions whose behavior is affected by Transactional NTFS. For example, the behavior of the [**ReadFile**](/windows/win32/FileAPI/nf-fileapi-readfile?branch=master) function will vary depending on whether the *hFile* parameter was created by the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function or the [**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master) function.



| Function                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CloseHandle"></span><span id="closehandle"></span><span id="CLOSEHANDLE"></span>[**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211)<br/>                                                                                                                                                                                                                                                                                                             | Applications should close all handles bound to a transaction before the transaction is committed. An application must close a transacted handle opened with **FILE\_FLAG\_DELETE\_ON\_CLOSE** before committing the transaction in order for the delete operation to occur.<br/>                                                                                                                                     |
| <span id="CreateFileMapping"></span><span id="createfilemapping"></span><span id="CREATEFILEMAPPING"></span>[**CreateFileMapping**](https://msdn.microsoft.com/library/windows/desktop/aa366537)<br/>                                                                                                                                                                                                                                                                                 | If there is a transaction associated with *hFile*, then the file-mapping object that this function creates will be associated with the same transaction. Modifications made through views of this file-mapping object are transacted. Applications must call [**FlushViewOfFile**](https://msdn.microsoft.com/library/windows/desktop/aa366563), unmap all views, and close all handles to the file-mapping object before committing transacted changes.<br/> |
| <span id="FindNextFile"></span><span id="findnextfile"></span><span id="FINDNEXTFILE"></span>[**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master)<br/>                                                                                                                                                                                                                                                                                                         | If there is a transaction bound to the file enumeration handle, then the files that are returned are subject to transaction isolation rules.<br/>                                                                                                                                                                                                                                                                    |
| <span id="FSCTL_SET_COMPRESSION"></span><span id="fsctl_set_compression"></span>[**FSCTL\_SET\_COMPRESSION**](/windows/win32/WinIoCtl/?branch=master)<br/>                                                                                                                                                                                                                                                                                                  | You cannot change the compression state of a file opened by [**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master).<br/>                                                                                                                                                                                                                                                                                               |
| <span id="GetFileInformationByHandle__________and__________GetFileInformationByHandleEx"></span><span id="getfileinformationbyhandle__________and__________getfileinformationbyhandleex"></span><span id="GETFILEINFORMATIONBYHANDLE__________AND__________GETFILEINFORMATIONBYHANDLEEX"></span>[**GetFileInformationByHandle**](/windows/win32/FileAPI/nf-fileapi-getfileinformationbyhandle?branch=master) and [**GetFileInformationByHandleEx**](/windows/win32/WinBase/nf-winbase-getfileinformationbyhandleex?branch=master)<br/> | If there is a transaction bound to the file handle, then the function returns information for the isolated file view.<br/>                                                                                                                                                                                                                                                                                           |
| <span id="GetFileSize_and__________GetFileSizeEx"></span><span id="getfilesize_and__________getfilesizeex"></span><span id="GETFILESIZE_AND__________GETFILESIZEEX"></span>[**GetFileSize**](/windows/win32/FileAPI/nf-fileapi-getfilesize?branch=master) and [**GetFileSizeEx**](/windows/win32/FileAPI/nf-fileapi-getfilesizeex?branch=master)<br/>                                                                                                                                                                                  | If there is a transaction bound to the file handle, then the function returns information for the isolated file view.<br/>                                                                                                                                                                                                                                                                                           |
| <span id="GetVolumeInformation"></span><span id="getvolumeinformation"></span><span id="GETVOLUMEINFORMATION"></span>[**GetVolumeInformation**](/windows/win32/FileAPI/nf-fileapi-getvolumeinformationa?branch=master)<br/>                                                                                                                                                                                                                                                                 | If the volume supports file system transactions, the function returns **FILE\_SUPPORTS\_TRANSACTIONS** in *lpFileSystemFlags*.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="MapViewOfFile_and__________MapViewOfFileEx"></span><span id="mapviewoffile_and__________mapviewoffileex"></span><span id="MAPVIEWOFFILE_AND__________MAPVIEWOFFILEEX"></span>[**MapViewOfFile**](https://msdn.microsoft.com/library/windows/desktop/aa366761) and [**MapViewOfFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa366763)<br/>                                                                                                                                                                | If there is a transaction associated with the file handle used to create the file-mapping object that is being mapped, then the associated view is transacted. If the view is used to make transacted changes to a file, then the user must call [**FlushViewOfFile**](https://msdn.microsoft.com/library/windows/desktop/aa366563), close the file-mapping object, and close the file handle before committing the associated transaction.<br/>              |
| <span id="ReadDirectoryChangesW"></span><span id="readdirectorychangesw"></span><span id="READDIRECTORYCHANGESW"></span>[**ReadDirectoryChangesW**](/windows/win32/WinBase/nf-winbase-readdirectorychangesw?branch=master)<br/>                                                                                                                                                                                                                                                            | If there is a transaction bound to the directory handle, then the notifications reflect the isolated view of the directory. Changes to files outside the transacted view of the directory are not included in the notifications.<br/>                                                                                                                                                                                |
| <span id="ReadFile___________ReadFileEx__and__________ReadFileScatter"></span><span id="readfile___________readfileex__and__________readfilescatter"></span><span id="READFILE___________READFILEEX__AND__________READFILESCATTER"></span>[**ReadFile**](/windows/win32/FileAPI/nf-fileapi-readfile?branch=master), [**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master), and [**ReadFileScatter**](/windows/win32/FileAPI/nf-fileapi-readfilescatter?branch=master)<br/>                                                                                  | If there is a transaction bound to the file handle, then the function returns data from the transacted view of the file. A transacted read handle is guaranteed to show the same view of a file for the duration of the handle.<br/>                                                                                                                                                                                 |
| <span id="SetEndOfFile"></span><span id="setendoffile"></span><span id="SETENDOFFILE"></span>[**SetEndOfFile**](/windows/win32/FileAPI/nf-fileapi-setendoffile?branch=master)<br/>                                                                                                                                                                                                                                                                                                         | If there is a transaction bound to the handle, then the change in the end-of-file position is transacted.<br/>                                                                                                                                                                                                                                                                                                       |
| <span id="SetFileInformationByHandle"></span><span id="setfileinformationbyhandle"></span><span id="SETFILEINFORMATIONBYHANDLE"></span>[**SetFileInformationByHandle**](/windows/win32/FileAPI/nf-fileapi-setfileinformationbyhandle?branch=master)<br/>                                                                                                                                                                                                                                   | If there is a transaction bound to the handle, then the changes made will be transacted for the information classes **FileBasicInfo**, **FileRenameInfo**, **FileAllocationInfo**, **FileEndOfFileInfo**, and **FileDispositionInfo**.<br/>                                                                                                                                                                          |
| <span id="SetFileShortName"></span><span id="setfileshortname"></span><span id="SETFILESHORTNAME"></span>[**SetFileShortName**](/windows/win32/WinBase/nf-winbase-setfileshortnamea?branch=master)<br/>                                                                                                                                                                                                                                                                                     | If there is a transaction bound to the handle, then the change in the file's short name is transacted.<br/>                                                                                                                                                                                                                                                                                                          |
| <span id="SetFileTime"></span><span id="setfiletime"></span><span id="SETFILETIME"></span>[**SetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724933)<br/>                                                                                                                                                                                                                                                                                                             | If there is a transaction bound to the handle, then the change in file time is transacted.<br/>                                                                                                                                                                                                                                                                                                                      |
| <span id="WriteFile__________WriteFileEx__and_________WriteFileGather"></span><span id="writefile__________writefileex__and_________writefilegather"></span><span id="WRITEFILE__________WRITEFILEEX__AND_________WRITEFILEGATHER"></span>[**WriteFile**](/windows/win32/FileAPI/nf-fileapi-writefile?branch=master), [**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master), and [**WriteFileGather**](/windows/win32/FileAPI/nf-fileapi-writefilegather?branch=master)<br/>                                                                              | If there is a transaction bound to the file handle, then the file write is transacted.<br/>                                                                                                                                                                                                                                                                                                                          |



 

 

 




