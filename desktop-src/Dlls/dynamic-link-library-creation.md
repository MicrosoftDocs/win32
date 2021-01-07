---
description: To create a Dynamic-Link Library (DLL), you must create one or more source code files, and possibly a linker file for exporting the functions.
ms.assetid: b66ea0e8-84c3-40be-bf02-765b9dd61f9f
title: Dynamic-Link Library Creation
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Creation

To create a Dynamic-Link Library (DLL), you must create one or more source code files, and possibly a linker file for exporting the functions. If you plan to allow applications that use your DLL to use load-time dynamic linking, you must also create an import library.

## Creating Source Files

The source files for a DLL contain exported functions and data, internal functions and data, and an optional [entry-point function](dynamic-link-library-entry-point-function.md) for the DLL. You may use any development tools that support the creation of Windows-based DLLs.

If your DLL may be used by a multithreaded application, you should make your DLL "thread-safe". You must synchronize access to all of the DLL's global data to avoid data corruption. You must also ensure that you link only with libraries that are thread-safe as well. For example, Microsoft Visual C++ contains multiple versions of the C Run-time Library, one that is not thread-safe and two that are.

## Exporting Functions

How you specify which functions in a DLL should be exported depends on the tools that you are using for development. Some compilers allow you to export a function directly in the source code by using a modifier in the function declaration. Other times, you must specify exports in a file that you pass to the linker.

For example, using Visual C++, there are two possible ways to export DLL functions: with the [**\_\_declspec(dllexport)**](https://msdn.microsoft.com/library/3y1sfaz2(v=VS.71).aspx) modifier or with a module-definition (.def) file. If you use the **\_\_declspec(dllexport)** modifier, it is not necessary to use a .def file. For more information, see [Exporting from a DLL](/cpp/build/exporting-from-a-dll?view=vs-2019).

## Creating an Import Library

An import library (.lib) file contains information the linker needs to resolve external references to exported DLL functions, so the system can locate the specified DLL and exported DLL functions at run time. You can create an import library for your DLL when you build your DLL.

For more information, see [Building an Import Library and Export File](/cpp/build/reference/building-an-import-library-and-export-file?view=vs-2019).

## Using an Import Library

For example, to call the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) function, you must link your code with the import library User32.lib. The reason is that **CreateWindow** resides in a system DLL named User32.dll, and User32.lib is the import library used to resolve the calls to exported functions in User32.dll in your code. The linker creates a table that contains the address of each function call. Calls to functions in a DLL will be fixed up when the DLL is loaded. While the system is initializing the process, it loads User32.dll because the process depends on exported functions in that DLL, and it updates the entries in the function address table. All calls to **CreateWindow** invoke the function exported from User32.dll.

For information, see [Linking Implicitly with a DLL](/previous-versions/d14wsce5(v=vs.140)).

## Related topics

<dl> <dt>

[Creating a Simple Dynamic-link Library](creating-a-simple-dynamic-link-library.md)
</dt> <dt>

[DLLs (Visual C++)](/cpp/build/dlls-in-visual-cpp?view=vs-2019)
</dt> </dl>

 

 
