---
title: Reference
description: Reference
ms.assetid: 5edd6586-fe6a-44bf-9fd5-ed876af7b007
keywords:
- tracing options
- trace flags
- kernel flags
- stackwalk filters
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reference

### Usage

To initiate tracing, type the following:


```
xbootmgr -trace boot|hibernate|standby|shutdown|rebootCycle [options]
```



To abort tracing and reset any prior configurations, type the following:


```
xbootmgr -remove
```



### Tracing Options

The following table lists the options that can be used with the On/Off Transition Trace Capture tool.



| Option                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-numRuns \[***num***\]**<br/>       | Defines the number of test runs. Three or more (preferably ten) traces are required to collect data that is statistically significant. <br/> Default:1<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **-resultPath \[***path***\]**<br/>   | Defines the path where the trace results should be stored.<br/> Default:The current directory.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **-traceFlags \[***flags***\]**<br/>  | Specifies the trace flags to use. For a full list of possible flags, see later in this table or type the following at the command prompt:<br/> **xperf -providers k**<br/> <dl> <dt> Default: </dt> <dt>BASE+CSWITCH</dt> </dl> <br/>                                                                                                                                                                                                                                                  |
| **-callBack \[***cmd***\]**<br/>      | Specifies the file that is launched via ShellExecute after all trace runs are complete. This option is used when constructing an automation harness.<br/> <dl> <dt> Default: </dt> <dt>No callback.</dt> </dl> <br/>                                                                                                                                                                                                                                                                         |
| **-runTag \[***tag***\]**<br/>        | Specifies a text string that is inserted into the trace file name and provides a quick and easy way to differentiate between different traces.<br/> Example: <br/> To quickly create two traces with "before" and "after" as part of the file name, type:<br/> **xbootmgr -trace rebootCycle -runtag before** <br/> Followed by:<br/> **xbootmgr -trace rebootCycle -runtag after**<br/> Default:None.<br/>                                                                                                                                                       |
| **-prepSystem**<br/>                  | Optimizes the computer before the trace begins to create an idealized set of results. This option applies only to boot/rebootCycle traces.<br/> <dl> <dt> Default: </dt> <dt>Off.</dt> </dl> <br/>                                                                                                                                                                                                                                                                                           |
| **-postBootDelay \[***sec***\]**<br/> | For boot traces, sets the post-boot delay (in seconds) before stopping the trace.<br/> For shutdown traces, sets the post-boot delay (in seconds) before shutting the system down to begin the trace.<br/> For standby/hibernate traces, sets the post-resume delay (in seconds) before stopping the trace.<br/> For reboot cycle, sets the post-boot delay (in seconds) before stopping the trace.<br/> In general, this value should not be changed because reducing it undermines the post-boot calculations that Xperf.exe performs.<br/> Default:120 seconds.<br/> |
| **-wakeupDelay   \[***sec***\]**<br/> | During a standby/hibernate trace, sets the delay for waking the machine from a sleep state (in seconds). If the test computer takes more than 60 seconds to achieve the sleep state, this value might need to be increased.<br/> <dl> <dt> Default: </dt> <dt>60 seconds.</dt> </dl> <br/>                                                                                                                                                                                                   |
| **-issueFlush**<br/>                  | No longer required.<br/> <dl> <dt> Default: </dt> <dt>Off.</dt> </dl> <br/>                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **-sleeperCmd \[***cmd***\]**<br/>    | No longer required.<br/> <dl> <dt> Default: </dt> <dt>XbootmgrSleep.exe.</dt> </dl> <br/>                                                                                                                                                                                                                                                                                                                                                                                                    |
| **-preTraceCmd \[***cmd***\]**<br/>   | Specifies the file that is launched via ShellExecute before every trace iteration. This option can be used as part of an automation harness to collect additional pretrace state information during multiple traces.<br/> Default:None.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| **-stackWalk**<br/>                   | Specifies the stackwalk filters to be used, in one of the following ways:<br/> An immediate list of flags, for example: <br/> **xperfmgr -trace boot -stackwalk ProcessCreate+CSwitch**<br/> A list of one of more filters stored in a file, for example:<br/> **xperfmgr -trace boot -stackwalk @stack.txt**<br/> For a list of possible stackwalk filters, see later in this table or type the following at a command prompt:<br/> **xperf -help stackwalk**<br/> Default:No filter enabled.<br/>                                                         |
| **-noPopups**<br/>                    | If an error occurs during the trace, returns the error code to the command line, rather than opening a message box. This option prevents an error from breaking an automated test procedure. Automation harnesses can also process the Xbootmgr.log file, which is automatically created and appended to the results directory, to check for errors.<br/> <dl> <dt> Default: </dt> <dt>An error opens a message box.</dt> </dl> <br/>                                                        |
| **-noPrepReboot**<br/>                | Prevents a preparatory reboot during a shutdown/rebootCycle trace. Usually, the reboot is required to ensure a consistent machine state before the first shutdown if multiple traces are being taken (c.f. -numRuns).<br/> This option can be used to quickly capture a single trace.<br/> <dl> <dt> Default: </dt> <dt>A preparatory reboot for shutdown/rebootCycle traces is performed.</dt> </dl> <br/>                                                                            |
| **-leavePremerged**<br/>              | Retains the premerged trace files, for debugging purposes.<br/> Default:The premerge files are deleted.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **-noTraceFlagslnFileName**<br/>      | When specified, prevents the output file names from containing trace flag names, for example, BASE.<br/> <dl> <dt> Default: </dt> <dt>Output file names contain trace flags.</dt> </dl> <br/>                                                                                                                                                                                                                                                                                                |
| **-verboseReadyBoot**<br/>            | Saves verbose status information for ReadyBoot prefetching.<br/> <dl> <dt> Default: </dt> <dt>Off. Only minimal prefetching information is saved.</dt> </dl> <br/>                                                                                                                                                                                                                                                                                                                           |



 

