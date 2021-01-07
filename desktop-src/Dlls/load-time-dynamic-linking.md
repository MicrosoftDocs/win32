---
description: When the system starts a program that uses load-time dynamic linking, it uses the information the linker placed in the file to locate the names of the DLLs that are used by the process.
ms.assetid: 29a17116-bb08-4fdd-857c-b7a7f8d2278c
title: Load-Time Dynamic Linking
ms.topic: article
ms.date: 05/31/2018
---

# Load-Time Dynamic Linking

When the system starts a program that uses load-time dynamic linking, it uses the information the linker placed in the file to locate the names of the DLLs that are used by the process. The system then searches for the DLLs. For more information, see [Dynamic-Link Library Search Order](dynamic-link-library-search-order.md).

If the system cannot locate a required DLL, it terminates the process and displays a dialog box that reports the error to the user. Otherwise, the system maps the DLL into the virtual address space of the process and increments the DLL reference count.

The system calls the entry-point function. The function receives a code indicating that the process is loading the DLL. If the entry-point function does not return TRUE, the system terminates the process and reports the error. For more information about the entry-point function, see [Dynamic-Link Library Entry-Point Function](dynamic-link-library-entry-point-function.md).

Finally, the system modifies the function address table with the starting addresses for the imported DLL functions.

The DLL is mapped into the virtual address space of the process during its initialization and is loaded into physical memory only when needed.

## Related topics

<dl> <dt>

[Using Load-Time Dynamic Linking](using-load-time-dynamic-linking.md)
</dt> </dl>

 

 



