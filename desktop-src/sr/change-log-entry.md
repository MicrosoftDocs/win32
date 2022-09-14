---
title: CHANGE_LOG_ENTRY structure
description: A change log entry.
ms.assetid: adbdc6e6-895e-486d-a194-c74d2cbd0052
keywords:
- CHANGE_LOG_ENTRY structure System Restore
- PCHANGE_LOG_ENTRY structure pointer System Restore
topic_type:
- apiref
api_name:
- CHANGE_LOG_ENTRY
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CHANGE\_LOG\_ENTRY structure

\[This information applies only to Windows XP with Service Pack 2 (SP2).\]

A change log entry.

## Syntax


```C++
typedef struct _CHANGE_LOG_ENTRY {
  RECORD_HEADER RecordHeader;
  DWORD         dwMagicNum;
  DWORD         dwEntryType;
  DWORD         dwEntryFlags;
  DWORD         dwAttributes;
  INT64         i64SequenceNum;
  WCHAR         szProcName[16];
} CHANGE_LOG_ENTRY, *PCHANGE_LOG_ENTRY;
```



## Members

<dl> <dt>

**RecordHeader**
</dt> <dd>

A [**RECORD\_HEADER**](record-header.md) structure. The **dwRecordType** member should be set to **RecordTypeLogEntry** (1).

</dd> <dt>

**dwMagicNum**
</dt> <dd>

This member should be set to 0xabcdef12.

</dd> <dt>

**dwEntryType**
</dt> <dd>

This member can be one of the following values:

<dl><span id="CHANGE_LOG_ENTRYTYPES_ACLCHANGE__0x2_"></span><span id="change_log_entrytypes_aclchange__0x2_"></span><span id="CHANGE_LOG_ENTRYTYPES_ACLCHANGE__0X2_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_ACLCHANGE** (0x2)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_ATTRCHANGE__0x4_"></span><span id="change_log_entrytypes_attrchange__0x4_"></span><span id="CHANGE_LOG_ENTRYTYPES_ATTRCHANGE__0X4_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_ATTRCHANGE** (0x4)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_DIRCREATE__0x80_"></span><span id="change_log_entrytypes_dircreate__0x80_"></span><span id="CHANGE_LOG_ENTRYTYPES_DIRCREATE__0X80_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_DIRCREATE** (0x80)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_DIRRENAME__0x100_"></span><span id="change_log_entrytypes_dirrename__0x100_"></span><span id="CHANGE_LOG_ENTRYTYPES_DIRRENAME__0X100_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_DIRRENAME** (0x100)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_DIRDELETE__0x200_"></span><span id="change_log_entrytypes_dirdelete__0x200_"></span><span id="CHANGE_LOG_ENTRYTYPES_DIRDELETE__0X200_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_DIRDELETE** (0x200)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_FILECREATE__0x20_"></span><span id="change_log_entrytypes_filecreate__0x20_"></span><span id="CHANGE_LOG_ENTRYTYPES_FILECREATE__0X20_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_FILECREATE** (0x20)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_FILEDELETE__0x10_"></span><span id="change_log_entrytypes_filedelete__0x10_"></span><span id="CHANGE_LOG_ENTRYTYPES_FILEDELETE__0X10_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_FILEDELETE** (0x10)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_FILERENAME__0x40_"></span><span id="change_log_entrytypes_filerename__0x40_"></span><span id="CHANGE_LOG_ENTRYTYPES_FILERENAME__0X40_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_FILERENAME** (0x40)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_INPRECREATE__0x100000_"></span><span id="change_log_entrytypes_inprecreate__0x100000_"></span><span id="CHANGE_LOG_ENTRYTYPES_INPRECREATE__0X100000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_INPRECREATE** (0x100000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_ISDIR__0x20000_"></span><span id="change_log_entrytypes_isdir__0x20000_"></span><span id="CHANGE_LOG_ENTRYTYPES_ISDIR__0X20000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_ISDIR** (0x20000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_ISNOTDIR__0x40000_"></span><span id="change_log_entrytypes_isnotdir__0x40000_"></span><span id="CHANGE_LOG_ENTRYTYPES_ISNOTDIR__0X40000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_ISNOTDIR** (0x40000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_MOUNTCREATE__0x400_"></span><span id="change_log_entrytypes_mountcreate__0x400_"></span><span id="CHANGE_LOG_ENTRYTYPES_MOUNTCREATE__0X400_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_MOUNTCREATE** (0x400)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_MOUNTDELETE__0x800_"></span><span id="change_log_entrytypes_mountdelete__0x800_"></span><span id="CHANGE_LOG_ENTRYTYPES_MOUNTDELETE__0X800_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_MOUNTDELETE** (0x800)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_NOOPTIMIZE__0x10000_"></span><span id="change_log_entrytypes_nooptimize__0x10000_"></span><span id="CHANGE_LOG_ENTRYTYPES_NOOPTIMIZE__0X10000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_NOOPTIMIZE** (0x10000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_OPENBYID__0x200000_"></span><span id="change_log_entrytypes_openbyid__0x200000_"></span><span id="CHANGE_LOG_ENTRYTYPES_OPENBYID__0X200000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_OPENBYID** (0x200000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_SIMULATEDELETE__0x80000_"></span><span id="change_log_entrytypes_simulatedelete__0x80000_"></span><span id="CHANGE_LOG_ENTRYTYPES_SIMULATEDELETE__0X80000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_SIMULATEDELETE** (0x80000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_STREAMCHANGE__0x1_"></span><span id="change_log_entrytypes_streamchange__0x1_"></span><span id="CHANGE_LOG_ENTRYTYPES_STREAMCHANGE__0X1_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_STREAMCHANGE** (0x1)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_STREAMCREATE__0x2000_"></span><span id="change_log_entrytypes_streamcreate__0x2000_"></span><span id="CHANGE_LOG_ENTRYTYPES_STREAMCREATE__0X2000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_STREAMCREATE** (0x2000)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_STREAMOVERWRITE__0x8_"></span><span id="change_log_entrytypes_streamoverwrite__0x8_"></span><span id="CHANGE_LOG_ENTRYTYPES_STREAMOVERWRITE__0X8_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_STREAMOVERWRITE** (0x8)**
</dt><span id="CHANGE_LOG_ENTRYTYPES_VOLUMEERROR__0x1000_"></span><span id="change_log_entrytypes_volumeerror__0x1000_"></span><span id="CHANGE_LOG_ENTRYTYPES_VOLUMEERROR__0X1000_"></span><dt>