### Trace Flags

The following table lists the flags that can be used with the `-traceFlags` option.



| Kernel flags                | Descriptions                                                                            |
|-----------------------------|-----------------------------------------------------------------------------------------|
| PROC\_THREAD<br/>     | Process and thread create/delete<br/>                                             |
| LOADER<br/>           | Kernel- and user-mode image load/unload events<br/>                               |
| PROFILE<br/>          | CPU sample profile<br/>                                                           |
| CSWITCH<br/>          | Context switch<br/>                                                               |
| COMPACT\_CSWITCH<br/> | Compact context switch<br/>                                                       |
| DISPATCHER<br/>       | CPU scheduler<br/>                                                                |
| DPC<br/>              | Deferred procedure call (DPC)events<br/>                                          |
| INTERRUPT<br/>        | Interrupt events<br/>                                                             |
| SYSCALL<br/>          | System calls<br/>                                                                 |
| PRIORITY<br/>         | Priority change events<br/>                                                       |
| ALPC<br/>             | Advanced local procedure call<br/>                                                |
| PERF\_COUNTER<br/>    | Process perf counters<br/>                                                        |
| DISK\_IO<br/>         | Disk I/O<br/>                                                                     |
| DISK\_IO\_INIT<br/>   | Disk I/O initiation<br/>                                                          |
| FILE\_IO<br/>         | File system operation end times and results<br/>                                  |
| FILE\_IO\_INIT<br/>   | File system operation (create/open/close/read/write)<br/>                         |
| HARD\_FAULTS<br/>     | Hard page faults<br/>                                                             |
| FILENAME<br/>         | FileName (for example, FileName create/delete/rundown)<br/>                       |
| SPLIT\_IO<br/>        | Split I/O<br/>                                                                    |
| REGISTRY<br/>         | Registry tracing<br/>                                                             |
| DRIVERS<br/>          | Driver events<br/>                                                                |
| POWER<br/>            | Power management events<br/>                                                      |
| NETWORKTRACE<br/>     | Network events (for example, tcp/udp send/receive)<br/>                           |
| VIRT\_ALLOC<br/>      | Virtual allocation reserve and release<br/>                                       |
| MEMINFO<br/>          | Memory list information<br/>                                                      |
| ALL\_FAULTS<br/>      | All page faults including hard, copy on write, demand zero faults, and so on<br/> |



 

