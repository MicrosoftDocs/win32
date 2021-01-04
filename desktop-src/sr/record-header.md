---
title: RECORD_HEADER structure
description: The record header used by the CHANGE\_LOG\_ENTRY and CHANGE\_LOG\_HEADER structures.
ms.assetid: f8d2147c-ad13-4be4-94d7-ae0ca26511da
keywords:
- RECORD_HEADER structure System Restore
- PRECORD_HEADER structure pointer System Restore
topic_type:
- apiref
api_name:
- RECORD_HEADER
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RECORD\_HEADER structure

\[This information applies only to Windows XP with Service Pack 2 (SP2).\]

The record header used by the [**CHANGE\_LOG\_ENTRY**](change-log-entry.md) and [**CHANGE\_LOG\_HEADER**](change-log-header.md) structures.

## Syntax


```C++
typedef struct _RECORD_HEADER {
  DWORD dwRecordSize;
  DWORD dwRecordType;
} RECORD_HEADER, *PRECORD_HEADER;
```



## Members

<dl> <dt>

**dwRecordSize**
</dt> <dd>

The total size of the record, including the header, in bytes.

</dd> <dt>

**dwRecordType**
</dt> <dd>

The record type. This member may be one of the following values.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RecordTypeLogHeader"></span><span id="recordtypelogheader"></span><span id="RECORDTYPELOGHEADER"></span><dl> <dt>**RecordTypeLogHeader**</dt> <dt>0</dt> </dl>     | The record is the header for the change log.<br/>                                                                                                                                                                                                                            |
| <span id="RecordTypeLogEntry"></span><span id="recordtypelogentry"></span><span id="RECORDTYPELOGENTRY"></span><dl> <dt>**RecordTypeLogEntry**</dt> <dt>1</dt> </dl>         | The record is the header for a change log entry.<br/>                                                                                                                                                                                                                        |
| <span id="RecordTypeVolumePath"></span><span id="recordtypevolumepath"></span><span id="RECORDTYPEVOLUMEPATH"></span><dl> <dt>**RecordTypeVolumePath**</dt> <dt>2</dt> </dl> | The data is the volume path for the change log entry.<br/>                                                                                                                                                                                                                   |
| <span id="RecordTypeFirstPath"></span><span id="recordtypefirstpath"></span><span id="RECORDTYPEFIRSTPATH"></span><dl> <dt>**RecordTypeFirstPath**</dt> <dt>3</dt> </dl>     | The data is the file path for the change log entry.<br/>                                                                                                                                                                                                                     |
| <span id="RecordTypeSecondPath"></span><span id="recordtypesecondpath"></span><span id="RECORDTYPESECONDPATH"></span><dl> <dt>**RecordTypeSecondPath**</dt> <dt>4</dt> </dl> | The data is used when renaming change log entries; this path is where the renamed file is stored.<br/>                                                                                                                                                                       |
| <span id="RecordTypeTempPath"></span><span id="recordtypetemppath"></span><span id="RECORDTYPETEMPPATH"></span><dl> <dt>**RecordTypeTempPath**</dt> <dt>5</dt> </dl>         | The data is the name of the backup file used to restore the change log entry. The backup files are located in the RP*n* folder. The file name has the following format: A*xxxxxxx*.*ext*, where *xxxxxxx* is a seven-digit number and *ext* is the file name extension.<br/> |
| <span id="RecordTypeAclInline"></span><span id="recordtypeaclinline"></span><span id="RECORDTYPEACLINLINE"></span><dl> <dt>**RecordTypeAclInline**</dt> <dt>6</dt> </dl>     | The data is an ACL. The data format is a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure. <br/> This value cannot be larger than 8,192 bytes. To specify a value larger than 8,192 bytes, use the **RecordTypeAclFile** member.<br/>                |
| <span id="RecordTypeAclFile"></span><span id="recordtypeaclfile"></span><span id="RECORDTYPEACLFILE"></span><dl> <dt>**RecordTypeAclFile**</dt> <dt>7</dt> </dl>             | The data is the name of the ACL file used to store the ACL. The ACL files are located in the RP*n* folder. The file name has the following format: S*xxxxxxx*.acl, where *xxxxxxx* is a seven-digit number.<br/>                                                             |
| <span id="RecordTypeDebugInfo"></span><span id="recordtypedebuginfo"></span><span id="RECORDTYPEDEBUGINFO"></span><dl> <dt>**RecordTypeDebugInfo**</dt> <dt>8</dt> </dl>     | The data is debug information for the change log entry. The data format is a **SR\_LOG\_DEBUG\_INFO** structure. For more information, see Remarks.<br/>                                                                                                                     |
| <span id="RecordTypeShortName"></span><span id="recordtypeshortname"></span><span id="RECORDTYPESHORTNAME"></span><dl> <dt>**RecordTypeShortName**</dt> <dt>9</dt> </dl>     | The data is the short name of the backup file.<br/>                                                                                                                                                                                                                          |



 

</dd> </dl>

## Remarks

The **SR\_LOG\_DEBUG\_INFO** structure is defined as follows.

``` syntax
typedef struct _SR_LOG_DEBUG_INFO {
    RECORD_HEADER Header;         // log entry header
    HANDLE ThreadId;              // thread identifier
    HANDLE ProcessId;             // process identifier
    ULARGER_INTEGER TimeStamp;    // event time stamp
    CHAR ProcesName[13];          // process name
} SR_LOG_DEBUG_INFO, *PSR_LOG_DEBUG_INFO;
```

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported<br/>                            |
| End of client support<br/>    | Windows XP with SP2<br/>                       |



 

