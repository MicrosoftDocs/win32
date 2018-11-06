---
title: Encapsulated Unions
description: A union that is contained with its discriminant in a structure within is an encapsulated union.
ms.assetid: d32c18b4-b2f6-4ce2-94fe-a495a3c15d14
keywords:
- data types MIDL , encapsulated unions
ms.topic: article
ms.date: 05/31/2018
---

# Encapsulated Unions

A union that is contained with its discriminant in a structure within is an encapsulated union. The encapsulated union is indicated by the presence of the [**switch**](switch.md) keyword. This type of union is so named because the MIDL compiler automatically encapsulates the union and its discriminant in a structure for transmission during a remote procedure call.

If the union tag is missing (U1\_TYPE in the example above), the compiler will generate the structure with the union field named *tagged\_union*.

The shape of unions must be the same across platforms to ensure interconnectivity.

For a description of the form of an encapsulated union, see [**union**](union.md).

## Examples

``` syntax
typedef union _S1_TYPE switch (long l1) U1_TYPE 
{ 
    case 1024: 
        float f1; 
    case 2048: 
        double d2; 
} S1_TYPE; 
 
/* in generated header file */ 
typedef struct _S1_TYPE 
{ 
    long l1; 
    union 
    { 
        float f1; 
        double d2; 
    } U1_TYPE; 
} S1_TYPE;
```

For related information, see [MIDL Base Types](midl-base-types.md), [**char**](char-idl.md), **\[**[**context\_handle**](context-handle.md)**\]**, [**enum**](enum.md), **\[**[**first\_is**](first-is.md)**\]**, **\[**[**handle**](handle.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, [**int**](int.md), **\[**[**ignore**](ignore.md)**\]**, **\[**[**last\_is**](last-is.md)**\]**, **\[**[**length\_is**](length-is.md)**\]**, **\[**[**max\_is**](max-is.md)**\]**, **\[**[**ms\_union**](ms-union-attrib.md)**\]**, [Nonencapsulated Unions](nonencapsulated-unions.md), **\[**[**ptr**](ptr.md)**\]**, **\[**[**ref**](ref.md)**\]**, **\[**[**size\_is**](size-is.md)**\]**, **\[**[**string**](string.md)**\]**, [**struct**](struct.md), [**switch**](switch.md), **\[**[**switch\_is**](switch-is.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**, [**union**](union.md), and **\[**[**unique**](unique.md)**\]**

 

 




