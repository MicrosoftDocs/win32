---
title: Translating to C++ from Visual Basic
description: Visual Basic handles pointers implicitly. In C++, your application is responsible for performing any necessary pointer arithmetic.
ms.assetid: bbbcaba1-cf5a-4768-ad1d-22a040bfe384
ms.topic: article
ms.date: 05/31/2018
---

# Translating to C++ from Visual Basic

Visual Basic handles pointers implicitly. In C++, your application is responsible for performing any necessary pointer arithmetic.

By default, Visual Basic passes parameters by reference (as pointers). Parameters that are meant to be passed by value only are specified by the keyword **ByVal**. For example, a **ByVal**Â **Integer** parameter in Visual Basic is equivalent to a **short** parameter in C++, whereas a **ByRef**Â **Integer** parameter in Visual Basic is equivalent to a **short\*** parameter.

A parameter that is declared **As String** in Visual Basic is declared as a pointer to a **BSTR** in C++. Setting a string pointer to **NULL** in C++ is equivalent to setting the string to the **vbNullString** constant in Visual Basic. Passing a zero-length string ("") to a function designed to receive **NULL** does not work, because this passes a pointer to a zero-length string instead of a zero pointer.

C++ and Visual Basic differ slightly in how they represent properties. In C++, properties are represented as a set of accessor functions, one that sets the property value and one that retrieves the property value. In Visual Basic, properties are represented as a single item that can be used to retrieve or set the property value.

## Related topics

<dl> <dt>

[Translating to C++](translating-to-c--.md)
</dt> </dl>

 

 




