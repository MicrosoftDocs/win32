---
title: IWMPMedia2 (VB and C ) interface (Wmp.h)
description: Provides access to an additional media item property.
ms.assetid: 7d9f8304-ae26-4175-b9d4-9f272861ef87
keywords:
- IWMPMedia2 (VB and C ) interface Windows Media Player
- IWMPMedia2 (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMedia2 (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia2 (VB and C#) interface

Provides access to an additional media item property.

In addition to the properties and methods inherited from **IWMPMedia**, the **IWMPMedia2** interface exposes the following property.



| Property                                                 | Description                                                                   |
|----------------------------------------------------------|-------------------------------------------------------------------------------|
| [Error](wmplibiwmpmedia2-iwmpmedia2-error--vb-and-c.md) | Gets an **IWMPErrorItem** interface if the media item has an error condition. |



 

Get an **IWMPMedia2** interface by casting the value returned by one of the following properties or methods accessed through the following object or interface.



| Object or interface                                               | Property or method                                                                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [IWMPControls](iwmpcontrols--vb-and-c.md)                        | [currentItem](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)                                                          |
| [AxWindowsMediaPlayer](axwindowsmediaplayer-object--vb-and-c.md) | [currentMedia](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md) , [newMedia](axwmplib-axwindowsmediaplayer-newmedia.md) |
| [IWMPPlaylist](iwmpplaylist--vb-and-c.md)                        | [Item](iwmpplaylist-item--vb-and-c.md) ( **get\_Item** in C#)                                                                   |



 

## Members

The **IWMPMedia2 (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPErrorItem (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMedia3 Interface (VB and C#)**](iwmpmedia3--vb-and-c.md)
</dt> </dl>

 

 





