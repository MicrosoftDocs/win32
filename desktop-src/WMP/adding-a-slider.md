---
title: Adding a Slider
description: Adding a Slider
ms.assetid: 7062d580-a9d1-4fd7-bc28-db2615464838
keywords:
- creating skins,sliders
- Windows Media Player skins,sliders
- skins,sliders
- sliders in skins
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Slider

You can add a slider to show the current position of the media, and also enable the user to change the position in the current media file.

First you must add the **SLIDER** element:


```C++
<SLIDER
  id = "myslider"
  min = "0"
  max = "wmpprop:player.currentMedia.duration"
  onmouseup = "player.controls.currentPosition = myslider.value; "
  tooltip = "current position"
  height = "10"
  width = "180"
  top = "150"
  left = "88"
  backgroundColor = "red"
  foregroundColor = "blue"
  thumbImage = "thumb.bmp"/>

```



This sets a maximum value based on the duration of the current media file. This uses a tiny thumb image bitmap that is just a 10 pixel by 10 pixel green square. The background of the slider will be red and the foreground will be blue. When the user drags the thumb image to a new position and lets go of the mouse button, the media will change to that position.

But the slider will not move by itself unless you measure the current position with the **currentPosition\_onchange** attribute of the **CONTROLS** element, which is embedded in the **PLAYER** element.


```C++
<PLAYER
    URL = "https://proseware.com/laure.wma">

    <CONTROLS
        currentPosition_onchange = "myslider.value = player.controls.currentPosition; "/>

</PLAYER>

```



When the position of the media changes, this fires an event which then runs the line of code that changes the value of the slider to the current position of the media.

You can see a similar working slider skin in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




