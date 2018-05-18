---
title: The Butterfly View
description: The Butterfly View
ms.assetid: '4996bac8-1160-4522-a0a4-bf5380305a20'
---

# The Butterfly View

The butterfly view of a summary table flips the call stack in order that a "pivot" function will be used as a base function. This feature provides the following:

-   Ability to analyze only allocations involving a specific function.

-   A hierarchical view of function execution allowing the user to view a function in a recursive manner.

-   Using the butterfly view on ntdll.dll!RtlAllocateHeap helps to aggregate split stacks in a more meaningful manner since the aggregation is done starting at the leaf node and not at the missing call stack root. However, it should be noted not all heap allocations will be made during calls to ntdll.dll!RtlAllocateHeap. Care should be taken to account for those allocations made from calls to different allocating functions in ntdll.dll.

-   Note the size and lifetime data for the allocations will be more separated from the allocating function in the summary table which makes some data interpretation more difficult.

To create a butterfly view of the calls to a function, select its row, right click and then select "callers/Innermost..." from the context menu. If the selected function is ntdll.dll!RtlAllocateHeap, the call stacks will "flip" such that this function will be used as the base function for the stack displays. Regular stack navigation can then take place on the reordered stack.

The following screen shot shows a Butterfly view of heap handle 0x 01de 0000.

![screen shot of a butterfly view of heap handle 0x 01de 0000 ](images/he-img16.png)

In this table, Butterfly view of heap handle 0x 01de 0000, a butterfly view is opened using the ntdll.dll!RtlAllocateHeap function as the outermost caller in the 0x01de 000 heap. 164 allocations using 916,929 bytes have been made by GdiPlus.dll. Applications based on the Microsoft Win32 API do not access graphics hardware directly. Instead, GDI+ interacts with device drivers on behalf of applications.

The following screen shot shows a Butterfly view sorted by allocation count.

![screen shot of a butterfly view sorted by allocation count](images/he-img17.png)

By changing the sorting order to count, and then expanding the call stacks, a view of the data showing functions that have the most allocations based on count is displayed.

 

 




