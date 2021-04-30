---
description: Contains the standard information attribute. This attribute is present in every base file record and must be resident.
ms.assetid: 8e668309-2722-4115-923d-bf0aa78d24f1
title: STANDARD_INFORMATION structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- STANDARD_INFORMATION
api_type: 
- NA
api_location: 
---

# STANDARD\_INFORMATION structure

\[This structure is valid only for version 3 of NTFS volumes; it may be altered in future versions.\]

Contains the standard information attribute. This attribute is present in every base file record and must be resident.

## Syntax


```C++
typedef struct _STANDARD_INFORMATION {
  UCHAR Reserved[0x30];
  ULONG OwnerId;
  ULONG SecurityId;
} STANDARD_INFORMATION, *PSTANDARD_INFORMATION;
```



## Members

<dl> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**OwnerId**
</dt> <dd>

The identifier of the file owner, from the security index.

</dd> <dt>

**SecurityId**
</dt> <dd>

The security identifier for the file.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

This structure definition is valid only for major version 3 and minor version 0 or 1, as reported by [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data).

## See also

<dl> <dt>

[Master File Table](master-file-table.md)
</dt> </dl>

 

 
