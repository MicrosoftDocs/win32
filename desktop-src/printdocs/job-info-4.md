---
description: Describes a full set of values associated with a job and supports large spool files with sizes expressed with 64 bits.
ms.assetid: 90932ae2-ea9e-43bc-9a1d-c68223f6d0ee
title: JOB_INFO_4 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- JOB_INFO_4
- _JOB_INFO_4A
- _JOB_INFO_4W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# JOB\_INFO\_4 structure

Describes a full set of values associated with a job and supports large spool files with sizes expressed with 64 bits.

## Syntax


```C++
typedef struct _JOB_INFO_4 {
  DWORD                JobId;
  LPTSTR               pPrinterName;
  LPTSTR               pMachineName;
  LPTSTR               pUserName;
  LPTSTR               pDocument;
  LPTSTR               pNotifyName;
  LPTSTR               pDatatype;
  LPTSTR               pPrintProcessor;
  LPTSTR               pParameters;
  LPTSTR               pDriverName;
  LPDEVMODE            pDevMode;
  LPTSTR               pStatus;
  PSECURITY_DESCRIPTOR pSecurityDescriptor;
  DWORD                Status;
  DWORD                Priority;
  DWORD                Position;
  DWORD                StartTime;
  DWORD                UntilTime;
  DWORD                TotalPages;
  DWORD                Size;
  SYSTEMTIME           Submitted;
  DWORD                Time;
  DWORD                PagesPrinted;
  LONG                 SizeHigh;
} JOB_INFO_4, *PJOB_INFO_4;
```



## Members

<dl> <dt>

**JobId**
</dt> <dd>

A job identifier value.

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

A pointer to a null-terminated string that specifies the name of the user who owns the print job.

</dd> <dt>

**pDocument**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print job (for example, "MS-WORD: Review.doc").

</dd> <dt>

**pNotifyName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the user who should be notified when the job has been printed, or when an error occurs while printing the job.

</dd> <dt>

**pDatatype**
</dt> <dd>

A pointer to a null-terminated string that specifies the type of data used to record the print job.

</dd> <dt>

**pPrintProcessor**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the print processor that should be used to print the job.

</dd> <dt>

**pParameters**
</dt> <dd>

A pointer to a null-terminated string that specifies print-processor parameters.

</dd> <dt>

**pDriverName**
</dt> <dd>

A pointer to a null-terminated string that specifies the name of the printer driver that should be used to process the print job.

</dd> <dt>

**pDevMode**
</dt> <dd>

A pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that contains device-initialization and environment data for the printer driver.

</dd> <dt>

**pStatus**
</dt> <dd>

A pointer to a null-terminated string that specifies the status of the print job. This member should be checked prior to **Status** and, if **pStatus** is **NULL**, the status is defined by the contents of the Status member.

</dd> <dt>

**pSecurityDescriptor**
</dt> <dd>

The value of this member is **NULL**. Retrieval and setting of document security descriptors is not supported in this release.

</dd> <dt>

**Status**
</dt> <dd>

The job status. This member can be one or more of the following values:

| Value                           | Meaning                                                      |
|---------------------------------|--------------------------------------------------------------|
| JOB\_STATUS\_BLOCKED\_DEVQ      | The driver cannot print the job.                             |
| JOB\_STATUS\_DELETED            | Job has been deleted.                                        |
| JOB\_STATUS\_DELETING           | Job is being deleted.                                        |
| JOB\_STATUS\_ERROR              | An error is associated with the job.                         |
| JOB\_STATUS\_OFFLINE            | Printer is offline.                                          |
| JOB\_STATUS\_PAPEROUT           | Printer is out of paper.                                     |
| JOB\_STATUS\_PAUSED             | Job is paused.                                               |
| JOB\_STATUS\_PRINTED            | Job has printed.                                             |
| JOB\_STATUS\_PRINTING           | Job is printing.                                             |
| JOB\_STATUS\_RESTART            | Job has been restarted.                                      |
| JOB\_STATUS\_SPOOLING           | Job is spooling.                                             |
| JOB\_STATUS\_USER\_INTERVENTION | Printer has an error that requires the user to do something. |



 

In Windows XP and later versions of Windows, the following values can also be used:

| Value                 | Meaning                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------|
| JOB\_STATUS\_COMPLETE | The job is sent to the printer, but may not be printed yet. See Remarks for more information. |
| JOB\_STATUS\_RETAINED | The job has been retained in the print queue following printing.                              |



 

</dd> <dt>

**Priority**
</dt> <dd>

The job priority. This member can be one of the following values, or in the range between 1 through 99 (MIN\_PRIORITY through MAX\_PRIORITY).



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

**StartTime**
</dt> <dd>

The earliest time that the job can be printed.

</dd> <dt>

**UntilTime**
</dt> <dd>

The latest time that the job can be printed.

</dd> <dt>

**TotalPages**
</dt> <dd>

The number of pages required for the job. This value may be zero if the print job does not contain page delimiting information.

</dd> <dt>

**Size**
</dt> <dd>

The lower four bytes of the size, in bytes, of the job. See also the **SizeHigh** member below.

</dd> <dt>

**Submitted**
</dt> <dd>

A [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure that specifies the time when the job was submitted.

This time value is in Universal Time Coordinate (UTC) format. You should convert it to a local time value before displaying it. You can use the [**FileTimeToLocalFileTime**](/windows/desktop/api/fileapi/nf-fileapi-filetimetolocalfiletime) function to perform the conversion.

</dd> <dt>

**Time**
</dt> <dd>

The total time, in milliseconds, that has elapsed since the job began printing.

</dd> <dt>

**PagesPrinted**
</dt> <dd>

The number of pages that have printed. This value may be zero if the print job does not contain page delimiting information.

</dd> <dt>

**SizeHigh**
</dt> <dd>

The higher four bytes of the size, in bytes, of the job. See also the **Size** member above.

</dd> </dl>

## Remarks

Port monitors that do not support TrueEndOfJob will set the job as JOB\_STATUS\_PRINTED immediately after the job is submitted to the printer.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Winspool.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_JOB\_INFO\_4W** (Unicode) and **\_JOB\_INFO\_4A** (ANSI)<br/>               |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> <dt>

[**EnumJobs**](enumjobs.md)
</dt> <dt>

[**GetJob**](getjob.md)
</dt> <dt>

[**SetJob**](setjob.md)
</dt> </dl>

 

