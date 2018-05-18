---
title: Log File Modes
description: Log File Modes
ms.assetid: '4d2e6d9a-4d48-4a6d-822e-e3b961188187'
keywords: ["log file", "InSequentialFile", "InBuffer", "InCircularFile", "InAppendedFile", "InNewFile", "system time", "ProcessTrace", "MaximumFileSize"]
---

# Log File Modes

The most commonly used file modes are aliases for ETW log file modes:

-   InSequentialFile mode: corresponds to a *sequential-mode* ETW trace, that is, the trace is stored in a file only, and older events are kept preferentially, while newer events may be discarded if the maximum file size has been reached.

-   InBuffer mode: corresponds to a *buffered-mode* ETW trace, that is, the trace is in memory only, and newer events displace older events once a pre-determined amount of memory has been filled.

The following log file modes are identical in name to ETW log file modes:

-   InCircularFile corresponds to a *circular-mode* ETW trace, i.e. the trace is stored in a circular file. The events are written to a log file. After the file reaches the maximum size, the newer events displace older events once a pre-determined amount of memory has been filled.

-   InAppendedFile corresponds to an *append-mode* ETW trace, i.e., the trace is stored in a sequential file that can be appended. The older events are kept in the file and the new traces are appended to it. If the file does not exist, it is created. Use only if you specify [System Time](http://go.microsoft.com/fwlink/p/?linkid=116402) for the clock resolution, otherwise, [ProcessTrace](http://go.microsoft.com/fwlink/p/?linkid=116403) will return events with incorrect time stamps.

-   InNewFile corresponds to a *newfile-mode* ETW trace, i.e., the trace is stored in a new file. Older events are kept, while newer events may cause the session to switch to a new, indexed trace file once the maximum file size has been reached. The MaximumFileSize must be set. The specified file name must be a formatted string (for example, the string contains a %d, such as c:\\test%d.etl). Each time a new file is created, a counter is incremented and its value is used, the formatted string is updated, and the resulting string is used as the file name. This option is not allowed for private event tracing sessions and should not be used for NT kernel logger sessions.

> [!Note]  
> The file modes cannot be combined.

 

 

 




