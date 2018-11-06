---
title: Sample Button Section
description: Sample Button Section
ms.assetid: 52358f83-8c74-4957-87c4-ca1ed7f667fc
keywords:
- Windows Media Player Mobile skins,Button section
- skins,Button section
- reference for skins,Button section
- buttons in skins,Button section
- skin definition files,Button section
ms.topic: article
ms.date: 05/31/2018
---

# Sample Button Section

The following lines show a typical Buttons section of a skin definition file:


```C++
[ Buttons ]

//  <Function> <Type>     <Location>     <Push Image Src>  <Dis Image Src>    <Hit R,G,B>  <Norm 2 Image Src>  <Push 2 Image Src>
//  ---------- ------     ----------     ----------------  ---------------    -----------  ------------------  ------------------
    PlayPause  2PushHit   84,99,67,67   Pushed @ 44,50    Disabled @ 44,50     0,255,255  Pushed @ 160,5      Pushed @ 160,98
    Info       PushHit    97,49,43,43    Pushed @ 57,0     Disabled @ 57,0      0,  0,  0
    Stop       PushHit    97,173,43,43   Pushed @ 57,124   Disabled @ 57,124  255,255,  0
    Prev       PushHit    40,83,43,43    Pushed @ 0,34     Disabled @ 0,34      0,  0,255
    Next       PushHit    153,83,43,43   Pushed @ 113,34   Disabled @ 113,34  255,  0,  0
    Shuffle    ToggleHit  40,136,43,43   Pushed @ 0,87     Disabled @ 0,87      0,255,  0
    Repeat     ToggleHit  153,136,43,43  Pushed @ 113,87   Disabled @ 113,87  255,  0,255
    Mute       Toggle     5,220,24,23    Super @ 247,29    Super @ 4,28         0,  0,  0

```



This code defines eight buttons that are used to provide all of the following functions in a skin:

-   Play, pause, and stop media items.
-   Shuffle, repeat, and move through the playlist.
-   Mute the volume.

All the buttons except the mute button are region buttons. The mute button gets its Pushed and Disabled images from the Super bitmap for convenience.

> [!Note]  
> Buttons types are deprecated in skins for Windows Media Player 10 Mobile or later. Instead of a button type declared in your skin file, enter "NA" for each type.

 

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