### Stackwalk Filters

The following table shows the filters that can be added to a trace by using the `-stackwalk` option.



| Stackwalk filters                |                                       |
|----------------------------------|---------------------------------------|
| ProcessCreate<br/>         | RegCloseKey<br/>                |
| ProcessDelete<br/>         | HardFault<br/>                  |
| ImageLoad<br/>             | PagefaultTransition<br/>        |
| ImageUnload<br/>           | PagefaultDemandZero<br/>        |
| ThreadCreate<br/>          | PagefaultCopyOnWrite<br/>       |
| ThreadDelete<br/>          | PagefaultGuard<br/>             |
| CSwitch<br/>               | PagefaultHard<br/>              |
| ReadyThread<br/>           | PagefaultAV<br/>                |
| ThreadSetPriority<br/>     | VirtualAlloc<br/>               |
| ThreadSetBasePriority<br/> | VirtualFree<br/>                |
| Mark<br/>                  | PagefileBackedImageMapping<br/> |
| SyscallEnter<br/>          | HeapRangeCreate<br/>            |
| SyscallExit<br/>           | HeapRangeReserve<br/>           |
| Profile<br/>               | HeapRangeRelease<br/>           |
| ProfileSetInterval<br/>    | HeapRangeDestroy<br/>           |
| DiskReadInit<br/>          | HeapCreate<br/>                 |
| DiskWriteInit<br/>         | HeapAlloc<br/>                  |
| DiskFlushInit<br/>         | HeapRealloc<br/>                |
| FileCreate<br/>            | HeapFree<br/>                   |
| FileCleanup<br/>           | HeapDestroy<br/>                |
| FileClose<br/>             | AlpcSendMessage<br/>            |
| FileRead<br/>              | AlpcReceiveMessage<br/>         |
| FileWrite<br/>             | AlpcWaitForReply<br/>           |
| FileSetInformation<br/>    | AlpcWaitForNewMessage<br/>      |
| FileDelete<br/>            | AlpcUnwait<br/>                 |
| FileRename<br/>            | ThreadPoolCallbackEnqueue<br/>  |
| FileDirEnum<br/>           | ThreadPoolCallbackDequeue<br/>  |
| FileFlush<br/>             | ThreadPoolCallbackStart<br/>    |
| FileQueryInformation<br/>  | ThreadPoolCallbackStop<br/>     |
| FileFSCTL<br/>             | ThreadPoolCallbackCancel<br/>   |
| FileDirNotify<br/>         | ThreadPoolCreate<br/>           |
| FileOpEnd<br/>             | ThreadPoolClose<br/>            |
| SplitIO<br/>               | ThreadPoolSetMinThreads<br/>    |
| RegQueryKey<br/>           | ThreadPoolSetMaxThreads<br/>    |
| RegEnumerateKey<br/>       | PowerSetPowerAction<br/>        |
| RegEnumerateValueKey<br/>  | PowerSetPowerActionReturn<br/>  |
| RegDeleteKey<br/>          | PowerSetDevicesState<br/>       |
| RegCreateKey<br/>          | PowerSetDevicesStateReturn<br/> |
| RegOpenKey<br/>            | PowerDeviceNotify<br/>          |
| RegSetValue<br/>           | PowerDeviceNotifyComplete<br/>  |
| RegDeleteValue<br/>        | PowerSessionCallout<br/>        |
| RegQueryValue<br/>         | PowerSessionCalloutReturn<br/>  |
| RegQueryMultipleValue<br/> | PowerPreSleep<br/>              |
| RegSetInformation<br/>     | PowerPostSleep<br/>             |
| RegFlush<br/>              | PowerPerfStateChange<br/>       |
| RegKcbCreate<br/>          | PowerThermalConstraint<br/>     |
| RegKcbDelete<br/>          | PowerIdleStateChange<br/>       |
| RegVirtualize<br/>         | CritSecCollision<br/>           |
| RegCloseKey<br/>           |                                       |



 

### Resources

<dl>

[Windows Performance Toolkit (v.4.6)](http://go.microsoft.com/fwlink/p/?linkid=103276)  
</dl>

 

 





