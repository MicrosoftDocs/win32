---
description: Represents the file record segment. This is the header for each file record segment in the master file table (MFT).
ms.assetid: 4548ad49-1924-4888-8966-c45f8e453c6f
title: FILE_RECORD_SEGMENT_HEADER structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FILE_RECORD_SEGMENT_HEADER
api_type: 
- NA
api_location: 
---

# FILE\_RECORD\_SEGMENT\_HEADER structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents the file record segment. This is the header for each file record segment in the master file table (MFT).

## Syntax


```C++
typedef struct _FILE_RECORD_SEGMENT_HEADER {
  MULTI_SECTOR_HEADER   MultiSectorHeader;
  ULONGLONG             Reserved1;
  USHORT                SequenceNumber;
  USHORT                Reserved2;
  USHORT                FirstAttributeOffset;
  USHORT                Flags;
  ULONG                 Reserved3[2];
  FILE_REFERENCE        BaseFileRecordSegment;
  USHORT                Reserved4;
  UPDATE_SEQUENCE_ARRAY UpdateSequenceArray;
} FILE_RECORD_SEGMENT_HEADER, *PFILE_RECORD_SEGMENT_HEADER;
```



## Members

<dl> <dt>

**MultiSectorHeader**
</dt> <dd>

The multisector header defined by the cache manager. The [**MULTI\_SECTOR\_HEADER**](multi-sector-header.md) structure always contains the signature "FILE" and a description of the location and size of the update sequence array.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**SequenceNumber**
</dt> <dd>

The sequence number. This value is incremented each time that a file record segment is freed; it is 0 if the segment is not used. The **SequenceNumber** field of a file reference must match the contents of this field; if they do not match, the file reference is incorrect and probably obsolete.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**FirstAttributeOffset**
</dt> <dd>

The offset of the first attribute record, in bytes.

</dd> <dt>

**Flags**
</dt> <dd>

The file flags.

<dl> <dt>

<span id="FILE_RECORD_SEGMENT_IN_USE"></span><span id="file_record_segment_in_use"></span>**FILE\_RECORD\_SEGMENT\_IN\_USE** (0x0001)
</dt> <dt>

<span id="FILE_FILE_NAME_INDEX_PRESENT"></span><span id="file_file_name_index_present"></span>**FILE\_FILE\_NAME\_INDEX\_PRESENT** (0x0002)
</dt> </dl> </dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**BaseFileRecordSegment**
</dt> <dd>

A file reference to the base file record segment for this file. If this is the base file record, the value is 0. See [**MFT\_SEGMENT\_REFERENCE**](mft-segment-reference.md).

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved.

</dd> <dt>

**UpdateSequenceArray**
</dt> <dd>

The update sequence array to protect multisector transfers of the file record segment.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
