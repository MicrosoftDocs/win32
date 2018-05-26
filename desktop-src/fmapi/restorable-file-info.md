---
title: RESTORABLE\_FILE\_INFO structure
description: Provides information about a restorable file. This structure is used when calling ScanRestorableFiles.
ms.assetid: c54eb086-159e-4649-a92d-cb2a026d6ec2
keywords:
- RESTORABLE_FILE_INFO structure Files
- PRESTORABLE_FILE_INFO structure pointer Files
topic_type:
- apiref
api_name:
- RESTORABLE_FILE_INFO
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RESTORABLE\_FILE\_INFO structure

Provides information about a restorable file. This structure is used when calling [**ScanRestorableFiles**](scanrestorablefiles.md).

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef struct _RESTORABLE_FILE_INFO {
  ULONG     Size;
  DWORD     Version;
  ULONGLONG FileSize;
  FILETIME  CreationTime;
  FILETIME  LastAccessTime;
  FILETIME  LastWriteTime;
  DWORD     Attributes;
  BOOL      IsRemoved;
  LONGLONG  ClustersUsedByFile;
  LONGLONG  ClustersCurrentlyInUse;
  ULONG     RestoreDataOffset;
  WCHAR     FileName[1];
} RESTORABLE_FILE_INFO, *PRESTORABLE_FILE_INFO;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of the structure, in bytes.

</dd> <dt>

**Version**
</dt> <dd>

The major and minor version of the file.

</dd> <dt>

**FileSize**
</dt> <dd>

The size of the file.

</dd> <dt>

**CreationTime**
</dt> <dd>

The time the file was created. See [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284).

</dd> <dt>

**LastAccessTime**
</dt> <dd>

The time the file was last accessed.

</dd> <dt>

**LastWriteTime**
</dt> <dd>

The time the file was last modified.

</dd> <dt>

**Attributes**
</dt> <dd>

The attributes for the file. This member can be a combination of one or more of the following values.



