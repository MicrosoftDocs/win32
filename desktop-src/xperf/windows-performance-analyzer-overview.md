---
title: Windows Performance Analyzer Overview
description: Windows Performance Analyzer Overview
ms.assetid: '7eae462c-d404-4ce4-b8c1-da5e440d7280'
keywords: ["Windows Performance Analyzer, about", "Windows Performance Analyzer, Event Tracing for Windows", "Windows Performance Analyzer, ETW", "Windows Performance Analyzer, graphs", "Windows Performance Analyzer, summary table", "Windows Performance Analyzer, stack walking", "Windows Performance Analyzer, actions"]
---

# Windows Performance Analyzer Overview

WPA is a powerful set of programs that provide detailed views of system and application behavior and resource usage. WPA can be used to investigate particular areas of performance and to gain an overall understanding of resource consumption. Using WPA gives development teams the opportunity to proactively identify and resolve performance issues.

WPA uses the extremely low overhead [Event Tracing for Windows](event-tracing-for-windows.md) (ETW) infrastructure to collect performance and system data. ETW functions are built into the operating system and any applications that run on Windows. Windows Vista and Windows Server 2008 have hundreds of ETW events available for capture. These events can provide extensive information by capturing data generated during execution. ETW is fully documented and supported by Microsoft. Application developers and architects are encouraged to implement ETW in new applications. By including these functions, a new application will be able to take full advantage of Windows Performance Analyzer features and benefits. For more information on ETW please see Event Tracing for Windows.

WPA collates and displays data into three formats:

-   **Graphs**
    -   Graphs are consistently formatted with the x-axis representing time and the y-axis representing the captured event data.

    -   Trace activities resulting in multiple sets of data produce multiple graphs. Time periods are consistent across the entire set of graphs produced by a trace.

    -   Selected areas of a graph may be "zoomed in" to examine trace data on a more granular level. For example, if a CPU sample graph showed normal activity for all but a short time segment, a user can zoom in on the time segment showing the abnormal activity. By zooming in the user can determine which process and thread caused the abnormal activity.

    -   Since all the graphs in the set are linked, the zoom function will magnify the selected time segment on all of the graphs in the set, allowing the user to observe all relevant activity during the selected time segment.

    -   Graphs can be overlaid or merged in order to provide a more holistic view of the system activity in question. At any time the user may revert to the original graphic representation by "zooming out".

    -   For more information on Graphs, please the [Graphs](windows-performance-analyzer-feature--graphs.md) section of this document.

-   **Summary Table Data**
    -   Summary tables are formatted with rows representing time units and columns representing captured event data.

    -   Using the summary table format, the user can show, hide, or reposition individual data columns.

    -   A sophisticated sort and aggregation facility is also available when working with summary tables.

    -   Call stack data can be displayed using summary tables combined with symbol decoding.

    -   For more information on using summary tables, please see the [Summary Tables](summary-tables.md) section of this document.

-   **Text and Custom File Formats**
    -   Customized file formats can be created to accommodate specialized performance profiling for a specific environment.

    -   Captured event data from WPA may be output in a number of file formats including ASCII text and csv format.

    -   Customized call stack data can be included in output files using the [Actions](actions.md) syntax.

    -   For more information on producing custom file output from WPA traces, please see the [Actions](actions.md) section of this document.

Other WPA Features:

-   Stack Walking - Using WPA, the kernel can capture the call stack when an event is generated. The generating event and the associated call stack can be saved in a trace file. When stacks are combined with symbol decoding, you can display the call stack information for the events that had stack walking enabled during the trace. For more information on stack walking, please see the [Stack Walking](stack-walking.md) section of this document.

-   WPA is designed for both scripting and command line operation. Using the automatic scripting features, WPA can be employed in "lights out" environments while capturing real time performance information.

-   WPA event tracing can be enabled and disabled at any time without requiring system or process restarts. This benefit can be critical when capturing performance information from real time user environments.

-   Once trace data has been captured, this data can be processed on the machine on which it was or copied to another machine. For example, a trace generated from Windows Server 2008 can be analyzed on a Windows Vista machine.

 

 




