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
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Nesting Metafiles

A metafile can reference another metafile. To reference another metafile, use the **ENTRYREF** element. An **ENTRYREF** element in the primary metafile points to an external metafile.

The Windows Media Player control processes the **ENTRY** elements of the referenced metafile as if they were included in the primary metafile at the position of the **ENTRYREF** element. However, it skips any **ENTRY** elements in the referenced metafile that have the **SKIPIFREF** attribute set to YES.

The Windows Media Player 7.0, 7.1, and Windows Media Player for Windows XP controls ignore any **ENTRYREF** elements in the referenced metafile. Thus, metafiles can only be nested one level deep using these versions. These versions also ignore the **ASX** element and its attributes in the referenced file. Windows Media Player 9 Series or later supports nesting metafiles up to 5 deep.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> </dl>

 

 




