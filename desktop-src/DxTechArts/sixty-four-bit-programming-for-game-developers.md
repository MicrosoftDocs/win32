---
title: 64-bit programming for Game Developers
description: This article addresses compatibility and porting issues and helps developers ease their transition to 64-bit platforms.
ms.assetid: 23a7ed41-6637-0607-327e-983b622e9104
ms.topic: article
ms.date: 05/31/2018
---

# 64-bit programming for Game Developers

Processor manufacturers are exclusively shipping 64-bit processors in their desktop computers, and even the chipsets of most laptop computers support x64 technology. It is important for game developers to take advantage of the improvements that 64-bit processors offer with their new applications and to ensure that their earlier applications run correctly on the new processors and the 64-bit editions of Windows Vista and Windows 7. This article addresses compatibility and porting issues and helps developers ease their transition to 64-bit platforms.

Microsoft currently has the following 64-bit operating systems:

-   Windows 10
-   Windows 11
-   Windows Server 2019 or later

Past 64-bit operating systems:

-   Windows Server 2003 Service Pack 1
-   Windows XP Professional x64 Edition (available to OEMs and to developers through MSDN)
-   Windows Vista
-   Windows 7
-   Windows 8.0
-   Windows 8.1
-   Windows Server 2008 - 2016

> [!Note]  
> Windows Server 2008 R2 or later is only available as a 64-bit edition. Windows 11 is only available as a 64-bit or ARM64 edition.

 

