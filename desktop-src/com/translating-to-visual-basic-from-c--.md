---
title: Translating to Visual Basic from C++
description: Translating to Visual Basic from C++
ms.assetid: fce7ea25-cb24-4cc4-8f36-0e8aed2f3ada
ms.topic: article
ms.date: 05/31/2018
---

# Translating to Visual Basic from C++

Using the C++ programming language, developers can directly access the memory that stores a particular variable. Memory pointers provide this direct access. In Visual Basic, pointers are handled for you. For example, a parameter declared as a pointer to an **int** in C++ is equivalent to a parameter declared in Visual Basic as a **ByRef** **Integer**.

A parameter that is declared **As String** in Visual Basic is declared as a pointer to a **BSTR** in C++. Setting a string pointer to **NULL** in C++ is equivalent to setting the string to the **vbNullString** constant in Visual Basic. Passing in a zero-length string ("") to a function designed to receive **NULL** does not work, as this passes a pointer to a zero-length string instead of a zero pointer.

C++ supports data containers, namely structures and unions, that have no equivalent in early versions of Visual Basic. For this reason, COM objects typically wrap information that usually is stored in structures and unions in object classes. Some COM objects, however, may contain structures, causing portions of the object's methods or functionality to be inaccessible to Visual Basic.

Some C++ data types are not supported in Visual Basic, for example unsigned types and **HWND** types. Methods that accept or return these data types are not available in Visual Basic.

Visual Basic uses Automation-compatible data types as its internal data types. Thus, C++ data types that are Automation-compatible are also compatible with Visual Basic. Data types that are not Automation-compatible may not be able to be converted to Visual Basic.

The following table lists the data types are supported by Visual Basic and their **VARTYPE** equivalents. **VARTYPE** is an enumeration that lists the Automation variant types.



| Visual Basic data type  | VARTYPE equivalent                |
|-------------------------|-----------------------------------|
| **Integer**<br/>  | 16 bit, signed, VT\_I2<br/> |
| **Long**<br/>     | 32 bit, signed, VT\_I4<br/> |
| **Date**<br/>     | VT\_DATE<br/>               |
| **Currency**<br/> | VT\_CY<br/>                 |
| **Object**<br/>   | \*VT\_DISPATCH<br/>         |
| **String**<br/>   | VT\_BSTR<br/>               |
| **Boolean**<br/>  | VT\_BOOL<br/>               |
| **Currency**<br/> | VT\_DECIMAL<br/>            |
| **Single**<br/>   | VT\_R4<br/>                 |
| **Double**<br/>   | VT\_R8<br/>                 |
| **Decimal**<br/>  | VT\_DECIMAL<br/>            |
| **Byte**<br/>     | VT\_DECIMAL<br/>            |
| **Variant**<br/>  | VT\_VARIANT<br/>            |



 

All parameters in Visual Basic, unless labeled with the keyword **ByVal**, are passed by reference (as pointers) instead of by value.

C++ and Visual Basic differ slightly in how they represent properties. In C++, properties are represented as a set of accessor functions, one that sets the property value and one that retrieves the property value. In Visual Basic, properties are represented as a single item that can be used to retrieve or set the property value.

## Related topics

<dl> <dt>

[Translating to Visual Basic](translating-to-visual-basic.md)
</dt> </dl>

 

 





