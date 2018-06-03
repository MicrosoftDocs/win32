---
title: Actions
description: Actions
ms.assetid: 7e02eca4-9ffb-49ab-af48-185d52933070
keywords:
- boot
- cpudisk
- cswitch
- diskio
- dpcisr
- drvdelay
- dumper
- filename
- focuschange
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Actions

Xperf actions are trace processing components that collate event information to produce text reports. Actions produce summarized reports that are specific to a set of events such as registry accesses, context switches, file accesses, or system configuration.

All actions are invoked using the following command-line pattern:


```
xperf -i input.etl -o output.txt   -a <action_name> [action_parameters] 
```



Where *action\_name* is the name of the action. The *action\_name* is always preceded by the **-a** command-line switch. The action name can be followed by one or more action-specific parameters. You can get help for each action by using the following command:


```
xperf -help <action_name>
```



WPT offers a large number of actions. You can list all available processing actions by using the built-in command-line help:


```
xperf -help processing 
```



The following table summarizes all the actions that are available in version 4.6 of Xperf.



| Action name                                                                 | Description                                                                                                                                                                                          |
|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [boot](the-boot-action.md)<br/>                                      | Shows boot and shut down statistics <br/>                                                                                                                                                      |
| [bootprefetch](the-boot-prefetch-action.md)<br/>                     | Show boot pre-fetching events<br/>                                                                                                                                                             |
| [cpudisk](the-cpu-and-disk-action.md)<br/>                           | CPU/Disk activity report <br/>                                                                                                                                                                 |
| [cswitch](the-context-switch-action.md)<br/>                         | Shows Context Switch data <br/>                                                                                                                                                                |
| [diskio](the-disk-i-o-action.md)<br/>                                | Shows disk IO statistics <br/>                                                                                                                                                                 |
| [The DiskIdleHistogram Action](the-diskidlehistogram-action.md)<br/> | Shows a histogram of disk activity and idle times<br/>                                                                                                                                         |
| [dpcisr](the-dpc-isr-action.md)<br/>                                 | Shows DPC/ISR statistics <br/>                                                                                                                                                                 |
| [drvdelay](the-driver-delay-action.md)<br/>                          | Shows driver delays <br/>                                                                                                                                                                      |
| [dumper](the-dumper-action.md)<br/>                                  | Dumps events in the trace in text form <br/>                                                                                                                                                   |
| [filename](the-filename-action.md)<br/>                              | Shows file names in the trace <br/>                                                                                                                                                            |
| [focuschange](the-focus-change-action.md)<br/>                       | Shows the Windows thread focus change events in the trace <br/>                                                                                                                                |
| [hardfault](the-hard-fault-action.md)<br/>                           | Shows hard fault statistics by process and file <br/>                                                                                                                                          |
| [heap](the-heap-action.md)<br/>                                      | Shows process heap information. For complete information on Process Heap actions please see [Using Actions to Analyze Process Heap Data](using-actions-to-analyze-process-heap-data.md).<br/> |
| [marks](the-marks-action.md)<br/>                                    | Shows marks information <br/>                                                                                                                                                                  |
| [pagefault](the-page-fault-action.md)<br/>                           | Shows page fault information in the trace <br/>                                                                                                                                                |
| [perfctrs](the-performance-counters-action.md)<br/>                  | Shows process performance counters <br/>                                                                                                                                                       |
| [pnp](the-pnp-action.md)<br/>                                        | Shows PnP events in the trace <br/>                                                                                                                                                            |
| [prefetch](the-prefetch-action.md)<br/>                              | Shows Prefetch information <br/>                                                                                                                                                               |
| [process](the-process-action.md)<br/>                                | Shows process, thread, image information <br/>                                                                                                                                                 |
| [profile](the-profile-action.md)<br/>                                | Shows sampled profiler data <br/>                                                                                                                                                              |
| [readyboot](the-readyboot-action.md)<br/>                            | Shows ReadyBoot statistics <br/>                                                                                                                                                               |
| [registry](the-registry-action.md)<br/>                              | Shows registry access statistics <br/>                                                                                                                                                         |
| [services](the-services-action.md)<br/>                              | Shows service status information <br/>                                                                                                                                                         |
| [shutdown](the-shutdown-action.md)<br/>                              | Shows shut down statistics <br/>                                                                                                                                                               |
| [spinlock](the-spinlock-action.md)<br/>                              | Shows Spin Lock information<br/>                                                                                                                                                               |
| [stack](the-stack-action.md)<br/>                                    | Shows stack information <br/>                                                                                                                                                                  |
| [suspend](the-suspend-action.md)<br/>                                | Shows suspend transition information <br/>                                                                                                                                                     |
| [sysconfig](the-system-configuration-action.md)<br/>                 | Shows system configuration <br/>                                                                                                                                                               |
| [tracestats](the-trace-statistics-action.md)<br/>                    | Shows trace statistics <br/>                                                                                                                                                                   |
| [winlogon](the-win-logon-action.md)<br/>                             | Shows Winlogon events in the trace <br/>                                                                                                                                                       |



 

