---
description: The MONITOR\_INFO\_1 structure identifies an installed monitor.
ms.assetid: 7a4660bd-5df8-49dd-92f6-9574f451f10d
title: MONITOR_INFO_1 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MONITOR_INFO_1
- _MONITOR_INFO_1A
- _MONITOR_INFO_1W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# MONITOR\_INFO\_1 structure

The **MONITOR\_INFO\_1** structure identifies an installed monitor.

## Syntax


```C++
typedef struct _MONITOR_INFO_1 {
  LPTSTR pName;
} MONITOR_INFO_1, *PMONITOR_INFO_1;
```



## Members

<dl> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that identifies an installed monitor.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_MONITOR\_INFO\_1W** (Unicode) and **\_MONITOR\_INFO\_1A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**EnumMonitors**](enummonitors.md)
</dt> <dt>

[**MONITOR\_INFO\_2**](monitor-info-2.md)
</dt> </dl>

 

 




