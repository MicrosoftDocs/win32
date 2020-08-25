---
title: Data Type Conversions
description: Data Type Conversions
ms.assetid: 54688ee9-2dd7-466b-b278-13d6f9d1e6ce
ms.topic: article
ms.date: 05/31/2018
---

# Data Type Conversions

Each programming language defines certain types and containers for data. Most of these data types, especially the primitives, map easily to other programming languages. Some data types, however, have no equivalent in another language and cannot be converted.

For specific information about data types not recognized by your programming language, see the following topics:

-   [Translating to C++](translating-to-c--.md)
-   [Translating to Visual Basic](translating-to-visual-basic.md)
-   [Translating to Java](translating-to-java.md)

The following table lists conversions between programming languages for common data types.



| C++                                     | Visual Basic             | Java                               | Contains                                                                                       |
|-----------------------------------------|--------------------------|------------------------------------|------------------------------------------------------------------------------------------------|
| **signed char**<br/>              | Not supported<br/> | **byte**<br/>                | 1-byte signed integer <br/> (VT\_I1, \[T\])<br/>                                   |
| **unsigned char**<br/>            | **Byte**<br/>      | Not supported<br/>           | 1-byte unsigned integer <br/> (VT\_UI1, \[V\]\[T\]\[P\]\[S\])<br/>                 |
| **unsigned char**<br/>            | **Character**<br/> | **char**<br/>                | 2-byte Unicode character <br/> (VT\_UI2, \[T\]\[P\])<br/>                          |
| **short**<br/>                    | **Integer**<br/>   | **short**<br/>               | 2-byte signed integer <br/> (VT\_I2, \[V\]\[T\]\[P\]\[S\])<br/>                    |
| **unsigned short**<br/>           | Not supported<br/> | Not supported<br/>           | 2-byte unsigned integer <br/> (VT\_UI2, \[T\]\[P\])<br/>                           |
| **int**<br/>                      | **Long**<br/>      | **int**<br/>                 | 4-byte signed integer <br/> (VT\_I4, \[V\]\[T\]\[P\]\[S\])<br/>                    |
| **unsigned int**<br/>             | Not supported<br/> | Not supported<br/>           | 4-byte unsigned integer <br/> (VT\_UI4, \[T\]\[P\])<br/>                           |
| **\_\_int64**<br/>                | Not supported<br/> | **long**<br/>                | 8-byte signed integer <br/> (VT\_I8, \[T\]\[P\])<br/>                              |
| **unsigned \_\_int64**<br/>       | Not supported<br/> | Not supported<br/>           | 8-byte unsigned integer <br/> (VT\_UI8, \[T\]\[P\])<br/>                           |
| **float**<br/>                    | **Single**<br/>    | **float**<br/>               | 4-byte floating-point number <br/> (VT\_R4, \[V\]\[T\]\[P\]\[S\])<br/>             |
| **double**<br/>                   | **Double**<br/>    | **double**<br/>              | 8-byte floating-point number <br/> (VT\_R8, \[V\]\[T\]\[P\]\[S\])<br/>             |
| **BSTR**<br/>                     | **String**<br/>    | **java.lang.String**<br/>    | Automation string <br/> (VT\_BSTR, \[V\]\[T\]\[P\]\[S\])<br/>                      |
| **BOOL**<br/>                     | **Boolean**<br/>   | **boolean**<br/>             | Boolean <br/> (VT\_BOOL, \[V\]\[T\]\[P\]\[S\])<br/>                                |
| **VARIANT**<br/>                  | **Variant**<br/>   | **com.ms.com.Variant**<br/>  | VARIANT FAR\* <br/> (VT\_VARIANT, \[V\]\[T\]\[P\]\[S\])<br/>                       |
| [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown)<br/> | **object**<br/>    | **com.ms.com.IUnknown**<br/> | IDispatch interface pointer <br/> (VT\_DISPATCH, \[V\]\[T\]\[P\]\[S\])<br/>        |
| **DATE**<br/>                     | **Date**<br/>      | **com.ms.com.Variant**<br/>  | Date <br/> (VT\_DATE, \[V\]\[T\]\[P\]\[S\])<br/>                                   |
| **CURRENCY**<br/>                 | **Currency**<br/>  | **com.ms.com.Variant**<br/>  | Currency <br/> (VT\_CY, \[V\]\[T\]\[P\]\[S\] or VT\_DECIMAL, \[V\]\[T\]\[S\])<br/> |



 

For information about VARTYPE values and how to use them, see the topic [IDispatch Data Types and Structures](/previous-versions/ms221600(v=vs.100)).

The data type conversions between scripting languages are simpler than those for programming languages. JScript and JavaScript both support the same data types, and VBScript supports only a single data type, **Variant**. Thus, all JScript and JavaScript data types become **Variant** types when converted to VBScript. When you convert VBScript to JScript or JavaScript, the **Variant** types become numbers, strings, Boolean values, and so on.

 

