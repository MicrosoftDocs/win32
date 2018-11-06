---
title: Listening Attributes
description: Listening Attributes
ms.assetid: 51b10507-5c2e-49ca-b560-6db6a1a7ee87
keywords:
- Windows Media Player skins,listening attributes
- skins,listening attributes
- reference for skins,listening attributes
- listening attributes
- attributes,listening
ms.topic: article
ms.date: 05/31/2018
---

# Listening Attributes

A listening attribute is used to connect one attribute to another so that its value changes every time the value of the other attribute changes.

The listening attribute **wmpprop:** is the most useful. If the value of one attribute is specified to be the **wmpprop:** of a second attribute, the first value will be automatically updated to reflect the second value each time the second value changes.

**Example:**


```C++
<TEXT
  value="wmpprop:mySlider.value"
/>

```



In this way, the value of mySlider, shown by the position of the slider control, can also be shown as a number within a text box.

The two other listening attributes, **wmpenabled:** and **wmpdisabled:**, can be used to change the **enabled** attribute of a control depending on whether its functionality is currently available in the player. These attributes can listen only to methods of the **Controls** object.

**Example:**


```C++
<BUTTON 
  id="play" 
  enabled="wmpenabled:player.controls.play"
/>

```



## Related topics

<dl> <dt>

[**Miscellaneous**](miscellaneous.md)
</dt> </dl>

 

 




