---
title: Creating the Region File
description: Creating the Region File
ms.assetid: e901dfa1-1e06-4136-b877-64be03107f6f
keywords:
- Windows Media Player Mobile skins,Region files
- skins,Region files
- creating skins,Region files
- Region files in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating the Region File

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You will want to create a Region file that shows what areas respond to taps. You can simply copy the base layers of each element to a new layer, and color them to correspond to the color numbers you will use in the skin definition file. Be sure that the images you create in this layer are solid and that no effects are applied. You will probably want to write down the color numbers for each image. You can get the color numbers from the Photoshop Color Picker. You want the RGB numbers, which are three decimal numbers. Each number ranges from 0 to 255. For example, a solid red would be 255, 0, 0.

> [!Note]  
> Region files are not used in Windows Media Player 10 Mobile skins because button types are not supported in Windows Media Player 10 Mobile or later.

 

The following image is the Region file.

![region file](images/ceswmreg.png)

There are only four images in this file because only the PlayPause, Stop, Next, and Prev buttons are hit-type buttons.

## Related topics

<dl> <dt>

[**Creating the Art**](creating-the-art.md)
</dt> </dl>

 

 




