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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMetadataPicture (VB and C#) interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

