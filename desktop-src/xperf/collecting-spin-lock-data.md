---
title: Collecting Spin Lock Data
description: Collecting Spin Lock Data
ms.assetid: 074dd18a-a767-4815-8b9f-3b41ad1df1dd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Collecting Spin Lock Data

Collecting Spin Lock event data consists of three steps:

1.  Start Spin Lock Event Data Collection

2.  Run the scenario under investigation

3.  Stop Spin Lock Event Data Collection

### Starting Spin Lock Event Data Collection

Spin Lock data is collected using standard WPA command line syntax. For more information on using WPA command line syntax please see [Starting a Trace](starting-a-trace.md). To begin event data collection enter the following at an administrator command prompt:


```
xperf -on PROC_THREAD+LOADER+SPINLOCK  
```





| Command, Parameter or Option | Usage                                                       |
|------------------------------|-------------------------------------------------------------|
| -on<br/>               | Starts the kernel logger process<br/>                 |
| PROC\_THREAD<br/>      | Collects process and thread create/delete events<br/> |
| LOADER<br/>            | Collects kernel and user mode load/unload events<br/> |
| SPINLOCK<br/>          | Collects Spin Lock events <br/>                       |



 

Spin Lock event data can be collected using only the "SPINLOCK" option. For example:


```
xperf -on SPINLOCK  
```



However, if the "PROC\_THREAD+LOADER" options are omitted symbol information will not be available for decoding. For more information on symbols please see the [Symbol Support](symbol-support.md) section of this document.

### Run Your Scenario

If your test scenario is already running, it is not necessary to stop the scenario in order to collect Spin Lock events. You can start Spin Lock events collection while the code of interest is being actively exercised. Nor is it necessary to suspend your scenario when Spin Lock event data has been collected.

> [!Note]  
> In certain cases, a large number of Spin Lock events can tax the ability WPT to keep up with logging events. A message box indicating that a number of events have been lost is displayed when merging data. In order to mitigate this circumstance WPT offers a number of parameters that can be tuned. For a complete discussion on avoiding lost events please see [Avoiding Lost Buffers](avoiding-lost-buffers.md).

 

### Stopping Spin Lock Event Data Collection and Merging Data

To stop WPA data collection and prepare the data for analysis use the following command:


```
xperf -d example.etl
```





| Command, Parameter or Option | Usage                                                                                                                              |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| -d<br/>                | Stops the kernel logger process and collates the event data that has been collected.<br/>                                    |
| example.etl<br/>       | The user selected name for the event data file. In order to avoid any issues with analysis, use the ".etl" file suffix.<br/> |



 

For more information on stopping a trace please see [Stopping a Trace](stopping-a-trace.md).

### Customizing Spin Lock Event Collection Parameters

By default, the system will log one spinlock event for every 1000 non-contended acquisitions, and one spinlock event for every contended acquisition. Spin Lock data collection supports three parameters that allow you to customize data collection. To set Spin Lock collection parameters use:


```
xperf -setspinlocksample [spin_threshold] [acquire_sample_rate] [contention_sample_rate]
```



**Parameters:**

-   **spin\_threshold** - The Spin Lock instrumentation provides a capability to trace heavily contended locks. This is achieved by setting a high spin threshold. If a lock that spins less than this threshold, no spinlock event will be acquired. For example, if this value is 1, one spinlock event will be acquired for each attempt to acquire a lock. If this value is 10, one spinlock event will be acquired for each ten attempts to acquire a lock. Default = 1

-   **acquire\_sample\_rate** - The sample rate at which spinlock events are acquired during a trace. For example, if this value is 1000, one spinlock event will be acquired for each one thousand non-collision event acquisitions. Default = 1000

-   **contention\_sample\_rate** - The rate at which spinlock events are acquired when collisions occur. For example, if this value is 100, one spinlock event is acquired for each one hundred Spin Lock collisions. Default = 1

For example,


```
xperf -setspinlocksample 1 1000 100
```



To query current spinlock parameters:


```
xperf -spinlock
```



Returns:


```
Current Spinlock Spin Threshold = 1
Current Spinlock Acquire Sample Rate = 1000
Current Spinlock Contention Sample Rate = 100
```



> [!Note]  
> Spinlock collection parameters are returned to the default values when the system is rebooted. To ensure valid data collection, always query or set spinlock parameters before starting event data collection.

 

 

 





