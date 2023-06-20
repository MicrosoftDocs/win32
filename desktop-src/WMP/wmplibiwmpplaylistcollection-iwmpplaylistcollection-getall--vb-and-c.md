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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylistCollection::getAll method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





