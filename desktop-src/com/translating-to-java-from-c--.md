---
title: Translating to Java from C++
description: Using the C++ programming language, developers can directly access the memory that stores a particular variable. Memory pointers provide this direct access. In Java, pointers are handled for you.
ms.assetid: 2c8de3d9-3410-4153-b612-4afab8a69a18
ms.topic: article
ms.date: 05/31/2018
---

# Translating to Java from C++

Using the C++ programming language, developers can directly access the memory that stores a particular variable. Memory pointers provide this direct access. In Java, pointers are handled for you.

In Java, **struct**, **union**, and **typedef** composite data types are handled exclusively through the use of classes. For example, the C++ **VARIANT** data type maps to **com.ms.com.Variant** in Java.

In C++, strings are an array of characters. In Java, strings are objects. Methods that act on strings treat the string as a complete object.

COM methods return a value known as a **HRESULT**, which is a 32-bit error code. The Java support for Microsoft Internet Explorer defines a class, **com.ms.com.ComException**, which wraps the **HRESULT** error code.

Java does not support unsigned data types except for **char**, which is a 16-bit unsigned integer. Methods that accept or return other unsigned data types cannot be used from Java.

Java does not support multidimensional arrays. Methods that accept or return multidimensional arrays are not available from Java.

Boolean values in Java cannot be cast to 0 and 1.

## Related topics

<dl> <dt>

[Translating to Java](translating-to-java.md)
</dt> </dl>

 

 




