---
title: External.OnChangeViewOnlineListError Event
description: Note This topic describes functionality designed for use by online stores. | External.OnChangeViewOnlineListError Event
ms.assetid: f53dfc80-a7d7-42b1-b390-e90aa108145f
keywords:
- External.OnChangeViewOnlineListError Event Windows Media Player
topic_type:
- apiref
api_name:
- External.OnChangeViewOnlineListError Event
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.OnChangeViewOnlineListError Event

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **OnChangeViewOnlineListError** event occurs when a call to the [External.changeViewOnlineList](external-changeviewonlinelist.md) method results in an error.

``` syntax
window.external.OnChangeViewOnlineListError = functionname
```

## Possible Values

This is a write-only property that specifies the name of the function in script that Windows Media Player calls when the event occurs.

## Parameters

The function that handles this error has the following parameters.

<dl> <dt>

<span id="hr"></span><span id="HR"></span>*hr*
</dt> <dd>

An **HRESULT** failure code that indicates the reason for the failure.

</dd> <dt>

<span id="LibraryLocationType"></span><span id="librarylocationtype"></span><span id="LIBRARYLOCATIONTYPE"></span>*LibraryLocationType*
</dt> <dd>

The same string that was passed in the **LibraryLocationType** parameter of **changeViewOnlineList**.

</dd> <dt>

<span id="LibraryLocationID"></span><span id="librarylocationid"></span><span id="LIBRARYLOCATIONID"></span>*LibraryLocationID*
</dt> <dd>

The same string that was passed in the **LibraryLocationID** parameter of **changeViewOnlineList**.

</dd> <dt>

<span id="Params"></span><span id="params"></span><span id="PARAMS"></span>*Params*
</dt> <dd>

The same string that was passed in the **Params** parameter of **changeViewOnlineList**.

</dd> <dt>

<span id="FriendlyName"></span><span id="friendlyname"></span><span id="FRIENDLYNAME"></span>*FriendlyName*
</dt> <dd>

The same string that was passed in the **FriendlyName** parameter of **changeViewOnlineList**.

</dd> <dt>

<span id="ListType"></span><span id="listtype"></span><span id="LISTTYPE"></span>*ListType*
</dt> <dd>

The same string that was passed in the **ListType** parameter of **changeViewOnlineList**.

</dd> <dt>

<span id="ViewMode"></span><span id="viewmode"></span><span id="VIEWMODE"></span>*ViewMode*
</dt> <dd>

The same string that was passed in the **ViewMode** parameter of **changeViewOnlineList**.

</dd> </dl>

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> </dl>

 

 





