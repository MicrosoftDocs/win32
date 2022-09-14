---
title: CHANGE_LOG_HEADER structure
description: The change log header.
ms.assetid: 24fee9a5-b073-474f-afd5-d81f66399936
keywords:
- CHANGE_LOG_HEADER structure System Restore
- PCHANGE_LOG_HEADER structure pointer System Restore
topic_type:
- apiref
api_name:
- CHANGE_LOG_HEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CHANGE\_LOG\_HEADER structure

\[This information applies only to Windows XP with Service Pack 2 (SP2).\]

The change log header.

## Syntax


```C++
typedef struct _CHANGE_LOG_HEADER {
  RECORD_HEADER RecordHeader;
  DWORD         dwMagicNum;
  DWORD         dwLogVersion;
  RECORD_HEADER DataHeader;
  BYTE          byteData[1];
} CHANGE_LOG_HEADER, *PCHANGE_LOG_HEADER;
```



## Members

<dl> <dt>

**RecordHeader**
</dt> <dd>

A [**RECORD\_HEADER**](record-header.md) structure. The **dwRecordType** member should be set to RecordTypeLogHeader (0). The **dwRecordSize** member should account for all the members, plus the extra **DWORD** value that follows this header. For more information, see Remarks.

</dd> <dt>

**dwMagicNum**
</dt> <dd>

This member should be set to 0xabcdef12.

</dd> <dt>

**dwLogVersion**
</dt> <dd>

This member should be set to 2.

</dd> <dt>

**DataHeader**
</dt> <dd>

A [**RECORD\_HEADER**](record-header.md) structure. The **dwRecordType** member should be set to **RecordTypeVolumePath** (2).

</dd> <dt>

**byteData**
</dt> <dd>

The start of a null-terminated string that specifies the volume path.

</dd> </dl>

## Remarks

This header is followed by a **DWORD** value that should be identical to the value of the **dwRecordSize** member of **RecordHeader**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                            |
| End of client support<br/>    | Windows XP with SP2<br/>                       |



 

 





