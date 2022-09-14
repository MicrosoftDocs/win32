---
title: IWMPMediaCollection2 (VB and C ) interface (Wmp.h)
description: Provides methods that supplement the IWMPMediaCollection interface.
ms.assetid: 204f336c-ea78-43d4-9686-bcab72362bc9
keywords:
- IWMPMediaCollection2 (VB and C ) interface Windows Media Player
- IWMPMediaCollection2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMediaCollection2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection2 (VB and C#) interface

Provides methods that supplement the **IWMPMediaCollection** interface.

## Members

The **IWMPMediaCollection2 (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPMediaCollection2 (VB and C#)** interface has these methods.



| Method                                                                                                                     | Description                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**createQuery**](wmplibiwmpmediacollection2-iwmpmediacollection2-createquery--vb-and-c.md)                               | Returns an **IWMPQuery** interface that represents a new query.<br/>                                                                                               |
| [**getByAttributeAndMediaType**](wmplibiwmpmediacollection2-iwmpmediacollection2-getbyattributeandmediatype--vb-and-c.md) | Returns an **IWMPPlaylist** interface that provides access to media items that have a specified attribute and media type.<br/>                                     |
| [**getPlaylistByQuery**](wmplibiwmpmediacollection2-iwmpmediacollection2-getplaylistbyquery--vb-and-c.md)                 | Returns an **IWMPPlaylist** interface that provides access to media items that match the query conditions.<br/>                                                    |
| [**getStringCollectionByQuery**](wmplibiwmpmediacollection2-iwmpmediacollection2-getstringcollectionbyquery--vb-and-c.md) | Returns an **IWMPStringCollection** interface that provides access to the set of all string values for a specified attribute that match the query conditions.<br/> |



 

Get an **IWMPMediaCollection2** interface by casting the value returned by the [**AxWindowsMediaPlayer.mediaCollection**](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md) property or the value returned by the [**IWMPLibrary.mediaCollection**](wmplibiwmplibrary-iwmplibrary-mediacollection--vb-and-c.md) property.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> </dl>

 

 





