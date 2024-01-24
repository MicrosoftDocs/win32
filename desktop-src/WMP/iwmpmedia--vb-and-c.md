---
title: IWMPMedia (VB and C ) interface (Wmp.h)
description: Provides a way to set and retrieve the properties of a media item.The IWMPMedia interface exposes the following properties.
ms.assetid: 4f67336e-d1d3-4f18-b063-086edf9d9094
keywords:
- IWMPMedia (VB and C ) interface Windows Media Player
- IWMPMedia (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMedia (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMedia (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a way to set and retrieve the properties of a media item.

The **IWMPMedia** interface exposes the following properties.

## Members

The **IWMPMedia (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPMedia (VB and C#)** interface has these methods.



| Method                                                                             | Description                                                                                                   |
|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| [**getAttributeName**](wmplibiwmpmedia-iwmpmedia-getattributename--vb-and-c.md)   | Returns the name of the attribute corresponding to the specified index.<br/>                            |
| [**getItemInfo**](wmplibiwmpmedia-iwmpmedia-getiteminfo--vb-and-c.md)             | Returns the value of the specified attribute for the media item.<br/>                                   |
| [**getItemInfoByAtom**](wmplibiwmpmedia-iwmpmedia-getiteminfobyatom--vb-and-c.md) | Returns the value of the attribute with the specified index number.<br/>                                |
| [**getMarkerName**](wmplibiwmpmedia-iwmpmedia-getmarkername--vb-and-c.md)         | Returns the name of the marker at the specified index.<br/>                                             |
| [**getMarkerTime**](wmplibiwmpmedia-iwmpmedia-getmarkertime--vb-and-c.md)         | Returns the time of the marker at the specified index.<br/>                                             |
| [**isMemberOf**](wmplibiwmpmedia-iwmpmedia-ismemberof--vb-and-c.md)               | Returns a value indicating whether the specified media item is a member of the specified playlist.<br/> |
| [**isReadOnlyItem**](wmplibiwmpmedia-iwmpmedia-isreadonlyitem--vb-and-c.md)       | Returns a value indicating whether the attributes of the specified media item can be edited.<br/>       |
| [**setItemInfo**](wmplibiwmpmedia-iwmpmedia-setiteminfo--vb-and-c.md)             | Sets the value of the specified attribute for the media item.<br/>                                      |



 

### Properties

The **IWMPMedia (VB and C#)** interface has these properties.



| Property                                                                                      | Access type          | Description                                                                                                                                          |
|:----------------------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**attributeCount**](wmplibiwmpmedia-iwmpmedia-attributecount--vb-and-c.md)<br/>       | Read-only<br/> | Gets the number of attributes that can be queried and/or set for the media item.<br/>                                                          |
| [**duration**](wmplibiwmpmedia-iwmpmedia-duration--vb-and-c.md)<br/>                   | Read-only<br/> | Gets the duration in seconds of the current media item.<br/>                                                                                   |
| [**durationString**](wmplibiwmpmedia-iwmpmedia-durationstring--vb-and-c.md)<br/>       | Read-only<br/> | Gets a value indicating the duration of the current media item in HH:MM:SS format.<br/>                                                        |
| [**imageSourceHeight**](wmplibiwmpmedia-iwmpmedia-imagesourceheight--vb-and-c.md)<br/> | Read-only<br/> | Gets the height of the current media item in pixels.<br/>                                                                                      |
| [**imageSourceWidth**](wmplibiwmpmedia-iwmpmedia-imagesourcewidth--vb-and-c.md)<br/>   | Read-only<br/> | Gets the width of the current media item in pixels.<br/>                                                                                       |
| [**isIdentical**](iwmpmedia-isidentical--vb-and-c.md)<br/>                             | Read-only<br/> | Gets a value indicating whether the specified media item is the same as the current one. In C#, this is the **get\_isIdentical** method.<br/> |
| [**markerCount**](wmplibiwmpmedia-iwmpmedia-markercount--vb-and-c.md)<br/>             | Read-only<br/> | Gets the number of markers in the media item.<br/>                                                                                             |
| [**name**](wmplibiwmpmedia-iwmpmedia-name--vb-and-c.md)<br/>                           | Read-only<br/> | Gets or sets the name of the media item.<br/>                                                                                                  |
| [**sourceURL**](wmplibiwmpmedia-iwmpmedia-sourceurl--vb-and-c.md)<br/>                 | Read-only<br/> | Gets the URL of the media item.<br/>                                                                                                           |



 

Get an **IWMPMedia** interface by using the following properties or methods accessed through the following object or interface.



| Object or interface                                               | Property or method                                                                                                                       |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMPControls**](iwmpcontrols--vb-and-c.md)                    | [**currentitem**](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)                                                             |
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md) | [**currentMedia**](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md), [**newMedia**](axwmplib-axwindowsmediaplayer-newmedia.md) |
| [**IWMPPlaylist**](iwmpplaylist--vb-and-c.md)                    | [**Item**](iwmpplaylist-item--vb-and-c.md) (get\_Item in C#)                                                                           |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPMedia2 Interface (VB and C#)**](iwmpmedia2--vb-and-c.md)
</dt> <dt>

[**IWMPMedia3 Interface (VB and C#)**](iwmpmedia3--vb-and-c.md)
</dt> </dl>

 

 





