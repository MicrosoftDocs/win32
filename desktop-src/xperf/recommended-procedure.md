---
title: Recommended Procedure
description: Recommended Procedure
ms.assetid: 'b42aae95-ddaf-4da2-963f-b40697bfcb93'
keywords: ["xbootmgr", "trace", "rebootCycle", "noPrepReboot", "prepSystem", "standby", "numRuns"]
---

# Recommended Procedure

When you use the On/Off Transition Trace Capture tool to measure performance, consider the following two benchmark measurements:

1.  The current state of the test system

2.  The optimized state of the test system

To gain an understanding of existing issues on a system, you can use the On/Off Transition Trace Capture tool to capture a single trace without applying any modifications to the system. For example, the following command produces two traces, one capturing a shutdown and one capturing a subsequent boot (including the logon procedure):


```
xbootmgr -trace rebootCycle -noPrepReboot
```



This trace helps you to gain insight into potential optimizations that can be made to the machine and its environment, such as group policy settings, network connectivity issues, and so on.

You can also use the On/Off Transition Trace Capture tool to force existing internal operating system optimization mechanisms to update their state based on the current configuration of the system. You should do this if you want to determine the best possible boot time that the system can deliver in its existing configuration. It is especially important to re-optimize the system when you perform iterative tuning by progressively modifying the state of the system between traces.

To create a trace of the optimized system state, type the following:


```
xbootmgr -trace rebootCycle -prepSystem
```



Using the -prepSystem option with Windows XP will yield the following behavior

-   The system will reboot six times. These reboots will not contain any trace information.

-   After the six "empty" reboots, the system will commence with the reboots as indicated with the -numRuns option.

Starting with Windows Vista, the operating system will yield this behavior:

-   Reboot three times, no trace data will be saved.

-   The user will possibly encounter a short pause as WPA checks for tasks. This checking will be transparent to the user.

-   Reboot three more times, no trace data will be saved.

-   After a total of six "empty" reboots, the system will commence with the reboots as indicated with the -numRuns option

Remember that these optimization mechanisms always run automatically when the machine becomes idle and that the On/Off Transition Trace Capture tool simply provides a way to force these mechanisms to update synchronously and in the foreground to facilitate test automation.

Another helpful feature of the On/Off Transition Trace Capture tool is that it can gather multiple traces to build a statistically significant base of data. The following command line gathers ten standby/resume traces:


```
xbootmgr -trace standby -numRuns 10
```



 

 




