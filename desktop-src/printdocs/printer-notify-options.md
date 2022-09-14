---
description: The PRINTER\_NOTIFY\_OPTIONS structure specifies options for a change notification object that monitors a printer or print server.
ms.assetid: 712c546d-dbb3-4f78-b14e-fbb8619b57f9
title: PRINTER_NOTIFY_OPTIONS structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_NOTIFY_OPTIONS
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_NOTIFY\_OPTIONS structure

The **PRINTER\_NOTIFY\_OPTIONS** structure specifies options for a change notification object that monitors a printer or print server.

## Syntax


```C++
typedef struct _PRINTER_NOTIFY_OPTIONS {
  DWORD                        Version;
  DWORD                        Flags;
  DWORD                        Count;
  PPRINTER_NOTIFY_OPTIONS_TYPE pTypes;
} PRINTER_NOTIFY_OPTIONS, *PPRINTER_NOTIFY_OPTIONS;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set this member to 2.

</dd> <dt>

**Flags**
</dt> <dd>

A bit flag. If you set the PRINTER\_NOTIFY\_OPTIONS\_REFRESH flag in a call to the [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function, the function provides current data for all monitored printer information fields. The [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function ignores the **Flags** member.

</dd> <dt>

**Count**
</dt> <dd>

The number of elements in the **pTypes** array.

</dd> <dt>

**pTypes**
</dt> <dd>

A pointer to an array of [**PRINTER\_NOTIFY\_OPTIONS\_TYPE**](printer-notify-options-type.md) structures. Use one element of this array to specify the printer information fields to monitor, and one element to specify the job information fields to monitor. You can monitor either printer information, job information, or both.

</dd> </dl>

## Remarks

Use this structure with the [**FindFirstPrinterChangeNotification**](findfirstprinterchangenotification.md) function to specify the set of printer or job information fields to monitor for change.

Use this structure with the [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function to request the current data for all monitored printer and job information fields. In this case, the **Flags** member specifies the PRINTER\_NOTIFY\_OPTIONS\_REFRESH flag, and the function ignores the other structure members.

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

[**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_OPTIONS\_TYPE**](printer-notify-options-type.md)
</dt> </dl>

 

 




