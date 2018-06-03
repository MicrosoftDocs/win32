---
title: WPA Providers
description: WPA Providers
ms.assetid: 46965a8a-e99f-4841-af01-510350d04c9f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPA Providers

Providers are Event Tracing for Windows components that expose events to WPA. Providers are grouped in multiple ways in order to allow maximum flexibility.

### NT Kernel Logger

WPA exposes a number of providers that are specific to the kernel. These kernel providers have been built to expose the useful events captured from the kernel mode only. Because these events are generated in kernel mode special syntax and naming is associated with these providers.

-   "NT Kernel Logger" is the logger name where kernel events are stored.

-   There can be one and only one NT Kernel Logger per tracing activity.

-   Events to be captured by the kernel logger can be identified in one of three ways:

    1.  **Kernel Flags** - This is the most granular way of listing events to be captured. Each kernel flag identifies a specific type of event. Kernel flags are separated by a "+" sign. For example,

        ```
        Xperf -on FILE_IO+CSWITCH+PROFILE
        ```

        

        Turns the kernel logger "on" and collects FILE\_IO, CSWITCH and PROFILE events.

        To obtain a list of kernel flags use the syntax:

        ```
        Xperf  -providers kf
        ```

        

        > [!Note]  
        > Kernel flags are not case sensitive.

         

    2.  **Kernel Groups** - Are sets of kernel flags that are logically grouped together. For example,

        ```
        Xperf  -on DiagEasy
        ```

        

        Turns the kernel logger "on" using the kernel group DiagEasy. DiagEasy contains the following kernel flags:

        

        | Kernel Flag                  | Description                                              |
        |------------------------------|----------------------------------------------------------|
        | **PROC\_THREAD**<br/>  | Process and Thread create/delete<br/>              |
        | **LOADER**<br/>        | Kernel and user mode Image Load/Unload events<br/> |
        | **DISK\_IO**<br/>      | Disk I/O<br/>                                      |
        | **HARD\_FAULTS**<br/>  | Hard Page Faults<br/>                              |
        | **DPC**<br/>           | Deferred Procedure Calls<br/>                      |
        | **INTERRUPT**<br/>     | Interrupt Events<br/>                              |
        | **CSWITCH**<br/>       | Context Switch<br/>                                |
        | **PERF\_COUNTER**<br/> | Process Performance Counters<br/>                  |

        

         

        To obtain a list of kernel flags use the syntax:

        ```
        Xperf -providers kg
        ```

        

        > [!Note]  
        > Kernel groups are not case sensitive.

         

    3.  **Trace Profiles** - A trace profile is a collection of various settings of a specific type of trace. You can gather and control these settings with a single command per operation. For more information on trace profiles please see the [Trace Profiles](overview.md) section of this document.

-   When using kernel flags or groups the xperf option to start tracing is "on" rather than start.

### Command-line Usage

To get help for the providers, type the following in the command line:


```
xperf -help providers 
```



You can query which providers are available by using query options in the following form:


```
xperf -providers [Installed|I] [Registered|R] [KernelFlags|KF] [KernelGroups|KG] [Kernel|K] 
```



The following table shows where each option is located.



| Option                         | Description                                                       |
|--------------------------------|-------------------------------------------------------------------|
| I or Installed <br/>     | Include installed/known providers <br/>                     |
| R or Registered <br/>    | Include registered providers <br/>                          |
| KF or KernelFlags <br/>  | Include kernel flags <br/>                                  |
| KG or KernelGroups <br/> | Include kernel groups <br/>                                 |
| K or Kernel <br/>        | Include kernel flags and groups; shortcut for "KF KG" <br/> |



 

If you do not specify an option, all providers are included in the output. The set of registered providers is obtained by enumerating all providers that are registered through ETW for enable/disable operations that are managed by the controller. The set of installed providers is the set of providers that are installed on the test system, which includes hundreds of providers that are included with Windows Vista and later versions of Windows. You can find this list by running the following command:


```
logman.exe query providers 
```



The kernel provider exposes a large amount of information. The kernel provider can be controlled by using flags and/or groups. A kernel provider flag enables/disables the logging of a kernel event type, such as "context switch." If you use the CSWITCH flag during tracing, events will be logged for all context switches that occur on the test system. A kernel provider group is a set of flags that are organized by component or area of interest. For example, the group network consists of flags to provide information that is necessary to do network related analysis. You can enable multiple groups and flags for the same trace. Conventionally, kernel flag names are printed in all capital letters (for example, CSWITCH, PROFILE, DISK\_IO) and kernel group names are printed in initial capital (for example, Base, Latency, Network). The Xperf command line is not case sensitive, though, so any capitalization of the kernel flags and groups will be accepted (for example, Base, BASE, base, CSWITCH, cswitch, CSwitch).

 

 





