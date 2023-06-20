---
title: IWMPPlaylistCollection getByName method
description: The getByName method returns a IWMPPlaylistArray interface that provides access to playlists with the specified name, if any exist.
ms.assetid: d41afab1-4103-4f59-a432-21a502499444
keywords:
- getByName method Windows Media Player
- getByName method Windows Media Player , IWMPPlaylistCollection interface
- IWMPPlaylistCollection interface Windows Media Player , getByName method
topic_type:
- apiref
api_name:
- IWMPPlaylistCollection.getByName
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylistCollection::getByName method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getByName** method returns a **IWMPPlaylistArray** interface that provides access to playlists with the specified name, if any exist.

## Syntax


```CSharp
public IWMPPlaylistArray getByName(
  System.String bstrName
);
```


```VB

Public Function getByName( _
  ByVal bstrName As System.String _
) As IWMPPlaylistArray
Implements IWMPPlaylistCollection.getByName
```





## Parameters

<dl> <dt>

*bstrName* \[in\]
</dt> <dd>

A **System.String** that is the name of the playlist.

</dd> </dl>

## Return value

A **WMPLib.IWMPPlaylistArray** interface for the retrieved array of playlists.

## Remarks

Use **IWMPPlaylistArray.count** to determine whether a playlist exists. If **count** is zero, the array is empty.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **getByName** to check the playlist collection for a playlist named "Favorites -- 4 and 5 star rated". If a playlist by that name exists, **getByName** sets it as the current playlist. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Get the count of the playlists named "Favorites -- 4 and 5 star rated".
int checkit = player.playlistCollection.getByName("Favorites -- 4 and 5 star rated").count;

// Since duplicate playlist names are allowed, the count returned
// will be either zero (no playlist) or greater than zero (playlist exists).
if (checkit > 0)
{
    // Retrieve a playlist array containing "Favorites -- 4 and 5 star rated".
    // Assume that there is only one playlist with that name, and assign it to the 
    // current playlist.
    player.currentPlaylist = player.playlistCollection.getByName("Favorites -- 4 and 5 star rated").Item(0);
}
```


```VB

'  Get the count of the playlists named &quot;Favorites -- 4 and 5 star rated&quot;.
Dim checkit As Integer = player.playlistCollection.getByName(&quot;Favorites -- 4 and 5 star rated&quot;).count

&#39;  Since duplicate playlist names are allowed, the count returned
&#39;  will be either zero (no playlist) or greater than zero (playlist exists).
If (checkit > 0) Then

    &#39;  Retrieve a playlist array object containing &quot;Favorites -- 4 and 5 star rated&quot;.
    &#39;  Assume that there is only one playlist with that name, and assign it to the 
    &#39;  current playlist.
    player.currentPlaylist = player.playlistCollection.getByName(&quot;Favorites -- 4 and 5 star rated&quot;).Item(0)

End If
```





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

[**IWMPPlaylistArray.count (VB and C#)**](wmplibiwmpplaylistarray-iwmpplaylistarray-count--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> </dl>

 

 





