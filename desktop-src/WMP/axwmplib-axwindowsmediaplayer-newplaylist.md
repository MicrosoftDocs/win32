---
title: AxWindowsMediaPlayer.newPlaylist method
description: The newPlaylist method returns an IWMPPlaylist interface for a new playlist.
ms.assetid: caee8ee5-6201-474d-a4cb-80e574f84f0b
keywords:
- newPlaylist method Windows Media Player
- newPlaylist method Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , newPlaylist method
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.newPlaylist
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.newPlaylist method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The newPlaylist method returns an IWMPPlaylist interface for a new playlist.

## Syntax


```CSharp
public IWMPPlaylist newPlaylist(
  System.String bstrName,
  System.String bstrURL
);
```


```VB

Public Function newPlaylist( _
  ByVal bstrName As System.String, _
  ByVal bstrURL As System.String _
) As IWMPPlaylist
```





## Parameters

<dl> <dt>

*bstrName* 
</dt> <dd>

The **System.String** that is the name of the new playlist.

</dd> <dt>

*bstrURL* 
</dt> <dd>

The **System.String** that is the URL of the Windows Media metafile playlist that is used to initialize the new playlist.

</dd> </dl>

## Return value

A WMPLib.IWMPPlaylist interface that represents the newly created playlist.

## Remarks

If the *bstrURL* parameter is a null or zero-length string (""), this method creates an empty **playlist**. If the *bstrName* parameter is a zero-length string (""), this method applies the current metafile name.

The new playlist created with this method is not added to the library. To add a new playlist to the library, use IWMPPlaylistCollection.**importPlaylist** or IWMPPlaylistCollection.**newPlaylist**. Any leading or trailing spaces in the playlist name are automatically removed when it is added to the library.

Because the library allows multiple playlists with the same name, you may want to check for the presence of a playlist with a given name before adding a new one.

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.importPlaylist (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-importplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.newPlaylist (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-newplaylist--vb-and-c.md)
</dt> </dl>

 

 





