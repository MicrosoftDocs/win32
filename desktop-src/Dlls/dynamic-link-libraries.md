---
description: A dynamic-link library (DLL) is a module that contains functions and data that can be used by another module (application or DLL).
ms.assetid: '09e35b46-86a1-44ed-ab6d-207857b2605c'
title: Dynamic-Link Libraries (Dynamic-Link Libraries)
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Libraries (Dynamic-Link Libraries)

A *dynamic-link library* (DLL) is a module that contains functions and data that can be used by another module (application or DLL).

A DLL can define two kinds of functions: exported and internal. The exported functions are intended to be called by other modules, as well as from within the DLL where they are defined. Internal functions are typically intended to be called only from within the DLL where they are defined. Although a DLL can export data, its data is generally used only by its functions. However, there is nothing to prevent another module from reading or writing that address.

DLLs provide a way to modularize applications so that their functionality can be updated and reused more easily. DLLs also help reduce memory overhead when several applications use the same functionality at the same time, because although each application receives its own copy of the DLL data, the applications share the DLL code.

The Windows application programming interface (API) is implemented as a set of DLLs, so any process that uses the Windows API uses dynamic linking.

-   [About Dynamic-Link Libraries](about-dynamic-link-libraries.md)
-   [Using Dynamic-Link Libraries](using-dynamic-link-libraries.md)
-   [Dynamic-Link Library Reference](dynamic-link-library-reference.md)

> [!Note]  
> If you are a user experiencing difficulty with a DLL on your computer, you should contact customer support for the software vendor that publishes the DLL. If you feel you are in need of support for a Microsoft product (including Windows), please go to our technical support site at [support.microsoft.com](https://support.microsoft.com).

 

## Related topics

<dl> <dt>

[DLLs (Visual C++)](/cpp/build/dlls-in-visual-cpp)
</dt> </dl>

 

 
