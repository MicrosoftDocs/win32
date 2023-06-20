---
title: IWMPPlaylistArray (VB and C ) interface (Wmp.h)
description: Provides a property and a method for accessing a collection of IWMPPlaylist interfaces by index number.The IWMPPlaylistArray interface exposes the following property.
ms.assetid: 8a7477ee-58c5-41b2-9259-d1976433ae02
keywords:
- IWMPPlaylistArray (VB and C ) interface Windows Media Player
- IWMPPlaylistArray (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPPlaylistArray (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPPlaylistArray (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a property and a method for accessing a collection of **IWMPPlaylist** interfaces by index number.

The **IWMPPlaylistArray** interface exposes the following property.

## Members

The **IWMPPlaylistArray (VB and C#)** interface has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IWMPPlaylistArray (VB and C#)** interface has these methods.



| Method                                                                   | Description                                                                                        |
|:-------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Item**](wmplibiwmpplaylistarray-iwmpplaylistarray-item--vb-and-c.md) | Returns an **IWMPPlaylist** interface representing the playlist at the specified index.<br/> |



 

### Properties

The **IWMPPlaylistArray (VB and C#)** interface has these properties.



| Property                                                                              | Access type          | Description                                                   |
|:--------------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------|
| [**count**](wmplibiwmpplaylistarray-iwmpplaylistarray-count--vb-and-c.md)<br/> | Read-only<br/> | Gets the number of playlists in the playlist array<br/> |



 

Get an **IWMPPlaylistArray** interface by using the following methods.



| Interface                                                      | Method                                                                                                                                                                               |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IWMPPlaylistCollection](iwmpplaylistcollection--vb-and-c.md) | [**getAll**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getall--vb-and-c.md), [**getByName**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getbyname--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> </dl>

 

 





