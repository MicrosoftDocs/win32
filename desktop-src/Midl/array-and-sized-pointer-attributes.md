---
title: Array and Sized-Pointer Attributes
description: MIDL provides a rich set of features for passing arrays of data and pointers to data. You can use these attributes to specify characteristics of arrays and multiple levels of pointers.
ms.assetid: 482be83f-eb09-40a0-8dd6-a0cbf5dc4485
keywords:
- IDL MIDL , attributes, array and sized-pointer
ms.topic: article
ms.date: 05/31/2018
---

# Array and Sized-Pointer Attributes

MIDL provides a rich set of features for passing arrays of data and pointers to data. You can use these attributes to specify characteristics of arrays and multiple levels of pointers.



| Attribute                       | Usage                                                                                                                                                                                                |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**size\_is**](size-is.md)     | Specifies the amount of memory to be allocated for sized pointers, sized pointers to sized pointers, and single- or multidimensional arrays.                                                         |
| [**max\_is**](max-is.md)       | The maximum value for an array index.                                                                                                                                                                |
| [**length\_is**](length-is.md) | The number of array elements to be transmitted.                                                                                                                                                      |
| [**first\_is**](first-is.md)   | The index of the first array element to be transmitted.                                                                                                                                              |
| [**last\_is**](last-is.md)     | Gives the index of the last array element to be transmitted.                                                                                                                                         |
| [**string**](string.md)        | Indicates that the one-dimensional [**char**](char-idl.md), [**wchar\_t**](wchar-t.md), [**byte**](byte.md) (or equivalent) array, or the pointer to such an array, is to be handled as a string. |
| [**range**](range.md)          | Specifies a range of allowable values for arguments or fields whose values are set at runtime.                                                                                                       |



 

MIDL supports three kinds of pointers: reference pointers, unique pointers, and full pointers. These pointers are specified by the pointer attributes [**ref**](ref.md), [**unique**](unique.md), and [**ptr**](ptr.md).

A pointer attribute can be applied as a type attribute; as a field attribute that applies to a structure member, union member, or parameter; or as a function attribute that applies to the function return type. The pointer attribute can also appear with the [**pointer\_default**](pointer-default.md) keyword.

To allow a pointer parameter to change in value during a remote function, you must provide another level of indirection by supplying multiple pointer declarators. The explicit pointer attribute applied to the parameter affects only the rightmost pointer declarator for the parameter. When there are multiple pointer declarators in a parameter declaration, the other declarators default to the pointer attribute specified by the [**pointer\_default**](pointer-default.md) attribute. To apply different pointer attributes to multiple pointer declarators, you must define intermediate types that specify the explicit pointer attributes.

## Default Pointer-Attribute Values

When no pointer attribute is associated with a pointer that is a parameter, the pointer is assumed to be a [**ref**](ref.md) pointer.

When no pointer attribute is associated with a pointer that is a member of a structure or union, the MIDL compiler assigns pointer attributes using the following priority rules (1 is highest):

1.  Attributes explicitly applied to the pointer type
2.  Attributes explicitly applied to the pointer parameter or member
3.  The [**pointer\_default**](pointer-default.md) attribute in the IDL file that defines the type
4.  The [**pointer\_default**](pointer-default.md) attribute in the IDL file that imports the type
5.  [**ptr**](ptr.md) (osf mode); [**unique**](unique.md) (Microsoft RPC default mode)

When the IDL file is compiled in default mode, imported files can inherit pointer attributes from importing files. This feature is not available when you compile using the /[**osf**](-osf.md) switch. For more information, see [**import**](import.md).

## Function Return Types

A pointer returned by a function must be a [**unique**](unique.md) pointer or a full pointer. The MIDL compiler reports an error if a function result is a reference pointer, either explicitly or by default. The returned pointer always indicates new storage.

Functions that return a pointer value can specify a pointer attribute as a function attribute. If a pointer attribute is not present, the function-result pointer uses the value provided as the [**pointer\_default**](pointer-default.md) attribute.

## Pointer Attributes in Type Definitions

When you specify a pointer attribute at the top level of a [**typedef**](typedef.md) statement, the specified attribute is applied to the pointer declarator, as expected. When no pointer attribute is specified, pointer declarators at the top level of a typedef statement inherit the pointer attribute type when used.

DCE IDL does not allow the same pointer attribute to be explicitly applied twice—for example, in both the [**typedef**](typedef.md) declaration and the parameter attribute list. When you use the default (Microsoft extensions) mode of the MIDL compiler, this constraint is relaxed.

For a discussion of using MIDL arrays and pointers in remote procedure calls, see [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers).

 

 