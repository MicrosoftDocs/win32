---
title: Windows Advanced Rasterization Platform (WARP) Guide
description: This article describes Windows Advanced Rasterization Platform (WARP) and the following aspects of WARP.
ms.assetid: C40A96EB-64AA-46EB-85A9-7C996ABC8BFE
ms.topic: article
ms.date: 05/31/2018
---

# Windows Advanced Rasterization Platform (WARP) Guide

This article describes Windows Advanced Rasterization Platform (WARP) and the following aspects of WARP.

-   [What is WARP?](#what-is-warp)
-   [WARP Benefits](#warp-benefits)
    -   [Removing the Need for Custom Software Rasterizers](#removing-the-need-for-custom-software-rasterizers)
    -   [Enabling Maximum Performance from Graphics Hardware](#enabling-maximum-performance-from-graphics-hardware)
    -   [Enabling Rendering When Direct3D Hardware is Not Available](#enabling-rendering-when-direct3d-hardware-is-not-available)
    -   [Leveraging Existing Resources for Software Rendering](#leveraging-existing-resources-for-software-rendering)
    -   [Enabling Scenarios that Do Not Require Graphics Hardware](#enabling-scenarios-that-do-not-require-graphics-hardware)
    -   [Completing the DirectX Graphics Platform](#completing-the-directx-graphics-platform)
-   [WARP Capabilities and Requirements](#warp-capabilities-and-requirements)
-   [How to Use WARP](#how-to-use-warp)
-   [Recommended Application Types for WARP](#recommended-application-types-for-warp)
    -   [Casual Games](#casual-games)
    -   [Existing Non-Gaming Applications](#existing-non-gaming-applications)
    -   [Advanced Rendering Games](#advanced-rendering-games)
    -   [Other Applications](#other-applications)
-   [WARP Architecture and Performance](#warp-architecture-and-performance)
-   [WARP Conformance](#warp-conformance)

## What is WARP?

WARP is a high speed, fully conformant software rasterizer. It is a component of the DirectX graphics technology that was introduced by the Direct3D 11 runtime. The Direct3D 11 runtime is installed on Windows 7, Windows Server 2008 R2, and Windows Vista with the \[KB971644\] update. Windows 8, Windows 10, Windows Server 2012 & above, and Windows RT include the Direct3D 11.1 runtime, which has an updated version of WARP. Windows 10 Fall Creators Update (1709) includes a version of WARP that supports both Direct3D 11 and Direct3D 12 runtimes.

## WARP Benefits

WARP provides the following benefits:

-   [Removing the Need for Custom Software Rasterizers](#removing-the-need-for-custom-software-rasterizers)
-   [Enabling Maximum Performance from Graphics Hardware](#enabling-maximum-performance-from-graphics-hardware)
-   [Enabling Rendering When Direct3D Hardware is Not Available](#enabling-rendering-when-direct3d-hardware-is-not-available)
-   [Leveraging Existing Resources for Software Rendering](#leveraging-existing-resources-for-software-rendering)
-   [Enabling Scenarios that Do Not Require Graphics Hardware](#enabling-scenarios-that-do-not-require-graphics-hardware)
-   [Completing the DirectX Graphics Platform](#completing-the-directx-graphics-platform)

### Removing the Need for Custom Software Rasterizers

WARP simplifies development by removing the need to build a custom software rasterizer and to tune your application for it instead of tuning your application for hardware. By providing a single, general purpose software rasterizer, you no longer need to write image rendering algorithms in multiple ways to run on hardware or software with different features and capabilities. You can still implement algorithms in multiple ways to achieve better performance or scaling; however, you do not need to change the API or rendering architecture that is used to implement those algorithms. Instead, you can focus on creating a great Direct3D 10 or later application that will look the same and perform well on hardware or in software.

### Enabling Maximum Performance from Graphics Hardware

When an application is tuned to run efficiently on hardware, it will run efficiently on WARP as well. The converse is also true; any application that is tuned to run well on WARP will perform well on hardware. Applications that use Direct3D 10 and later inefficiently might not scale efficiently on different hardware. WARP has similar performance profiles to hardware, so tuning an application for large batches, minimizing state changes, removing synchronizing points or locks will benefit both hardware and WARP.

### Enabling Rendering When Direct3D Hardware is Not Available

WARP allows fast rendering in a variety of situations where hardware implementations are undesirable or unavailable, including:

-   When the user does not have any Direct3D-capable hardware
-   When an application runs as a service or in a server environment
-   When an application wants to reserve the Direct3D hardware resources for other uses
-   When a video card is not installed
-   When a video driver is not available, or is not working correctly
-   When a video card is out of memory, hangs, or would take too many system resources to initialize

### Leveraging Existing Resources for Software Rendering

There is a huge community, many books, Web sites, SDKs, samples, white papers, mailing lists and other resources that can help you take advantage of Direct3D 10 and later shader-based image rendering. With WARP as a software fallback, you can use existing knowledge about hardware to improve the performance of your application when it runs with hardware or software. In addition, many excellent tools from the graphics card vendors and in the DirectX SDK can help you design, build, develop, debug and analyze performance issues of graphics applications. These tools and knowledge can now benefit application development that targets both hardware and software when you use WARP.

### Enabling Scenarios that Do Not Require Graphics Hardware

Various algorithms and applications (image processing algorithms, printing, remoting, Virtual PCs and other emulators, high quality font rendering, charts, graphs, and so on) have typically been optimized for the CPU because they are not dependent on hardware. With WARP, you can use a single architecture that runs these algorithms and applications and that can run fully in software; yet, if hardware acceleration is available, you can take advantage of it.

### Completing the DirectX Graphics Platform

WARP allows you to access all Direct3D 10 and later graphics features even on computers without Direct3D 10 and later graphics hardware. Direct3D 10 removed capability bits (caps); that is, you no longer need to verify whether graphics capabilities are available from graphics hardware because Direct3D 10 and later guarantees this availability. You can now use all the features of a wide range of video cards knowing that their application will behave and look the same everywhere. You can scale the performance of these applications by simply disabling expensive graphics features on low end video cards or rendering to smaller targets.

## WARP Capabilities and Requirements

WARP fully supports all Direct3D 10 and 10.1 features. For example, WARP supports the following most important features:

-   All the precision requirements of the Direct3D 10 and 10.1 specification
-   Direct3D 11 when used with feature levels 9\_1, 9\_2, 9\_3, 10\_0, and 10\_1 (for more information about feature levels, see [**D3D\_FEATURE\_LEVEL**](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_feature_level))
-   All optional texture formats, such as multisample render targets and sampling from float surfaces
-   Antialiased, high quality rendering up to 8x multisample antialiasing (MSAA)
-   Anisotropic filtering
-   32-bit and 64-bit applications and large address aware 32-bit applications

When you install the [Platform Update for Windows 7](https://support.microsoft.com/kb/2670838) on Windows 7 SP1 or Windows Server 2008 R2 SP1, that operating system then includes the Direct3D 11.1 runtime and a version of WARP that supports Direct3D 11.x when used with [feature levels](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 9\_1, 9\_2, 9\_3, 10\_0, 10\_1, and 11\_0.

Windows 8, Windows 10, Windows Server 2012 & above, and Windows RT include the Direct3D 11.1 runtime and a new version of WARP. This version supports Direct3D 11.x when used with [feature levels](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-intro) 9\_1, 9\_2, 9\_3, 10\_0, 10\_1, 11\_0, and 11\_1.

Windows 10 Fall Creators Update (1709) includes a new version of WARP that supports [Direct3D 12](../direct3d12/direct3d-12-graphics.md) feature levels 12\_0 and 12\_1. 

The minimum computer requirements for WARP are the same as for Windows Vista, specifically:

-   Minimum 800 MHz CPU
-   MMX, SSE, or SSE2 is not required
-   Minimum 512 MB of RAM

## How to Use WARP

For Direct3D 12, creating a WARP device requires first identifying the WARP adapter. To facilitate this, DXGI 1.4 provides the [IDXGIFactory4::EnumWarpAdapter](/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgifactory4-enumwarpadapter) method. The WARP adapter can then be provided to [D3D12CreateDevice](/windows/desktop/api/d3d12/nf-d3d12-d3d12createdevice) to create a WARP device.

Direct3D 10, 10.1, and 11 components can use an additional driver type that you can specify when you create the device (for example, when you call the [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice) function). This driver type is [**D3D10\_DRIVER\_TYPE\_WARP**](/windows/desktop/api/d3d10misc/ne-d3d10misc-d3d10_driver_type) or [**D3D\_DRIVER\_TYPE\_WARP**](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_driver_type). When you specify this driver type, the runtime creates a WARP device and does not initialize a hardware device.

Because WARP uses the same software interface to Direct3D as the reference rasterizer does, any Direct3D application that can support running with the reference rasterizer can be tested by using WARP. To use WARP, rename D3d10warp.dll to D3d10ref.dll and place it in the same folder as the sample or application. Next, when you switch to ref, you will see WARP rendering.

If you rename WARP to D3d10ref.dll and place it in C:\\Program Files (x86)\\Microsoft DirectX SDK (June 2010)\\Samples\\C++\\Direct3D\\Bin\\x86, you can run all the DirectX samples against WARP, either by clicking the "Toggle Ref" button in the sample, or by running the sample with /ref specified on the command line.

## Recommended Application Types for WARP

All applications that can use Direct3D can use WARP. This includes the following types of applications:

-   [Casual Games](#casual-games)
-   [Existing Non-Gaming Applications](#existing-non-gaming-applications)
-   [Advanced Rendering Games](#advanced-rendering-games)
-   [Other Applications](#other-applications)

### Casual Games

Games typically have simple rendering requirements. However, they also require the use of impressive visual effects that might need hardware acceleration. The majority of the best selling game titles for Windows are either simulations or casual games, neither of which requires high performance graphics. However, both styles of games greatly benefit from modern shader-based graphics and the ability to scale on hardware.

### Existing Non-Gaming Applications

A large amount of graphical applications require a minimal number of code paths in their rendering layer. WARP enables these applications to implement a single Direct3D code path that can target a large number of computer configurations.

### Advanced Rendering Games

Game developers might want to isolate graphics-card or driver-specific rendering errors. Therefore, all games, even extremely graphically demanding games, can benefit from being able to render their content by using WARP. You can use WARP to validate whether any visual artifacts that you find are rendering errors or problems with hardware or drivers.

### Other Applications

The target applications for WARP also include those that might not currently use Direct3D 10 or Direct3D 10.1. These target applications include applications that must always work on all computers, image processing applications that do not write CPU and GPU versions of image processing algorithms, image processing algorithms where speed or use the GPU is not critical, such as printing, and emulators and virtual environments that display advanced 3D graphics.

## WARP Architecture and Performance

WARP is based on the reference rasterizer codebase. Therefore, WARP uses the same software interface to both Direct3D 10 and later and DXGI. WARP is included in Windows 7 in the D3d10warp.dll, located in Windows systems folders. Two versions of WARP are installed on 64 bit machines, an x86 and x64 version. The x64 version might run faster in certain circumstances because the code generator contained in WARP can take advantage of the additional registers that are available when users run 64-bit applications.

WARP contains the following two high-speed, real-time compilers:

-   The high-level intermediate language compiler that converts HLSL bytecode and the current render state into an optimized stream of vector commands for the geometry shader (GS), vertex shader (VS), and pixel shader (PS) stages of the pipeline.
-   The high-performance just-in-time code generator that can take these commands and generate optimized SSE2, SSE4.1, x86, x64, arm, and arm64 assembly code.

WARP uses the thread pool and complex task management and dependency tracking that was introduced in Windows Vista to allow all parts of the rendering pipeline to be distributed efficiently across available CPU cores.

WARP uses deferred rendering. That is, WARP can batch rendering commands so that rasterization occurs only when sufficient data is available to use all the CPU resources efficiently. Work on the main application thread is minimized to allow the application to submit commands as quickly as possible. If an application is also multi-threaded, and it uses the thread pool, work will be evenly distributed between WARP and the application.

The WARP code generator has been tuned to make best use of the modern CPU architecture. WARP runs on all computers that can run Windows Vista and later operating systems, even if the computer does not support SSE. However, WARP has been optimized for computers that support SSE2. It also contains optimizations for specific architectures of AMD and Intel processors, as well as support for the SSE 4.1 extensions.

WARP does not require graphics hardware to execute. It can execute even in situations where hardware is not available or cannot be initialized.

Applications and samples that were designed and built to run on Direct3D 10 and later hardware without any knowledge of WARP will likely run well by using WARP. However, we recommend that you lower the quality settings and resolution as much as possible to achieve usable frame rates. You can use WARP to develop and tune applications that run well on both hardware and software.

Because WARP uses multiple CPU cores for parallel execution, it performs best on modern multi-core CPUs. WARP also runs significantly faster on computers with SSE4.1 extensions installed. Microsoft performed significant testing and performance tuning on computers with eight or more cores and SSE4.1 because these high end computers will become more common during the lifetime of Windows 7 and later operating systems.

When WARP is running on the CPU, it is limited compared to a graphics card in a number of ways. The front-side bus speed of a CPU is typically around or under 10 GB/s. In contrast, a graphics card often has dedicated memory that uses 20 to 100GB/s or more of graphics bandwidth. Graphics hardware also has fixed-function units that can perform complex and expensive tasks, such as texture filtering, format decompression, or conversions, asynchronously with little overhead or power cost. Performing these operations on a typical CPU is expensive in terms of both power consumption and performance cycles.

The typical performance numbers for an Intel Penryn based 3.0GHz Quad Core machine show that WARP can in some cases outperform low-end integrated Direct3D 10 and later graphics GPUs on a number of benchmarks. Low-end discrete graphics hardware is typically 4 to 5 times faster than WARP at running these benchmarks. These low-end integrated or discrete GPUs have minimal use of CPU resources. Mid-range or high-end graphics cards are significantly faster than WARP for many applications, particularly when an application can take advantage of the parallelism and memory bandwidth that these graphics cards provide.

WARP is not a replacement for graphics hardware, particularly as reasonably performing low-end Direct3D 10 and later discrete hardware is now inexpensive. The goal of WARP is to allow applications to target Direct3D-compatible level hardware without having significantly different code paths or testing requirements whether they run on hardware or in software.

The following two tables show WARP example data with various CPUs and graphics cards.

The first table shows WARP example data with Direct3D 10 Crysis running at 800x600 with all the quality settings on their lowest levels:

| CPU                         | Time   | Ave FPS | Min FPS | Min Frame | Max FPS | Max Frame |
|-----------------------------|--------|---------|---------|-----------|---------|-----------|
| Core i7 8 Core @ 3.0GHz     | 271.57 | 7.36    | 3.46    | 1966      | 15.01   | 995       |
| Penryn 4 Core @ 3.0GHz      | 351.35 | 5.69    | 2.49    | 1967      | 10.95   | 980       |
| Penryn 2 Core @ 3.0GHz      | 573.98 | 3.48    | 1.35    | 1964      | 6.61    | 988       |
| Core 2 Duo @ 2.6GHz         | 707.19 | 2.83    | 0.81    | 1959      | 5.18    | 982       |
| Core 2 Duo @ 2.4GHz         | 763.25 | 2.62    | 0.76    | 1964      | 4.70    | 984       |
| Core 2 Duo @ 2.1GHz         | 908.87 | 2.20    | 0.64    | 1965      | 3.72    | 986       |
| Xeon 8 Core @ 2.0GHz        | 424.04 | 4.72    | 1.84    | 1967      | 9.56    | 988       |
| AMD FX74 4 Core @ 3.0GHz    | 583.12 | 3.43    | 1.41    | 1967      | 5.78    | 986       |
| Phenom 9550 4 Core @ 2.2GHz | 664.69 | 3.01    | 0.53    | 1959      | 5.46    | 987       |

The second table shows example data running the same test across a variety of graphics cards:

| Graphics Card         | Time   | Ave FPS | Min FPS | Min Frame | Max FPS | Max Frame |
|-----------------------|--------|---------|---------|-----------|---------|-----------|
| NVIDIA 8800 GTS       | 23.58  | 84.80   | 60.78   | 1957      | 130.83  | 1022      |
| NVIDIA 8500 GT        | 47.63  | 41.99   | 25.67   | 1986      | 72.57   | 991       |
| NVIDIA Quadro 290     | 67.16  | 29.78   | 18.19   | 1969      | 49.87   | 1017      |
| NVIDIA 8400 GS        | 59.01  | 33.89   | 21.22   | 1962      | 51.82   | 1021      |
| ATI 3400              | 53.79  | 37.18   | 22.97   | 618       | 59.77   | 1021      |
| ATI 3200              | 67.19  | 29.77   | 18.91   | 1963      | 45.74   | 980       |
| ATI 2400 PRO          | 67.04  | 29.83   | 17.97   | 606       | 45.91   | 987       |
| Intel DX10 Integrated | 386.94 | 5.17    | 1.74    | 1974      | 16.22   | 995       |

## WARP Conformance

WARP passes all the standard Windows Hardware Quality Labs (WHQL) conformance tests for validating Direct3D hardware devices.

WARP has been tested against a suite of Direct3D 10 and Direct3D 10.1 applications and benchmarks, and against SDK samples from DirectX, NVIDIA, and AMD.

WARP used the [PIX](https://msdn.microsoft.com/library/ee417062(v=VS.85).aspx) debugging and analysis tool for Windows in its testing; Microsoft has a large library of single frame captures of applications that are used to compare between hardware and WARP. The majority of the images appear almost identical between hardware and WARP; where small differences sometimes occur, they are found to be within the tolerances defined by the Direct3D 10 specification.
