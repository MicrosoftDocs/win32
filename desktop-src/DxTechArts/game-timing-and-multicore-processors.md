---
title: Game Timing and Multicore Processors
description: This article suggests a more accurate, reliable solution to obtain high-resolution CPU timings by using the Windows APIs QueryPerformanceCounter and QueryPerformanceFrequency.
ms.assetid: 1512324d-dffa-3681-be3f-f63a3b8f11db
ms.topic: article
ms.date: 05/31/2018
---

# Game Timing and Multicore Processors

With power management technologies becoming more commonplace in today's computers, a commonly-used method to obtain high-resolution CPU timings, the RDTSC instruction, may no longer work as expected. This article suggests a more accurate, reliable solution to obtain high-resolution CPU timings by using the Windows APIs [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency).

-   [Background](#background)
-   [Recommendations](#recommendations)
-   [Application Compatibility](#application-compatibility)

## Background

Since the introduction of the x86 P5 instruction set, many game developers have made use of read time stamp counter, the RDTSC instruction, to perform high-resolution timing. The Windows multimedia timers are precise enough for sound and video processing, but with frame times of a dozen milliseconds or less, they don't have enough resolution to provide delta-time information. Many games still use a multimedia timer at start-up to establish the frequency of the CPU, and they use that frequency value to scale results from RDTSC to get accurate time. Due to the limitations of RDTSC, the Windows API exposes the more correct way to access this functionality through the routines of [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency).

This use of RDTSC for timing suffers from these fundamental issues:

-   Discontinuous values. Using RDTSC directly assumes that the thread is always running on the same processor. Multiprocessor and dual-core systems do not guarantee synchronization of their cycle counters between cores. This is exacerbated when combined with modern power management technologies that idle and restore various cores at different times, which results in the cores typically being out of synchronization. For an application, this generally results in glitches or in potential crashes as the thread jumps between the processors and gets timing values that result in large deltas, negative deltas, or halted timing.
-   Availability of dedicated hardware. RDTSC locks the timing information that the application requests to the processor's cycle counter. For many years this was the best way to get high-precision timing information, but newer motherboards are now including dedicated timing devices which provide high-resolution timing information without the drawbacks of RDTSC.
-   Variability of the CPU's frequency. The assumption is often made that the frequency of the CPU is fixed for the life of the program. However, with modern power management technologies, this is an incorrect assumption. While initially limited to laptop computers and other mobile devices, technology that changes the frequency of the CPU is in use in many high-end desktop PCs; disabling its function to maintain a consistent frequency is generally not acceptable to users.

## Recommendations

Games need accurate timing information, but you also need to implement timing code in a way that avoids the problems associated with using RDTSC. When you implement high-resolution timing, take the following steps:

1.  Use [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) instead of RDTSC. These APIs may make use of RDTSC, but might instead make use of a timing devices on the motherboard or some other system services that provide high-quality high-resolution timing information. While RDTSC is much faster than **QueryPerformanceCounter**, since the latter is an API call, it is an API that can be called several hundred times per frame without any noticeable impact. (Nevertheless, developers should attempt to have their games call **QueryPerformanceCounter** as little as possible to avoid any performance penalty.)
2.  When computing deltas, the values should be clamped to ensure that any bugs in the timing values do not cause crashes or unstable time-related computations. The clamp range should be from 0 (to prevent negative delta values) to some reasonable value based on your lowest expected framerate. Clamping is likely to be useful in any debugging of your application, but be sure to keep it in mind if doing performance analysis or running the game in some unoptimized mode.
3.  Compute all timing on a single thread. Computation of timing on multiple threads — for example, with each thread associated with a specific processor — greatly reduces performance of multi-core systems.
4.  Set that single thread to remain on a single processor by using the Windows API [**SetThreadAffinityMask**](/windows/win32/api/winbase/nf-winbase-setthreadaffinitymask). Typically, this is the main game thread. While [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) typically adjust for multiple processors, bugs in the BIOS or drivers may result in these routines returning different values as the thread moves from one processor to another. So, it's best to keep the thread on a single processor.

    All other threads should operate without gathering their own timer data. We do not recommend using a worker thread to compute timing, as this will become a synchronization bottleneck. Instead, worker threads should read timestamps from the main thread, and because the worker threads only read timestamps, there is no need to use critical sections.

5.  Call [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) only once, because the frequency will not change while the system is running.

## Application Compatibility

Many developers have made assumptions about the behavior of RDTSC over many years, so it is quite likely that some existing applications will exhibit problems when run on a system with multiple processors or cores due to the timing implementation. These problems will usually manifest as glitching or slow-motion movement. There is no easy remedy for applications that are not aware of power management, but there is an existing shim for forcing an application to always run on a single processor in a multiprocessor system.

To create this shim, download the Microsoft Application Compatibility Toolkit from [Windows Application Compatibility](/archive/blogs/yongrhee/download-application-compatibility-toolkit-act-for-windows-10).

Using the Compatibility Administrator, part of the toolkit, create a database of your application and associated fixes. Create a new compatibility mode for this database and select the compatibility fix **SingleProcAffinity** to force all of the threads of the application to run on a single processor/core. By using the command-line tool Fixpack.exe (also part of the toolkit), you can convert this database into an installable package for installation, testing, and distribution.

For instruction on using Compatibility Administrator, see the toolkit's documentation. For syntax for and examples of using Fixpack.exe, see its command-line help.

For customer-oriented information, see the following knowledge base articles from Microsoft Help and Support:

-   [Programs that use the QueryPerformanceCounter function may perform poorly in Windows Server 2003 and in Windows XP](https://support.microsoft.com/kb/895980) (article 895980)
-   [Game performance may be poor on a Windows XP-based computer that is using a dual-core processor](https://support.microsoft.com/kb/909944) (article 909944)

 

 
