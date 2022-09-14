---
title: Adding Visualizations
description: Adding Visualizations
ms.assetid: adb5d10b-070c-426c-a74a-8d4881d9acbf
keywords:
- creating skins,visualizations
- Windows Media Player skins,visualizations
- skins,visualizations
- visualizations,skins
ms.topic: article
ms.date: 05/31/2018
---

# Adding Visualizations

You can add a visualization window the same way you added a video window. The same skin can be used, but an **EFFECTS** element is used.

First you must add the **EFFECTS** element and give it an ID and size:


```C++
       <EFFECTS
            id = "myeffects"
            top = "25"
            left = "88"
            width = "180"
            height = "150"/>

```



Then you can assign the two buttons a previous and next visualization code string:


```C++
        <BUTTONELEMENT
            mappingColor = "#00FF00"
            upToolTip = "Next"
            onClick = "JScript:myeffects.next(); " />
                          
        <BUTTONELEMENT
            mappingColor = "#FF0000"
            upToolTip = "Previous"
            onClick = "JScript:myeffects.previous(); " />

```



The layers and bitmaps were the same ones used in the video example, except that the play arrow was copied and flipped horizontally.

Finally, a simple **PLAYER** element with the **URL** attribute was added to choose a song to play.


```C++
      <PLAYER
          URL = "https://proseware.com/mellow.wma">
      </PLAYER>

```



You can see a similar working visualization skin in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




