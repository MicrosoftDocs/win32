---
description: The MONITOR\_INFO\_2 structure identifies a monitor.
ms.assetid: 4dd1ca15-6983-403e-8159-1a6d35a88162
title: MONITOR_INFO_2 structure (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MONITOR_INFO_2
- _MONITOR_INFO_2A
- _MONITOR_INFO_2W
api_type: 
- HeaderDef
api_location: 
- Winspool.h
---

# MONITOR\_INFO\_2 structure

The **MONITOR\_INFO\_2** structure identifies a monitor.

## Syntax


```C++
typedef struct _MONITOR_INFO_2 {
  LPTSTR pName;
  LPTSTR pEnvironment;
  LPTSTR pDLLName;
} MONITOR_INFO_2, *PMONITOR_INFO_2;
```



## Members

<dl> <dt>

**pName**
</dt> <dd>

A pointer to a null-terminated string that is the name of the monitor.

</dd> <dt>

**pEnvironment**
</dt> <dd>

A pointer to a null-terminated string that specifies the environment for which the monitor was written (for example, Windows NT x86, Windows IA64, Windows x64).

</dd> <dt>

**pDLLName**
</dt> <dd>

A pointer to a null-terminated string that is the name of the monitor DLL.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Unicode and ANSI names<br/>   | **\_MONITOR\_INFO\_2W** (Unicode) and **\_MONITOR\_INFO\_2A** (ANSI)<br/>                           |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Structures](printing-and-print-spooler-structures.md)
</dt> <dt>

[**AddMonitor**](addmonitor.md)
</dt> <dt>

[**EnumMonitors**](enummonitors.md)
</dt> <dt>

[**MONITOR\_INFO\_1**](monitor-info-1.md)
</dt> </dl>

 

 




