---
title: Quick Start - Enabling Data Capture on Process Launch
description: Quick Start - Enabling Data Capture on Process Launch
ms.assetid: e3334695-518c-4077-a702-051dea45fcfd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Quick Start - Enabling Data Capture on Process Launch

Enabling data capture on process launch guarantees that there will be no loss of allocation information or history. Take the following steps to enable data capture on process launch:

1.  If Windows Sidebar is running, open Windows Task Manager and end any sidebar.exe processes.

2.  Open an elevated command prompt. It is recommended to identify a single directory from which WPA is run and change to that directory.

3.  From the command prompt enter the following:

    ```
    C:\etl> xperf -on Base -BufferSize 1024  -MinBuffers 10 -MaxBuffers 16
    ```

    

    By default, WPA will automatically turn on the "NT Kernel Logger" which collects kernel events. The kernel group "Base" will trigger the collection of events from the following event providers:

    

    | Option                  | Usage                                                        |
    |-------------------------|--------------------------------------------------------------|
    | PROC\_THREAD<br/> | Lists process and thread create/delete events<br/>     |
    | LOADER<br/>       | Shows kernel and user mode load and unload events<br/> |
    | DISK\_IO<br/>     | Tracks disk activity for the session<br/>              |
    | HARD\_FAULTS<br/> | Lists hard page faults<br/>                            |
    | PROFILE<br/>      | Creates a CPU sample profile<br/>                      |
    | MEMINFO<br/>      | Captures memory list information<br/>                  |

    

     

4.  Next, enter the following on a single line:

    ```
    C:\etl> xperf -start HeapSession -heap -PidNewProcess "C:\Program Files\Windows Sidebar\sidebar.exe" -BufferSize 1024 -MinBuffers 128 -MaxBuffers 128 -stackwalk HeapAlloc+HeapRealloc
    ```

    

    The following table explains each of the commands, parameters and options employed.

    

    | Option, command or parameter     | Usage                                                                                                                                                            |
    |----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | xperf<br/>                 | Runs the main xperf program with the specified parameters and options. <br/>                                                                               |
    | -start HeapSession<br/>    | Initializes a tracing session or logger session. In this case the session is named "HeapSession".<br/>                                                     |
    | -heap <br/>                | Identifies HeapSession as a heap trace.<br/>                                                                                                               |
    | -PidNewProcess <br/>       | Initializes a process. In this case the Windows Sidebar will be started.<br/>                                                                              |
    | -BufferSize<br/>           | Sets the buffer size where the event data will be stored. 1024K is an optimum buffer size. By default WPA will use 64K.<br/>                               |
    | -MinBuffers<br/>           | Sets the minimum number of buffers for event data storage. MinBuffers should be equal to MaxBuffers in order to guarantee consistency between traces.<br/> |
    | -MaxBuffers<br/>           | MaxBuffers should be allocated conservatively because buffers are allocated from non-paged memory, a finite system resource.<br/>                          |
    | -stackwalk<br/>            | Initializes the stackwalk facility to collect allocation and de-allocation information and associate that information with specific threads.<br/>          |
    | HeapAlloc+HeapRealloc<br/> | Identifies specific heap events to be captured and presented by the stackwalk facility.<br/>                                                               |

    

     

5.  At this point the sidebar will open on the desktop.

6.  In the command window, enter the following on a single line:

    ```
    C:\etl> xperf -stop -stop HeapSession -d heapTrace.etl
    ```

    

    The following table explains each of the commands, parameters and options:

    

    | Option, Command or Parameter | Usage                                                                                      |
    |------------------------------|--------------------------------------------------------------------------------------------|
    | xperf<br/>             | Runs the main xperf program with the specified parameters and options.<br/>          |
    | -stop HeapSession<br/> | Indicates a session will be ended. In this case, end the session "HeapSession".<br/> |
    | -d heapTrace.etl<br/>  | Merges traces produced in the session into the trace file "heapTrace.etl".<br/>      |

    

     

    For more information on WPA start and stop options, use the command line query:

    ```
    C:\etl> xperf -help start
    C:\etl> xperf -help stop
    ```

    

 

 





