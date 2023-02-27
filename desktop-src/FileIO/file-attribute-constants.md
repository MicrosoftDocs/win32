---
description: File attributes are metadata values stored by the file system on disk and are used by the system and are available to developers via various file I/O APIs.
ms.assetid: ed9a73d2-7fb6-4fb7-97f6-4dbf89e2f156
title: File Attribute Constants (WinNT.h)
ms.topic: reference
ms.custom: snippet-project
ms.date: 02/27/2023
---

# File Attribute Constants

File attributes are metadata values stored by the file system on disk and are used by the system and are available to developers via various file I/O APIs. For a list of related APIs and topics, see the See Also section.

## Example

```cpp
FILE_BASIC_INFO basicInfo;
    BOOL result;

    result = GetFileInformationByHandleEx( hFile,
                                               FileBasicInfo,
                                               &basicInfo,
                                               sizeof(basicInfo));

\\...

printf("  File Attributes: ");
    PrintFileAttributes(basicInfo.FileAttributes);

\\...
VOID
PrintFileAttributes(
    ULONG FileAttributes
    )
{
    
    if (FileAttributes & FILE_ATTRIBUTE_ARCHIVE) {
        printf("Archive ");
    }
    if (FileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
        printf("Directory ");
    }
    if (FileAttributes & FILE_ATTRIBUTE_READONLY) {
        printf("Read-Only ");
    }
}
```

Example taken from a [Windows Classic Sample](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/winbase/io/extendedfileapis/ExtendedFileAPIs.cpp) on GitHub.

