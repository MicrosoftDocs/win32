---
title: Creating Custom Sliders
description: Creating Custom Sliders
ms.assetid: eb26ba44-a891-4cb6-be74-5acf881e896f
keywords:
- creating skins,sliders
- Windows Media Player skins,sliders
- skins,sliders
- sliders in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Custom Sliders

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can create custom sliders in any shape you want. For this example, a simple strip is chosen, but the actual shape can be anything. Here is the code for the **CUSTOMSLIDER** element:


```C++
<CustomSlider 
  top="160"
  left="130"
  min="0"
  max="100"
  toolTip="volume control"
  image="slider.bmp"
  positionImage="graymap.bmp"
  enabled="true"
  value="wmpprop:player.settings.volume"
  value_onchange="player.settings.volume = value" />

```



This sets up an initial value for the slider. Two new bitmaps are introduced. One is the grayscale bitmap (slider.bmp) that defines which values will be used when clicked on, and the other (slider.bmp) that determines which image will be shown when a particular portion of the grayscale is clicked on.

The initial value is determined by listening to the volume with wmpprop and then the volume can be changed when the user clicks on a portion of the slider that triggers a change in value.

You can see a similar working slider skin in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




