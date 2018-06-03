---
title: AutoLogger
description: AutoLogger
ms.assetid: 28232075-cae9-42cf-9f81-5acae5f50851
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AutoLogger

AutoLogger can turn on heap tracing at boot time. When AutoLogger is used in conjunction with WPA [On/Off Transition Trace Capture](trace-profiles.md), also referred to as xbootmgr, information can be collected during the on/off transition phases of the operating system.

The accompanying example shows how to set the appropriate registry values.


```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\MyHeapSession]

; NOTE: You might think the Guid could be any value to identify the session uniquely, 
; but in order to turn on heap tracing it *MUST* be the HeapGuid,
"GUID"="{222962ab-6180-4b88-a825-346b75f2a24a}"

"Start"=dword:00000001

; Default LogFileMode = EVENT_TRACE_FILE_MODE_SEQUENTIAL | _DELAY_OPEN_FILE_MODE | _ADD_HEADER_MODE
; See etw\tracesub.c, ValidModeMask for a list of all valid bits.
;// Logger Mode flags
;#define EVENT_TRACE_FILE_MODE_NONE          0x00000000  // Logfile is off
;#define EVENT_TRACE_FILE_MODE_SEQUENTIAL    0x00000001  // Log sequentially
;#define EVENT_TRACE_FILE_MODE_CIRCULAR      0x00000002  // Log in circular manner
;#define EVENT_TRACE_FILE_MODE_APPEND        0x00000004  // Append sequential log
;#define EVENT_TRACE_REAL_TIME_MODE          0x00000100  // Real time mode on
;#define EVENT_TRACE_DELAY_OPEN_FILE_MODE    0x00000200  // Delay opening file
;#define EVENT_TRACE_BUFFERING_MODE          0x00000400  // Buffering mode only
;#define EVENT_TRACE_PRIVATE_LOGGER_MODE     0x00000800  // Process Private Logger
;#define EVENT_TRACE_ADD_HEADER_MODE         0x00001000  // Add a logfile header
;#define EVENT_TRACE_USE_GLOBAL_SEQUENCE     0x00004000  // Use global sequence no.
;#define EVENT_TRACE_USE_LOCAL_SEQUENCE      0x00008000  // Use local sequence no.
;#define EVENT_TRACE_RELOG_MODE              0x00010000  // Relogger
;#define EVENT_TRACE_USE_PAGED_MEMORY        0x01000000  // Use pageable buffers
;
; Setting it to sequential is sufficient - EVENT_TRACE_DELAY_OPEN_FILE_MODE and EVENT_TRACE_ADD_HEADER_MODE are not needed.
;0x00000001  // Log sequentially
"LogFileMode"=dword:00000001
"FileName"="F:\\tmpHeapAutologger.etl"

; 64KB * 0x0400 =  64 MB
; 64KB * 0x1000 = 256 MB
"BufferSize"=dword:00000040
"MaximumBuffers"=dword:00001000
"MinimumBuffers"=dword:00000400

; Max file size in MB.
; Default (if we leave absent) is 100 (MB) and after that the trace session is shut down.  That will cause xperf to fail when trying to merge.
; If we leave it blank, then "xperf -loggers" shows it set to 100.
; Set to 0 for no limit.  
"MaxFileSize"=dword:00000000

; This value copied from GlobalLogger, where it was set based on -stackwalk VirtualAlloc+HeapCreate+HeapAlloc+HeapRealloc
"StackWalkingFilter"=hex:62,02,00,00,20,10,00,00,21,10,00,00,22,10,00,00

; NOTE: There are no guids below this.
; We accomplish the goal of heap logging by using the HeapGuid as the session instance guid.
; [end]
```



 

 




