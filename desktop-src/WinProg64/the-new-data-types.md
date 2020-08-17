---
title: The New Data Types
description: Three classes of data types were introduced for 64-bit Windows fixed-precision data types, pointer-precision types, and specific-pointer-precision types.
ms.assetid: 016977d4-e7bf-463e-9755-7ef13f16e9e5
keywords:
- 64-bit Windows programming guide 64-bit Windows Programming , data types
- data types 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# The New Data Types

Three classes of data types were introduced for 64-bit Windows: fixed-precision data types, pointer-precision types, and specific-pointer-precision types. These types were added to the development environment to allow developers to prepare for 64-bit Windows. These types are derived from the basic C-language integer and long types. Therefore, you can use these data types in code that you compile and test on 32-bit Windows, and then recompile with the 64-bit compiler when targeting 64-bit Windows.

Even for applications that target only 32-bit Windows, adopting these new data types makes your code more robust. To use these data types, you must scan your code for potentially unsafe pointer usage, polymorphism, and data definitions. For example, when a variable is of type **ULONG\_PTR**, it is clear that it will be used for casting pointers for arithmetic operations or polymorphism. It is not possible to indicate such usage directly by using the older data types. (You can do this indirectly by using derived type naming or Hungarian notation, but both techniques are prone to errors.)

All of these data types are declared in BaseTsd.h. For more information, including definitions of these data types, see [Windows Data Types](/windows/desktop/WinProg/windows-data-types).

## Fixed Precision

Fixed-precision data types are the same length in both 32- and 64-bit Windows. To help you remember this, their precision is part of the name of the data type. The following are the fixed-precision data types.



| Term                                                                       | Description                        |
|----------------------------------------------------------------------------|------------------------------------|
| <span id="DWORD32"></span><span id="dword32"></span>**DWORD32**<br/> | 32-bit unsigned integer<br/> |
| <span id="DWORD64"></span><span id="dword64"></span>**DWORD64**<br/> | 64-bit unsigned integer<br/> |
| <span id="INT32"></span><span id="int32"></span>**INT32**<br/>       | 32-bit signed integer<br/>   |
| <span id="INT64"></span><span id="int64"></span>**INT64**<br/>       | 64-bit signed integer<br/>   |
| <span id="LONG32"></span><span id="long32"></span>**LONG32**<br/>    | 32-bit signed integer<br/>   |
| <span id="LONG64"></span><span id="long64"></span>**LONG64**<br/>    | 64-bit signed integer<br/>   |
| <span id="UINT32"></span><span id="uint32"></span>**UINT32**<br/>    | Unsigned **INT32**<br/>      |
| <span id="UINT64"></span><span id="uint64"></span>**UINT64**<br/>    | Unsigned **INT64**<br/>      |
| <span id="ULONG32"></span><span id="ulong32"></span>**ULONG32**<br/> | Unsigned **LONG32**<br/>     |
| <span id="ULONG64"></span><span id="ulong64"></span>**ULONG64**<br/> | Unsigned **LONG64**<br/>     |



 

## Pointer Precision

As the pointer precision changes (that is, as it becomes 32 bits on 32-bit Windows and 64 bits with 64-bit Windows), the pointer precision data types reflect the precision accordingly. Therefore, it is safe to cast a pointer to one of these types when performing pointer arithmetic; if the pointer precision is 64 bits, the type is 64 bits. The count types also reflect the maximum size to which a pointer can refer. The following are the pointer-precision and count types.



| Term                                                                              | Description                                                                                                                      |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <span id="DWORD_PTR"></span><span id="dword_ptr"></span>**DWORD\_PTR**<br/> | Unsigned long type for pointer precision.<br/>                                                                             |
| <span id="HALF_PTR"></span><span id="half_ptr"></span>**HALF\_PTR**<br/>    | Half the size of a pointer. Use within a structure that contains a pointer and two small fields.<br/>                      |
| <span id="INT_PTR"></span><span id="int_ptr"></span>**INT\_PTR**<br/>       | Signed integer type for pointer precision.<br/>                                                                            |
| <span id="LONG_PTR"></span><span id="long_ptr"></span>**LONG\_PTR**<br/>    | Signed long type for pointer precision.<br/>                                                                               |
| <span id="SIZE_T"></span><span id="size_t"></span>**SIZE\_T**<br/>          | The maximum number of bytes to which a pointer can refer. Use for a count that must span the full range of a pointer.<br/> |
| <span id="SSIZE_T"></span><span id="ssize_t"></span>**SSIZE\_T**<br/>       | Signed **SIZE\_T**.<br/>                                                                                                   |
| <span id="UHALF_PTR"></span><span id="uhalf_ptr"></span>**UHALF\_PTR**<br/> | Unsigned **HALF\_PTR**.<br/>                                                                                               |
| <span id="UINT_PTR"></span><span id="uint_ptr"></span>**UINT\_PTR**<br/>    | Unsigned **INT\_PTR**.<br/>                                                                                                |
| <span id="ULONG_PTR"></span><span id="ulong_ptr"></span>**ULONG\_PTR**<br/> | Unsigned **LONG\_PTR**.<br/>                                                                                               |



 

## Specific Pointer-Precision Types

The following new pointer types explicitly size the pointer. Be cautious when using pointers in 64-bit code: If you declare the pointer using a 32-bit type, the operating system creates the pointer by truncating a 64-bit pointer. (All pointers are 64 bits on 64-bit Windows.)



| Term                                                                                 | Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="POINTER_32"></span><span id="pointer_32"></span>**POINTER\_32**<br/> | A 32-bit pointer. On 32-bit Windows, this is a native pointer. On 64-bit Windows, this is a truncated 64-bit pointer.<br/>                                                                                       |
| <span id="POINTER_64"></span><span id="pointer_64"></span>**POINTER\_64**<br/> | A 64-bit pointer. On 64-bit Windows, this is a native pointer. On 32-bit Windows, this is a sign-extended 32-bit pointer. <br/> Note that it is not safe to assume the state of the high pointer bit.<br/> |



 

 

