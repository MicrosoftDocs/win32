---
title: Exception Handling under WOW64
description: WOW64 uses native x64, ia64, or ARM64 exceptions as a transport for x86 exceptions. Therefore, in a 32-bit application running under WOW64, uncaught exceptions behave like native 64-bit exceptions.
ms.assetid: 2EE1A1F3-A691-4ee6-9587-7FF7C4F9DD98
ms.topic: article
ms.date: 05/31/2018
---

# Exception Handling under WOW64

WOW64 uses native x64, ia64, or ARM64 exceptions as a transport for x86 exceptions. Therefore, in a 32-bit application running under WOW64, uncaught exceptions behave like native 64-bit exceptions.

In an application running on a 32-bit version of Windows, uncaught exceptions are passed on to higher-level exception handlers of the application, when available. In the same 32-bit application running under WOW64, the system may suppress uncaught exceptions.

**Windows Vista, Windows Server 2003 and Windows XP:** In the same 32-bit application running under WOW64, the system calls the exception filters but may suppress uncaught exceptions without invoking the associated handlers. This behavior changed starting with Windows Vista with Service Pack 1 (SP1).

For more information about uncaught exceptions in window procedures, see the [WindowProc](/windows/win32/api/winuser/nc-winuser-wndproc) function.

 

 