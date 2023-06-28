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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MetadataPicture Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 