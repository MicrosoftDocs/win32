---
title: stackwalk
description: Displays the stakwalking options. Stack walking flags can be specified either directly on the command line or in a file.
ms.assetid: 43aebeb9-5bb9-475f-a092-e5017f40c0d4
keywords:
- stackwalk Windows Performance Analyzer
topic_type:
- apiref
api_name:
- stackwalk
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# stackwalk

Displays the stakwalking options. Stack walking flags can be specified either directly on the command line or in a file.

``` syntax
xperf -on base -stackwalk ThreadCreate+ProcessCreate
xperf -on base -stackwalk ThreadCreate -stackwalk ProcessCreate
xperf -on base -stackwalk @stack.txt

The stack walking flag file can contain any number of stack walking flags per line, separated by spaces, plus ("+") signs, or on new lines:

ThreadCreate ProcessCreate
DiskReadInit+DiskWriteInit+DiskFlushInit
CSwitch
```

### Comments

The file can also contain empty lines or comments prefixed by "!".

The following is a list of recognized stack walking flags:



|                                      |                                      |                                       |
|--------------------------------------|--------------------------------------|---------------------------------------|
| ProcessCreate <br/>            | ProcessDelete <br/>            | ImageLoad <br/>                 |
| ImageUnload <br/>              | ThreadCreate <br/>             | ThreadDelete <br/>              |
| CSwitch <br/>                  | ReadyThread <br/>              | ThreadSetPriority <br/>         |
| ThreadSetBasePriority <br/>    | Mark <br/>                     | SyscallEnter <br/>              |
| SyscallExit <br/>              | Profile <br/>                  | ProfileSetInterval <br/>        |
| DiskReadInit <br/>             | DiskWriteInit <br/>            | DiskFlushInit <br/>             |
| FileCreate <br/>               | FileCleanup <br/>              | FileClose <br/>                 |
| FileRead <br/>                 | FileWrite <br/>                | FileSetInformation <br/>        |
| FileDelete <br/>               | FileRename <br/>               | FileDirEnum <br/>               |
| FileFlush <br/>                | FileQueryInformation <br/>     | FileFSCTL <br/>                 |
| FileDirNotify <br/>            | FileOpEnd <br/>                | SplitIO <br/>                   |
| RegQueryKey <br/>              | RegEnumerateKey <br/>          | RegEnumerateValueKey<br/>       |
| RegDeleteKey <br/>             | RegCreateKey <br/>             | RegOpenKey <br/>                |
| RegSetValue <br/>              | RegDeleteValue <br/>           | RegQueryValue <br/>             |
| RegQueryMultipleValue <br/>    | RegSetInformation <br/>        | RegFlush <br/>                  |
| RegKcbCreate <br/>             | RegKcbDelete <br/>             | RegVirtualize <br/>             |
| RegCloseKey<br/>               | RegCloseKey<br/>               | HardFault<br/>                  |
| PagefaultTransition<br/>       | PagefaultDemandZero<br/>       | PagefaultCopyOnWrite<br/>       |
| PagefaultGuard<br/>            | PagefaultHard<br/>             | PagefaultAV<br/>                |
| VirtualAlloc<br/>              | VirtualFree<br/>               | PagefileBackedImageMapping<br/> |
| HeapRangeCreate<br/>           | HeapRangeReserve<br/>          | HeapRangeRelease<br/>           |
| HeapRangeDestroy<br/>          | HeapCreate<br/>                | HeapAlloc<br/>                  |
| HeapRealloc<br/>               | HeapFree<br/>                  | HeapDestroy<br/>                |
| AlpcSendMessage<br/>           | AlpcReceiveMessage<br/>        | AlpcWaitForReply<br/>           |
| AlpcWaitForNewMessage<br/>     | AlpcUnwait<br/>                | ThreadPoolCallbackEnqueue<br/>  |
| ThreadPoolCallbackDequeue<br/> | ThreadPoolCallbackStart<br/>   | ThreadPoolCallbackStop<br/>     |
| ThreadPoolCallbackCancel<br/>  | ThreadPoolCreate<br/>          | ThreadPoolClose<br/>            |
| ThreadPoolSetMinThreads<br/>   | ThreadPoolSetMaxThreads<br/>   | PowerSetPowerAction<br/>        |
| PowerSetPowerActionReturn<br/> | PowerSetDevicesState<br/>      | PowerSetDevicesStateReturn<br/> |
| PowerDeviceNotify<br/>         | PowerDeviceNotifyComplete<br/> | PowerSessionCallout<br/>        |
| PowerSessionCalloutReturn<br/> | PowerPreSleep<br/>             | PowerPostSleep<br/>             |
| PowerPerfStateChange<br/>      | PowerThermalConstraint<br/>    | PowerIdleStateChange<br/>       |
| CritSecCollision<br/>          |                                      |                                       |



 

 

 





