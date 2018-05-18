---
title: Processing
description: Displays trace post-processing options.
ms.assetid: '2a4b4220-e99f-4d11-bd05-ead3d9737467'
keywords: ["Processing Windows Performance Analyzer"]
topic_type:
- apiref
api_name:
- processing
api_type:
- NA
---

# Processing

Displays trace post-processing options.

``` syntax
xperf -i <trace file>... 
     [-o output] 
     [-symbols ...] 
     [-target {human|machine}] 
     [-a action ...[-a action ...] ...]
     [-quiet]
     [-tle]
     [-tli]
```

## Parameters

<dl> <dt>

<span id="_______-i_______trace_file_______"></span><span id="_______-I_______TRACE_FILE_______"></span> **-i** trace file 
</dt> <dd>

The trace file to be processed.

</dd> <dt>

<span id="_______-o_______output_file______"></span><span id="_______-O_______OUTPUT_FILE______"></span> **-o** output file 
</dt> <dd>

Optional, the name of the file that output goes to. If not given, **stdout** is used.

</dd> <dt>

<span id="_______-symbols__options_________"></span><span id="_______-SYMBOLS__OPTIONS_________"></span> **-symbols** \[options\] 
</dt> <dd>

Enable and configure symbol decoding support. See "xperf -help symbols" for detailed help

</dd> <dt>

<span id="_______________-target___human_machine___"></span><span id="_______________-TARGET___HUMAN_MACHINE___"></span> **-target** {**human**\|**machine**} 
</dt> <dd>

Select the target audience of the output. Default is human.

</dd> <dt>

<span id="_______-a_______action_..._______"></span><span id="_______-A_______ACTION_..._______"></span> **-a** action ... 
</dt> <dd>

Optional, the actions to take. Default action is to dump the event in text form.

</dd> <dt>

<span id="_______-quiet______"></span><span id="_______-QUIET______"></span> **-quiet** 
</dt> <dd>

Do not print progress information.

</dd> <dt>

<span id="_______-tle______"></span><span id="_______-TLE______"></span> **-tle** 
</dt> <dd>

Process the trace even in the presence of lost events.

Lost events generally happen because the buffers for the trace sessions were too small or too few. If this happens, you should increase the ETW session sizes instead of using the **-tle** parameter. For more information, see [Using Event Tracing](https://msdn.microsoft.com/library/windows/desktop/aa364158).

> [!Note]  
> You must use **-tle** parameter only when a trace with missing events must be processed. If the parameter is specified and events were indeed lost, none of the calculations and aggregations produced by XPerf can be considered accurate.

 

</dd> <dt>

<span id="_______-tti______"></span><span id="_______-TTI______"></span> **-tti** 
</dt> <dd>

Process the trace even in the presence of time inversions.

On some systems, the time source may not be completely reliable. Although XPerf handles small time inversions by default, it issues a warning only in those cases where time inversions were too large or frequent.

> [!Note]  
> You must use **-tti** parameter only when a trace on a system with large time inversions must be processed. As a workaround, you may want to switch to another hardware platform whenever your trace sessions encounter time inversions.

 

</dd> </dl>

### Examples



|                                                         |                                                                     |
|---------------------------------------------------------|---------------------------------------------------------------------|
| xperf -i trace.etl -o out.csv<br/>                | dump the events in trace.etl to file out.csv<br/>             |
| xperf -help registry<br/>                         | print help on action registry<br/>                            |
| xperf -i trace.etl -a registry <br/>              | print registry access statistics to **stdout**<br/>           |
| xperf -i trace32.etl trace64.etl -o out.csv <br/> | dump the events in trace32.etl and trace64.etl to file o<br/> |



 

### Available Actions



| Action                  | Meaning                                                             |
|-------------------------|---------------------------------------------------------------------|
| boot <br/>        | Show boot and shutdown statistics<br/>                        |
| Bootprefetch<br/> | Show boot-time prefetching information<br/>                   |
| cpudisk <br/>     | Show CPU/Disk activity report<br/>                            |
| cswitch <br/>     | Show Context Switch data<br/>                                 |
| diskio <br/>      | Show Disk IO Statistics<br/>                                  |
| dpcisr <br/>      | Show DPC/ISR Statistics<br/>                                  |
| drvdelay <br/>    | Show Driver delays<br/>                                       |
| drvdelay <br/>    | Show Driver delays<br/>                                       |
| dumper <br/>      | Dump events in the trace in text form<br/>                    |
| filename <br/>    | Show File Names in the trace<br/>                             |
| focuschange <br/> | Show the Windows thread focus change events in the trace<br/> |
| hardfault <br/>   | Show hard fault statistics by process and file.<br/>          |
| marks <br/>       | Show Marks Information<br/>                                   |
| pagefault <br/>   | Show page fault information in the trace<br/>                 |
| perfctrs <br/>    | Show process performance counters<br/>                        |
| pnp <br/>         | Show PnP events in the trace<br/>                             |
| prefetch <br/>    | Show Prefetch Information<br/>                                |
| process <br/>     | Show process, thread, image information<br/>                  |
| profile <br/>     | Show Sampled profiler data<br/>                               |
| readyBoot <br/>   | Show ReadyBoot statistics<br/>                                |
| registry <br/>    | Show Registry Access Statistics<br/>                          |
| services <br/>    | Show service status information<br/>                          |
| shutdown <br/>    | Show shutdown statistics<br/>                                 |
| stack <br/>       | Show stack information<br/>                                   |
| suspend <br/>     | Show suspend transition information<br/>                      |
| sysconfig<br/>    | Show system configuration information<br/>                    |
| tracestats <br/>  | Show trace statistics<br/>                                    |
| winlogon <br/>    | Show Winlogon events in the trace<br/>                        |



 

Use xperf -help &lt;action&gt; \[&lt;action&gt; ...\] for detailed help. If no action is present, Dumper will be invoked.

 

 





