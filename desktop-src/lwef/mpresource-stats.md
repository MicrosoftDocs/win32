---
title: MPRESOURCE_STATS structure (MpClient.h)
description: Resource-related statistics.
ms.assetid: D1DC4BC9-911D-448C-A421-11D2F51F0A61
keywords:
- MPRESOURCE_STATS structure Legacy Windows Environment Features
- PMPRESOURCE_STATS structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPRESOURCE_STATS
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPRESOURCE\_STATS structure

Resource-related statistics.

## Syntax


```C++
typedef struct tagMPRESOURCE_STATS {
  DWORD  PPMProgress;
  UINT64 ProcessCount;
  UINT64 FileCount;
  UINT64 FileBytesCount;
  UINT64 RegKeyCount;
  UINT64 Reserved[4];
} MPRESOURCE_STATS, *PMPRESOURCE_STATS;
```



## Members

<dl> <dt>

**PPMProgress**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Approximate progress for scan in ppm (parts per million). Set to **MPPROGRESS\_INVALID** if progress information is not available.

</dd> <dt>

**ProcessCount**
</dt> <dd>

Type: **UINT64**

</dd> <dd>

Number of processes scanned.

</dd> <dt>

**FileCount**
</dt> <dd>

Type: **UINT64**

</dd> <dd>

Number of files scanned.

</dd> <dt>

**FileBytesCount**
</dt> <dd>

Type: **UINT64**

</dd> <dd>

Number of bytes scanned for files.

</dd> <dt>

**RegKeyCount**
</dt> <dd>

Type: **UINT64**

</dd> <dd>

Number of RegKeys scanned.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **UINT64\[4\]**

</dd> <dd>

Fields reserved for future use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