| Constant/value | Description |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FILE_ATTRIBUTE_READONLY"></span><span id="file_attribute_readonly"></span><dl> <dt>**FILE\_ATTRIBUTE\_READONLY**</dt> <dt>1 (0x00000001)</dt> </dl> | A file that is read-only. Applications can read the file, but cannot write to it or delete it. This attribute is not honored on directories. For more information, see [You cannot view or change the Read-only or the System attributes of folders in Windows Server 2003, in Windows XP, in Windows Vista or in Windows 7](https://support.microsoft.com/kb/326549). |
| <span id="FILE_ATTRIBUTE_HIDDEN"></span><span id="file_attribute_hidden"></span><dl> <dt>**FILE\_ATTRIBUTE\_HIDDEN**</dt> <dt>2 (0x00000002)</dt> </dl> | The file or directory is hidden. It is not included in an ordinary directory listing. |
| <span id="FILE_ATTRIBUTE_SYSTEM"></span><span id="file_attribute_system"></span><dl> <dt>**FILE\_ATTRIBUTE\_SYSTEM**</dt> <dt>4 (0x00000004)</dt> </dl> | A file or directory that the operating system uses a part of, or uses exclusively. |
| <span id="FILE_ATTRIBUTE_DIRECTORY"></span><span id="file_attribute_directory"></span><dl> <dt>**FILE\_ATTRIBUTE\_DIRECTORY**</dt> <dt>16 (0x00000010)</dt> </dl> | The handle that identifies a directory. |
| <span id="FILE_ATTRIBUTE_ARCHIVE"></span><span id="file_attribute_archive"></span><dl> <dt>**FILE\_ATTRIBUTE\_ARCHIVE**</dt> <dt>32 (0x00000020)</dt> </dl> | A file or directory that is an archive file or directory. Applications typically use this attribute to mark files for backup or removal. |
| <span id="FILE_ATTRIBUTE_DEVICE"></span><span id="file_attribute_device"></span><dl> <dt>**FILE\_ATTRIBUTE\_DEVICE**</dt> <dt>64 (0x00000040)</dt> </dl> | This value is reserved for system use. |
| <span id="FILE_ATTRIBUTE_NORMAL"></span><span id="file_attribute_normal"></span><dl> <dt>**FILE\_ATTRIBUTE\_NORMAL**</dt> <dt>128 (0x00000080)</dt> </dl> | A file that does not have other attributes set. This attribute is valid only when used alone. |
| <span id="FILE_ATTRIBUTE_TEMPORARY"></span><span id="file_attribute_temporary"></span><dl> <dt>**FILE\_ATTRIBUTE\_TEMPORARY**</dt> <dt>256 (0x00000100)</dt> </dl> | A file that is being used for temporary storage. File systems avoid writing data back to mass storage if sufficient cache memory is available, because typically, an application deletes a temporary file after the handle is closed. In that scenario, the system can entirely avoid writing the data. Otherwise, the data is written after the handle is closed. |
| <span id="FILE_ATTRIBUTE_SPARSE_FILE"></span><span id="file_attribute_sparse_file"></span><dl> <dt>**FILE\_ATTRIBUTE\_SPARSE\_FILE**</dt> <dt>512 (0x00000200)</dt> </dl> | A file that is a sparse file. |
| <span id="FILE_ATTRIBUTE_REPARSE_POINT"></span><span id="file_attribute_reparse_point"></span><dl> <dt>**FILE\_ATTRIBUTE\_REPARSE\_POINT**</dt> <dt>1024 (0x00000400)</dt> </dl> | A file or directory that has an associated reparse point, or a file that is a symbolic link. |
| <span id="FILE_ATTRIBUTE_COMPRESSED"></span><span id="file_attribute_compressed"></span><dl> <dt>**FILE\_ATTRIBUTE\_COMPRESSED**</dt> <dt>2048 (0x00000800)</dt> </dl> | A file or directory that is compressed. For a file, all of the data in the file is compressed. For a directory, compression is the default for newly created files and subdirectories. |
| <span id="FILE_ATTRIBUTE_OFFLINE"></span><span id="file_attribute_offline"></span><dl> <dt>**FILE\_ATTRIBUTE\_OFFLINE**</dt> <dt>4096 (0x00001000)</dt> </dl> | The data of a file is not available immediately. This attribute indicates that the file data is physically moved to offline storage. This attribute is used by Remote Storage, which is the hierarchical storage management software. Applications should not arbitrarily change this attribute. |
| <span id="FILE_ATTRIBUTE_NOT_CONTENT_INDEXED"></span><span id="file_attribute_not_content_indexed"></span><dl> <dt>**FILE\_ATTRIBUTE\_NOT\_CONTENT\_INDEXED**</dt> <dt>8192 (0x00002000)</dt> </dl> | The file or directory is not to be indexed by the content indexing service. |
| <span id="FILE_ATTRIBUTE_ENCRYPTED"></span><span id="file_attribute_encrypted"></span><dl> <dt>**FILE\_ATTRIBUTE\_ENCRYPTED**</dt> <dt>16384 (0x00004000)</dt> </dl> | A file or directory that is encrypted. For a file, all data streams in the file are encrypted. For a directory, encryption is the default for newly created files and subdirectories. |
| <span id="FILE_ATTRIBUTE_INTEGRITY_STREAM"></span><span id="file_attribute_integrity_stream"></span><dl> <dt>**FILE\_ATTRIBUTE\_INTEGRITY\_STREAM**</dt> <dt>32768 (0x00008000)</dt> </dl> | The directory or user data stream is configured with integrity (only supported on ReFS volumes). It is not included in an ordinary directory listing. The integrity setting persists with the file if it's renamed. If a file is copied the destination file will have integrity set if either the source file or destination directory have integrity set.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This flag is not supported until Windows Server 2012. |
| <span id="FILE_ATTRIBUTE_VIRTUAL"></span><span id="file_attribute_virtual"></span><dl> <dt>**FILE\_ATTRIBUTE\_VIRTUAL**</dt> <dt>65536 (0x00010000)</dt> </dl> | This value is reserved for system use. |
| <span id="FILE_ATTRIBUTE_NO_SCRUB_DATA"></span><span id="file_attribute_no_scrub_data"></span><dl> <dt>**FILE\_ATTRIBUTE\_NO\_SCRUB\_DATA**</dt> <dt>131072 (0x00020000)</dt> </dl> | The user data stream not to be read by the background data integrity scanner (AKA scrubber). When set on a directory it only provides inheritance. This flag is only supported on Storage Spaces and ReFS volumes. It is not included in an ordinary directory listing.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This flag is not supported until Windows 8 and Windows Server 2012. |
| <span id="FILE_ATTRIBUTE_EA"></span><span id="file_attribute_ea"></span><dl> <dt>**FILE\_ATTRIBUTE\_EA**</dt> <dt>262144 (0x00040000)</dt> </dl> | A file or directory with extended attributes. |
| <span id="FILE_ATTRIBUTE_PINNED"></span><span id="file_attribute_pinned"></span><dl> <dt>**FILE\_ATTRIBUTE\_PINNED**</dt> <dt>524288 (0x00080000)</dt> </dl> | This attribute indicates user intent that the file or directory should be kept fully present locally even when not being actively accessed. This attribute is for use with hierarchical storage management software. |
| <span id="FILE_ATTRIBUTE_UNPINNED"></span><span id="file_attribute_unpinned"></span><dl> <dt>**FILE\_ATTRIBUTE\_UNPINNED**</dt> <dt>1048576 (0x00100000)</dt> </dl> | This attribute indicates that the file or directory should not be kept fully present locally except when being actively accessed. This attribute is for use with hierarchical storage management software. |
| <span id="FILE_ATTRIBUTE_RECALL_ON_OPEN"></span><span id="file_attribute_recall_on_open"></span><dl> <dt>**FILE\_ATTRIBUTE\_RECALL\_ON\_OPEN**</dt> <dt>262144 (0x00040000)</dt> </dl> | This attribute only appears in directory enumeration classes (FILE\_DIRECTORY\_INFORMATION, FILE\_BOTH\_DIR\_INFORMATION, etc.). When this attribute is set, it means that the file or directory has no physical representation on the local system; the item is virtual. Opening the item will be more expensive than normal, e.g. it will cause at least some of it to be fetched from a remote store. |
| <span id="FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS"></span><span id="file_attribute_recall_on_data_access"></span><dl> <dt>**FILE\_ATTRIBUTE\_RECALL\_ON\_DATA\_ACCESS**</dt> <dt>4194304 (0x00400000)</dt> </dl> | When this attribute is set, it means that the file or directory is not fully present locally. For a file that means that not all of its data is on local storage (e.g. it may be sparse with some data still in remote storage). For a directory it means that some of the directory contents are being virtualized from another location. Reading the file / enumerating the directory will be more expensive than normal, e.g. it will cause at least some of the file/directory content to be fetched from a remote store. Only kernel-mode callers can set this bit.<br/> File system mini filters below the 180000 – 189999 altitude range (FSFilter HSM Load Order Group) must not issue targeted cached reads or writes to files that have this attribute set. This could lead to cache pollution and potential file corruption. More information can be found [here](/windows-hardware/drivers/ifs/placeholders_guidance).  |

