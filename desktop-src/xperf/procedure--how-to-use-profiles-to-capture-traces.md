---
title: Procedure How to Use Profiles to Capture Traces
description: Procedure How to Use Profiles to Capture Traces
ms.assetid: 9b82b670-6a95-45bb-aca2-e2cc0831b509
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Procedure: How to Use Profiles to Capture Traces

The following procedure shows you how to capture traces by using profiles. If you are doing memory analysis, you might want to write your trace to a file since ETW writes through and doesn't disturb the cache. If you are doing a disk I/O analysis, you might want to save your trace into a circular buffer in memory. There are also other considerations such as whether you need to capture a long trace, which wouldn't fit into a buffer in memory, or if you only care about the last 5-10 seconds of the trace content.

-   Select a profile such as perf!FileIOProfiles.InBuffer and use the following command to display information about it:

    ```
    xperf -profiles perf!FileIOProfiles.InBuffer
    ```

    

    The result of this command would be listing all the profiles, as in the previous step, followed by the sessions and providers in that profile, for example:

    <dl> Profile: FileIOProfiles.InBuffer  
    Sessions: FileIOProfiles.InBuffer.Sessions  
    Session: FileIOProfiles.InBuffer.Sessions\[0\].Kernel\[0\]  
    Session: FileIOProfiles.InBuffer.Sessions\[0\].User\[0\]  
    Providers: FileIOProfiles.InBuffer.Providers  
    Provider: FileIOProfiles.InBuffer.Providers\[0\].Kernel\[0\]  
    Provider: FileIOProfiles.InBuffer.Providers\[0\].User\[0\]  
    </dl>

-   Assuming that you chose to use a file-based trace, start an **InSequentialFile** trace profile by using the following command:

    ```
    xperf -start perf!GeneralProfiles.InSequentialFile
    ```

    

    If a problem occurs an error is reported. For example, starting the same profile twice would result in an error that the session is already running.

-   Show which **InSequentialFile** loggers have already started for a specific profile by using the following command:

    ```
    xperf -profileloggers perf!GeneralProfiles.InSequentialFile
    ```

    

    The response to this command would be as shown below.

    ``` syntax
    Session Status for "perf!GeneralProfiles.InSequentialFile":
    "NT Kernel Logger" : Running
    PerfCoreUserSession_InSequentialFile : Running
    ```

-   Stop the **InSequentialFile** trace profile, save the traces, and merge them into a trace file, such as merged.etl. Do that by using the following command:

    ```
    xperf -stop perf!GeneralProfiles.InSequentialFile merged.etl
    ```

    

    If a problem occurs an error is reported.

-   Start **InSequentialFile** trace profile, overriding, at start time, MaxBuffers values for all ETW sessions, for which loggers are to be started to 256. To do that, use the following command:

    ```
    xperf -start perf!GeneralProfiles.InSequentialFile -MaxBuffers 256
    ```

    

    If a problem occurs an error is reported.

-   Update **MaxBuffers** values for the active **InSequentialFile** ETW loggers specified in the trace profile. To do that, use the following command:

    ```
    xperf -update perf!GeneralProfiles.InSequentialFile -MaxBuffers 256
    ```

    

    No response is displayed after issuing this command.

-   You can display the resulting trace by using the following command:

    ```
    xperfview merged.etl
    ```

    

    As usual, you can check or uncheck any of the check boxes to hide or show a specific graph. For more information on visualizing traces, see [Quick Start](quick-start.md).

 

 




