---
title: MediaCollection.getByAttributeAndMediaType method
description: The getByAttributeAndMediaType method retrieves a Playlist object containing Media objects having the specified attribute and media type.
ms.assetid: 75241b38-ae0e-4216-b405-af9a9c71f5ec
keywords:
- getByAttributeAndMediaType method Windows Media Player
- getByAttributeAndMediaType method Windows Media Player , MediaCollection class
- MediaCollection class Windows Media Player , getByAttributeAndMediaType method
topic_type:
- apiref
api_name:
- MediaCollection.getByAttributeAndMediaType
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MediaCollection.getByAttributeAndMediaType method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getByAttributeAndMediaType** method retrieves a **Playlist** object containing **Media** objects having the specified attribute and media type.

## Syntax


```JScript
retVal = MediaCollection.getByAttributeAndMediaType(
  attribute,
  value,
  mediaType
)
```



## Parameters

<dl> <dt>

*attribute* \[in\]
</dt> <dd>

**String** containing the attribute.

</dd> <dt>

*value* \[in\]
</dt> <dd>

**String** containing the value.

</dd> <dt>

*mediaType* \[in\]
</dt> <dd>

**String** containing the media type. Must contain one of the following values: "audio", "video", "photo", "playlist", or "other".

</dd> </dl>

## Return value

This method returns a **Playlist** object

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 