## Requirements

| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\] |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header | WinNT.h (include Windows.h) |

## See also

[Compression Attribute](compression-attribute.md)

[Creating and Opening Files](creating-and-opening-files.md)

[CreateFile](/windows/win32/api/FileAPI/nf-fileapi-createfilea)

[CreateFileTransacted](/windows/win32/api/WinBase/nf-winbase-createfiletransacteda)

[GetFileAttributes](/windows/win32/api/FileAPI/nf-fileapi-getfileattributesa)

[GetFileAttributesEx](/windows/win32/api/FileAPI/nf-fileapi-getfileattributesexa)

[GetFileAttributesTransacted](/windows/win32/api/WinBase/nf-winbase-getfileattributestransacteda)

[GetFileInformationByHandle](/windows/win32/api/FileAPI/nf-fileapi-getfileinformationbyhandle)

[GetFileInformationByHandleEx](/windows/win32/api/WinBase/nf-winbase-getfileinformationbyhandleex)

[SetFileAttributes](/windows/win32/api/FileAPI/nf-fileapi-setfileattributesa)

[SetFileAttributesTransacted](/windows/win32/api/WinBase/nf-winbase-setfileattributestransacteda)

[SetFileInformationByHandle](/windows/win32/api/FileAPI/nf-fileapi-setfileinformationbyhandle)