-   [Differences in Addressable Memory](#differences-in-addressable-memory)
-   [Specifying Large-Address-Aware When Building](#specifying-large-address-aware-when-building)
-   [Compatibility of 32-Bit Applications on 64-Bit Platforms](#compatibility-of-32-bit-applications-on-64-bit-platforms)
    -   [Potential Compatibility Pitfalls](#potential-compatibility-pitfalls)
-   [Porting Applications to 64-Bit Platforms](#porting-applications-to-64-bit-platforms)
-   [Profiling and Optimization of Ported Applications](#profiling-and-optimization-of-ported-applications)
-   [Managed Code on a 64-bit Operating System](#managed-code-on-a-64-bit-operating-system)
-   [Performance Implications of Running a 64-bit Operating System](#performance-implications-of-running-a-64-bit-operating-system)
-   [Summary](#summary)

## Differences in Addressable Memory

The first thing most developers notice is that 64-bit processors provide a huge leap in the amount of physical and virtual memory that can be addressed.

-   32-bit applications on 32-bit platforms can address up to 2 GB.
-   32-bit applications built with the /LARGEADDRESSAWARE:YES linker flag on 32-bit Windows XP or Windows Server 2003 with the special /3gb boot option can address up to 3 GB. This constrains the kernel to only 1 GB which may cause some drivers and/or services to fail.
-   32-bit applications built with the /LARGEADDRESSAWARE:YES linker flag on the 32-bit editions of Windows Vista, Windows Server 2008, and Windows 7 can address memory up to the number specified by the boot configuration data (BCD) element IncreaseUserVa. IncreaseUserVa can have a value ranging from 2048, the default, to 3072 (which matches the amount of memory configured by the /3gb boot option on Windows XP). The remainder of 4 GB is allocated to the kernel and can result in failing driver and service configurations.

    For more information about BCD, see [Boot Configuration Data](/windows-hardware/drivers/devtest/boot-options-in-windows).

-   32-bit applications on 64-bit platforms can address up to 2 GB, or up to 4 GB with the /LARGEADDRESSAWARE:YES linker flag.
-   64-bit applications use 43 bits for addressing, which provides 8 TB of virtual address for applications and 8 TB reserved for the kernel.

Beyond just memory, 64-bit applications that use memory-mapped file I/O benefit greatly from the increased virtual address space. The 64-bit architecture also has improved floating-point performance and faster passing of parameters. Sixty-four-bit processors have double the number of registers, of both general purpose and streaming SIMD extensions (SSE) types, as well as support for SSE and SSE2 instruction sets; many 64-bit processors even support SSE3 instruction sets.

## Specifying Large-Address-Aware When Building

It is a good practice to specify large-address-aware when building 32-bit applications, by using the linker flag /LARGEADDRESSAWARE, even if the application is not intended for a 64-bit platform, because of the advantages that are gained at no cost. As explained earlier, enabling this flag for a build allows a 32-bit program to access more memory with special boot options on a 32-bit OS or on a 64-bit OS. However, developers must be careful that pointer assumptions are not made, such as assuming that the high-bit is never set in a 32-bit pointer. In general, enabling the /LARGEADDRESSAWARE flag is a good practice.

Thirty-two-bit applications that are large-address-aware can determine at run time how much total virtual address space is available to them with the current OS configuration by calling [**GlobalMemoryStatusEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex). The ullTotalVirtual result will range from 2147352576 bytes (2 GB) to 4294836224 bytes (4 GB). Values that are larger than 3221094400 (3 GB) can only be obtained on 64-bit editions of Windows. For example, if IncreaseUserVa has a value of 2560, the result is ullTotalVirtual with a value of 2684223488 bytes.

## Compatibility of 32-Bit Applications on 64-Bit Platforms

Sixty-four-bit Windows operating systems are binary compatible with the IA32 architecture, and the majority of APIs that 32-bit applications use are available through the Windows 32-bit on Windows 64-bit Emulator, WOW64. WOW64 helps ensure that these APIs will work as intended.

WOW64 has an execution layer that handles the marshalling of 32-bit data. WOW64 redirects DLL file requests, redirects some registry branches for 32-bit applications, and reflects some registry branches for 32- and 64-bit applications.

More information on WOW64 can be found at [WOW64 Implementation Details](/windows/win32/winprog64/wow64-implementation-details).

### Potential Compatibility Pitfalls

Most applications developed for a 32-bit platform will run without problems on a 64-bit platform. A few applications could have issues, which might include the following:

-   All drivers for by 64-bit editions of Windows operating systems must be 64-bit versions. Requiring new 64-bit drivers has implications for copy-protection schemes that rely on old drivers. Note that kernel-mode drivers must be Authenticode-signed to be loaded by 64-bit editions of Windows.
-   64-bit processes cannot load 32-bit DLLs, and 32-bit processes cannot load 64-bit DLLs. Developers must ensure that 64-bit versions of third-party DLLs are available before proceeding with development. If you must use a 32-bit DLL in a 64-bit process, then Windows inter-process communication (IPC) can be used. COM components can also make use of out-of-process servers and marshalling to communicate between boundaries, but doing so may introduce a performance penalty.
-   Many x64 processors are also multi-core processors, and developers need to test to how this affects their legacy applications. More information on multi-core processors and the implications for gaming applications can be found in [Game Timing and Multicore Processors](/windows/win32/dxtecharts/game-timing-and-multicore-processors).
-   Applications should also call [**SHGetFolderPath**](/windows/win32/api/shlobj_core/nf-shlobj_core-shgetfolderpathw) to discover file paths, as some folder names have changed in certain cases. For example, CSIDL\_PROGRAM\_FILES would return "C:\\Program Files(x86)" for a 32-bit application running on a 64-bit platform instead of "C:\\Program Files". Developers must be mindful of how the WOW64 emulator's redirection and reflection capabilities work.

In addition, developers need to be wary of 16-bit programs that they might still be using. WOW64 cannot handle 16-bit applications; this includes old installers and all MS-DOS programs.

> [!Note]  
> The most common compatibility issues are installers that execute 16-bit code and not having 64-bit drivers for copy protection schemes.

 

The next section discusses issues related to porting code to 64-bit native for developers that want to ensure their legacy programs work on 64-bit platforms. It is also for developers who are unfamiliar with 64-bit programming.

## Porting Applications to 64-Bit Platforms

Having the right tools and libraries will help to ease the transition from 32-bit to 64-bit development. The DirectX 9 SDK has libraries to support both x86- and x64-based projects. Microsoft Visual Studio 2005 and Visual Studio 2008 support code generation for both x86 and x64, and they comes with libraries optimized for generating x64 code. However, it will also be necessary for developers to distribute the Visual C runtimes with their applications. Note that the Express Editions of Visual Studio 2005 and Visual Studio 2008 do not include the x64 compiler, but that the Standard, Professional, and Team System editions all do.

Developers who are targeting 32-bit platforms can prepare for 64-bit development to make their transition easier later on. When compiling 32-bit projects, developers should use the /Wp64 flag, which will cause the generation of warnings about issues that affect portability. Switching to 64-bit tools and libraries will probably generate a lot of new build errors initially; so, it is advisable to switch bit-neutral tools and libraries and correct any warnings before switching to a 64-bit build.

Changing tools, changing libraries, and using certain compiler flags will not be enough, though. Assumptions in coding standards must be reevaluated to ensure that current coding standards don't allow portability issues. Portability issues can include pointer truncation, size and alignment of data types, reliance on 32-bit DLLs, use of legacy APIs, assembly code, and old binary files.

> [!Note]  
> Visual C++ 2010 or later includes the stdint.h and cstdint C99 headers which define the standard portability types int32\_t, uint32\_t, int64\_t, uint64\_t, intptr\_t, and uintptr\_t. Using these along with the standard ptrdiff\_t and size\_t data types may be preferrable to the Windows portabilty types used below for improving portability of code.

 

Major porting issues include the following:

<dl> <dt>

<span id="Pointer_Truncation"></span><span id="pointer_truncation"></span><span id="POINTER_TRUNCATION"></span>**Pointer Truncation**
</dt> <dd>

Pointers are 64-bits on a 64-bit OS, so casting pointers to other data types can result in truncation, and pointer arithmetic can result in corruption. Using the /Wp64 flag will usually provide a warning about this kind of issue, but using polymorphic types (INT\_PTR, DWORD\_PTR, SIZE\_T, UINT\_PTR, and so on) when casting pointer types is a good practice to help avoid this issue altogether. Since pointers are 64-bit on new platforms, developers should check the ordering of pointers, and the data types in classes and structures, to reduce or eliminate padding.

</dd> <dt>

<span id="Data_Types_and_Binary_Files"></span><span id="data_types_and_binary_files"></span><span id="DATA_TYPES_AND_BINARY_FILES"></span>**Data Types and Binary Files**
</dt> <dd>

While pointers increase from 32 bits to 64 on a 64-bit platform, other data types don't. Fixed-precision data types (DWORD32, DWORD64, INT32, INT64, LONG32, LONG64, UINT32, UINT64) can be used in places where the size of the data type must be known; for example, in a binary file structure. The changes in pointer size and data alignment require special handling to ensure 32-bit-to-64-bit compatibility. More information can be found in [New Data Types](/windows/win32/winprog64/the-new-data-types).

</dd> <dt>

<span id="Older_Win32_APIs_and_Data_Alignment"></span><span id="older_win32_apis_and_data_alignment"></span><span id="OLDER_WIN32_APIS_AND_DATA_ALIGNMENT"></span>**Older Win32 APIs and Data Alignment**
</dt> <dd>

Some Win32 APIs have been deprecated and replaced with more neutral API calls such as SetWindowLongPtr in place of SetWindowLong.

The performance penalty for non-aligned accesses is greater on x64 platform than on an x86 platform. The TYPE\_ALIGNMENT(t) and the FIELD\_OFFSET(t, member) macros can be used to determine alignment information that can used directly by code. Correct use of these aforementioned macros should eliminate potential non-aligned access penalties.

More information on the TYPE\_ALIGNMENT macro, the FIELD\_OFFSET macro, and general 64-bit programming information can be found at [64-bit Windows Programming: Migration Tips: Additional Considerations](/windows/win32/winprog64/migration-tips) and [Rules for Using Pointers](/windows/win32/winprog64/rules-for-using-pointers).

</dd> <dt>

<span id="Assembly_Code"></span><span id="assembly_code"></span><span id="ASSEMBLY_CODE"></span>**Assembly Code**
</dt> <dd>

Inline assembly code is not supported on 64-bit platforms and needs to be replaced. Changes in the architecture may have changed application bottlenecks, and C/C++ or intrinsics can achieve similar results with code that is easier to read. The most advisable practice is to switch all assembly code to C or C++. Intrinsics can be used in place of assembly code, but should only be used after full profiling and analysis has been performed.

The x87, MMX, and 3DNow! instruction sets are deprecated in 64-bit modes. The instructions sets are still present for backward compatibility for 32-bit mode; however, to avoid compatibility issues in the future, their use in current and future projects is discouraged.

</dd> <dt>

<span id="Deprecated_APIs"></span><span id="deprecated_apis"></span><span id="DEPRECATED_APIS"></span>**Deprecated APIs**
</dt> <dd>

Some older DirectX APIs have been dropped for 64-bit native applications: DirectPlay 4 and earlier, DirectDraw 6 and earlier, Direct3D 8 and earlier, and DirectInput 7 and earlier. Also, the core API of DirectMusic is available to native 64-bit applications, but the performance layer and DirectMusic Producer are deprecated.

Visual Studio issues deprecation warnings, and these changes are not an issue for developers who use the latest APIs.

</dd> </dl>

## Profiling and Optimization of Ported Applications

All developers need to re-profile any applications that are being ported to new architectures. Many applications being ported to 64-bit platforms will have different performance profiles from their 32-bit versions. Developers need to run 64-bit performance tests before assessing what needs to be optimized. The good news about this is that many traditional optimizations work on 64-bit platforms. In addition, 64-bit compilers can also perform many optimizations with the correct use of compiler flags and coding hints.

Some structures may have their internal data types reordered to conserve memory space and improve caching. Array indices can be used instead of a full 64-bit pointer in some cases. The /fp:fast flag can improve floating-point optimizing and vectorization. Using \_\_restrict, declspec(restrict), and declspec(noalias) can help the compiler resolve aliasing and improve use of the register file.

More information on /fp:fast can be found at [/fp (Specify Floating-Point Behavior)](/cpp/build/reference/fp-specify-floating-point-behavior).

More information on \_\_restrict can be found at [Microsoft-Specific Modifiers](/cpp/cpp/microsoft-specific-modifiers).

More information on declspec(restrict) can be found at [Optimization Best Practices](/cpp/build/optimization-best-practices).

More information on declspec(noalias) can be found at [\_\_declspec(noalias)](/cpp/cpp/noalias).

## Managed Code on a 64-bit Operating System

Managed code is used by many game developers in their tool chain, so an understanding of how it behaves on a 64-bit OS can be helpful. Managed code is instruction-set neutral, so when you run a managed application on a 64-bit OS, the Common Language Runtime (CLR) can run it as either a 32-bit or 64-bit process. By default, the CLR runs managed applications as 64-bit, and they should work fine with no problems. However, if your application depends on a DLL that is native 32-bit, then your application will fail when it tries to call this DLL. A 64-bit process needs completely 64-bit code, and a 32-bit DLL cannot be called from a 64-bit process. The best long-term solution is to compile your native code as 64-bit also, but a perfectly reasonable short-term solution is to simply mark your managed application as being for x86 only by using the /platform:x86 build flag.

## Performance Implications of Running a 64-bit Operating System

Because processors with AMD64 and Intel 64 architecture can execute 32-bit instructions natively, they can run 32-bit applications at full speed, even on a 64-bit OS. There is a modest cost for converting parameters between 32-bit and 64-bit when calling operating system functions, but this cost is generally negligible. This means that you should see no slowdown when running 32-bit applications on a 64-bit OS.

When you compile applications as 64-bit, the calculations get more complicated. A 64-bit program uses 64-bit pointers, and its instructions are slightly larger, so the memory requirement is slightly increased. This can cause a slight drop in performance. On the other hand, having twice as many registers and having the ability to do 64-bit integer calculations in a single instruction will often more than compensate. The net result is that a 64-bit application might run slightly slower than the same application compiled as 32-bit, but it will often run slightly faster.

## Summary

Sixty-four-bit architectures allow developers to push the limitations on how games look, sound, and play. Transitioning from 32-bit programming to 64-bit programming is not trivial, however. By understanding the differences between the two, and by using the newest tools, the transition to 64-bit platforms can be easier and faster.

More information on 64-bit programming can be found at [Visual C++ Developer Center: 64-Bit Programming](/windows/win32/winprog64/programming-guide-for-64-bit-windows).

 

 
