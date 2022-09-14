---
title: Adding Video
description: Adding Video
ms.assetid: 6f20a9ad-e92e-4774-868d-ad0e071f4935
keywords:
- creating skins,video
- Windows Media Player skins,video
- skins,video
- video in skins,adding
ms.topic: article
ms.date: 05/31/2018
---

# Adding Video

You can add a video to your file by simply using the **VIDEO** element and defining where you want the video window to be placed.

Use the same code as you did in the Choosing Files section; all you need to do is add the **VIDEO** element with the top, left, width, and height attributes.


```C++
        <VIDEO
            top = "10"
            left = "80"
            width = "180"
            height = "180"/>

```



Then when you play a video, it will be displayed in the window. The art for the video sample was modified to make a slightly larger skin. Because layers were used in Photoshop, the buttons were easily moved around and a new set was created very quickly. Only the background image was changed. A fill was used in a blank layer and a bevel and emboss effect was added.

You can see a similar working video skin in the sample section of the SDK.

## Related topics

<dl> <dt>

[**Skin Creation Guide**](skin-creation-guide.md)
</dt> </dl>

 

 




