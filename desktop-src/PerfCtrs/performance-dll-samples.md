---
Description: 'The Windows SDK (WSDK) contains three complete sample performance DLLs.'
ms.assetid: '862be53a-3d58-42b9-adf0-2f913dc6fb06'
title: Performance DLL Samples
---

# Performance DLL Samples

The Windows SDK (WSDK) contains three complete sample performance DLLs. These samples are located in the Samples\\WinBase\\WinNT\\PerfTool\\PerfDlls directory. The root of this path is the base installation directory of the WSDK. You can download the WSDK from the [Microsoft Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=162443) (search for Windows SDK and select the download for the latest released operating system).

The samples contained in this directory are:

-   **AppMem**—Provides counterparts of the [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574), [**GlobalReAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366590), and [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579) functions that report performance information. Performance counters in the registry and the Performance tool can read the performance information.
-   **LeakyBin**—Demonstrates the use of application performance counters.
-   **PerfGen**—Provides three waveforms at five different periods for use with the Performance tool to provide data at a known rate and value. This can be useful in testing applications that use performance data and need predictable values to test against.

 

 



