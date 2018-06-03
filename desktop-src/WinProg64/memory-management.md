---
title: Memory Management Under WOW64
description: Memory management under WOW64 depends on the processor architecture.
ms.assetid: a3fa6e51-2895-4941-9304-5939208e8102
keywords:
- WOW64 64-bit Windows Programming , memory management
- memory management 64-bit Windows Programming
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management Under WOW64

Memory management under WOW64 depends on the processor architecture.

## Itanium Support

WOW64 simulates 4 KB pages on top of the native 8 KB pages that the Itanium processor uses. The processor assists by providing excellent simulation with low overhead. The simulation code cannot handle the following cases:

-   Write tracking. The [**GetWriteWatch**](https://msdn.microsoft.com/library/windows/desktop/aa366573) and [**ResetWriteWatch**](https://msdn.microsoft.com/library/windows/desktop/aa366874) functions are implemented in the kernel using native page-size granularity, which means the WOW64 4 KB page simulation cannot determine which simulated 4 KB pages are written within the underlying 8 KB page.
-   [Address Windowing Extensions (AWE)](https://msdn.microsoft.com/library/windows/desktop/aa366527). The AWE functions operate on page numbers, and there is no way to map 64-bit page numbers to 32-bit page numbers.
-   Section alignment. For executable images with section alignment smaller than 8 KB (the default is 4 KB for x86 images), WOW64 must dirty all image pages. This effectively copies each page to the page file, and prevents read-only image pages from being shared between processes.
-   The [**ReadFileScatter**](https://msdn.microsoft.com/library/windows/desktop/aa365469) and [**WriteFileGather**](https://msdn.microsoft.com/library/windows/desktop/aa365749) functions are not supported.

## x64 and ARM64 Support

The native page size is 4 KB. Therefore, the following are supported:

-   The [**GetWriteWatch**](https://msdn.microsoft.com/library/windows/desktop/aa366573) and [**ResetWriteWatch**](https://msdn.microsoft.com/library/windows/desktop/aa366874) functions are supported.
-   The [**ReadFileScatter**](https://msdn.microsoft.com/library/windows/desktop/aa365469) and [**WriteFileGather**](https://msdn.microsoft.com/library/windows/desktop/aa365749) functions are supported.
-   There are advantages to using large addresses because x64 WOW64 supports a 4 GB virtual address space.

## Related topics

<dl> <dt>

[Memory Limits for Windows Releases](https://msdn.microsoft.com/library/windows/desktop/aa366778)
</dt> <dt>

[4GT RAM Tuning](https://msdn.microsoft.com/library/windows/desktop/bb613473)
</dt> </dl>

 

 




