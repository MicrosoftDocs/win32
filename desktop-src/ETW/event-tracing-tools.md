---
description: Lists the tools that are used in event tracing.
ms.assetid: 7a1c9d8c-5bf4-4f0c-b815-5b70e53c5e2d
title: Event Tracing Tools
ms.topic: reference
ms.date: 07/14/2025
---

# Event Tracing Tools

The following event tracing tools are available for your use.



| Tool     | Description                                                                                                                                                                                                                                                                                                                                |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Logman   | Manages and schedules performance counter and event trace log collections on local and remote systems. You can use this tool to list the providers that have [published the layout of their event data](publishing-your-event-schema.md) in the root\\wmi namespace. For details on using this tool, see the **Help and Support Center**. |
| Tracefmt | Formats information in a trace log file in human-readable form. For details, see Tools for Software Tracing in the Microsoft Windows Driver Development Kit (DDK). Used by WPP Software Tracing only.                                                                                                                                      |
| Tracelog | Controls an event trace session. For details, see Tools for Software Tracing in the DDK.                                                                                                                                                                                                                                                   |
| Tracepdb | Creates a trace message format file that the Tracefmt tool uses to convert logged messages to a human-readable form. For details, see Tools for Software Tracing in the DDK. Used by WPP Software Tracing only.                                                                                                                            |
| Tracerpt | Processes event trace logs or real-time events from instrumented event trace providers and allows you to generate trace analysis reports and CSV (comma-delimited) files for the events generated. For details, see the **Help and Support Center**.                                                                                       |
| [Windows Performance Recorder (WPR)](/windows-hardware/test/wpt/windows-performance-recorder) | Captures ETW traces with predefined or custom recording profiles. Part of the Windows Performance Toolkit (Windows ADK). |
| [Windows Performance Analyzer (WPA)](/windows-hardware/test/wpt/windows-performance-analyzer) | Graphical tool for visualizing and analyzing ETW traces captured by WPR or xperf. Provides detailed CPU, disk, memory, and UI responsiveness analysis. |
| [xperf](/windows-hardware/test/wpt/xperf-command-line-reference) | Command-line tool for capturing and processing kernel and user-mode ETW traces. Part of the Windows Performance Toolkit. |
| [PerfView](https://github.com/microsoft/perfview) | Free, open-source .NET and native performance analysis tool using ETW. Excels at CPU profiling, GC heap analysis, and wall-clock time investigations. |



 

 

 