****CHANGE\_LOG\_ENTRYTYPES\_VOLUMEERROR** (0x1000)**
</dt> </dl> </dd> <dt>

**dwEntryFlags**
</dt> <dd>

This member can be one of the following values:

<dl><span id="CHANGE_LOG_ENTRYFLAGS_ACLINFO__0x4_"></span><span id="change_log_entryflags_aclinfo__0x4_"></span><span id="CHANGE_LOG_ENTRYFLAGS_ACLINFO__0X4_"></span><dt>

**CHANGE\_LOG\_ENTRYFLAGS\_ACLINFO (0x4)**
</dt><span id="CHANGE_LOG_ENTRYFLAGS_DEBUGINFO__0x8_"></span><span id="change_log_entryflags_debuginfo__0x8_"></span><span id="CHANGE_LOG_ENTRYFLAGS_DEBUGINFO__0X8_"></span><dt>

**CHANGE\_LOG\_ENTRYFLAGS\_DEBUGINFO (0x8)**
</dt><span id="CHANGE_LOG_ENTRYFLAGS_SECONDPATH__0x2_"></span><span id="change_log_entryflags_secondpath__0x2_"></span><span id="CHANGE_LOG_ENTRYFLAGS_SECONDPATH__0X2_"></span><dt>

**CHANGE\_LOG\_ENTRYFLAGS\_SECONDPATH (0x2)**
</dt><span id="CHANGE_LOG_ENTRYFLAGS_SHORTNAME__0x10_"></span><span id="change_log_entryflags_shortname__0x10_"></span><span id="CHANGE_LOG_ENTRYFLAGS_SHORTNAME__0X10_"></span><dt>

**CHANGE\_LOG\_ENTRYFLAGS\_SHORTNAME (0x10)**
</dt><span id="CHANGE_LOG_ENTRYFLAGS_TEMPPATH__0x1_"></span><span id="change_log_entryflags_temppath__0x1_"></span><span id="CHANGE_LOG_ENTRYFLAGS_TEMPPATH__0X1_"></span><dt>

**CHANGE\_LOG\_ENTRYFLAGS\_TEMPPATH (0x1)**
</dt> </dl> </dd> <dt>

**dwAttributes**
</dt> <dd>

The file attributes of the change log file. If no attributes are specified, this value should be set to 0xFFFFFFFF.

</dd> <dt>

**i64SequenceNum**
</dt> <dd>

The sequence number assigned to the change log entry.

</dd> <dt>

**szProcName**
</dt> <dd>

The name of the process making the change.

</dd> </dl>

## Remarks

This structure is followed by a variable number of variable-length data records, plus a **DWORD** value that should be identical to the value of the **dwRecordSize** member of **RecordHeader**.

The variable-length data records consist of a [**RECORD\_HEADER**](record-header.md) structure plus data that can be used to restore the change log entry. The format of the data depends on the value of the **dwRecordType** member of the **RECORD\_HEADER** structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                            |
| End of client support<br/>    | Windows XP with SP2<br/>                       |



 

 





