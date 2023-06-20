---
title: VIDEOSETTINGS Element
description: VIDEOSETTINGS Element
ms.assetid: 2d147bd2-0010-41ab-8073-a4dc2979be1e
keywords:
- Windows Media Player skins,VIDEOSETTINGS element
- skins,VIDEOSETTINGS element
- VIDEOSETTINGS element
- reference for skins,VIDEOSETTINGS element
- elements,VIDEOSETTINGS
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIDEOSETTINGS Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **VIDEOSETTINGS** element provides a way to modify various video settings, using the attributes and method listed here.

The **VIDEOSETTINGS** element supports the following attributes.



| Attribute                                  | Description                                                 |
|--------------------------------------------|-------------------------------------------------------------|
| [brightness](videosettings-brightness.md) | Specifies or retrieves the brightness setting of the video. |
| [contrast](videosettings-contrast.md)     | Specifies or retrieves the contrast setting of the video.   |
| [hue](videosettings-hue.md)               | Specifies or retrieves the hue setting of the video.        |
| [saturation](videosettings-saturation.md) | Specifies or retrieves the saturation setting of the video. |



 

The **VIDEOSETTINGS** element supports the following method.



| Method                           | Description                                    |
|----------------------------------|------------------------------------------------|
| [reset](videosettings-reset.md) | Resets all attributes to their default values. |



 

The **VIDEOSETTINGS** element can implement the [attribute\_onchange](attribute-onchange.md) event handlers.

> [!Note]  
> This element requires Windows Media Player for Windows XP or later.

 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