| Attribute                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FILE_ATTRIBUTE_ARCHIVE"></span><span id="file_attribute_archive"></span><dl> <dt>**FILE\_ATTRIBUTE\_ARCHIVE**</dt> </dl>                    | The file or directory is an archive file. Applications use this attribute to mark files for backup or removal.<br/>                                                                                                                                                                                                                                                 |
| <span id="FILE_ATTRIBUTE_COMPRESSED"></span><span id="file_attribute_compressed"></span><dl> <dt>**FILE\_ATTRIBUTE\_COMPRESSED**</dt> </dl>           | The file or directory is compressed. For a file, this means that all of the data in the file is compressed. For a directory, this means that compression is the default for newly created files and subdirectories.<br/>                                                                                                                                            |
| <span id="FILE_ATTRIBUTE_DIRECTORY"></span><span id="file_attribute_directory"></span><dl> <dt>**FILE\_ATTRIBUTE\_DIRECTORY**</dt> </dl>              | The handle identifies a directory.<br/>                                                                                                                                                                                                                                                                                                                             |
| <span id="FILE_ATTRIBUTE_ENCRYPTED"></span><span id="file_attribute_encrypted"></span><dl> <dt>**FILE\_ATTRIBUTE\_ENCRYPTED**</dt> </dl>              | The file or directory is encrypted. For a file, this means that all data in the file is encrypted. For a directory, this means that encryption is the default for newly created files and subdirectories.<br/>                                                                                                                                                      |
| <span id="FILE_ATTRIBUTE_HIDDEN"></span><span id="file_attribute_hidden"></span><dl> <dt>**FILE\_ATTRIBUTE\_HIDDEN**</dt> </dl>                       | The file or directory is hidden. It is not included in an ordinary directory listing.<br/>                                                                                                                                                                                                                                                                          |
| <span id="FILE_ATTRIBUTE_NORMAL"></span><span id="file_attribute_normal"></span><dl> <dt>**FILE\_ATTRIBUTE\_NORMAL**</dt> </dl>                       | The file does not have other attributes. This attribute is valid only if used alone.<br/>                                                                                                                                                                                                                                                                           |
| <span id="FILE_ATTRIBUTE_OFFLINE"></span><span id="file_attribute_offline"></span><dl> <dt>**FILE\_ATTRIBUTE\_OFFLINE**</dt> </dl>                    | The file data is not available immediately. This attribute indicates that the file data is physically moved to offline storage. This attribute is used by Remote Storage, the hierarchical storage management software. Applications should not arbitrarily change this attribute.<br/>                                                                             |
| <span id="FILE_ATTRIBUTE_READONLY"></span><span id="file_attribute_readonly"></span><dl> <dt>**FILE\_ATTRIBUTE\_READONLY**</dt> </dl>                 | The file or directory is read-only. Applications can read the file, but cannot write to it or delete it. If it is a directory, applications cannot delete it.<br/>                                                                                                                                                                                                  |
| <span id="FILE_ATTRIBUTE_REPARSE_POINT"></span><span id="file_attribute_reparse_point"></span><dl> <dt>**FILE\_ATTRIBUTE\_REPARSE\_POINT**</dt> </dl> | The file or directory has an associated reparse point.<br/>                                                                                                                                                                                                                                                                                                         |
| <span id="FILE_ATTRIBUTE_SPARSE_FILE"></span><span id="file_attribute_sparse_file"></span><dl> <dt>**FILE\_ATTRIBUTE\_SPARSE\_FILE**</dt> </dl>       | The file is a sparse file.<br/>                                                                                                                                                                                                                                                                                                                                     |
| <span id="FILE_ATTRIBUTE_SYSTEM"></span><span id="file_attribute_system"></span><dl> <dt>**FILE\_ATTRIBUTE\_SYSTEM**</dt> </dl>                       | The file or directory is part of the operating system or is used exclusively by the operating system.<br/>                                                                                                                                                                                                                                                          |
| <span id="FILE_ATTRIBUTE_TEMPORARY"></span><span id="file_attribute_temporary"></span><dl> <dt>**FILE\_ATTRIBUTE\_TEMPORARY**</dt> </dl>              | The file is being used for temporary storage. File systems avoid writing data back to mass storage if sufficient cache memory is available, because often the application deletes the temporary file after the handle is closed. In that case, the system can entirely avoid writing the data. Otherwise, the data will be written after the handle is closed.<br/> |
| <span id="FILE_ATTRIBUTE_VIRTUAL"></span><span id="file_attribute_virtual"></span><dl> <dt>**FILE\_ATTRIBUTE\_VIRTUAL**</dt> </dl>                    | A file is a virtual file.<br/>                                                                                                                                                                                                                                                                                                                                      |



 

</dd> <dt>

**IsRemoved**
</dt> <dd>

**TRUE** if the file has been removed; otherwise, **FALSE**.

</dd> <dt>

**ClustersUsedByFile**
</dt> <dd>

The number of clusters that the file allocates. This member is used in conjunction with **ClustersCurrentlyInUse** to determine the percentage of file data that can be recovered.

</dd> <dt>

**ClustersCurrentlyInUse**
</dt> <dd>

The number of clusters that are marked as used for the file in the volume bitmap.

</dd> <dt>

**RestoreDataOffset**
</dt> <dd>

The offset from the beginning of the structure to the Binary Large Object (BLOB) that is used by [**RestoreFile**](restorefile.md).

</dd> <dt>

**FileName**
</dt> <dd>

The full path of the file.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

The **FileName** member is variable in length. An additional implementation-specific BLOB is added after the name of the file. The location of the BLOB is determined by **RestoreDataOffset**.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**RestoreFile**](restorefile.md)
</dt> <dt>

[**ScanRestorableFiles**](scanrestorablefiles.md)
</dt> </dl>

 

 





