---
description: Represents a file name attribute. A file has one file name attribute for every directory it is entered into.
ms.assetid: 54458eee-b786-446c-80bd-213c13bdeb4a
title: FILE_NAME structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FILE_NAME
api_type: 
- NA
api_location: 
---

# FILE\_NAME structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents a file name attribute. A file has one file name attribute for every directory it is entered into.

## Syntax


```C++
typedef struct _FILE_NAME {
  FILE_REFERENCE ParentDirectory;
  UCHAR          Reserved[0x38];
  UCHAR          FileNameLength;
  UCHAR          Flags;
  WCHAR          FileName[1];
} FILE_NAME, *PFILE_NAME;
```



## Members

<dl> <dt>

**ParentDirectory**
</dt> <dd>

A file reference to the directory that indexes to this name. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference.md).

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**FileNameLength**
</dt> <dd>

The length of the file name, in Unicode characters.

</dd> <dt>

**Flags**
</dt> <dd>

The file name flags.

<dl> <dt>

<span id="FILE_NAME_NTFS"></span><span id="file_name_ntfs"></span>**FILE\_NAME\_NTFS** (0x01)
</dt> <dt>

<span id="FILE_NAME_DOS"></span><span id="file_name_dos"></span>**FILE\_NAME\_DOS** (0x02)
</dt> </dl> </dd> <dt>

**FileName**
</dt> <dd>

The first character of the file name.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
