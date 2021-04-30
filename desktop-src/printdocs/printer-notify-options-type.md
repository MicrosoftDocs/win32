---
description: The PRINTER\_NOTIFY\_OPTIONS\_TYPE structure specifies the set of printer or job information fields to be monitored by a printer change notification object.A call to the FindFirstPrinterChangeNotification function specifies a PRINTER\_NOTIFY\_OPTIONS structure, which contains an array of PRINTER\_NOTIFY\_OPTIONS\_TYPE structures.
ms.assetid: 1009f892-d3a8-4887-99b4-a35d1268eeb4
title: PRINTER_NOTIFY_OPTIONS_TYPE structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_NOTIFY_OPTIONS_TYPE
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_NOTIFY\_OPTIONS\_TYPE structure

The **PRINTER\_NOTIFY\_OPTIONS\_TYPE** structure specifies the set of printer or job information fields to be monitored by a printer change notification object.

A call to the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function specifies a [**PRINTER\_NOTIFY\_OPTIONS**](printer-notify-options.md) structure, which contains an array of **PRINTER\_NOTIFY\_OPTIONS\_TYPE** structures.

## Syntax


```C++
typedef struct _PRINTER_NOTIFY_OPTIONS_TYPE {
  WORD  Type;
  WORD  Reserved0;
  DWORD Reserved1;
  DWORD Reserved2;
  DWORD Count;
  PWORD pFields;
} PRINTER_NOTIFY_OPTIONS_TYPE, *PPRINTER_NOTIFY_OPTIONS_TYPE;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

The type to be watched. This member can be one of the following values.



| Value                                                                                                                                                                                                                                      | Meaning                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <span id="JOB_NOTIFY_TYPE"></span><span id="job_notify_type"></span><dl> <dt>**JOB\_NOTIFY\_TYPE**</dt> <dt>0x01</dt> </dl>             | Indicates that the fields specified in the **pFields** array are JOB\_NOTIFY\_FIELD\_\* constants.<br/>     |
| <span id="PRINTER_NOTIFY_TYPE"></span><span id="printer_notify_type"></span><dl> <dt>**PRINTER\_NOTIFY\_TYPE**</dt> <dt>0x00</dt> </dl> | Indicates that the fields specified in the **pFields** array are PRINTER\_NOTIFY\_FIELD\_\* constants.<br/> |



 

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**Count**
</dt> <dd>

The number of elements in the **pFields** array.

</dd> <dt>

**pFields**
</dt> <dd>

A pointer to an array of values. Each element of the array specifies a job or printer information field of interest. For a list of supported printer and job information fields, see the [**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md) structure.

</dd> </dl>

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

[**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_OPTIONS**](printer-notify-options.md)
</dt> </dl>

 

 




