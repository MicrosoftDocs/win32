---
title: IWMPQuery (VB and C ) interface (Wmp.h)
description: Represents a compound query.
ms.assetid: b9cfeec9-f928-4b12-88c2-0f78b26f8687
keywords:
- IWMPQuery (VB and C ) interface Windows Media Player
- IWMPQuery (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPQuery (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPQuery (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Represents a compound query.

## Members

The **IWMPQuery (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPQuery (VB and C#)** interface has these methods.



| Method                                                                       | Description                                                            |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**addCondition**](wmplibiwmpquery-iwmpquery-addcondition--vb-and-c.md)     | Adds a condition to the compound query using **AND** logic.<br/> |
| [**beginNextGroup**](wmplibiwmpquery-iwmpquery-beginnextgroup--vb-and-c.md) | Begins a new condition group.<br/>                               |



 

Get an **IWMPQuery** interface by using the following method.



| Interface                                                      | Method                                                  |
|----------------------------------------------------------------|---------------------------------------------------------|
| [**IWMPMediaCollection2**](iwmpmediacollection2--vb-and-c.md) | [**createQuery**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection2-createquery) |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.createQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-createquery--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.getPlaylistByQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-getplaylistbyquery--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.getStringCollectionByQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-getstringcollectionbyquery--vb-and-c.md)
</dt> </dl>

 

 





