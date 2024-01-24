---
title: EFFECTS Element
description: EFFECTS Element
ms.assetid: ada3c452-1bc6-4700-8048-1a4b2ee00aeb
keywords:
- Windows Media Player skins,EFFECTS element
- skins,EFFECTS element
- EFFECTS element
- reference for skins,EFFECTS element
- elements,EFFECTS
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# EFFECTS Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **EFFECTS** element provides a way to organize and manipulate visualizations by using the following attributes and methods. A predefined **EFFECTS** element is also provided for convenience.

The **EFFECTS** element supports the following attributes.



| Attribute                                                        | Description                                                                                                                                                                                                                                          |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [allowAll](effects-allowall.md)                                 | Specifies or retrieves a value indicating whether to include all the visualizations in the registry.                                                                                                                                                 |
| [currentEffect](effects-currenteffect.md)                       | Specifies or retrieves the current visualization.                                                                                                                                                                                                    |
| [currentEffectPresetCount](effects-currenteffectpresetcount.md) | Retrieves number of available presets for the current visualization.                                                                                                                                                                                 |
| [currentEffectTitle](effects-currenteffecttitle.md)             | Retrieves the display title of the current visualization.                                                                                                                                                                                            |
| [currentEffectType](effects-currenteffecttype.md)               | Retrieves the registry name of the current visualization.                                                                                                                                                                                            |
| [currentPreset](effects-currentpreset.md)                       | Specifies or retrieves the current preset of the current visualization.                                                                                                                                                                              |
| [currentPresetTitle](effects-currentpresettitle.md)             | Retrieves the title of the current preset of the current visualization.                                                                                                                                                                              |
| [effectCanGoFullScreen](effects-effectcangofullscreen.md)       | Retrieves a value indicating whether the current visualization can be displayed full-screen.                                                                                                                                                         |
| [effectCount](effects-effectcount.md)                           | Retrieves the number of visualizations available.                                                                                                                                                                                                    |
| [effectHasPropertyPage](effects-effecthaspropertypage.md)       | Retrieves a value indicating whether the current visualization has a property page.                                                                                                                                                                  |
| [fullScreen](effects-fullscreen.md)                             | Specifies or retrieves a value indicating whether the current visualization is displayed full-screen. Can only be set at run time.                                                                                                                   |
| [windowed](effects-windowed.md)                                 | Specifies or retrieves a value indicating whether the visualization will be windowed or windowless, that is, whether the entire rectangle of the control will be visible at all times, or whether it can be clipped. Can only be set at design time. |



 

The **EFFECTS** element supports the following methods.



| Method                                       | Description                                                                                                       |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [effectTitle](effects-effecttitle.md)       | Retrieves the friendly name of the visualization with the specified registry index.                               |
| [effectType](effects-effecttype.md)         | Retrieves the registry name of the visualization with the specified registry index.                               |
| [next](effects-next.md)                     | Displays the next visualization preset, moving to the next visualization if necessary.                            |
| [nextEffect](effects-nexteffect.md)         | Displays the first preset of the next visualization, skipping intervening presets.                                |
| [nextPreset](effects-nextpreset.md)         | Displays the next preset of the current visualization.                                                            |
| [previous](effects-previous.md)             | Displays the previous visualization preset, moving to the last preset of the previous visualization if necessary. |
| [previousEffect](effects-previouseffect.md) | Displays the previous visualization, skipping presets.                                                            |
| [previousPreset](effects-previouspreset.md) | Displays the previous preset of the current visualization.                                                        |
| [settings](effects-settings.md)             | Displays the attribute page for the current visualization, if present.                                            |



 

The **EFFECTS** element supports the ambient attributes and can implement the ambient event handlers. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined effects are normal **EFFECTS** elements with various common attribute settings specified by default. The following predefined effects are available.



| Predefined EFFECTS           | Description                                                         |
|------------------------------|---------------------------------------------------------------------|
| [WMPEFFECTS](wmpeffects.md) | An **EFFECTS** element that iterates through the available effects. |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




