---
title: Capturing and Collecting CPU Processor Power Information
description: Capturing and Collecting CPU Processor Power Information
ms.assetid: f5a294aa-0097-46c8-894a-536692a51c0d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Capturing and Collecting CPU Processor Power Information

For installation support see the [Installation](installation.md) section of this document.

Perform the following steps to begin capture and collection of CPU processor data:.

1.  Open a command prompt with administrator privileges.

2.  Create a directory \\etl and change to that directory. Run WPA from this directory to store all of your trace files in one location.

    ``` syntax
    C:\>mkdir c:\etl
    C:\>cd c:\etl
    ```

3.  From the command prompt, start NT Kernel Logger with base and power flags.

    ``` syntax
    xperf -on power+base
    ```

    In this case, we are setting two options or flags. The first option, **power**, sets a kernel flag that causes WPA to collect events related with CPU power and frequency modulation. The second flag, **base**, is a kernel group that includes the flags shown in the following table.

    

    | Option                  | Usage                                                        |
    |-------------------------|--------------------------------------------------------------|
    | PROC\_THREAD<br/> | Lists process and thread create/delete events<br/>     |
    | LOADER<br/>       | Shows kernel and user-mode load and unload events<br/> |
    | DISK\_IO<br/>     | Tracks disk activity for the session<br/>              |
    | HARD\_FAULTS<br/> | Lists hard page faults<br/>                            |
    | PROFILE<br/>      | Creates a CPU sample profile<br/>                      |
    | MEMINFO<br/>      | Displays Memory list information<br/>                  |

    

     

4.  Run an application that causes the CPU to work. In this case, we will start a DVD and turn it off immediately.

5.  Stop the trace. Use the -d flag with the **xperf** command that causes WPA to stop collecting events. powerTrace.etl names the trace file where the captured events are collated and stored.

    ``` syntax
    xperf -d powerTrace.etl
    ```

6.  Analyze the trace.

    ``` syntax
    xperfview powerTrace
    ```

The [Reviewing Trace Event Information](reviewing-trace-event-information.md) topic explains some of the information that has been collected in the trace file powerTrace.etl.

 

 





