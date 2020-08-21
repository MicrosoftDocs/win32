---
title: Marshaling OLE Data Types
description: Marshaling Automation and OLE data types.
ms.assetid: 0cab4208-d40d-40a1-88f2-4933b52c0c29
keywords:
- MIDL and COM MIDL , marshaling OLE data types
- marshaling MIDL
- OLE data MIDL
ms.topic: article
ms.date: 05/31/2018
---

# Marshaling OLE Data Types

To make it easier to use certain Automation and OLE data types, as well as some system handles frequently used in COM, typedefs for these data types and their related helper functions are available by importing Windows IDL files and linking to the OLE and Automation DLL files. These files are automatically installed on your system.

-   To use the [**BSTR**](/previous-versions/windows/desktop/automat/bstr) data type in remote procedure calls, import the wtypes.idl file into your interface definition (IDL) file and link to Oleaut32.lib when building your distributed application. This will let your stubs use the ready-made helper functions **BSTR\_UserSize**, **BSTR\_UserMarshal**, **BSTR\_UserUnmarshal**, and **BSTR\_UserFree**.
-   To use other Automation data types, such as [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) and [**SAFEARRAY**](/windows/win32/api/oaidl/ns-oaidl-safearray), or types that use those types (for example, [**DISPPARAMS**](/windows/win32/api/oaidl/ns-oaidl-dispparams) and [**EXCEPINFO**](/windows/win32/api/oaidl/ns-oaidl-excepinfo)), import the objidl.idl file into your IDL file and link to the oleaut32.lib at build time. This will allow you to use the appropriate helper routines.
-   To use OLE data types (such as CLIPFORMAT, SNB, STGMEDIUM, ASYNC\_STGMEDIUM), or system handles (such as HMETAFILE\_PICT, HENHMETAFILE, HMETAFILE, HBITMAP, HPALETTE, and HGLOBAL), import the objidl.idl file into your interface definition file and link to the ole32.lib at build time.
-   The following OLE handles are also defined with the **\[wire\_marshal\]** attribute, but only as handles within a computer since they cannot be used in remote procedure calls to other computers at this time: HWND, HMENU, HACCEL, HDC, HFONT, HICON, HBRUSH. Import the objidl.idl file into your IDL file and link to ole32.lib at build time to use these handles in interprocess communication on a single computer.

For more information, see [The wire\_marshal Attribute](/windows/desktop/Rpc/the-wire-marshal-attribute), [The type\_UserSize Function](/windows/desktop/Rpc/the-type-usersize-function), [The type\_UserMarshal Function](/windows/desktop/Rpc/the-type-usermarshal-function), [The type\_UserUnmarshal Function](/windows/desktop/Rpc/the-type-userunmarshal-function), [The type\_UserFree Function](/windows/desktop/Rpc/the-type-userfree-function), and [Targeting Stubs for Specific 32-bit or 64-bit Platforms](targeting-stubs-for-specific-32-bit-or-64-bit-platforms.md).

 

 