---
title: Data Formats and Transfer Media
description: Data Formats and Transfer Media
ms.assetid: c6023c42-ce20-40e4-9d88-55fa1d2a4d38
ms.topic: article
ms.date: 05/31/2018
---

# Data Formats and Transfer Media

Most platforms, including Windows, define a standard protocol for transferring data between applications, based on a set of functions called the clipboard. Applications using these functions can share data even if their native data formats are wildly different. Generally, these clipboards have two significant shortcomings that COM has overcome.

First, data descriptions use only a format identifier, such as the single 16-bit clipboard format identifier on Windows, which means the clipboard can only describe the structure of its data, that is, the ordering of the bits. It can report, "I have a bitmap" "or I have some text," but it cannot specify the target devices for which the data is composed, which views or aspects of itself the data can provide, or which storage media are best suited for its transfer. For example, it cannot report, "I have a string of text that is stored in global memory and formatted for presentation either on screen or on a printer" or "I have a thumbnail sketch bitmap rendered for a 100 dpi dot-matrix printer and stored as a disk file."

Second, all data transfers using the clipboard generally occur through global memory. Using global memory is reasonably efficient for small amounts of data but horribly inefficient for large amounts, such as a 20 MB multimedia object. Global memory is slow for a large data object, whose size requires considerable swapping to virtual memory on disk. In cases where the data being exchanged is going to reside mostly on disk anyway, forcing it through this virtual-memory bottleneck is highly inefficient. A better way would skip global memory entirely and simply transfer the data directly to disk.

To alleviate these problems, COM provides two data structures: [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) and [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1). For more information, see the following topics:

-   [The FORMATETC Structure](the-formatetc-structure.md)
-   [The STGMEDIUM Structure](the-stgmedium-structure.md)

## Related topics

<dl> <dt>

[Data Transfer](data-transfer.md)
</dt> </dl>

 

 




