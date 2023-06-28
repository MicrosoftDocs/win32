---
title: IWMPPlaylist (VB and C ) interface (Wmp.h)
description: Provides properties and methods to organize, manage, and manipulate media items in a playlist.The IWMPPlaylist interface exposes the following properties.
ms.assetid: c3f4f9dd-eb5f-493a-b8d0-22e70c63a2d1
keywords:
- IWMPPlaylist (VB and C ) interface Windows Media Player
- IWMPPlaylist (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPPlaylist (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylist (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides properties and methods to organize, manage, and manipulate media items in a playlist.

The **IWMPPlaylist** interface exposes the following properties.

## Members

The **IWMPPlaylist (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPPlaylist (VB and C#)** interface has these methods.



| Method                                                                       | Description                                                             |
|:-----------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**appendItem**](wmplibiwmpplaylist-iwmpplaylist-appenditem--vb-and-c.md)   | Adds a media item to the end of the playlist.<br/>                |
| [**clear**](iwmpplaylist-iwmpplaylist-clear--vb-and-c.md)                   | Reserved for future use.<br/>                                     |
| [**getItemInfo**](wmplibiwmpplaylist-iwmpplaylist-getiteminfo--vb-and-c.md) | Returns the value of a playlist attribute specified by name.<br/> |
| [**insertItem**](wmplibiwmpplaylist-iwmpplaylist-insertitem--vb-and-c.md)   | Inserts a media item at a specified location in a playlist.<br/>  |
| [**moveItem**](wmplibiwmpplaylist-iwmpplaylist-moveitem--vb-and-c.md)       | Changes the location of a media item in the playlist.<br/>        |
| [**removeItem**](wmplibiwmpplaylist-iwmpplaylist-removeitem--vb-and-c.md)   | Removes the specified media item from the playlist.<br/>          |
| [**setItemInfo**](wmplibiwmpplaylist-iwmpplaylist-setiteminfo--vb-and-c.md) | Sets the value of a playlist attribute.<br/>                      |



 

### Properties

The **IWMPPlaylist (VB and C#)** interface has these properties.



| Property                                                                                      | Access type           | Description                                                                                                                                         |
|:----------------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**attributeCount**](wmplibiwmpplaylist-iwmpplaylist-attributecount--vb-and-c.md)<br/> | Read-only<br/>  | Gets the number of attributes associated with a playlist.<br/>                                                                                |
| [**attributeName**](iwmpplaylist-attributename--vb-and-c.md)<br/>                      | Read-only<br/>  | Gets the name of a playlist attribute specified by an index. In C# this is the get\_attributeName method.<br/>                               |
| [**count**](wmplibiwmpplaylist-iwmpplaylist-count--vb-and-c.md)<br/>                   | Read-only<br/>  | Gets the number of media items in a playlist.<br/>                                                                                            |
| [**isIdentical**](iwmpplaylist-isidentical--vb-and-c.md)<br/>                          | Read-only<br/>  | Gets a value indicating whether the specified playlist is identical to the current playlist. In C# this is the get\_isIdentical method.<br/> |
| [**Item**](iwmpplaylist-item--vb-and-c.md)<br/>                                        | Read-only<br/>  | Gets an interface to the media item at the specified index. In C# this is the get\_Item method.<br/>                                         |
| [**name**](wmplibiwmpplaylist-iwmpplaylist-name--vb-and-c.md)<br/>                     | Read/write<br/> | Gets or sets the name of the playlist.<br/>                                                                                                   |



 

Get an **IWMPPlaylist** interface by using the following properties or methods accessed through the following object or interface.



| Object or interface                                                | Property or method                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWMPCdrom**](iwmpcdrom--vb-and-c.md)                           | [**Playlist**](wmplibiwmpcdrom-iwmpcdrom-playlist--vb-and-c.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**IWMPMediaCollection**](iwmpmediacollection--vb-and-c.md)       | [**getAll**](wmplibiwmpmediacollection-iwmpmediacollection-getall--vb-and-c.md), [**getByAlbum**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection-getbyalbum), [**getByAttribute**](wmplibiwmpmediacollection-iwmpmediacollection-getbyattribute--vb-and-c.md), [**getByAuthor**](wmplibiwmpmediacollection-iwmpmediacollection-getbyauthor--vb-and-c.md), [**getByGenre**](wmplibiwmpmediacollection-iwmpmediacollection-getbygenre--vb-and-c.md), [**getByName**](wmplibiwmpmediacollection-iwmpmediacollection-getbyname--vb-and-c.md) |
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md)  | [**currentPlaylist**](axwmplib-axwindowsmediaplayer-currentplaylist--vb-and-c.md), [**newPlaylist**](axwmplib-axwindowsmediaplayer-newplaylist.md)                                                                                                                                                                                                                                                                                                                                                                   |
| [**IWMPPlaylistArray**](iwmpplaylistarray--vb-and-c.md)           | [**Item**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylistarray-item)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**IWMPPlaylistCollection**](iwmpplaylistcollection--vb-and-c.md) | [**newPlaylist**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylistcollection-newplaylist)                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

 





