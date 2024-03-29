---
title: Nesting Metafiles
description: Nesting Metafiles
ms.assetid: fa355c98-31e2-4bb9-ad67-fd9a727300c3
keywords:
- Windows Media metafiles,nesting
- Windows Media metafiles,referencing other metafiles
- nesting metafiles
- metafiles,nesting
- metafiles,referencing other metafiles
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Nesting Metafiles

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A metafile can reference another metafile. To reference another metafile, use the **ENTRYREF** element. An **ENTRYREF** element in the primary metafile points to an external metafile.

The Windows Media Player control processes the **ENTRY** elements of the referenced metafile as if they were included in the primary metafile at the position of the **ENTRYREF** element. However, it skips any **ENTRY** elements in the referenced metafile that have the **SKIPIFREF** attribute set to YES.

The Windows Media Player 7.0, 7.1, and Windows Media Player for Windows XP controls ignore any **ENTRYREF** elements in the referenced metafile. Thus, metafiles can only be nested one level deep using these versions. These versions also ignore the **ASX** element and its attributes in the referenced file. Windows Media Player 9 Series or later supports nesting metafiles up to 5 deep.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> </dl>

 

 




