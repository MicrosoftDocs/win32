---
description: Control Flow Guard (CFG) is a highly-optimized platform security feature that was created to combat memory corruption vulnerabilities.
ms.assetid: 116EAD64-7CAE-455C-BA43-9492F78DE873
title: Control Flow Guard
ms.topic: article
ms.date: 05/31/2018
---

# Control Flow Guard

## What is Control Flow Guard?

Control Flow Guard (CFG) is a highly-optimized platform security feature that was created to combat memory corruption vulnerabilities. By placing tight restrictions on where an application can execute code from, it makes it much harder for exploits to execute arbitrary code through vulnerabilities such as buffer overflows. CFG extends previous exploit mitigation technologies such as [/GS](/cpp/build/reference/gs-buffer-security-check?view=vs-2019), [DEP](../memory/data-execution-prevention.md), and [ASLR](/archive/blogs/michael_howard/address-space-layout-randomization-in-windows-vista).

This feature is available in Microsoft Visual Studio 2015, and runs on "CFG-Aware" versions of Windows—the x86 and x64 releases for Desktop and Server of Windows 10 and Windows 8.1 Update (KB3000850).

We strongly encourage developers to enable CFG for their applications. You don't have to enable CFG for every part of your code, as a mixture of CFG enabled and non-CFG enabled code will execute fine. But failing to enable CFG for all code can open gaps in the protection. Furthermore, CFG enabled code works fine on "CFG-Unaware" versions of Windows and is therefore fully compatible with them.

## How Can I Enable CFG?

In most cases, there is no need to change source code. All you have to do is add an option to your Visual Studio 2015 project, and the compiler and linker will enable CFG.

The simplest method is to navigate to **Project \| Properties \| Configuration Properties \| C/C++ \| Code Generation** and choose **Yes (/guard:cf)** for Control Flow Guard.

![cfg property in visual studio](images/cfg-vs.png)

Alternatively, add **/guard:cf** to **Project \| Properties \| Configuration Properties \| C/C++ \| Command Line \| Additional Options** (for the compiler) and **/guard:cf** to **Project \| Properties \| Configuration Properties \| Linker \| Command Line \| Additional Options** (for the linker).

![cfg property for compiler](images/cfg-compiler.png)![cfg property for linker](images/cfg-linker.png)

See [/guard (Enable Control Flow Guard)](/cpp/build/reference/guard-enable-control-flow-guard?view=vs-2019) for additional info.

If you are building your project from the command line, you can add the same options. For example, if you are compiling a project called test.cpp, use **cl /guard:cf test.cpp /link /guard:cf**.

You also have the option of dynamically controlling the set of icall target addresses that are considered valid by CFG using the [**SetProcessValidCallTargets**](/windows/desktop/api/memoryapi/nf-memoryapi-setprocessvalidcalltargets) from the Memory Management API. The same API can be used to specify whether pages are invalid or valid targets for CFG. The [**VirtualProtect**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualprotect) and [**VirtualAlloc**](/windows/desktop/api/memoryapi/nf-memoryapi-virtualalloc) functions will by default treat a specified region of executable and committed pages as valid indirect call targets. It is possible to override this behavior, such as when implementing a Just-in-Time compiler, by specifying **PAGE\_TARGETS\_INVALID** when calling **VirtualAlloc** or **PAGE\_TARGETS\_NO\_UPDATE** when calling **VirtualProtect** as detailed under [**Memory Protection Constants**](/windows/desktop/Memory/memory-protection-constants).

## How Do I Tell That a Binary is under Control Flow Guard?

Run the [dumpbin tool](/cpp/build/reference/dumpbin-reference) (included in the Visual Studio 2015 installation) from the Visual Studio command prompt with the */headers* and */loadconfig* options: **dumpbin /headers /loadconfig test.exe**. The output for a binary under CFG should show that the header values include "Guard", and that the load config values include "CF Instrumented" and "FID table present".

![output from dumpbin /headers](images/cfg-dumpbin-headers.png)

![output from dumpbin /loadconfig](images/cfg-dumpbin-loadconfig.png)

## How Does CFG Really Work?

Software vulnerabilities are often exploited by providing unlikely, unusual, or extreme data to a running program. For example, an attacker can exploit a buffer overflow vulnerability by providing more input to a program than expected, thereby over-running the area reserved by the program to hold a response. This could corrupt adjacent memory that may hold a function pointer. When the program calls through this function it may then jump to an unintended location specified by the attacker.

However, a potent combination of compile and run-time support from CFG implements control flow integrity that tightly restricts where indirect call instructions can execute.

The compiler does the following:

1.  Adds lightweight security checks to the compiled code.
2.  Identifies the set of functions in the application that are valid targets for indirect calls.

The runtime support, provided by the Windows kernel:

1.  Efficiently maintains state that identifies valid indirect call targets.
2.  Implements the logic that verifies that an indirect call target is valid.

To illustrate:

![cfg pseudocode](images/cfg-pseudocode.jpg)

When a CFG check fails at runtime, Windows immediately terminates the program, thus breaking any exploit that attempts to indirectly call an invalid address.

 

 
