---
title: /robust switch
description: The /robust switch tells the MIDL compiler to generate additional error-checking information, which the NDR engine uses to perform integrity checks at run time.
ms.assetid: 7a858600-ea06-4396-9a1b-240d646e8c7d
keywords:
- /robust switch MIDL
topic_type:
- apiref
api_name:
- /robust
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /robust switch

The **/robust** switch tells the MIDL compiler to generate additional error-checking information, which the NDR engine uses to perform integrity checks at run time.

``` syntax
midl /robust {/Oicf | /Oif }
```

## Switch Options

<dl> <dt>

*/Oicf* 
</dt> <dd></dd> <dt>

*/Oif* 
</dt> <dd>

These switches are identical in their functionality. They specify the codeless proxy method of marshaling and use fast format strings for improved performance. See / [**Oi**](-oi.md).

</dd> </dl>

## Remarks

Using the **/robust** switch generates additional information that allows the Network Data Representation (NDR) engine to perform run-time error checking on correlated arguments in dynamic arrays, unions, and in [**out**](out-idl.md) interface pointers in DCOM applications. The **/robust** switch is only available under WindowsÂ 2000 and later versions of Windows.

A correlated argument is an argument that uses any of the attributes that allow the size of a data object to be determined at run time: [**size\_is**](size-is.md), [**length\_is**](length-is.md), [**first\_is**](first-is.md), [**last\_is**](last-is.md), [**max\_is**](max-is.md), [**switch\_is**](switch-is.md), and [**iid\_is**](iid-is.md). In accordance with the OSF-DCE specification for the wire representation, this correlated argument appears in two different places. For example, consider a typical usage of the **size\_is** attribute:

``` syntax
HRESULT Func1([in] long Size, 
              [in, size_is(Size)]BAR_TYPE *pBarType);
```

In this example, the client passes a long that specifies the size of a block of BAR\_TYPEs (in terms of number of BAR\_TYPES elements), and a pointer to the actual block of BAR\_TYPEs. The Size argument correlates with the pBarType argument. In accordance with the OSF-DCE specification, the Size argument is represented twice on the wire—first as itself and then with the array of BAR\_TYPE elements that represent the pBarType argument. Each argument is unmarshaled independently, according to its own wire representation. Normally, the Size argument and its copy, which is used to represent part of the other argument, have the same values. However, if the Size argument becomes corrupted (for example, when the block of BAR\_TYPES is larger than what was allocated), the server application may stop responding, because it uses the value of the Size argument to measure incoming data.

The **/robust** switch is required to implement valid range checking with the [**range**](range.md) attribute.

## Examples

**midl /robust /Oicf filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/Oi**](-oi.md)
</dt> <dt>

[**range**](range.md)
</dt> </dl>

 

 




