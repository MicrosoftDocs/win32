---
title: Mapping Images
description: Mapping Images
ms.assetid: ecdee7ec-f9a6-4d6f-845f-8706a2e29376
keywords:
- Windows Media Player skins,art files
- skins,art files
- files for skins,art
- art files for skins,mapping images
- Windows Media Player skins,mapping images
- skins,mapping images
- mapping images in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Mapping Images

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Mapping images are used for specific controls to specify which regions will respond to mouse clicks and to determine which controls receive which events. The mapping image must be the same height and width as the primary image and should be created so that the images in both files line up exactly. For this reason, a graphics editing program that supports layers is recommended because you can be certain your images are perfectly aligned.

Different controls require different types of mapping. A **ButtonElement** element needs a map that has a different color for each button. The colored areas in the mapping file must correspond to the areas of the buttons you want to map.

## Related topics

<dl> <dt>

[**Art Files**](art-files.md)
</dt> </dl>

 

 




