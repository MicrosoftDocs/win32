---
title: Quick Start Capturing ReadyBoot Information
description: Quick Start Capturing ReadyBoot Information
ms.assetid: 'd4d4c9cc-e49f-4302-9a50-d9ab22af2636'
---

# Quick Start: Capturing ReadyBoot Information

When enabling data capture for a boot scenario, the reboot should be initiated by the WPA tools.

**Machine set-up notes:**

-   It is often beneficial to enable system auto-logon for boot scenario tracing.

-   For a complete list of best practices for boot tracing, please see the [Windows On/Off Transitions Solutions Guide](http://go.microsoft.com/fwlink/p/?linkid=163850).

To begin data capture, please take the following steps:

1.  Open a command prompt. It is recommended to identify a single directory from which WPA is run and change to that directory. Boot traces will be collected into that directory.

    From the command prompt enter the following command, which would initiate the machine reboot:

    ```
    C:\etl> xbootmgr -trace boot 
    ```

    

    

    | Command, Parameter or Option | Usage                                                                                            |
    |------------------------------|--------------------------------------------------------------------------------------------------|
    | xbootmgr<br/>          | Runs the WPA boot tracing control program with the specified parameters and options. <br/> |
    | -trace Boot<br/>       | Initializes a boot tracing session. <br/>                                                  |

    

     

    When **xbootmgr** is run in this context, WPA will automatically turn on the "NT Kernel Logger" which collects kernel events. The events enabled for a trace can be specified with the "-traceflags" argument. If the "-traceflags" argument is not present, WPA will enable the default core set of kernel events given in the following table:

    

    | Option                  | Usage                                                        |
    |-------------------------|--------------------------------------------------------------|
    | PROC\_THREAD<br/> | Lists process and thread create/delete events<br/>     |
    | LOADER<br/>       | Shows kernel and user mode load and unload events<br/> |
    | DISK\_IO<br/>     | Tracks disk activity<br/>                              |
    | HARD\_FAULTS<br/> | Lists hard page faults<br/>                            |
    | PROFILE<br/>      | Captures CPU sampled profile information<br/>          |
    | MEMINFO<br/>      | Captures memory list information<br/>                  |
    | CSWITCH<br/>      | Tracks thread context switch activity<br/>             |

    

     

2.  After the machine reboots, xbootmgr automatically launches and waits for preset amount of time before saving the trace. A timer window is presented that contains controls to cancel the current session or to end it early.

3.  When the timeout countdown reaches zero, xbootmgr saves the session trace to the original directory.

For more information on WPA boot tracing manager's start and stop options, see the [Windows On/Off Transitions Solutions Guide](http://go.microsoft.com/fwlink/p/?linkid=163850). Online help for boot tracing is also available using this command line query:


```
C:\etl> xbootmgr -help
```



 

 





