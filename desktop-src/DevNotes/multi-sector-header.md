---
description: Represents the multisector header.
ms.assetid: 0fad0e93-b940-4b52-be16-c5f177884dfb
title: MULTI_SECTOR_HEADER structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MULTI_SECTOR_HEADER
api_type: 
- NA
api_location: 
---

# MULTI\_SECTOR\_HEADER structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Represents the multisector header.

## Syntax


```C++
typedef struct _MULTI_SECTOR_HEADER {
  UCHAR  Signature[4];
  USHORT UpdateSequenceArrayOffset;
  USHORT UpdateSequenceArraySize;
} MULTI_SECTOR_HEADER, *PMULTI_SECTOR_HEADER;
```



## Members

<dl> <dt>

**Signature**
</dt> <dd>

The signature. This value is a convenience to the user.

</dd> <dt>

**UpdateSequenceArrayOffset**
</dt> <dd>

The offset to the update sequence array, from the start of this structure. The update sequence array must end before the last USHORT value in the first sector.

</dd> <dt>

**UpdateSequenceArraySize**
</dt> <dd>

The size of the update sequence array, in bytes.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

The multisector header and update sequence array provide detection of incomplete multisector transfers for devices that either have a physical sector size greater than or equal to the sequence number stride (512) or that do not transfer sectors out of order. If a device exists that has a sector size smaller than the sequence number stride and it sometimes transfers sectors out of order, then the update sequence array will not provide absolute detection of incomplete transfers. The sequence number stride is set to a small enough number to provide absolute protection for all known hard disks. It is not set any smaller or there might be excessive run time or space overhead.

The update sequence array consists of an array of *n* **USHORT** values, where *n* is the size of the structure being protected divided by the sequence number stride. The first word contains the update sequence number, which is a cyclical counter of the number of times the containing structure has been written to disk. Next are the *n* saved **USHORT** values that were overwritten by the update sequence number the last time the containing structure was written to disk.

Each time the protected structure is about to be written to disk, the last word in each sequence number stride is saved to its respective position in the sequence number array, then it is overwritten with the next update sequence number. After the write, or whenever the structure is read, the saved word from the sequence number array is restored to its actual position in the structure. Before restoring the saved words on reads, all the sequence numbers at the end of each stride are compared with the actual sequence number at the start of the array. If any of these comparisons are not equal, then a failed multisector transfer has been detected.

The size of the array is determined by the size of the containing structure. The update sequence array should be included at the end of the header of the structure it is protecting because of its variable size. The user must ensure that the correct space is reserved for the containing structure: (size of structure / 512 + 1) \* sizeof(USHORT).

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
