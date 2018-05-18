---
title: AxWindowsMediaPlayer.playlistCollection property
description: The playlistCollection property gets an IWMPPlaylistCollection interface.
ms.assetid: 'f3c65f70-b58f-41c1-afe0-3a9d9c95561c'
keywords: ["playlistCollection property Windows Media Player", "playlistCollection property Windows Media Player , AxWindowsMediaPlayer class", "AxWindowsMediaPlayer class Windows Media Player , playlistCollection property"]
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.playlistCollection
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
---

# AxWindowsMediaPlayer.playlistCollection property

The playlistCollection property gets an **IWMPPlaylistCollection** interface.

This property is read-only.

## Syntax


```CSharp
public IWMPPlaylistCollection playlistCollection {get;}
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
<td><pre><code>Public ReadOnly Property playlistCollection As IWMPPlaylistCollection</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The WMPLib.**IWMPPlaylistCollection** interface.

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



|                      |                                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





