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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding Video

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




