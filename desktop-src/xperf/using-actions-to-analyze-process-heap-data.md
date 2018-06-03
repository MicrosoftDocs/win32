---
title: Using Actions to Analyze Process Heap Data
description: Using Actions to Analyze Process Heap Data
ms.assetid: 4040f43a-b0f6-4fbc-a85f-56aae15186d3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Actions to Analyze Process Heap Data

It is important to understand the following list of terms before performing heap actions on a trace file.

-   A *frame* identifies a module together with a symbol in that module or an IP (instruction pointer) if symbol information is unavailable.

-   A *call stack* is a sequence of stack frames. If stacks are not available from a trace, WPA may assume the stack to be the empty sequence.

-   *Culling* removes certain heap allocation functions from stacks before aggregation in order that:

    -   The heap allocation functions do not clutter the output stacks
    -   Aggregation by "-frame" will aggregate by the frames that call the allocation functions, not the allocation functions.

    The longest prefix of a stack is taken where each element matches at least one of the items specified by "-cullFrames", "-cullLists" or an internal default list that includes items such as ntdll.dll!RtlAllocateHeap and msvcrt.dll!malloc. If the prefix to be culled is shorter than the stack, the prefix is removed from the stack and the remainder of the stack is used for the subsequent aggregation. If the prefix to be culled is as long as the stack every element of the stack is removed except for the bottom element.

    A sample cullLists file, cullFuncs.txt is provided with the WPA installation files.

-   *Filtering* allows only allocations that meet certain criteria to be counted; the rest are ignored during aggregation. The three filtering options are :

    -   **-requireFrames**: An allocation is counted for the desired aggregation activities only if its HeapAlloc stack contains at least one frame that matches any of the required frames. This check is performed before culling.
    -   **-lifetime**: An allocation is counted only if it was alive for a duration matching a provided time range.
    -   **-size**: An allocation is counted only if its size matched a provided size range.

-   *Frame matching* can be specified as **module!**, **module!symbol**, or **symbol** in order to match, respectively, frames for a specified module for any symbol, frames for a specified module and a specified symbol, or frames for a specified symbol for any module.

-   *Outstanding* allocations are allocations that do not have a matching HeapFree event for its HeapAlloc event (within any specified "-range" period).

-   *Total* allocations are considered as all allocations regardless of whether they have been freed. Each HeapAlloc event describing an allocation request results in one of these.

-   **Size vs count**: The aggregation output includes size as well as count for *outstanding* and *total*. For the options specifying sort order use

    <dl> outstanding size (**so**)  
    outstanding count (**soc**)  
    total size (**st**)  
    total count(**stc**)  
    realloc count (**src**)  
    </dl>

    The default is **so**.

-   **Realloc**: WPA also tracks the number of reallocations. Certain allocations are really the result of heap reallocation and realloc count simply means the number of such allocations.

> [!Note]  
> Symbol information is necessary for many of the heap actions provided by WPA. In general, any activity that outputs any symbol information in a call stack or a stack frame requires "-symbols". Specifying frames that are required or frames to be culled also require "-symbols" if symbols are given in the specified frames. If the required symbol information is not available, WPA will use the Instruction Pointer (IP) value of individual stack frames.

 

The following table lists the available heap action options:



| Option                                                | Description                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-stacks \[s\[o\|oc\|t\|tc\|rc\]\]**<br/>      | Displays the allocations, aggregated by stacks. This is the default behavior.<br/> Sorts by outstanding size (**so**), total size (**st**),outstanding count (**soc**), realloc count (**src**) and total count ( **stc**). The default is **so**.<br/>                                                                              |
| **-frames \[s\[o\|oc\|t\|tc\|rc\]\]**<br/>      | Displays the allocations, aggregated by topmost stack frame. The arguments are the same as for the -stacks option.<br/>                                                                                                                                                                                                                    |
| **-image \[s\[o\|oc\|t\|tc\|rc\]\]**<br/>       | Displays the allocations, aggregated by image name of the topmost stack. The arguments are the same as for the -stacks option.<br/>                                                                                                                                                                                                        |
| **-range***T1T2*<br/>                           | Specifies that only event data from between times T1 and T2 should be used.<br/>                                                                                                                                                                                                                                                           |
| **-lifetime***L1L2*<br/>                        | Includes only allocations with lifetimes greater than or equal to L1 and less than L2.<br/>                                                                                                                                                                                                                                                |
| **-size***S1S2*<br/>                            | Specifies that only allocations of sizes greater than or equal to S1 and less than S2 should be included. Sizes are specified in bytes.<br/>                                                                                                                                                                                               |
| **-cullFrames***frames*<br/>                    | Removes from the report (culls) any top stack frames that match any of the given frames. The argument format is \[image!\]\[symbol\]. The names are not case sensitive. <br/>                                                                                                                                                              |
| **-requireFrames***frames*<br/>                 | Requires that each stack has at least one frame that matches at least one of the given frames. This test occurs before any explicit frame culling with -cullFrames.<br/> If a stack does not include such a frame, it is excluded.<br/> Frames have the same format as for -cullFrames. The names are not case sensitive.<br/> |
| **-cullLists***filename* \[*filename*..\] <br/> | Culls frames listed in the specified file(s). Frames are listed in the file(s) one per line. Blank lines and lines that begin with '\#' are ignored. A sample cullLists file is included in the reference section of this document.<br/>                                                                                                   |
| **-top N**<br/>                                 | Restricts the number of items displayed to *N*. <br/> If -top is not used, the maximum number of items displayed is 10,000. Any item beyond the initial maximum number is discarded. The limit applies to every activity.<br/>                                                                                                       |
| **-totals**<br/>                                | Displays only the totals of the allocation events.<br/>                                                                                                                                                                                                                                                                                    |



 

 

 





