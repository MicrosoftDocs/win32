---
title: IWMPPlaylistCollection getAll method
description: The getAll method returns an IWMPPlaylistArray interface that provides access to all of the playlists in the library.
ms.assetid: d36dbc5c-ccb0-400a-ab5b-918598c218f1
keywords:
- getAll method Windows Media Player
- getAll method Windows Media Player , IWMPPlaylistCollection interface
- IWMPPlaylistCollection interface Windows Media Player , getAll method
topic_type:
- apiref
api_name:
- IWMPPlaylistCollection.getAll
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylistCollection::getAll method

The **getAll** method returns an **IWMPPlaylistArray** interface that provides access to all of the playlists in the library.

## Syntax


```CSharp
public IWMPPlaylistArray getAll();
```


```VB

Public Function getAll() As IWMPPlaylistArray
Implements IWMPPlaylistCollection.getAll
```





## Parameters

This method has no parameters.

## Return value

A **WMPLib.IWMPPlaylistArray** interface for the retrieved array of playlists.

## Remarks

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later.<br/>                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPPlaylistArray Interface (VB and C#)**](iwmpplaylistarray--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> </dl>

 

 





