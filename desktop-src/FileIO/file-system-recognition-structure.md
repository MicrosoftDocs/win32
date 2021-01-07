---
description: Contains the on-disk file system recognition information stored in the volumes boot sector (logical disk sector zero).
ms.assetid: d9c19e01-ff82-4bbc-9eb6-aac9dc5c34ac
title: FILE_SYSTEM_RECOGNITION_STRUCTURE structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FILE_SYSTEM_RECOGNITION_STRUCTURE
api_type: 
- NA
api_location: 
---

# FILE\_SYSTEM\_RECOGNITION\_STRUCTURE structure

Contains the on-disk file system recognition information stored in the volume's boot sector (logical disk sector zero).

This is an internally-defined data structure not available in a public header and is provided here for file system developers who want to take advantage of file system recognition. For more information, see [File System Recognition](file-system-recognition.md).

## Syntax


```C++
typedef struct _FILE_SYSTEM_RECOGNITION_STRUCTURE {
  UCHAR  Jmp[3];
  UCHAR  FsName[8];
  UCHAR  MustBeZero[5];
  ULONG  Identifier;
  USHORT Length;
  USHORT Checksum;
} FILE_SYSTEM_RECOGNITION_STRUCTURE;
```



## Members

<dl> <dt>

**Jmp**
</dt> <dd>

The JMP instruction. This data member is not included in the value contained in the **Checksum** data member.

</dd> <dt>

**FsName**
</dt> <dd>

The file system name. This is a sequence of 8 ASCII characters that represents the nonlocalizable human-readable name of the file system the volume is formatted with.

This string is in the same place as the OEM file system name on a disk with a normal BIOS parameter block (BPB) structure.

</dd> <dt>

**MustBeZero**
</dt> <dd>

Reserved space that contains all zeros.

This data member overlaps what normally are the following data members in a BPB:

-   **BytesPerSector**
-   **SectorsPerCluster**
-   **ReservedSectorCount**

Because these data members are set to zero, this should be sufficient to cause earlier OSs to conclude that this is not a valid BPB and therefore recognize the volume.

</dd> <dt>

**Identifier**
</dt> <dd>

A structure identifier. Must contain the value 0x53525346 arranged in little-endian byte order.

At this point in the structure, the data is aligned to 16 bytes.

</dd> <dt>

**Length**
</dt> <dd>

The number of bytes in this structure, from the beginning to the end, including the **Jmp** data member.

</dd> <dt>

**Checksum**
</dt> <dd>

A two-byte checksum calculated over the bytes starting at the **FsName** data member and ending at the last byte of this structure, excluding the **Jmp** and **Checksum** data members.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Computing a File System Recognition Checksum](computing-a-file-system-recognition-checksum.md)
</dt> <dt>

[File System Recognition](file-system-recognition.md)
</dt> <dt>

[**FILE\_SYSTEM\_RECOGNITION\_INFORMATION**](/windows/desktop/api/WinIoCtl/ns-winioctl-file_system_recognition_information)
</dt> <dt>

[**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_file_system_recognition)
</dt> </dl>

 

