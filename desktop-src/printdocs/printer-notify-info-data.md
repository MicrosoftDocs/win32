---
description: The PRINTER\_NOTIFY\_INFO\_DATA structure identifies a job or printer information field and provides the current data for that field.
ms.assetid: 7a7b9e01-32e0-47f8-a5b1-5f7e6a663714
title: PRINTER_NOTIFY_INFO_DATA structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_NOTIFY_INFO_DATA,
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_NOTIFY\_INFO\_DATA structure

The **PRINTER\_NOTIFY\_INFO\_DATA** structure identifies a job or printer information field and provides the current data for that field.

The [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function returns a [**PRINTER\_NOTIFY\_INFO**](printer-notify-info.md) structure, which contains an array of **PRINTER\_NOTIFY\_INFO\_DATA** structures.

## Syntax


```C++
typedef struct _PRINTER_NOTIFY_INFO_DATA {
  WORD  Type;
  WORD  Field;
  DWORD Reserved;
  DWORD Id;
  union {
    DWORD  adwData[2];
    struct {
      DWORD  cbBuf;
      LPVOID pBuf;
    } Data;
  } NotifyData;
} PRINTER_NOTIFY_INFO_DATA, *PPRINTER_NOTIFY_INFO_DATA; ;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Indicates the type of information provided. This member can be one of the following values.



| Value                                                                                                                                                                                                                                      | Meaning                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <span id="JOB_NOTIFY_TYPE"></span><span id="job_notify_type"></span><dl> <dt>**JOB\_NOTIFY\_TYPE**</dt> <dt>0x01</dt> </dl>             | Indicates that the **Field** member specifies a JOB\_NOTIFY\_FIELD\_\* constant.<br/>     |
| <span id="PRINTER_NOTIFY_TYPE"></span><span id="printer_notify_type"></span><dl> <dt>**PRINTER\_NOTIFY\_TYPE**</dt> <dt>0x00</dt> </dl> | Indicates that the **Field** member specifies a PRINTER\_NOTIFY\_FIELD\_\* constant.<br/> |



 

</dd> <dt>

**Field**
</dt> <dd>

Indicates the field that changed. For a list of possible values, see the Remarks section.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Id**
</dt> <dd>

Indicates the job identifier if the **Type** member specifies JOB\_NOTIFY\_TYPE. If the **Type** member specifies PRINTER\_NOTIFY\_TYPE, this member is undefined.

</dd> <dt>

**NotifyData**
</dt> <dd>

A union of data information based on the **Type** and **Field** members. For a description of the type of data associated with each field, see the Remarks section.

<dl> <dt>

**adwData\[2\]**
</dt> <dd>

An array of two **DWORD** values. For information fields that use only a single **DWORD**, the data is in **adwData** \[0\].

</dd> <dt>

**Data**
</dt> <dd> <dl> <dt>

**cbBuf**
</dt> <dd>

Indicates the size, in bytes, of the buffer pointed to by **pBuf**.

</dd> <dt>

**pBuf**
</dt> <dd>

Pointer to a buffer that contains the field's current data.

</dd> </dl> </dd> </dl> </dd> </dl>

## Remarks

If the **Type** member specifies PRINTER\_NOTIFY\_TYPE, the **Field** member can be one of the following values.



<table>
<thead>
<tr class="header">
<th>Field</th>
<th>Type of data</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_SERVER_NAME</td>
<td>Not supported.</td>
<td>0x00</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_PRINTER_NAME</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string containing the name of the printer.</td>
<td>0x01</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_SHARE_NAME</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string that identifies the share point for the printer.</td>
<td>0x02</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_PORT_NAME</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string containing the name of the port that the print jobs will be printed to. If &quot;Printer Pooling&quot; is selected, this is a comma separated list of ports.</td>
<td>0x03</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_DRIVER_NAME</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string containing the name of the printer's driver.</td>
<td>0x04</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_COMMENT</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string containing the new comment string, which is typically a brief description of the printer.</td>
<td>0x05</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_LOCATION</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string containing the new physical location of the printer (for example, &quot;Bldg. 38, Room 1164&quot;).</td>
<td>0x06</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_DEVMODE</td>
<td><strong>pBuf</strong> is a pointer to a <a href="/windows/win32/api/wingdi/ns-wingdi-devmodea"><strong>DEVMODE</strong></a> structure that defines default printer data such as the paper orientation and the resolution.</td>
<td>0x07</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_SEPFILE</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string that specifies the name of the file used to create the separator page. This page is used to separate print jobs sent to the printer.</td>
<td>0x08</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_PRINT_PROCESSOR</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string that specifies the name of the print processor used by the printer.</td>
<td>0x09</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_PARAMETERS</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string that specifies the default print-processor parameters.</td>
<td>0x0A</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_DATATYPE</td>
<td><strong>pBuf</strong> is a pointer to a null-terminated string that specifies the data type used to record the print job.</td>
<td>0x0B</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_SECURITY_DESCRIPTOR</td>
<td><strong>pBuf</strong> is a pointer to a <a href="/windows/desktop/api/winnt/ns-winnt-security_descriptor"><strong>SECURITY_DESCRIPTOR</strong></a> structure for the printer. The pointer may be <strong>NULL</strong> if there is no security descriptor.</td>
<td>0x0C</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_ATTRIBUTES</td>
<td><strong>adwData</strong> [0] specifies the printer attributes, which can be one of the following values:<dl> PRINTER_ATTRIBUTE_QUEUED<br />
PRINTER_ATTRIBUTE_DIRECT<br />
PRINTER_ATTRIBUTE_DEFAULT<br />
PRINTER_ATTRIBUTE_SHARED<br />
</dl></td>
<td>0x0D</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_PRIORITY</td>
<td><strong>adwData</strong> [0] specifies a priority value that the spooler uses to route print jobs.</td>
<td>0x0E</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_DEFAULT_PRIORITY</td>
<td><strong>adwData</strong> [0] specifies the default priority value assigned to each print job.</td>
<td>0x0F</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_START_TIME</td>
<td><strong>adwData</strong> [0] specifies the earliest time at which the printer will print a job. (This value is specified in minutes elapsed since 12:00 A.M.)</td>
<td>0x10</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_UNTIL_TIME</td>
<td><strong>adwData</strong> [0] specifies the latest time at which the printer will print a job. (This value is specified in minutes elapsed since 12:00 A.M.)</td>
<td>0x11</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_STATUS</td>
<td><strong>adwData</strong> [0] specifies the printer status. For a list of possible values, see the <a href="printer-info-2.md"><strong>PRINTER_INFO_2</strong></a> structure.</td>
<td>0x12</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_STATUS_STRING</td>
<td>Not supported.</td>
<td>0x13</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_CJOBS</td>
<td><strong>adwData</strong> [0] specifies the number of print jobs that have been queued for the printer.</td>
<td>0x14</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_AVERAGE_PPM</td>
<td><strong>adwData</strong> [0] specifies the average number of pages per minute that have been printed on the printer.</td>
<td>0x15</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_TOTAL_PAGES</td>
<td>Not supported.</td>
<td>0x16</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_PAGES_PRINTED</td>
<td>Not supported.</td>
<td>0x17</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_TOTAL_BYTES</td>
<td>Not supported.</td>
<td>0x18</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_BYTES_PRINTED</td>
<td>Not supported.</td>
<td>0x19</td>
</tr>
<tr class="odd">
<td>PRINTER_NOTIFY_FIELD_OBJECT_GUID</td>
<td>This is set if the object GUID changes.</td>
<td>0x1A</td>
</tr>
<tr class="even">
<td>PRINTER_NOTIFY_FIELD_FRIENDLY_NAME</td>
<td>This is set if the printer connection is renamed.</td>
<td>0x1B</td>
</tr>
</tbody>
</table>



 

If the **Type** member specifies JOB\_NOTIFY\_TYPE, the **Field** member can be one of the following values.



| Field                                    | Type of data                                                                                                                                                                                                                                            | Value |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| JOB\_NOTIFY\_FIELD\_PRINTER\_NAME        | **pBuf** is a pointer to a null-terminated string containing the name of the printer for which the job is spooled.                                                                                                                                      | 0x00  |
| JOB\_NOTIFY\_FIELD\_MACHINE\_NAME        | **pBuf** is a pointer to a null-terminated string that specifies the name of the machine that created the print job.                                                                                                                                    | 0x01  |
| JOB\_NOTIFY\_FIELD\_PORT\_NAME           | **pBuf** is a pointer to a null-terminated string that identifies the port(s) used to transmit data to the printer. If a printer is connected to more than one port, the names of the ports are separated by commas (for example, "LPT1:,LPT2:,LPT3:"). | 0x02  |
| JOB\_NOTIFY\_FIELD\_USER\_NAME           | **pBuf** is a pointer to a null-terminated string that specifies the name of the user who sent the print job.                                                                                                                                           | 0x03  |
| JOB\_NOTIFY\_FIELD\_NOTIFY\_NAME         | **pBuf** is a pointer to a null-terminated string that specifies the name of the user who should be notified when the job has been printed or when an error occurs while printing the job.                                                              | 0x04  |
| JOB\_NOTIFY\_FIELD\_DATATYPE             | **pBuf** is a pointer to a null-terminated string that specifies the type of data used to record the print job.                                                                                                                                         | 0x05  |
| JOB\_NOTIFY\_FIELD\_PRINT\_PROCESSOR     | **pBuf** is a pointer to a null-terminated string that specifies the name of the print processor to be used to print the job.                                                                                                                           | 0x06  |
| JOB\_NOTIFY\_FIELD\_PARAMETERS           | **pBuf** is a pointer to a null-terminated string that specifies print-processor parameters.                                                                                                                                                            | 0x07  |
| JOB\_NOTIFY\_FIELD\_DRIVER\_NAME         | **pBuf** is a pointer to a null-terminated string that specifies the name of the printer driver that should be used to process the print job.                                                                                                           | 0x08  |
| JOB\_NOTIFY\_FIELD\_DEVMODE              | **pBuf** is a pointer to a [**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea) structure that contains device-initialization and environment data for the printer driver.                                                                                                        | 0x09  |
| JOB\_NOTIFY\_FIELD\_STATUS               | **adwData** \[0\] specifies the job status. For a list of possible values, see the [**JOB\_INFO\_2**](job-info-2.md) structure.                                                                                                                        | 0x0A  |
| JOB\_NOTIFY\_FIELD\_STATUS\_STRING       | **pBuf** is a pointer to a null-terminated string that specifies the status of the print job.                                                                                                                                                           | 0x0B  |
| JOB\_NOTIFY\_FIELD\_SECURITY\_DESCRIPTOR | Not supported.                                                                                                                                                                                                                                          | 0x0C  |
| JOB\_NOTIFY\_FIELD\_DOCUMENT             | **pBuf** is a pointer to a null-terminated string that specifies the name of the print job (for example, "MS-WORD: Review.doc").                                                                                                                        | 0x0D  |
| JOB\_NOTIFY\_FIELD\_PRIORITY             | **adwData** \[0\] specifies the job priority.                                                                                                                                                                                                           | 0x0E  |
| JOB\_NOTIFY\_FIELD\_POSITION             | **adwData** \[0\] specifies the job's position in the print queue.                                                                                                                                                                                      | 0x0F  |
| JOB\_NOTIFY\_FIELD\_SUBMITTED            | **pBuf** is a pointer to a [**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure that specifies the time when the job was submitted.                                                                                                                          | 0x10  |
| JOB\_NOTIFY\_FIELD\_START\_TIME          | **adwData** \[0\] specifies the earliest time that the job can be printed. (This value is specified in minutes elapsed since 12:00 A.M.)                                                                                                                | 0x11  |
| JOB\_NOTIFY\_FIELD\_UNTIL\_TIME          | **adwData** \[0\] specifies the latest time that the job can be printed. (This value is specified in minutes elapsed since 12:00 A.M.)                                                                                                                  | 0x12  |
| JOB\_NOTIFY\_FIELD\_TIME                 | **adwData** \[0\] specifies the total time, in seconds, that has elapsed since the job began printing.                                                                                                                                                  | 0x13  |
| JOB\_NOTIFY\_FIELD\_TOTAL\_PAGES         | **adwData** \[0\] specifies the size, in pages, of the job.                                                                                                                                                                                             | 0x14  |
| JOB\_NOTIFY\_FIELD\_PAGES\_PRINTED       | **adwData** \[0\] specifies the number of pages that have printed.                                                                                                                                                                                      | 0x15  |
| JOB\_NOTIFY\_FIELD\_TOTAL\_BYTES         | **adwData** \[0\] specifies the size, in bytes, of the job.                                                                                                                                                                                             | 0x16  |
| JOB\_NOTIFY\_FIELD\_BYTES\_PRINTED       | **adwData** \[0\] specifies the number of bytes that have been printed on this job. For this field, the change notification object is signaled when bytes are sent to the printer.                                                                      | 0x17  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**DEVMODE**](/windows/win32/api/wingdi/ns-wingdi-devmodea)
</dt> <dt>

[**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md)
</dt> <dt>

[**JOB\_INFO\_2**](job-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_INFO**](printer-notify-info.md)
</dt> <dt>

[**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor)
</dt> <dt>

[**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime)
</dt> </dl>