### Examples

The following sections provide some examples that show how you can use actions.

**Dumping the system configuration**

The following command produces a report about system configuration that defines where the trace was taken.


```
xperf -i input.etl -a sysconfig 
```



The report includes the following items:

-   Hardware information, for example, the number of cores, processor speed, supported sleep states

-   Partition information about mounted hard disks

-   PnP device trees

-   Services that run on the analyzed system at the time the trace was taken

-   Device IRQs

-   Other configuration details

**Registry Access**

Accessing the registry can cause unnecessary usage of system memory. You can use the registry action to produce a report about registry activtity. This requires that the trace included the registry kernel events. To invoke this action, run the following command:


```
xperf -i input.etl -o output.txt -a registry 
```



The previous command runs the registry action on the input trace file, Input.etl, and produces an output file called Output.txt. Output.txt shows registry access statistics for every 1 millisecond interval in the trace.

**CPU and Disk utilization**

The cpudisk action produces a report that lists the CPU utilization and some disk I/O statistics for the trace. To generate a cpudisk report so that you can understand the output, run the following command:


```
xperf -i trace.etl -a cpudisk 
```



This trace shows you information for every process that was running during the trace session. The processes are sorted by overall CPU utilization. If you are interested in one process only, you can limit the report by using the **-exes** action option, for example:


```
xperf -i trace.etl -a cpudisk -exes devenv.exe 
```



Further filtering can be performed with the **-pids** action option, which selects only processes that match the given process IDs. The **cpudisk** action has further options. You can find out all available options of a given action by using the built-in command-line help:


```
xperf -help cpudisk 
```



If you want to send the output information to a file, use the **-o** top-level option to specify an output file name, for example:


```
xperf -i trace.etl -o report.txt -a cpudisk -exes devenv.exe 
```



The previous command sends the **cpudisk** output to the Report.txt file. You can also send the output to a file by using command-line redirection. Xperf provides progress information on the console whenever its output is redirected, unless the **-quiet** top-level option is specified.

**Dumping the events to an ANSI text file**

Actions are designed to display reports about traces. However, sometimes it is valuable to just look at the raw trace data. Because ETL files are in a dense binary format, the Xperf tools have a **dumper** action that moves all the events to an ANSI text file. To move all events into an ANSI text file, run the following command:


```
xperf -i trace.etl -o trace.txt -a dumper 
```



This command moves the contents of Trace.etl to the ANSI text file Trace.txt. Be aware that this can take a while for large traces. Xperf displays progress information while the contents are being moved. After the move is complete, view the trace in a text editor. Be aware that Notepad.exe will not open most traces because they are too large for it. The dumper action is so commonly used that it is the default Xperf processing action:


```
xperf -i trace.etl -o trace.txt 
```



When you look at Trace.txt, you should see one header line for each event type in the trace. These headers provide titles for each field for each event type in the trace.

 

 





