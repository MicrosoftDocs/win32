---
title: IWMPPlaylistCollection newPlaylist method
description: The newPlaylist method returns an IWMPPlaylist interface for a new, empty playlist in the library.
ms.assetid: cc0cb356-9a90-421c-8d1a-b79585f71124
keywords:
- newPlaylist method Windows Media Player
- newPlaylist method Windows Media Player , IWMPPlaylistCollection interface
- IWMPPlaylistCollection interface Windows Media Player , newPlaylist method
topic_type:
- apiref
api_name:
- IWMPPlaylistCollection.newPlaylist
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylistCollection::newPlaylist method

The **newPlaylist** method returns an **IWMPPlaylist** interface for a new, empty playlist in the library.

## Syntax


```CSharp
public IWMPPlaylist newPlaylist(
  System.String bstrName
);
```


```VB

Public Function newPlaylist( _
  ByVal bstrName As System.String _
) As IWMPPlaylist
Implements IWMPPlaylistCollection.newPlaylist
```





## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

A **System.String** that is the name of the new playlist.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylist** interface for the new playlist.

## Remarks

This method creates an empty playlist in the library. To fill the playlist with media items, use **IWMPPlaylist.appendItem** or **IWMPPlaylist.insertItem**.

Multiple playlists having the same name are permitted in the library. To avoid creating a duplicate playlist name with this method, use the **getByName** method and **IWMPPlaylistArray.count** to discover whether a playlist with a particular name already exists.

Leading and trailing spaces are not permitted in playlist names, and are automatically removed from the value specified for the *bstrName* parameter.

Before calling this method, you must have full access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example creates a new empty playlist called "ThreeList", adds it to the playlist collection, and returns an interface to it. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Add a new empty playlist, named ThreeList, to the playlist collection.
WMPLib.IWMPPlaylist newList = player.playlistCollection.newPlaylist("ThreeList");
```


```VB

'  Add a new empty playlist, named ThreeList, to the playlist collection.
Dim newList As WMPLib.IWMPPlaylist = player.playlistCollection.newPlaylist(&quot;ThreeList&quot;)
```





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

[**IWMPPlaylist.appendItem (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-appenditem--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist.insertItem (VB and C#)**](wmplibiwmpplaylist-iwmpplaylist-insertitem--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistArray.count (VB and C#)**](wmplibiwmpplaylistarray-iwmpplaylistarray-count--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.getByName (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getbyname--vb-and-c.md)
</dt> </dl>

 

 





