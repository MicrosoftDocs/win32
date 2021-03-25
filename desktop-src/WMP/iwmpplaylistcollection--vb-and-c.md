---
title: IWMPPlaylistCollection (VB and C ) interface (Wmp.h)
description: Provides methods for manipulating IWMPPlaylist and IWMPPlaylistArray interfaces in a collection.
ms.assetid: 19a4e0d7-cb3f-42ec-9acb-7ac0c5837662
keywords:
- IWMPPlaylistCollection (VB and C ) interface Windows Media Player
- IWMPPlaylistCollection (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPPlaylistCollection (VB and C )
- IWMPPlaylistCollection (VB and C ).setDeleted
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPPlaylistCollection (VB and C#) interface

Provides methods for manipulating **IWMPPlaylist** and **IWMPPlaylistArray** interfaces in a collection.

## Members

The **IWMPPlaylistCollection (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPPlaylistCollection (VB and C#)** interface has these methods.



| Method                                                                                                 | Description                                                                                                                    |
|:-------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**getAll**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getall--vb-and-c.md)                 | Returns an **IWMPPlaylistArray** interface that provides access to all of the playlists in the library.<br/>             |
| [**getByName**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getbyname--vb-and-c.md)           | Returns an **IWMPPlaylistArray** interface that provides access to playlists with the specified name, if any exist.<br/> |
| [**importPlaylist**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-importplaylist--vb-and-c.md) | Adds a static playlist to the library.<br/>                                                                              |
| [**isDeleted**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-isdeleted--vb-and-c.md)           | Returns a value indicating whether the specified playlist is in the deleted items folder.<br/>                           |
| [**newPlaylist**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-newplaylist--vb-and-c.md)       | Returns an **IWMPPlaylist** interface for a new, empty playlist in the library.<br/>                                     |
| [**remove**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-remove--vb-and-c.md)                 | Removes a playlist from the library.<br/>                                                                                |
| **setDeleted**                                                                                         | No longer supported.<br/>                                                                                                |



 

Get an **IWMPPlaylistCollection** interface by using the following property.



| Object                                                                   | Property                                                                                 |
|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [AxWindowsMediaPlayer Object](axwindowsmediaplayer-object--vb-and-c.md) | [**playlistCollection**](axwmplib-axwindowsmediaplayer-playlistcollection--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistArray Interface (VB and C#)**](iwmpplaylistarray--vb-and-c.md)
</dt> </dl>

 

 





