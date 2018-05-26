---
title: IWMPControls playItem method
description: The playItem method plays the specified media item.
ms.assetid: ddd4e4f7-475c-4964-a623-9123ed66be8e
keywords:
- playItem method Windows Media Player
- playItem method Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , playItem method
topic_type:
- apiref
api_name:
- IWMPControls.playItem
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWMPControls::playItem method

The **playItem** method plays the specified media item.

## Syntax


```CSharp
public void playItem(
  IWMPMedia pIWMPMedia
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public Sub playItem( _
  ByVal pIWMPMedia As IWMPMedia _
)
Implements IWMPControls.playItem</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*pIWMPMedia* \[in\]
</dt> <dd>

A **WMPLib.IWMPMedia** interface to the media item.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The media item will load and play automatically, regardless of the value of the **IWMPSettings.autoStart** property. To load an item without playing it automatically, set **IWMPSettings.autoStart** to **false** and assign a value to **AxWindowsMediaPlayer.URL**, after which **IWMPControls.play** can be called to start playing the item.

Note

**playItem** works only with items in **AxWindowsMediaPlayer.currentPlaylist**. Calling **playItem** with a reference to a saved media item is not supported.

## Examples

The following example uses **playItem** to play a media item from the current playlist. The item to play is chosen based upon its position in the playlist. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Declare a variable to hold the position of the media item 
// in the current playlist. An arbitrary value is supplied here.
int index = 3;

// Get the media item at the fourth position in the current playlist.
WMPLib.IWMPMedia media = player.currentPlaylist.get_Item(index);

// Play the media item.
player.Ctlcontrols.playItem(media);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>&#39; Declare a variable to hold the position of the media item 
&#39; in the current playlist. An arbitrary value is supplied here.
Dim index As Integer = 3

&#39; Get the media item at the fourth position in the current playlist.
Dim Media As WMPLib.IWMPMedia = player.currentPlaylist.Item(index)

&#39; Play the media item.
player.Ctlcontrols.playItem(Media)</code></pre></td>
</tr>
</tbody>
</table>



## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.currentPlaylist (VB and C#)**](axwmplib-axwindowsmediaplayer-currentplaylist--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPControls.play (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-play--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist.Item (VB and C#)**](iwmpplaylist-item--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.autoStart (VB and C#)**](wmplibiwmpsettings-iwmpsettings-autostart--vb-and-c.md)
</dt> </dl>

 

 





