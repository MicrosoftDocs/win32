---
title: Matching the Windows Media Player Colors
description: Matching the Windows Media Player Colors
ms.assetid: b4d1da08-a4cf-46dd-82a5-40562bb3c049
keywords:
- Windows Media Player online stores,matching Windows Media Player colors
- online stores,matching Windows Media Player colors
- type 1 online stores,matching Windows Media Player colors
- type 2 online stores,matching Windows Media Player colors
- Windows Media Player online stores,Windows Media Player color matching
- online stores,Windows Media Player color matching
- type 1 online stores,Windows Media Player color matching
- type 2 online stores,Windows Media Player color matching
- Windows Media Player online stores,color matching for Windows Media Player
- online stores,color matching for Windows Media Player
- type 1 online stores,color matching for Windows Media Player
- type 2 online stores,color matching for Windows Media Player
- color matching for Windows Media Player
- matching Windows Media Player colors
- Windows Media Player,matching colors
- Windows Media Player,color matching
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Matching the Windows Media Player Colors

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Making your online store webpage match the Windows Media Player color scheme is easy. Simply handle the **External.OnColorChange** event. To specify a function to handle the event, use code like the following when your webpage loads:


```C++
// Set up the color change event.
external.OnColorChange = OnAppColor;
```



Each time the user changes the color scheme of Windows Media Player, the Player will call your function. The following example shows a simple function that sets the webpage background to match the **External.appColorLight** property:


```C++
// Match the current color.
function OnAppColor()
{
    window.document.bgColor = external.appColorLight;
}
```



There are other color properties available for your use as well. See [External Object for Type 2 Online Stores](external-object-for-type-2-online-stores.md).

## Related topics

<dl> <dt>

[**External.appColorLight**](external-appcolorlight.md)
</dt> <dt>

[**External.OnColorChange Event**](external-oncolorchange-event.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




