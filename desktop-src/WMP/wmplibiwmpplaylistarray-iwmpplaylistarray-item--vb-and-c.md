---
title: IWMPPlaylistArray Item method
description: The Item method returns an IWMPPlaylist interface representing the playlist at the specified index.
ms.assetid: 5cb4b89f-b679-4d92-a5f9-5d0fe686775d
keywords:
- Item method Windows Media Player
- Item method Windows Media Player , IWMPPlaylistArray interface
- IWMPPlaylistArray interface Windows Media Player , Item method
topic_type:
- apiref
api_name:
- IWMPPlaylistArray.Item
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylistArray::Item method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Item** method returns an **IWMPPlaylist** interface representing the playlist at the specified index.

## Syntax


```CSharp
public IWMPPlaylist Item(
  System.Int32 lIndex
);
```


```VB

Public Function Item( _
  ByVal lIndex As System.Int32 _
) As IWMPPlaylist
Implements IWMPPlaylistArray.Item
```





## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** containing the index that identifies the playlist that the method should retrieve.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylist** interface for the retrieved playlist.

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

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistArray Interface (VB and C#)**](iwmpplaylistarray--vb-and-c.md)
</dt> </dl>

 

 





