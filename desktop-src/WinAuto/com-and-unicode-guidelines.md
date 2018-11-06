---
title: COM and Unicode Guidelines
description: Because Microsoft Active Accessibility is based on Component Object Model (COM), developers need a moderate level of understanding about COM objects and interfaces and must know how to perform basic tasks (for example, how to initialize the COM library).
ms.assetid: ed4bbef9-676a-4f4e-926a-044f71399c56
ms.topic: article
ms.date: 05/31/2018
---

# COM and Unicode Guidelines

Because Microsoft Active Accessibility is based on Component Object Model (COM), developers need a moderate level of understanding about COM objects and interfaces and must know how to perform basic tasks (for example, how to initialize the COM library). Server developers need to understand how to design classes that implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface and how to create accessible objects.

You also need a moderate level of understanding about Unicode to use many of the Microsoft Active Accessibility functions that return strings.

To use Microsoft Active Accessibility effectively, you should understand the following COM and Unicode functions, structures, data types, and interfaces. Limited information about some of these items is provided in this documentation.

### Functions:

-   [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134)
-   [**CoInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms678543) or [**CoInitializeEx**](https://msdn.microsoft.com/library/windows/desktop/ms695279)
-   [**IUnknown::AddRef**](https://msdn.microsoft.com/library/windows/desktop/ms691379) and [**IUnknown::Release**](https://msdn.microsoft.com/library/windows/desktop/ms682317)
-   [**VariantInit**](https://msdn.microsoft.com/library/windows/desktop/ms221402) and [**VariantClear**](https://msdn.microsoft.com/library/windows/desktop/ms221165)
-   [**MultiByteToWideChar**](https://msdn.microsoft.com/library/windows/desktop/dd319072) and [**WideCharToMultiByte**](https://msdn.microsoft.com/library/windows/desktop/dd374130)
-   [**SysAllocString**](https://msdn.microsoft.com/library/windows/desktop/ms221458) and [**SysFreeString**](https://msdn.microsoft.com/library/windows/desktop/ms221481)

### Structures and data types:

-   [**VARIANT**](variant-structure.md)
-   [**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/ms690088)
-   [**BSTR**](https://msdn.microsoft.com/library/windows/desktop/ms221069)

### COM Interfaces:

-   [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)
-   [**IDispatch**](idispatch-interface.md)
-   [**IEnumVARIANT**](https://msdn.microsoft.com/library/windows/desktop/ms221053)

## In this section

-   [VARIANT Structure](variant-structure.md)
-   [IDispatch Interface](idispatch-interface.md)
-   [Converting Unicode and ANSI Strings](converting-unicode-and-ansi-strings.md)

 

 




