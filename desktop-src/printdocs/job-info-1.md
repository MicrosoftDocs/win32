---
description: The JOB\_INFO\_1 structure specifies print-job information such as the job-identifier value, the name of the printer for which the job is spooled, the name of the machine that created the print job, the name of the user that owns the print job, and so on.
ms.assetid: 'd42ada89-6bc7-4006-81d9-dbcc0347edd3'
title: JOB_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JOB_INFO_1
- _JOB_INFO_1A
- _JOB_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# JOB\_INFO\_1 structure

The **JOB\_INFO\_1** structure specifies print-job information such as the job-identifier value, the name of the printer for which the job is spooled, the name of the machine that created the print job, the name of the user that owns the print job, and so on.

## Syntax


```C++
typedef struct _JOB_INFO_1 {
  DWORD      JobId;
  LPTSTR     pPrinterName;
  LPTSTR     pMachineName;
  LPTSTR     pUserName;
  LPTSTR     pDocument;
  LPTSTR     pDatatype;
  LPTSTR     pStatus;
  DWORD      Status;
  DWORD      Priority;
  DWORD      Position;
  DWORD      TotalPages;
  DWORD      PagesPrinted;
  SYSTEMTIME Submitted;
} JOB_INFO_1, *PJOB_INFO_1;
```



## Members

<dl> <dt>

**JobId**
</dt> <dd>

A job identifier.

</dd> <dt>

**pPrinterName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer for which the job is spooled.

</dd> <dt>

**pMachineName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the machine that created the print job.

</dd> <dt>

**pUserName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the user that owns the print job.

</dd> <dt>

**pDocument**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print job (for example, "MS-WORD: Review.doc").

</dd> <dt>

**pDatatype**
</dt> <dd>

A pointer to a null-terminated string that specifies the type of data used to record the print job.

</dd> <dt>

**pStatus**
</dt> <dd>

A pointer to a null-terminated string that specifies the status of the print job. This member should be checked prior to *Status* and, if *pStatus* is **NULL**, the status is defined by the contents of the Status member.

</dd> <dt>

**Status**
</dt> <dd>

The job status. The value of this member can be zero or a combination of one or more of the following values. A value of zero indicates that the print queue was paused after the document finished spooling.



| Value                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JOB\_STATUS\_BLOCKED\_DEVQ      | The driver cannot print the job.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| JOB\_STATUS\_COMPLETE           | **Windows XP and later:** Job is sent to the printer, but the job may not be printed yet.<br/> See Remarks for more information.<br/>                                                                                                                                                                                                                                                                                                                           |
| JOB\_STATUS\_DELETED            | Job has been deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| JOB\_STATUS\_DELETING           | Job is being deleted.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| JOB\_STATUS\_ERROR              | An error is associated with the job.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| JOB\_STATUS\_OFFLINE            | Printer is offline.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| JOB\_STATUS\_PAPEROUT           | Printer is out of paper.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| JOB\_STATUS\_PAUSED             | Job is paused.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| JOB\_STATUS\_PRINTED            | Job has printed.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| JOB\_STATUS\_PRINTING           | Job is printing.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| JOB\_STATUS\_RESTART            | Job has been restarted.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| JOB\_STATUS\_RETAINED           | **Windows Vista and later:** Job has been retained in the print queue and cannot be deleted. This can be caused by the following:<br/> 1) The job was manually retained by a call to SetJob and the spooler is waiting for the job to be released.<br/> 2) The job has not finished printing and must finish printing before it can be automatically deleted.<br/> See [**SetJob**](setjob.md) for more information about print job commands.<br/> |
| JOB\_STATUS\_SPOOLING           | Job is spooling.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| JOB\_STATUS\_USER\_INTERVENTION | Printer has an error that requires the user to do something.                                                                                                                                                                                                                                                                                                                                                                                                                |



 

</dd> <dt>

**Priority**
</dt> <dd>

The job priority. This member can be one of the following values or in the range between 1 through 99 (MIN\_PRIORITY through MAX\_PRIORITY).



| Value         | Meaning           |
|---------------|-------------------|
| MIN\_PRIORITY | Minimum priority. |
| MAX\_PRIORITY | Maximum priority. |
| DEF\_PRIORITY | Default priority. |



 

</dd> <dt>

**Position**
</dt> <dd>

The job's position in the print queue.

</dd> <dt>

**TotalPages**
</dt> <dd>

The total number of pages that the document contains. This value may be zero if the print job does not contain page delimiting information.

</dd> <dt>

**PagesPrinted**
</dt> <dd>

The number of pages that have printed. This value may be zero if the print job does not contain page delimiting information.

</dd> <dt>

**Submitted**
</dt> <dd>

A [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure that specifies the time that this document was spooled.

This time value is in Universal Time Coordinate (UTC) format. You should convert it to a local time value before displaying it. You can use the [**FileTimeToLocalFileTime**](/windows/desktop/api/fileapi/nf-fileapi-filetimetolocalfiletime) function to perform the conversion.

</dd> </dl>

## Remarks

Port monitors that do not support TrueEndOfJob will set the job as JOB\_STATUS\_PRINTED right after the job is submitted to the printer.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_JOB\_INFO\_1W** (Unicode) and **\_JOB\_INFO\_1A** (ANSI)<br/>                                   |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumJobs**](enumjobs.md)
</dt> <dt>

[**GetJob**](getjob.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

