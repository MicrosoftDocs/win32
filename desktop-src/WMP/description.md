---
title: Description (Windows Media Player SDK)
description: Description
ms.assetid: '940ef0bf-d651-411a-b36d-99dcc01d8508'
keywords:
- Windows Media Player Mobile skins,Description section
- skins,Description section
- reference for skins,Description section
- Description section in skins
- skin definition files,Description section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Description (Windows Media Player SDK)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you create a skin for Windows Media Player 9 Series for Windows Mobile 2003 or later, you must include a Description section. The Description section enables you to specify the width and height of the display, the display resolution, and the display orientation for which the skin was designed. The Description section must appear in the skin definition file before any other section, and just after the initial version declaration.

The Description section of the skin definition file must begin with the following line:


```C++
[ Description ]

```



You then must add information about the dimensions of the skin and the display resolution. The following example shows how to specify dimensions:


```C++
//              <X,Y>       <DPI>

//              -------     -----

    Dimensions  240,320      96

```



This specifies that you designed the skin to be displayed 240 pixels wide, 320 pixels high, and using 96 DPI display resolution. Note that this implies a portrait mode orientation.

You may optionally specify the orientation mode for which you designed the skin in the description section. The following example shows how to specify orientation:


```C++
//     <Orientation>

//     -------------

    Orientation Portrait

```



The following table lists the values you may use for Orientation.



| Orientation | Description                                                                                                  |
|-------------|--------------------------------------------------------------------------------------------------------------|
| Landscape   | The width of the skin is greater than height of the skin. The display is oriented in a horizontal fashion.   |
| Portrait    | The height of the skin is greater than the width of the skin. The display is oriented in a vertical fashion. |
| Square      | The height of the skin is equal to the width of the skin. The display has no orientation.                    |



 

> [!Note]  
> Windows Media Player 9 Series for Windows Mobile 2003 will only display a particular skin when the description section specified in the skin definition file matches the current state of the device.

 

You should be careful to always specify the correct dimensions, resolution, and orientation for which your skin was authored. For example, if the dimensions specified by your skin describe a landscape orientation, your skin will not be available when the device is in portrait mode, even if you specify Portrait in the orientation line.

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




