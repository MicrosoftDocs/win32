---
title: Intrinsic Data Types
description: The following data types are recognized by MIDL.
ms.assetid: 7f8e79cd-3702-4dfe-85b8-467ec414a824
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Intrinsic Data Types

The following data types are recognized by MIDL.



| Type                         | Description                                                                                                                 |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **boolean**                  | Data item that can have the value **True** or **False**. The size maps to VARIANT\_BOOL.                                    |
| **char**                     | 8-bit signed data item.                                                                                                     |
| **double**                   | 64-bit IEEE floating-point number.                                                                                          |
| **int**                      | Signed integer, whose size is system dependent.                                                                             |
| **float**                    | 32-bit IEEE floating point number.                                                                                          |
| **long**                     | 32-bit signed integer.                                                                                                      |
| **short**                    | 16-bit signed integer.                                                                                                      |
| **wchar\_t**                 | Unicode character accepted only for 32-bit type libraries.                                                                  |
| [**BSTR**](bstr.md)         | Length-prefixed string, as described in [Dispatch Interface and API Functions](75BFF268-BD85-49C4-B761-B557F4B1C588).       |
| [**CURRENCY**](currency.md) | 8-byte, fixed-point number.                                                                                                 |
| **DATE**                     | 64-bit floating-point fractional number of days since December 30, 1899.                                                    |
| [**DECIMAL**](decimal.md)   | 96-bit unsigned binary integer scaled by a variable power of 10. Provides a size and scale for a number.                    |
| **SCODE**                    | Built-in error type that corresponds to VT\_ERROR. Essentially identical to an HRESULT.                                     |
| [**VARIANT**](/windows/previous-versions/OaIdl/ns-oaidl-tagvariant?branch=master)   | One of the variant data types as described in [Dispatch Interface and API Functions](75BFF268-BD85-49C4-B761-B557F4B1C588). |
| **IDispatch** \*             | Pointer to the **IDispatch** interface.                                                                                     |
| **IUnknown** \*              | Pointer to the **IUnknown** interface. (Any OLE interface can be represented by its **IUnknown** interface.)                |
| **SAFEARRAY**(*TypeName*)    | *TypeName* is any of the above types. Array of these types.                                                                 |
| *TypeName*\*                 | *TypeName* is any of the above types. Pointer to a type.                                                                    |
| **void**                     | Allowed only as return type for a function, or in a function parameter list to indicate no arguments.                       |
| **HRESULT**                  | Return type used for reporting error information in interfaces, as described in *COM Programmer's Reference*.               |
| **LPWSTR**                   | Unicode string accepted only for 32-bit type libraries.                                                                     |
| **LPSTR**                    | Zero-terminated string.                                                                                                     |



 

Not all of the above types can be marshaled by Automation to another process or thread. The list of types that can be marshaled are called Automation compatible types, and are listed under the [oleautomation](335E8F55-C313-423E-A301-8EF6A38C5B05) attribute description.

The keyword **unsigned** can be specified before **int**, **char**, **short**, and **long**.

 

 




