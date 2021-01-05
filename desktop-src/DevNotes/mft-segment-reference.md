---
description: Represents an address in the master file table (MFT). The address is tagged with a circularly reused sequence number that is set at the time the MFT segment reference was valid.
ms.assetid: 59d83b95-83fb-4630-8ce4-f58441c748ab
title: MFT_SEGMENT_REFERENCE structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MFT_SEGMENT_REFERENCE
api_type: 
- NA
api_location: 
---

# MFT\_SEGMENT\_REFERENCE structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents an address in the master file table (MFT). The address is tagged with a circularly reused sequence number that is set at the time the MFT segment reference was valid.

## Syntax


```C++
typedef struct _MFT_SEGMENT_REFERENCE {
  ULONG  SegmentNumberLowPart;
  USHORT SegmentNumberHighPart;
  USHORT SequenceNumber;
} MFT_SEGMENT_REFERENCE, *PMFT_SEGMENT_REFERENCE;
```



## Members

<dl> <dt>

**SegmentNumberLowPart**
</dt> <dd>

The low part of the segment number.

</dd> <dt>

**SegmentNumberHighPart**
</dt> <dd>

The high part of the segment number.

</dd> <dt>

**SequenceNumber**
</dt> <dd>

The nonzero sequence number. The value 0 is reserved.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

The **FILE\_REFERENCE** data type is defined as follows.

``` syntax
typedef MFT_SEGMENT_REFERENCE FILE_REFERENCE, *PFILE_REFERENCE;
```

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
