---
title: IWMPMediaCollection (VB and C ) interface (Wmp.h)
description: Provides methods that can be used to organize a large collection of media items.
ms.assetid: a9e3d466-7dcf-4f1b-ba6f-9d166a35f03d
keywords:
- IWMPMediaCollection (VB and C ) interface Windows Media Player
- IWMPMediaCollection (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMediaCollection (VB and C )
- IWMPMediaCollection (VB and C ).isDeleted
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection (VB and C#) interface

Provides methods that can be used to organize a large collection of media items.

## Members

The **IWMPMediaCollection (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPMediaCollection (VB and C#)** interface has these methods.



| Method                                                                                                                       | Description                                                                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**add**](wmplibiwmpmediacollection-iwmpmediacollection-add--vb-and-c.md)                                                   | Adds a new media item or playlist to the library.<br/>                                                                                  |
| [**getAll**](wmplibiwmpmediacollection-iwmpmediacollection-getall--vb-and-c.md)                                             | Returns an **IWMPPlaylist** interface that corresponds to the playlist that contains all media items in the library.<br/>               |
| [**getAttributeStringCollection**](wmplibiwmpmediacollection-iwmpmediacollection-getattributestringcollection--vb-and-c.md) | Returns an **IWMPStringCollection** interface that represents the set of all values for a specified attribute within a media type.<br/> |
| [**getByAlbum**](wmplibiwmpmediacollection-iwmpmediacollection-getbyalbum--vb-and-c.md)                                     | Returns an **IWMPPlaylist** interface that provides access to media items from the specified album.<br/>                                |
| [**getByAttribute**](wmplibiwmpmediacollection-iwmpmediacollection-getbyattribute--vb-and-c.md)                             | Returns an **IWMPPlaylist** interface that corresponds to the specified attribute having the specified value.<br/>                      |
| [**getByAuthor**](wmplibiwmpmediacollection-iwmpmediacollection-getbyauthor--vb-and-c.md)                                   | Returns an **IWMPPlaylist** interface that provides access to the media items by the specified author.<br/>                             |
| [**getByGenre**](wmplibiwmpmediacollection-iwmpmediacollection-getbygenre--vb-and-c.md)                                     | Returns an **IWMPPlaylist** interface that provides access to media items of the specified genre.<br/>                                  |
| [**getByName**](wmplibiwmpmediacollection-iwmpmediacollection-getbyname--vb-and-c.md)                                       | Returns an **IWMPPlaylist** interface that provides access to media items with the specified name.<br/>                                 |
| [**getMediaAtom**](wmplibiwmpmediacollection-iwmpmediacollection-getmediaatom--vb-and-c.md)                                 | Returns the index of a specified attribute.<br/>                                                                                        |
| **isDeleted**                                                                                                                | No longer supported.<br/>                                                                                                               |
| [**remove**](wmplibiwmpmediacollection-iwmpmediacollection-remove--vb-and-c.md)                                             | Removes the specified media item from the media collection.<br/>                                                                        |
| [**setDeleted**](wmplibiwmpmediacollection-iwmpmediacollection-setdeleted--vb-and-c.md)                                     | Moves the specified media item to the deleted items folder.<br/>                                                                        |



 

Get an **IWMPMediaCollection** interface by using the following properties accessed through the following object or interface.



| Object or interface                                               | Property                                                                           |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md) | [**mediaCollection**](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md) |
| [**IWMPLibrary**](iwmplibrary--vb-and-c.md)                      | [**mediaCollection**](wmplibiwmplibrary-iwmplibrary-mediacollection--vb-and-c.md) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2 Interface**](iwmpmediacollection2--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> </dl>

 

 





