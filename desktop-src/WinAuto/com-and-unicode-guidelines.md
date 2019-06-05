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

-   [**OleInitialize**](https://docs.microsoft.com/windows/desktop/api/ole2/nf-ole2-oleinitialize)
-   [**CoInitialize**](https://docs.microsoft.com/windows/desktop/api/objbase/nf-objbase-coinitialize) or [**CoInitializeEx**](https://docs.microsoft.com/windows/desktop/api/combaseapi/nf-combaseapi-coinitializeex)
-   [**IUnknown::AddRef**](https://docs.microsoft.com/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref) and [**IUnknown::Release**](https://docs.microsoft.com/windows/desktop/api/unknwn/nf-unknwn-iunknown-release)
-   [**VariantInit**](https://docs.microsoft.com/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantinit) and [**VariantClear**](https://docs.microsoft.com/previous-versions/windows/desktop/api/oleauto/nf-oleauto-variantclear)
-   [**MultiByteToWideChar**](https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](https://docs.microsoft.com/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte)
-   [**SysAllocString**](https://docs.microsoft.com/previous-versions/windows/desktop/api/oleauto/nf-oleauto-sysallocstring) and [**SysFreeString**](https://docs.microsoft.com/previous-versions/windows/desktop/api/oleauto/nf-oleauto-sysfreestring)

### Structures and data types:

-   [**VARIANT**](variant-structure.md)
-   [**HRESULT**](https://docs.microsoft.com/windows/desktop/com/structure-of-com-error-codes)
-   [**BSTR**](https://docs.microsoft.com/previous-versions/windows/desktop/automat/bstr)

### COM Interfaces:

-   [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown)
-   [**IDispatch**](idispatch-interface.md)
-   [**IEnumVARIANT**](https://docs.microsoft.com/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ienumvariant)

## In this section

-   [VARIANT Structure](variant-structure.md)
-   [IDispatch Interface](idispatch-interface.md)
-   [Converting Unicode and ANSI Strings](converting-unicode-and-ansi-strings.md)

 

 




