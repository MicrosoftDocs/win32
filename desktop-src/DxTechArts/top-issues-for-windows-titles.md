---
title: Top Issues for Windows Titles
description: This article highlights many of the common issues we've seen in current-generation PC games.
ms.assetid: 89b83473-1aa9-9a2d-8778-15cfb91cdea4
ms.topic: article
ms.date: 05/31/2018
---

# Top Issues for Windows Titles

The Microsoft Windows Gaming and Graphics Technologies Developer Relations group performs performance analysis for many Windows games each year. During these sessions, we get hands-on experience to tie into the developer feedback and queries we receive daily. Occasionally we help track down a mysterious crash or other problem in a title, which gives us further insight into problems that developers are encountering.

This article highlights many of the common issues we've seen in current-generation PC games.

-   [CPU-Limited Performance](#cpu-limited-performance)
-   [Poor Batch Management](#poor-batch-management)
-   [Excessive Memory Copying](#excessive-memory-copying)
-   [Excessive Use of Dynamic Draw Submission](#excessive-use-of-dynamic-draw-submission)
-   [High Overhead in File Processing](#high-overhead-in-file-processing)
-   [Slow and Frustrating Installation](#slow-and-frustrating-installation)
-   [Lack of Consideration of Physical Memory](#lack-of-consideration-of-physical-memory)
-   [Over-Reliance on Real-Time Audio Sample Rate Conversion](#over-reliance-on-real-time-audio-sample-rate-conversion)
-   [Fragmention of Virtual Memory](#fragmention-of-virtual-memory)
-   [Manipulation of the Floating-Point Control Word](#manipulation-of-the-floating-point-control-word)
-   [Optional Installation of the DirectX Runtime](#optional-installation-of-the-directx-runtime)
-   [Excessive Use of Thread Synchronization](#excessive-use-of-thread-synchronization)
-   [Use of RDTSC](#use-of-rdtsc)

## CPU-Limited Performance

The vast majority of games are limited by CPU performance on systems with high-performance graphics processing units (GPUs). This is sometimes due to poor use of batching for draw submissions, but more typically, this is due to other game systems consuming a large portion of the available CPU cycles. In the few cases in which we have seen the GPU as the limitation, the cause is very high fill rates or pixel shader demand, in high-resolution settings, or low vertex-shader performance by a video card.

Because most titles are CPU-limited, the biggest performance wins come from optimizing CPU-intensive game systems. Typically, the AI or physics systems and the associated collision-detection logic are the primary consumers of CPU cycles in well-behaving Microsoft Direct3D applications. Any work to improve these systems can improve the overall performance of the game.

## Poor Batch Management

Achieving good parallelism with the GPU requires that draw batches contain enough geometry — and the shaders have the right complexity — to keep the video card busy, while not using so many batches that the command buffer is flooded. On current-generation hardware, we recommend approximately 300 or fewer draw-batch submissions per frame (fewer on lower-performance CPUs) to prevent the driver's processing of the command-buffer from becoming a performance bottleneck. Some other API state calls and driver combinations can result in costly CPU processing (driver compiling of shaders, for example), so we highly recommend routine performance analysis.

## Excessive Memory Copying

During the development of most PC titles, developers use convenient data structures and strings for content management. The CPU work required for string comparison, copying, and other manipulations often has a measurable overhead, particularly when taking into account the performance hits associated with the cache and memory subsystem. Plans should be made when developing these systems for removing or minimizing the reliance on string processing once the product enters into the primary testing and release phases.

## Excessive Use of Dynamic Draw Submission

Modern video hardware performs well when dealing with static data. High-end adapters often have a very large amount of video memory, but this memory cannot be effectively utilized by dynamic data.

While reasonably efficient usage patterns of dynamic vertex buffers/index buffers can be implemented for dynamic content, many titles overuse this idiom for what is otherwise static content. We most often see this with binary space partitioning (BSP) trees and portal-based systems that store geometry in a data structure that does not map to the hardware and must be processed into buffers for every frame. Putting as much content into static resources as possible can greatly reduce the bandwidth overhead of transferring data to the video card, make better use of on-board VRAM, and reduce the CPU/cache overhead involved in processing this content.

## High Overhead in File Processing

PC games have gotten a reputation for long loading times, particular when compared with console titles with strict loading-time requirements. Our analysis of the way that many titles make use of the file subsystem reveals some common issues.

The overhead of opening a file is usually much higher than developers expect. With on-demand virus scanners in widespread use, and the additional functionality of NTFS, opening a file is a fairly expensive operation. Opening many files at once or opening and closing the same file repeatedly is therefore a poor method of dealing with file management. Some games have attempted to mitigate this performance cost by testing for the existence of a file before opening it. The reality is that testing for the existence of a file on NTFS requires opening the file, so testing before opening results in paying the cost twice.

Games that allow add-on modifications, or mods, or that still include development scaffolding to check for override data files, can have significant delays in loading the game because of checking for these files, even when those files are not present. We recommend that games only check for these files when run with a special command-line switch, or other mode indicator, so that only those users who make use of this functionality actually pay the performance cost of these (often extensive) checks.

Additional performance can be obtained from the file system by the following:

-   Appropriate use of the file system hints FILE\_FLAG\_RANDOM\_ACCESS and FILE\_FLAG\_SEQUENTIAL\_SCAN
-   Sizing buffers to avoid a large quantity of calls to the read/write APIs of the OS
-   Accessing files asynchronously
-   Loading threads in the background

We also strongly recommend converting data offline (at build or installation time) rather than relying on conversion when the game is first run, as doing so imposes a significant performance tax for every user.

## Slow and Frustrating Installation

Another common issue we've seen is very long installation times required for many modern PC games. The installers prompt the user many times, sometimes simply to tell the user, for example, "You do not need DirectX installed." Generally, these offending installers require the user to select **Next** or **OK** many times before installation of the game actually begins. Once it does begin, we've seen some titles take an hour or more before the user gets the opportunity to play the game. We feel strongly that the first hour of game play experience should not be the installation.

We recommend a number of approaches for dealing with installation. First, keep the prompts simple and to a minimum. Second, architect your game data such that some or all the data files can be used directly from the distribution disk where possible — modern DVD drives have very high bandwidth. Third, consider implementing install-on-demand in your titles to reduce or eliminate the installation process and allow users to get into the game as quickly as possible. (For more information about installing on demand, see [Install-on-Demand for Games](/windows/desktop/DxTechArts/install-on-demand-for-games).)

For more recommendations about game installation, see [Simplifying Game Installation](/windows/desktop/DxTechArts/simplifying-game-installation).

## Lack of Consideration of Physical Memory

Because of the wide variability of PC hardware in the market, titles typically make use of ad hoc configuration tests to select default settings for the level of graphical detail. Some of the titles we've seen are using video memory size in these tests, but failing to correlate this with physical memory size. In order to handle lost-device situations, the majority of the video memory (both local VRAM on the card and the non-local AGP memory aperture) must be backed by physical memory, either through the use of managed resources or custom data structures. Some high-end video cards have VRAM sizes rivaling the size of low-end CPU memories. In situations where the system has limited physical memory compared to the video card, most of that VRAM cannot be effectively utilized, and lower detail settings should be configured.

## Over-Reliance on Real-Time Audio Sample Rate Conversion

Another common source of CPU cycle burn we've seen occurs when the audio system is required to convert the playback rate during mix into the hardware buffer. With Windows Driver Model (WDM) drivers, the hardware buffer format is not under direct application control, because it is a kernel-level resource; instead, the format is selected based on the highest-quality format of all sources and the capabilities of the hardware. By default, Windows XP uses a high-quality sample rate conversion for this process, and if the majority of the audio samples require a rate conversion, a significant portion of the CPU cycles will be consumed.

We recommend creating all of your DirectSound buffers with the same sample rate. If you make any use of Microsoft Win32 **waveOut** functions, you should use a consistent sample rate with these, too. With WDM drivers, the buffers will all be mixed by the kernel, and if you use a higher sampling rate on some of them, the sample rates of all of the rest will be converted to match. Note that this implies using the same playback rate for all your audio samples, including any streaming audio decompression buffers. Setting the primary buffer rate has no effect unless you are targeting either Windows 98 or Windows Millennium Edition.

> [!Note]  
> On Windows Vista and later versions of the operating system, DirectSound and **waveOut** use the [Windows Audio Session API (WASAPI)](/windows/desktop/CoreAudio/wasapi) for all audio output.

 

## Fragmention of Virtual Memory

We've seen a number of recent issues related to the 32-bit limit on process memory space. While 2 GB of virtual address space for user-mode processes has been more than adequate historically, the increased use of large memory-mapped files, custom memory allocators, and increasing VRAM size (which must be mapped into process space) has started to cause situations where allocations of virtual memory space are failing. Some non-Microsoft DLLs are using fixed-start locations in the middle of the virtual address space, which is causing fragmentation that results in failed allocations.

These problems most often appear when the game makes use of a custom memory allocation scheme that attempts to allocate a large continuous chunk of virtual memory space. Our recommendation is to write allocators such that they request more reasonably sized portions of the virtual address space as needed. For example, requesting 64 or 256 MB at a time, but not 1 GB. However, care should be taken to not cause further fragmentation. The advent of 64-bit operating systems and hardware will greatly help these issues in the future, but care must be taken on current-generation 32-bit systems.

## Manipulation of the Floating-Point Control Word

As a debugging aid, some developers have been enabling exceptions on the floating-point unit (FPU) via manipulations of the floating-point control word. Doing this is highly problematic and will likely cause the process to crash. Just like the calling convention requires that the ebx register be preserved, the majority of the system assumes that the FPU is in a default state, will give reasonable results, and won't generate exceptions. Drivers and other system components will often compute results based on the assumption that standard error values will appear in the registers for bad conditions, but if exceptions are enabled, these will go unhandled and result in crashes.

Direct3D will set the floating-point unit to single-precision, round-to-nearest as part of initialization for the calling thread, unless the D3DCREATE\_FPU\_PRESERVE flag is used, in which case, the floating-point control word is untouched. Since the control word is a per-thread setting, ensuring that all of your application threads are set to single-precision mode may optimize performance. Remember that calling [**\_control87**](https://msdn.microsoft.com/library/e9b52ceh(v=VS.71).aspx) is not valid for x64-native coding, which uses SSE exclusively instead, and it is extremely expensive on the PowerPC-based architecture of the Xbox 360 CPU.

> [!Note]  
> If you modify the control word, use [**\_controlfp\_s**](https://msdn.microsoft.com/library/c9676k6h(v=VS.80).aspx) and be aware that for x64 platforms you can't change the floating-point precision via the control word.

 

In any libraries where we need to have different rounding rules or other behavior — such as dealing with software vertex shaders or compilation — we save and restore the control word. If a game needs to make use of non-standard rounding or FPU exceptions, it should save and restore the floating-point control word, and you should be sure that it does not call any external code that has not been proven to be safe from these problems, including system APIs.

## Optional Installation of the DirectX Runtime

A number of games ask the user whether to install DirectX. This can cause problems if the user assumes that the system has the latest DirectX redistributable installed and skips installation, and subsequently, the installation continues successfully. If the game requires a specific version of D3DX, or other updated functionality that was not installed, then the game won't work, and the user will get very frustrated.

It is strongly recommended that the game's installer silently install the DirectX redistributable that the game was built against. The DirectX installation process is designed so that it verifies whether anything needs to be updated and quickly returns if it doesn't. So, there is no need to ask the user about installing DirectX.

A silent installation of DirectX can be done by running this command from your installation package: **dxsetup.exe /silent**

Furthermore, the actual size of the redistributable folder can be configured to include only those cabinet files (.cab) that are actually needed for the game's target platforms and usage.

> [!Note]  
> Before you use **dxsetup**, read [Not So Direct Setup](https://walbourn.github.io/).

 

## Excessive Use of Thread Synchronization

When profiling games, the top hotspots are often found to be related to entering and leaving critical sections. With the prevalence of multi-core CPUs, the use of multithreading in games has increased dramatically, and many implementations rely on heavy use of thread synchronization. The CPU time to take a critical section even without any contention is quite significant, and all other forms of thread synchronization are even more expensive. So, care must be taken to minimize the use of these primitives.

A common source of excessive synchronization in games is the use of [D3DCREATE\_MULTITHREADED](/windows/desktop/direct3d9/d3dcreate). This flag, while making Direct3D thread-safe for rendering from multiple threads, takes a very conservative approach, resulting in high synchronization overhead. Games should avoid this flag. Instead, architect the engine so that all communication with Direct3D is from a single thread and any communication between threads is handled directly. For more information about designing multi-threaded games, see the article [Coding For Multiple Cores on Xbox 360 and Microsoft Windows](/windows/desktop/DxTechArts/coding-for-multiple-cores).

## Use of RDTSC

Use of the x86 instruction **RDTSC** is not recommended. **RDTSC** fails to correctly compute timing on some power management schemes that change the CPU frequency dynamically and on many multi-core CPUs for which the cycle counter is not synchronized between cores. Games should instead use the [**QueryPerformanceCounter**](/windows/desktop/api/profileapi/nf-profileapi-queryperformancecounter) API. For more information about issues with **RDTSC** and implementing high-resolution timing with **QueryPerformanceCounter**, see the article [Game Timing and Multicore Processors](/windows/desktop/DxTechArts/game-timing-and-multicore-processors).

 

 