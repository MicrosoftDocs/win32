---
title: IWMPMetadataPicture (VB and C ) interface (Wmp.h)
description: Provides properties for getting information about the image contained in a digital media file that is represented by a WM/Picturemetadata attribute.
ms.assetid: f8260882-dfb8-4ff0-954c-5060cb7a6995
keywords:
- IWMPMetadataPicture (VB and C ) interface Windows Media Player
- IWMPMetadataPicture (VB and C ) interface Windows Media Player , described
topic_type:
- apiref
api_name:
- IWMPMetadataPicture (VB and C )
api_location:
- wmp.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMetadataPicture (VB and C#) interface

Provides properties for getting information about the image contained in a digital media file that is represented by a [**WM/Picture**](/windows/desktop/wmformat/wmpicture)metadata attribute. This attribute corresponds to album art images contained in a digital media file, not to album art downloaded over the Internet.

The **IWMPMetadataPicture** interface exposes the following properties.



| Property                                                                                   | Description                                                               |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**Description**](wmplibiwmpmetadatapicture-iwmpmetadatapicture-description--vb-and-c.md) | Gets the description of the image represented by the metadata attribute.  |
| [**mimeType**](wmplibiwmpmetadatapicture-iwmpmetadatapicture-mimetype--vb-and-c.md)       | Gets the MIME type of the image represented by the metadata attribute.    |
| [**pictureType**](wmplibiwmpmetadatapicture-iwmpmetadatapicture-picturetype--vb-and-c.md) | Gets the picture type of the image represented by the metadata attribute. |
| [**URL**](wmplibiwmpmetadatapicture-iwmpmetadatapicture-url--vb-and-c.md)                 | Internal use only.                                                        |



 

Get an **IWMPMetadataPicture** interface by passing in the attribute name [**WM/Picture**](/windows/desktop/wmformat/wmpicture) to the following method and casting the object that is returned.



| Interface                                  | Property                                                                             |
|--------------------------------------------|--------------------------------------------------------------------------------------|
| [**IWMPMedia3**](iwmpmedia3--vb-and-c.md) | [**getItemInfoByType**](wmplibiwmpmedia3-iwmpmedia3-getiteminfobytype--vb-and-c.md) |



 

## Members

The **IWMPMetadataPicture (VB and C#)** interface does not define any members.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmp.h</dt> </dl> |



## See also

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> </dl>

 

