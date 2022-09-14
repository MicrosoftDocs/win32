---
description: The PRINTER\_NOTIFY\_INFO structure contains printer information returned by the FindNextPrinterChangeNotification function. The function returns this information after a wait operation on a printer change notification object has been satisfied.
ms.assetid: c104fabe-edf5-426e-859b-694811975623
title: PRINTER_NOTIFY_INFO structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PRINTER_NOTIFY_INFO
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# PRINTER\_NOTIFY\_INFO structure

The **PRINTER\_NOTIFY\_INFO** structure contains printer information returned by the [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) function. The function returns this information after a wait operation on a printer change notification object has been satisfied.

## Syntax


```C++
typedef struct _PRINTER_NOTIFY_INFO {
  DWORD                    Version;
  DWORD                    Flags;
  DWORD                    Count;
  PRINTER_NOTIFY_INFO_DATA aData[1];
} PRINTER_NOTIFY_INFO, *PPRINTER_NOTIFY_INFO;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set this member to 2.

</dd> <dt>

**Flags**
</dt> <dd>

A bit flag that indicates the state of the notification structure. If the PRINTER\_NOTIFY\_INFO\_DISCARDED bit is set, it indicates that some notifications had to be discarded.

</dd> <dt>

**Count**
</dt> <dd>

The number of [**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md) elements in the **aData** array.

</dd> <dt>

**aData**
</dt> <dd>

An array of [**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md) structures. Each element of the array identifies a single job or printer information field, and provides the current data for that field.

</dd> </dl>

## Remarks

If the **Flags** member has the PRINTER\_NOTIFY\_INFO\_DISCARDED bit set, this indicates that an overflow or error occurred, and notifications may have been lost. In this case, you must call [**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md) and specify the PRINTER\_NOTIFY\_OPTIONS\_REFRESH flag to retrieve all current information. Until you request this refresh operation, the system will not send additional notifications for this change notification object.

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

[**FindNextPrinterChangeNotification**](findnextprinterchangenotification.md)
</dt> <dt>

[**PRINTER\_NOTIFY\_INFO\_DATA**](printer-notify-info-data.md)
</dt> </dl>

 

 




