---
title: Media Object
description: The Media object provides a way to specify or retrieve properties of a media item, using the following properties and methods.
ms.assetid: 45c1c760-808b-4d11-8e6b-057a2ca685d0
keywords:
- Media Object Windows Media Player
topic_type:
- apiref
api_name:
- Media Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Media Object

The **Media** object provides a way to specify or retrieve properties of a media item, using the following properties and methods.

The **Media** object supports the following properties.



| Property                                         | Description                                                                                        |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [attributeCount](media-attributecount.md)       | Retrieves the number of attributes that can be queried and/or set for the media item.              |
| [duration](media-duration.md)                   | Retrieves the duration in seconds of the current media item.                                       |
| [durationString](media-durationstring.md)       | Retrieves a **String** value indicating the duration of the current media item in HH:MM:SS format. |
| [error](media-error.md)                         | Retrieves an [ErrorItem](erroritem-object.md) object if the media item has an error condition.    |
| [imageSourceHeight](media-imagesourceheight.md) | Retrieves the height of the current media item in pixels.                                          |
| [imageSourceWidth](media-imagesourcewidth.md)   | Retrieves the width of the current media item in pixels.                                           |
| [markerCount](media-markercount.md)             | Retrieves the number of markers in the media item.                                                 |
| [name](media-name.md)                           | Specifies or retrieves the name of the media item.                                                 |
| [sourceURL](media-sourceurl.md)                 | Retrieves the URL of the media item.                                                               |



 

The **Media** object supports the following methods.



| Method                                                       | Description                                                                                              |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [getAttributeCountByType](media-getattributecountbytype.md) | Retrieves the number of attributes associated with the specified attribute name and language.            |
| [getAttributeName](media-getattributename.md)               | Retrieves the name of the attribute corresponding to the specified index.                                |
| [getItemInfo](media-getiteminfo.md)                         | Retrieves the value of the specified attribute for the media item.                                       |
| [getItemInfoByAtom](media-getiteminfobyatom.md)             | Retrieves the value of the attribute with the specified index number.                                    |
| [getItemInfoByType](media-getiteminfobytype.md)             | Retrieves the value of the attribute corresponding to the specified attribute name, language, and index. |
| [getMarkerName](media-getmarkername.md)                     | Retrieves the name of the marker at the specified index.                                                 |
| [getMarkerTime](media-getmarkertime.md)                     | Retrieves the time of the marker at the specified index.                                                 |
| [isIdentical](media-isidentical.md)                         | Retrieves a value indicating whether the supplied object is the same as the current one.                 |
| [isMemberOf](media-ismemberof.md)                           | Retrieves a value indicating whether the specified media item is a member of the specified playlist.     |
| [isReadOnlyItem](media-isreadonlyitem.md)                   | Retrieves a value indicating whether the attributes of the specified media item can be edited.           |
| [setItemInfo](media-setiteminfo.md)                         | Sets the value of the specified attribute for the media item.                                            |



 

The **Media** object is accessed through the following properties and methods.



| Object                          | Property or method                                                       |
|---------------------------------|--------------------------------------------------------------------------|
| [Controls](controls-object.md) | [currentItem](controls-currentitem.md)                                  |
| [Player](player-object.md)     | [currentMedia](player-currentmedia.md), [newMedia](player-newmedia.md) |
| [Playlist](playlist-object.md) | [item](playlist-item.md)                                                |



 

Because it is the most common means of access, *player*.**currentMedia** is used for purposes of illustration in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




