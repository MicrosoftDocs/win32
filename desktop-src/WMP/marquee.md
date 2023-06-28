---
title: Marquee
description: Marquee
ms.assetid: 2715732a-25cc-4ba9-9aa6-181ebb9e1d1c
keywords:
- Windows Media Player Mobile skins,marquees
- skins,marquees
- reference for skins,marquees
- marquees in skins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Marquee

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A marquee is a scrolling text display box that displays information from one or more text display boxes. You do not need to add a marquee, but it can be very useful when you have detailed information you want to display to the user in a limited space.

The text in the marquee will scroll only if both of the following conditions are met:

-   You have more text to display in the marquee than the width of the marquee display box.
-   The media item is either stopped or paused.

The Marquee section of the skin definition file must begin with this line:


```C++
[ Marquee ]

```



> [!Note]  
> To maintain compatibility with versions of Windows Media Player Mobile older than Windows Media Player 10 Mobile, using "Marquis" in a skin definition file is still considered valid.

 

You then must add one or more lines that contain information about each of the marquee display boxes in your skin.


```C++
    3,2,234,20   Tahoma,12,N  255,0,0    Playlist, Time, Filename

```



You can use the following template for the Marquee section of your skin definition file:


```C++
//  <Location>   <Font>       <Color>      <Text item combinations>
//  ----------   ------       -------      ------------------------

```



You must use the following order for information in each line of the Marquee section (each part of the line is required):

1.  [Marquee Location](marquee-location.md)
2.  [Marquee Font](marquee-font.md)
3.  [Marquee Color](marquee-color.md)
4.  [Text Combinations](text-combinations.md)

For an example of Marquee code, see [Sample Marquee Section](sample-marquee-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




