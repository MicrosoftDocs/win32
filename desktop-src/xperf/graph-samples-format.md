---
title: Graph Samples Format
description: Graph Samples Format
ms.assetid: 'bb3b1cf0-8493-4b33-880f-36e542572552'
---

# Graph Samples Format

The following information summarizes the manner sample graphs are presented in this document.

**Name of Graph:** - The name of the graph as it appears in the title section of the graph.

**Overview:** A brief summary of the information presented on the graph.

**Graph Type:** May be Usage, Histogram, Lifetime or Event. See the [Types of Graphs](types-of-graphs.md) section of this document for a definition of the various types of graphs available in WPA. For information regarding the algorithm

**Y-axis Units:** A description of the Y-axis, or vertical axis, of the graph.

**Required Flags:** Flags identify to WPA the events to capture in a trace. Multiple flags may be set for a trace in one of three ways:

1.  Using the "+" operator to add flags to a trace. An example of this syntax is:

    ```
    Xperf -on CSWITCH+DISPATCHER
    ```

    

    For a listing of the available kernel flags use this syntax:

    ```
    Xperf -providers kf
    ```

    

    Kernel flags are not case sensitive. For more information on flags see the [Start Trace](starting-a-trace.md) section of this document.

2.  Kernel groups aggregate flags into a single word. For example:

    ```
    Xperf -on Base
    ```

    

    For a listing of kernel groups, use this syntax:

    ```
    Xperf -providers kg
    ```

    

    Kernel groups are not case sensitive. For more information on flags see the Start Trace section of this document.

3.  Trace Profiles are sets of flags and options. An example of starting a trace using Trace Profiles is:

    ```
    Xperf -on perf!GeneralProfiles.InSequentialFile
    ```

    

    Trace Profiles are case sensitive. For more information on flags see the [Trace Profiles](trace-profiles.md) section of this document.

4.  For more information on starting and stopping traces see the [Command Line Reference](command-line-reference.md) section of this document.

**Legend Description:** Defines the data series enumerated in the Legend dropdown located on the right side of the graph.

**Graph Description:** Explains the data displayed. In certain cases the method of aggregation and other relevant information will be citied.

 

 




