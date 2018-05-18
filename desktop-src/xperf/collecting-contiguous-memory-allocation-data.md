---
title: Collecting Contiguous Memory Allocation Data
description: Collecting Contiguous Memory Allocation Data
ms.assetid: '53c95ea7-efe8-4e12-b7d1-4b79bf993ccd'
---

# Collecting Contiguous Memory Allocation Data

The example scenario used to illustrate collecting and evaluating contiguous memory allocation data uses a test executable, alloccontmemexe.exe. The alloccontmemexe.exe program executes calls to the MmAllocateContiguousMemory function.

The files used in this scenario are:



| File Name                      | Purpose                                                                |
|--------------------------------|------------------------------------------------------------------------|
| Alloccontmemexe.exe<br/> | Executable file that performs contiguous memory allocations<br/> |
| ContMem.etl<br/>         | The trace file created by WPT <br/>                              |
| ContMem.txt<br/>         | A text file containing trace information <br/>                   |



 

For complete information on collecting data using Windows Performance Toolkit (WPT) please see [Quick Start Guide: WPA Basics](quick-start-guide--wpa-basics.md).

1.  Click on Start, Run, CMD.exe.

2.  Change to the directory where the trace file is to be written.

3.  At the command line, enter the following:

    ```
    xperf.exe -on PROC_THREAD+LOADER+MEMINFO+CONTMEMGEN -stackwalk ContiguousMemoryGeneration -f ContMem.etl 
    ```

    

    Data files containing captured event data can grow to a large size. If the issue being captured is intermittent, it may be necessary to capture data for an extended period of time. Add the following options:

    ```
    BufferSize 1024 -MaxBuffers 1024 -MaxFile 1024 -FileMode Circular 
    ```

    

    This option will set the size and number of buffers to a practical limit and set the maximum size of the trace file to 1024 MB. If the trace file exceeds 1024 MB, WPT will write over the oldest data. For more information on starting a trace, please see Xperf Options - [**start**](start.md).

4.  Execute Alloccontmemexe.exe

5.  When the issue under investigation has been captured, use the following command to turn off event tracing and format the event data into a trace file.

    ```
    Xperf.exe -d ContMem.etl 
    ```

    

6.  Update the Register by setting HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management DisablePagingExecutive (dword) from 1 (hex) to 0 (hex).

 

 





