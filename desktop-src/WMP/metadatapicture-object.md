---
title: MetadataPicture Object
description: The MetadataPicture object provides a way to retrieve the values of the WM/Picture metadata attribute. This attribute corresponds to album art contained in a digital media file, not to album art downloaded over the Internet.
ms.assetid: 'c0d6f43d-1a88-4ac2-a7b3-c502f4d57afb'
keywords:
- MetadataPicture Object Windows Media Player
topic_type:
- apiref
api_name:
- MetadataPicture Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# MetadataPicture Object

The **MetadataPicture** object provides a way to retrieve the values of the [**WM/Picture**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_picture) metadata attribute. This attribute corresponds to album art contained in a digital media file, not to album art downloaded over the Internet.

The **MetadataPicture** object supports the following properties.



| Property                                           | Description                                       |
|----------------------------------------------------|---------------------------------------------------|
| [**description**](metadatapicture-description.md) | Retrieves a description of the metadata image.    |
| [**mimeType**](metadatapicture-mimetype.md)       | Retrieves the MIME type of the metadata image.    |
| [**pictureType**](metadatapicture-picturetype.md) | Retrieves the picture type of the metadata image. |
| [**URL**](metadatapicture-url.md)                 | Internal use only.                                |



 

The **MetadataPicture** object is accessed through the following method.



| Object                        | Method                                               |
|-------------------------------|------------------------------------------------------|
| [**Media**](media-object.md) | [**getItemInfoByType**](media-getiteminfobytype.md) |



 

For purposes of illustration, `player.currentMedia.getItemInfoByType(name, language, index)` is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 