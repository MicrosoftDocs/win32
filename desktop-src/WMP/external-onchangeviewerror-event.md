---
title: External.OnChangeViewError Event
description: Note This topic describes functionality designed for use by online stores. | External.OnChangeViewError Event
ms.assetid: d6370629-5f50-434d-8eb5-5b43d1b2f7fe
keywords:
- External.OnChangeViewError Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnChangeViewError Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.OnChangeViewError Event

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnChangeViewError** event occurs when a call to the [External.changeView](external-changeview.md) method results in an error.

``` syntax
window.external.OnChangeViewError = FunctionName
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this event has the following parameters.

<dl> <dt>

<span id="hr"></span><span id="HR"></span>*hr*
</dt> <dd>

An **HRESULT** failure code that indicates the reason for the failure.

</dd> <dt>

<span id="LibraryLocationType"></span><span id="librarylocationtype"></span><span id="LIBRARYLOCATIONTYPE"></span>*LibraryLocationType*
</dt> <dd>

The same string that was passed in the **LibraryLocationType** parameter of **changeView**.

</dd> <dt>

<span id="LibraryLocationID"></span><span id="librarylocationid"></span><span id="LIBRARYLOCATIONID"></span>*LibraryLocationID*
</dt> <dd>

The same string thatwas passed in the **LibraryLocationID** parameter of **changeView**.

</dd> <dt>

<span id="Filter"></span><span id="filter"></span><span id="FILTER"></span>*Filter*
</dt> <dd>

The same string that was passed in the **Filter** parameter of **changeView**.

</dd> <dt>

<span id="ViewParams"></span><span id="viewparams"></span><span id="VIEWPARAMS"></span>*ViewParams*
</dt> <dd>

The same string that was passed in the **ViewParams** parameter of **changeView**.

</dd> </dl>

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExternalObject for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





