---
title: AxWindowsMediaPlayer.currentPlaylist property
description: The currentPlaylist property gets or sets the current IWMPPlaylist interface that provides an easy way to organize and manipulate media items in a list.
ms.assetid: d5a9f126-a628-499c-a012-8a47c6c987ef
keywords:
- currentPlaylist property Windows Media Player
- currentPlaylist property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , currentPlaylist property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.currentPlaylist
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.currentPlaylist property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The currentPlaylist property gets or sets the current **IWMPPlaylist** interface that provides an easy way to organize and manipulate media items in a list.

## Syntax


```CSharp
public IWMPPlaylist currentPlaylist {get; set;}
```


```VB

Public Property currentPlaylist As IWMPPlaylist
```





## Property value

The WMPLib.IWMPPlaylist interface that provides access to the current playlist.

## Remarks

If the IWMPSettings.autoStart property (also accessed via AxWindowsMediaPlayer.settings.**autoStart**) is true, playback begins automatically whenever you set **currentPlaylist**.

This property takes an IWMPPlaylist interface, which can be acquired in several ways, such as by getting the value from the *IWMPPlaylistArray*.**Item** or *IWMPPlaylistCollection*.**newPlaylist** properties. To load a **playlist** item using a file name, set the URL property or use AxWindowsMediaPlayer.**newPlaylist**.

## Examples

The following example retrieves the first playlist in the library and uses the currentPlaylist property to set the retrieved playlist as the current playlist, and display its name. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Get an interface to the first playlist from the library. 
WMPLib.IWMPPlaylist firstPlaylist = player.playlistCollection.getAll().Item(0);

// Make the retrieved playlist the current playlist.
player.currentPlaylist = firstPlaylist;

// Display the name of the current playlist.
currentPlaylistLabel.Text = ("Found first playlist. Name = " + player.currentPlaylist.name);
```


```VB

' Get an interface to the first playlist from the library. 
Dim firstPlaylist As WMPLib.IWMPPlaylist = player.playlistCollection.getAll().Item(0)

&#39; Make the retrieved playlist the current playlist.
player.currentPlaylist = firstPlaylist

&#39; Display the name of the current playlist.
currentPlaylistLabel.Text = (&quot;Found first playlist. Name = &quot; + player.currentPlaylist.name)
```





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

[**AxWindowsMediaPlayer.newPlaylist (VB and C#)**](axwmplib-axwindowsmediaplayer-newplaylist.md)
</dt> <dt>

[**AxWindowsMediaPlayer.settings (VB and C#)**](axwmplib-axwindowsmediaplayer-settings--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistArray.Item (VB and C#)**](wmplibiwmpplaylistarray-iwmpplaylistarray-item--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.newPlaylist (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-newplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.autoStart (VB and C#)**](wmplibiwmpsettings-iwmpsettings-autostart--vb-and-c.md)
</dt> </dl>

 

 





