---
title: Quick Start Opening the Trace
description: Quick Start Opening the Trace
ms.assetid: '068fdd11-d84c-40ba-ac10-4416275bbd46'
---

# Quick Start: Opening the Trace

> [!Note]  
> Windows Vista and later versions of the operating system have a slightly different boot trace analysis procedure than later Windows versions.

 

### Opening The Collected Trace: Windows Vista

-   To begin viewing the ReadyBoot information, open a command prompt and change to the trace directory identified earlier. Verify that the collected trace file, "boot\_BASE+CSWITCH\_1.etl", created in the [Quick Start: Capturing ReadyBoot Information](quick-start--capturing-readyboot-information.md) section exists in that directory.

-   There should also be a cabinet file with the same name, for example "boot\_BASE+CSWITCH\_1.cab". Starting with Windows Vista, this cabinet file contains additional ReadyBoot events information required for ReadyBoot analysis.

    -   Open the cabinet file using Windows Explorer or any other utility which supports CAB archives and extract ReadyBoot.etl.old file into the same directory.

        Invoke the following command to merge the boot trace with additional ReadyBoot information:

        ```
        C:\etl> Xperf -merge boot_BASE+CSWITCH_1.etl ReadyBoot.etl.old Boot1.etl
        ```

        

        For more information on trace merging please see the [**merge**](merge.md) command.

    -   As a result a merged file, "Boot1.etl", will be written out.

    -   To start analyzing the boot trace with WPA, enter the following into the command window:
        ```
        C:\etl> Xperfview Boot1.etl
        ```

        

### Opening The Collected Trace: Windows 7 and later

-   To begin viewing the ReadyBoot information, open a command prompt and change to the trace directory identified earlier. Verify that the collected trace file, "boot\_BASE+CSWITCH\_1.etl", created in the [Quick Start: Capturing ReadyBoot Information](quick-start--capturing-readyboot-information.md) section exists in that directory.

-   Starting with Windows 7, simply enter the following in the command window:

    ```
    C:\etl> Xperfview boot_BASE+CSWITCH_1.etl
    ```

    

 

 




