---
title: About the MetadataText Object
description: About the MetadataText Object
ms.assetid: 91d74b16-5a34-4ff3-9099-6590b12ed1cb
keywords:
- Windows Media Player,MetadataText object
- Windows Media Player object model,MetadataText object
- object model,MetadataText object
- Windows Media Player ActiveX control,MetadataText object
- ActiveX control,MetadataText object
- Windows Media Player Mobile ActiveX control,MetadataText object
- Windows Media Player Mobile,MetadataText object
- MetadataText object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the MetadataText Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some metadata attributes, such as **WM/Lyrics\_Synchronised**, provide text accompanied by a description of the text. The **MetadataText** object provides a way to retrieve the text and the description separately. When you use *Media*.**getItemInfoByType** to retrieve information about complex textual attributes, you retrieve a **MetadataText** object that has properties, which contain the individual data.

## Related topics

<dl> <dt>

[**MetadataText Object**](metadatatext-object.md)
</dt> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> </dl>

 

 




