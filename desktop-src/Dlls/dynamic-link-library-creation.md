---
title: Dynamic-link library creation
description: To create a Dynamic-Link Library (DLL), you must create one or more source code files, and possibly a linker file for exporting the functions.
ms.assetid: b66ea0e8-84c3-40be-bf02-765b9dd61f9f
ms.topic: concept-article
ms.date: 01/26/2024
---

# Dynamic-link library creation

To create a Dynamic-link library (DLL), you must create one or more source code files, and possibly a linker file for exporting the functions. If you plan to allow applications that use your DLL to use load-time dynamic linking, then you must also create an import library.

## Creating source files

The source files for a DLL contain exported functions and data, internal functions and data, and an optional [entry-point function](dynamic-link-library-entry-point-function.md) for the DLL. You may use any development tools that support the creation of Windows-based DLLs.

If your DLL may be used by a multithreaded application, then you should make your DLL "thread-safe". To avoid data corruption, you must synchronize access to all of the DLL's global data. You must also ensure that you link only with libraries that are thread-safe as well. For example, Microsoft Visual C++ contains multiple versions of the C Run-time Library, one that is not thread-safe and two that are.

## Exporting functions

How you specify which functions in a DLL should be exported depends on the tools that you are using for development. Some compilers allow you to export a function directly in the source code by using a modifier in the function declaration. Other times, you must specify exports in a file that you pass to the linker.

For example, using Visual C++, there are two possible ways to export DLL functions: with the [**\_\_declspec(dllexport)**](/cpp/build/exporting-from-a-dll-using-declspec-dllexport) modifier or with a module-definition (`.def`) file. If you use the **\_\_declspec(dllexport)** modifier, then it's not necessary to use a `.def` file. For more info, see [Exporting from a DLL](/cpp/build/exporting-from-a-dll).

## Creating an import library

An import library (`.lib`) file contains information that the linker needs in order to resolve external references to exported DLL functions, so that the system can locate the specified DLL and exported DLL functions at run-time. You can create an import library for your DLL when you build your DLL.

For more info, see [Building an import library and export file](/cpp/build/reference/building-an-import-library-and-export-file).

## Using an import library

For example, to call the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) function, you must link your code with the import library `User32.lib`. The reason is that **CreateWindow** resides in a system DLL named `User32.dll`, and `User32.lib` is the import library used to resolve the calls in your code to exported functions in `User32.dll`. The linker creates a table that contains the address of each function call. Calls to functions in a DLL will be fixed up when the DLL is loaded. While the system is initializing the process, it loads `User32.dll` because the process depends on exported functions in that DLL, and it updates the entries in the function address table. All calls to **CreateWindow** invoke the function exported from `User32.dll`.

For more info, see [Link an executable to a DLL](/cpp/build/linking-an-executable-to-a-dll).

## Related topics

* [Creating a Simple Dynamic-link Library](creating-a-simple-dynamic-link-library.md)
* [DLLs (Visual C++)](/cpp/build/dlls-in-visual-cpp)
* 
