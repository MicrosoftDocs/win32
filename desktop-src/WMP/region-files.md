---
title: Region Files
description: Region Files
ms.assetid: 20952eb9-4cd1-4d7d-b5cc-f1741977745f
keywords:
- Windows Media Player Mobile skins,art files
- skins,art files
- files for skins,art
- art files for skins,Region files
- Windows Media Player Mobile skins,Region files
- skins,Region files
- Region files in skins
ms.topic: article
ms.date: 05/31/2018
---

# Region Files

Region files are required if you use any type of hit button (2PushHit, PushHit, or ToggleHit).

Region files are used to define areas that will respond to a tap, also known as a hit, on a specific button. For each hit button, an area in the Region bitmap is given a specific Web color (such as \#FF0000, which is the value for solid red). The color number is specified in the region button definition. When the user displays the skin, the button image is superimposed onto the background using the coordinates of the area in the Region bitmap.

For example, you could draw a red circle in a location corresponding to the location of the Next button and color it solid red (\#FF0000). Then in the button definition, you could assign a hit RGB value of 255,0,0 (which is the RGB equivalent of \#FF0000). In this case, the Next button would only respond to taps (hits) inside the red circle.

Hit buttons are used when you want to define shapes other than rectangles. You must still define the coordinates for each button so that secondary images such as Pushed and Disabled can be located correctly. In practice, each button is bounded by a rectangle, and these imaginary boundary rectangles must not overlap.

> [!Note]  
> Region art files are not needed in Windows Media Player 10 Mobile skins because button types are not supported in Windows Media Player 10 Mobile or later.

 

The following image is a typical Region file.

![region file](images/cesdkreg.png)

This file defines the parts of the skin for each hit-type button. Each color will be identified by its color number in the Buttons section of the skin definition file.

## Related topics

<dl> <dt>

[**Art Files**](art-files-mobile.md)
</dt> </dl>

 

 




