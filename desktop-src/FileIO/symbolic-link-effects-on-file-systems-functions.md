---
Description: How symbolic links affect standard file functions that use path names to specify one or more files.
ms.assetid: afda53eb-d0db-4844-9dd0-8a7d93ca341f
title: Symbolic Link Effects on File Systems Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Symbolic Link Effects on File Systems Functions

Several standard file functions that use path names to specify one or more files are affected by the use of symbolic links. This topic lists those functions and describes the changes in behavior:

-   [CopyFile and CopyFileTransacted](#copyfile-and-copyfiletransacted)
-   [CopyFileEx](#copyfileex)
-   [CreateFile and CreateFileTransacted](#createfile-and-createfiletransacted)
-   [CreateHardLink and CreateHardLinkTransacted](#createhardlink-and-createhardlinktransacted)
-   [DeleteFile and DeleteFileTransacted](#deletefile-and-deletefiletransacted)
-   [FindFirstChangeNotification](#findfirstchangenotification)
-   [FindFirstFile and FindFirstFileTransacted](#findfirstfile-and-findfirstfiletransacted)
-   [FindFirstFileEx](#findfirstfileex)
-   [FindNextFile](#findnextfile)
-   [GetBinaryType](#getbinarytype)
-   [GetCompressedFileSize and GetCompressedFileSizeTransacted](#getcompressedfilesize-and-getcompressedfilesizetransacted)
-   [GetDiskFreeSpace](#getdiskfreespaceex)
-   [GetDiskFreeSpaceEx](#getdiskfreespaceex)
-   [GetFileAttributes](#getfileattributesex)
-   [GetFileAttributesEx](#getfileattributesex)
-   [GetFileSecurity](#getfilesecurity)
-   [GetTempPath](#gettemppath)
-   [GetVolumeInformation](#getvolumeinformation)
-   [SetFileAttributes](#setfileattributes)
-   [SetFileSecurity](#setfilesecurity)
-   [Related topics](#related-topics)

In the descriptions below, the following terms are used:

-   Source file—The original file that is to be copied.
-   Destination file—The newly created copy of the file.
-   Target—The entity that a symbolic link points to.

> [!Note]  
> The behavior of functions that accept a handle created using the [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) function, such as the [**GetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724320) function, will differ based on whether or not the **CreateFile** function was called using the **FILE\_FLAG\_OPEN\_REPARSE\_POINT** flag. For more information, see [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) and the following [CreateFile and CreateFileTransacted](#createfile-and-createfiletransacted) section.

 

## CopyFile and CopyFileTransacted

If the source file is a symbolic link, the actual file copied is the target of the symbolic link.

If the destination file already exists and is a symbolic link, the symbolic link is overwritten by the source file.

## CopyFileEx

If **COPY\_FILE\_COPY\_SYMLINK** is specified and:

-   If the source file is a symbolic link, the symbolic link is copied, not the target file.
-   If the source file is not a symbolic link, there is no change in behavior.
-   If the destination file is an existing symbolic link, the symbolic link is overwritten, not the target file.
-   If **COPY\_FILE\_FAIL\_IF\_EXISTS** is also specified, and the destination file is an existing symbolic link, the operation fails in all cases.

If **COPY\_FILE\_COPY\_SYMLINK** is not specified and:

-   If **COPY\_FILE\_FAIL\_IF\_EXISTS** is also specified, and the destination file is an existing symbolic link, the operation fails only if the target of the symbolic link exists.
-   If **COPY\_FILE\_FAIL\_IF\_EXISTS** is not specified, there is no change in behavior.

**Windows Server 2003 and Windows XP:** The **COPY\_FILE\_COPY\_SYMLINK** flag is not supported. If the source file is a symbolic link, the actual file copied is the target of the symbolic link.

## CreateFile and CreateFileTransacted

If the call to this function creates a new file, there is no change in behavior.

If **FILE\_FLAG\_OPEN\_REPARSE\_POINT** is specified and:

-   If an existing file is opened and it is a symbolic link, the handle returned is a handle to the symbolic link.
-   If **CREATE\_ALWAYS**, **TRUNCATE\_EXISTING**, or **FILE\_FLAG\_DELETE\_ON\_CLOSE** are specified, the file affected is a symbolic link.

If **FILE\_FLAG\_OPEN\_REPARSE\_POINT** is not specified and:

-   If an existing file is opened and it is a symbolic link, the handle returned is a handle to the target.
-   If **CREATE\_ALWAYS**, **TRUNCATE\_EXISTING**, or **FILE\_FLAG\_DELETE\_ON\_CLOSE** are specified, the file affected is the target.

## CreateHardLink and CreateHardLinkTransacted

If the path points to a symbolic link, the function creates a hard link to the target.

## DeleteFile and DeleteFileTransacted

If the path points to a symbolic link, the symbolic link is deleted, not the target. To delete a target, you must call [**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master) and specify **FILE\_FLAG\_DELETE\_ON\_CLOSE**.

## FindFirstChangeNotification

If the path points to a symbolic link, the notification handle is created for the target. If an application has registered to receive change notifications for a directory that contains symbolic links, the application is only notified when the symbolic links have been changed, not the target files.

## FindFirstFile and FindFirstFileTransacted

If the path points to a symbolic link, the [**WIN32\_FIND\_DATA**](/windows/win32/MinWinBase/ns-minwinbase-_win32_find_dataa?branch=master) buffer contains information about the symbolic link, not the target.

## FindFirstFileEx

If the path points to a symbolic link, the [**WIN32\_FIND\_DATA**](/windows/win32/MinWinBase/ns-minwinbase-_win32_find_dataa?branch=master) buffer contains information about the symbolic link, not the target.

## FindNextFile

If the path points to a symbolic link, the [**WIN32\_FIND\_DATA**](/windows/win32/MinWinBase/ns-minwinbase-_win32_find_dataa?branch=master) buffer contains information about the symbolic link, not the target.

## GetBinaryType

If the path points to a symbolic link, the target file is used.

## GetCompressedFileSize and GetCompressedFileSizeTransacted

If the path points to a symbolic link, the function returns the file size of the target.

## GetDiskFreeSpace

If the path points to a symbolic link, the operation is performed on the target.

## GetDiskFreeSpaceEx

If the path points to a symbolic link, the operation is performed on the target.

## GetFileAttributes

If the path points to a symbolic link, the function returns attributes for the symbolic link.

## GetFileAttributesEx

If the path points to a symbolic link, the function returns attributes for the symbolic link.

## GetFileSecurity

If the path points to a symbolic link, the function returns attributes for the symbolic link.

## GetTempPath

If the path points to a symbolic link, the temp path name maintains any symbolic links.

## GetVolumeInformation

If the path points to a symbolic link, the function returns volume information for the target.

## SetFileAttributes

If the path points to a symbolic link, the function retrieves attributes for the symbolic link.

## SetFileSecurity

If the path points to a symbolic link, the function returns attributes for the symbolic link.

## Related topics

<dl> <dt>

[**CopyFile**](/windows/win32/WinBase/nf-winbase-copyfile?branch=master)
</dt> <dt>

[**CopyFileTransacted**](/windows/win32/WinBase/nf-winbase-copyfiletransacteda?branch=master)
</dt> <dt>

[**CopyFileEx**](/windows/win32/WinBase/nf-winbase-copyfileexa?branch=master)
</dt> <dt>

[**CreateFile**](/windows/win32/FileAPI/nf-fileapi-createfilea?branch=master)
</dt> <dt>

[**CreateFileTransacted**](/windows/win32/WinBase/nf-winbase-createfiletransacteda?branch=master)
</dt> <dt>

[**CreateHardLink**](/windows/win32/WinBase/nf-winbase-createhardlinka?branch=master)
</dt> <dt>

[**CreateHardLinkTransacted**](/windows/win32/WinBase/nf-winbase-createhardlinktransacteda?branch=master)
</dt> <dt>

[**DeleteFile**](/windows/win32/FileAPI/nf-fileapi-deletefilea?branch=master)
</dt> <dt>

[**DeleteFileTransacted**](/windows/win32/WinBase/nf-winbase-deletefiletransacteda?branch=master)
</dt> <dt>

[**FindFirstChangeNotification**](/windows/win32/FileAPI/nf-fileapi-findfirstchangenotificationa?branch=master)
</dt> <dt>

[**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master)
</dt> <dt>

[**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master)
</dt> <dt>

[**FindFirstFileTransacted**](/windows/win32/WinBase/nf-winbase-findfirstfiletransacteda?branch=master)
</dt> <dt>

[**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master)
</dt> <dt>

[**GetBinaryType**](/windows/win32/WinBase/nf-winbase-getbinarytypea?branch=master)
</dt> <dt>

[**GetCompressedFileSize**](/windows/win32/fileapi/nf-fileapi-getcompressedfilesizea?branch=master)
</dt> <dt>

[**GetCompressedFileSizeTransacted**](/windows/win32/WinBase/nf-winbase-getcompressedfilesizetransacteda?branch=master)
</dt> <dt>

[**GetDiskFreeSpace**](/windows/win32/FileAPI/nf-fileapi-getdiskfreespacea?branch=master)
</dt> <dt>

[**GetDiskFreeSpaceEx**](/windows/win32/FileAPI/nf-fileapi-getdiskfreespaceexa?branch=master)
</dt> <dt>

[**GetFileAttributes**](/windows/win32/FileAPI/nf-fileapi-getfileattributesa?branch=master)
</dt> <dt>

[**GetFileAttributesEx**](/windows/win32/FileAPI/nf-fileapi-getfileattributesexa?branch=master)
</dt> <dt>

[**GetFileSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa446639)
</dt> <dt>

[**GetTempPath**](/windows/win32/FileAPI/nf-fileapi-gettemppatha?branch=master)
</dt> <dt>

[**GetVolumeInformation**](/windows/win32/FileAPI/nf-fileapi-getvolumeinformationa?branch=master)
</dt> <dt>

[**SetFileAttributes**](/windows/win32/FileAPI/nf-fileapi-setfileattributesa?branch=master)
</dt> <dt>

[**SetFileSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379577)
</dt> </dl>

 

 



