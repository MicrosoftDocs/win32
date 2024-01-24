---
title: MetadataText Object
description: The MetadataText object provides a way to retrieve metadata for complex textual metadata attributes.
ms.assetid: 'cf8e4524-6fc5-4534-9542-6bdc7d34bca4'
keywords:
- MetadataText Object Windows Media Player
topic_type:
- apiref
api_name:
- MetadataText Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MetadataText Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **MetadataText** object provides a way to retrieve metadata for complex textual metadata attributes.

The **MetadataText** object supports the following properties.



| Property                                    | Description                                   |
|---------------------------------------------|-----------------------------------------------|
| [description](metadatatext-description.md) | Retrieves a description of the metadata text. |
| [text](metadatatext-text.md)               | Retrieves the metadata text.                  |



 

The **MetadataText** object is accessed through the following method.



| Object                    | Method                                           |
|---------------------------|--------------------------------------------------|
| [Media](media-object.md) | [getItemInfoByType](media-getiteminfobytype.md) |



 

For purposes of illustration, *player*.*currentMedia*.**getItemInfoByType**(*name*, *language*, *index*) is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




