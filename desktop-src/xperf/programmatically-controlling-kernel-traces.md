---
title: Programmatically Controlling Kernel Traces
description: Programmatically Controlling Kernel Traces
ms.assetid: '2e8149d4-ec96-42b0-aebb-796ac9cf416f'
---

# Programmatically Controlling Kernel Traces

### Related Links

<dl>

[Windows Performance Analyzer](http://go.microsoft.com/fwlink/p/?linkid=141497  )  
[Event Tracing for Windows](http://go.microsoft.com/fwlink/p/?linkid=141498   )  
</dl>

### Summary

This document introduces the Downlevel Public Kernel Trace Control APIs. These APIs facilitate capturing kernel stack traces, merging multiple trace files for analysis, and including system information in the merged files.

### Overview of Downlevel Kernel Trace Control API

[Windows Performance Analyzer](http://go.microsoft.com/fwlink/p/?linkid=141497  ) (WPT), which is based on [Event Tracing for Windows](http://go.microsoft.com/fwlink/p/?linkid=141498) (ETW), offers a powerful set of tools that can be used to capture and analyze application and system performance behavior. WPT facilitates to capture, buffer, and log built-in kernel events and customized user events. These events provide developers and administrators extensive details about the operation of systems or applications. Captured events can then be merged and collated by WPT to produce graphs, tables and text files that contain performance and configuration information.

Additionally, WPT allows to capture stack traces, known as stackwalking, for specified events. Stack walking offers an unprecedented view of system and application behavior by making the call stacks available that generate specific events.

Prior to the release of the Kernel Trace Control API, capture and analysis of kernel event call stacks was limited to a command-line interface or the use of scripts to control WPT functions. The Kernel Trace Control API has added significant new functionality to WPT by allowing the invocation of WPT capture and merge capabilities in a well developed API. Using the Kernel Trace Control API, developers are shielded from the complexities of ETW programming. Instead, the Kernel Trace Control API offers a straightforward programmatic way to embed standard instrumentation into applications or build dedicated monitoring programs.

Kernel Trace Control provides developers the ability to programmatically start kernel tracing sessions, take advantage of new trace flags, insert system information into traces, and merge multiple trace files into a single file. This information can then be organized and analyzed using powerful presentation features of Windows Performance Analyzer.

### New Functionality

1.  The [**StartKernelTrace**](startkerneltrace.md) function extends the ETW [StartTrace](http://go.microsoft.com/fwlink/p/?linkid=141509) function by including stack tracing events.

2.  The **STACK\_TRACING\_EVENT\_ID** structure is introduced. This structure identifies to the kernel logger which events can generate call stacks.

3.  New trace event Type flags are added to indentify kernel stack tracing event types.

4.  A new function, **CreateMergedTraceFile**, enables merging of multiple trace files programmatically is introduced.

5.  Flags that define the type of system information to be added to a merged trace file, are available.

### Where Applicable

Use Kernel Trace Control to programmatically collect event information directly from the kernel. This information can then be merged with other system and application data to present a complete view of system behavior.

### Developer Audience

Kernel Trace Control is designed for C and C++ developers. The API expands on functionality provided in Event Tracing for Windows APIs. Familiarity with [Event Tracing for Windows](http://go.microsoft.com/fwlink/p/?linkid=141498              ) and [Windows Performance Analyzer](http://go.microsoft.com/fwlink/p/?linkid=141497  ) is required to implement the Kernel Trace Control APIs.

### Run Time Requirements

The Kernel Trace Control API runs on Windows Vista and later versions of the Windows operating system.

### Special Note to Users of x64 Systems

WPT stack walking requires setting certain registry values on x64 systems. For more information, see How to Enable Stack Walking on x64 Systems in the [Installation](installation.md) section of this document.

### Distribution

Kernel Trace Control API is distributed as an installation option with Windows Performance Analyzer version 5.

 

 




