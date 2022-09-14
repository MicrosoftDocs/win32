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
ms.date: 05/31/2018
---

# Creating Custom Sliders

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

 

 




