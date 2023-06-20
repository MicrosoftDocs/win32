---
title: Hit RGB Color
description: Hit RGB Color
ms.assetid: b71a0a66-11aa-4a21-b78a-3bd90f80a428
keywords:
- Windows Media Player Mobile skins,button colors
- skins,button colors
- reference for skins,buttons
- buttons in skins,colors
- color reference for skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Hit RGB Color

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If you are using region buttons (PushHit, ToggleHit, and 2PushHit), you must define the color that Windows Media Player will use to determine the hit area of your button. This value must be specified using three positive integers separated by commas. These integers represent the amount of red, green, and blue for a bitmap color, and range from 0 to 255.

> [!Note]  
> Buttons types are deprecated in skins for Windows Media Player 10 Mobile or later.

 

You can use any colors for the values, but be sure that each region button you define has a unique color in the Region image file and that the color value you define here as a number matches the actual color used in the Region image.

The following table shows some typical colors you might want to use.



| Value       | Description |
|-------------|-------------|
| 0,0,0       | Black       |
| 255,255,255 | White       |
| 255,0,0     | Red         |
| 0,255,0     | Green       |
| 0,0,255     | Blue        |



 

If you do not use region buttons, you must enter the following:


```C++
0,0,0

```



## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




