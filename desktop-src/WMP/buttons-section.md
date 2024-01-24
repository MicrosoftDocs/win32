---
title: Buttons Section
description: Buttons Section
ms.assetid: fa413bb4-e04a-4e3d-9754-cd4c2d82de6e
keywords:
- Windows Media Player Mobile skins,Buttons section
- skins,Buttons section
- creating skins,Buttons section
- writing code for skins,Buttons section
- buttons in skins,Buttons section
- skin definition files,Buttons section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Buttons Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Next, you must define the buttons you will be using:


```C++
[ Buttons ]

//  <Function> <Type>     <Location>     <Push Image Src>  <Dis Image Src>    <Hit R,G,B>  <Norm 2 Image Src>  <Push 2 Image Src>
//  ---------- ------     ----------     ----------------  ---------------    -----------  ------------------  ------------------
    PlayPause  2PushHit   100,20,110,100 Pushed @ 100,20   Disabled @ 100,20    0,255,255  Pushed @ 270,20     Pushed @ 270,130
    Stop       PushHit    20,20,45,45    Pushed @ 20,20    Disabled @ 20,20   255,255,  0
    Next       PushHit    20,80,45,45    Pushed @ 20,80    Disabled @ 20,80   255,  0,  0
    Prev       PushHit    20,140,45,45   Pushed @ 20,140   Disabled @ 20,130    0,  0,255

```



There are four buttons defined in this section. The page you are viewing may wrap these lines, but when you type in the code, you must not wrap lines; that is, each line must be complete and end with a paragraph mark.

> [!Note]  
> Buttons types are deprecated in Windows Media Player 10 Mobile or later skins. Instead of a button type declared in your skin file, enter "NA" for each type.

 

For each button you must define the function, type, location, pushed image source, disabled source, and color (for hit-type buttons). In addition, for the PlayPause button, you must define the normal and pushed image sources for the paused state.

For more about the Buttons section of the skin definition file, see [Buttons](buttons.md) in the Skin Reference.

## Related topics

<dl> <dt>

[**Writing the Code**](writing-the-code.md)
</dt> </dl>

 

 




