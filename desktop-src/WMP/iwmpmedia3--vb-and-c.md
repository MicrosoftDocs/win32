---
title: IWMPMedia3 (VB and C ) interface (Wmp.h)
description: Provides additional methods to access the properties of a media item.
ms.assetid: e16aa5e2-ae44-41c2-8c61-fb688c2e89e2
keywords:
- IWMPMedia3 (VB and C ) interface Windows Media Player
- IWMPMedia3 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMedia3 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia3 (VB and C#) interface

Provides additional methods to access the properties of a media item.

## Members

The **IWMPMedia3 (VB and C#)** interface has these types of members:

-   [Methods](#methods)

### Methods

The **IWMPMedia3 (VB and C#)** interface has these methods.



| Method                                                                                           | Description                                                                                            |
|:-------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**getAttributeCountByType**](wmplibiwmpmedia3-iwmpmedia3-getattributecountbytype--vb-and-c.md) | Returns the number of attributes associated with the specified attribute type.<br/>              |
| [**getItemInfoByType**](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md)             | Returns the value of the attribute corresponding to the specified attribute type and index.<br/> |



 

Get an **IWMPMedia3** interface by casting the value returned by one of the following properties or methods accessed through the following object or interface.



| Object or interface                                               | Property or method                                                                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [IWMPControls](iwmpcontrols--vb-and-c.md)                        | [currentItem](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)                                                          |
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md) | [currentMedia](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md) , [newMedia](axwmplib-axwindowsmediaplayer-newmedia.md) |
| [IWMPPlaylist](iwmpplaylist--vb-and-c.md)                        | [Item](iwmpplaylist-item--vb-and-c.md) ( **get\_Item** in C#)                                                                   |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMedia2 Interface (VB and C#)**](iwmpmedia2--vb-and-c.md)
</dt> </dl>

 

 





