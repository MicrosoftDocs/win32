---
title: EQUALIZERSETTINGS Element
description: EQUALIZERSETTINGS Element
ms.assetid: 521f1c95-7904-4085-a8bc-5399d667dfb1
keywords:
- Windows Media Player skins,EQUALIZERSETTINGS element
- skins,EQUALIZERSETTINGS element
- EQUALIZERSETTINGS element
- reference for skins,EQUALIZERSETTINGS element
- elements,EQUALIZERSETTINGS
ms.topic: article
ms.date: 05/31/2018
---

# EQUALIZERSETTINGS Element

The **EQUALIZERSETTINGS** element provides a way to manipulate the graphic equalizer and other audio settings of Windows Media Player using the attributes and method listed here.

The **EQUALIZERSETTINGS** element supports the following attributes.



| Attribute                                                          | Description                                                                                             |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [bands](equalizersettings-bands.md)                               | Retrieves the number of frequency bands supported.                                                      |
| [bypass](equalizersettings-bypass.md)                             | Specifies or retrieves a value indicating whether the equalizer filter is bypassed in the filter graph. |
| [crossFade](equalizersettings-crossfade.md)                       | Specifies or retrieves a value indicating whether cross-fade is enabled.                                |
| [crossFadeWindow](equalizersettings-crossfadewindow.md)           | Specifies or retrieves the amount of cross-fade overlap in milliseconds.                                |
| [currentPreset](equalizersettings-currentpreset.md)               | Specifies or retrieves the index of the current preset.                                                 |
| [currentPresetTitle](equalizersettings-currentpresettitle.md)     | Retrieves the title of the current preset.                                                              |
| [currentSpeakerName](equalizersettings-currentspeakername.md)     | Retrieves the name of the current speaker setting.                                                      |
| [enableSplineTension](equalizersettings-enablesplinetension.md)   | Specifies or retrieves a value indicating whether spline tension is enabled or disabled.                |
| [enhancedAudio](equalizersettings-enhancedaudio.md)               | Specifies or retrieves a value indicating whether enhanced audio is turned on.                          |
| [gainLevels](equalizersettings-gainlevels.md)                     | Specifies or retrieves the gain level of the band corresponding to the index provided.                  |
| [gainLevel1](equalizersettings-gainlevel1.md)                     | Specifies or retrieves the gain level of band 1.                                                        |
| [gainLevel2](equalizersettings-gainlevel2.md)                     | Specifies or retrieves the gain level of band 2.                                                        |
| [gainLevel3](equalizersettings-gainlevel3.md)                     | Specifies or retrieves the gain level of band 3.                                                        |
| [gainLevel4](equalizersettings-gainlevel4.md)                     | Specifies or retrieves the gain level of band 4.                                                        |
| [gainLevel5](equalizersettings-gainlevel5.md)                     | Specifies or retrieves the gain level of band 5.                                                        |
| [gainLevel6](equalizersettings-gainlevel6.md)                     | Specifies or retrieves the gain level of band 6.                                                        |
| [gainLevel7](equalizersettings-gainlevel7.md)                     | Specifies or retrieves the gain level of band 7.                                                        |
| [gainLevel8](equalizersettings-gainlevel8.md)                     | Specifies or retrieves the gain level of band 8.                                                        |
| [gainLevel9](equalizersettings-gainlevel9.md)                     | Specifies or retrieves the gain level of band 9.                                                        |
| [gainLevel10](equalizersettings-gainlevel10.md)                   | Specifies or retrieves the gain level of band 10.                                                       |
| [normalization](equalizersettings-normalization.md)               | Specifies or retrieves a value indicating whether normalization is enabled.                             |
| [normalizationAverage](equalizersettings-normalizationaverage.md) | Retrieves the average normalization value.                                                              |
| [normalizationPeak](equalizersettings-normalizationpeak.md)       | Retrieves the peak normalization value.                                                                 |
| [presetCount](equalizersettings-presetcount.md)                   | Retrieves the number of presets available.                                                              |
| [speakerSize](equalizersettings-speakersize.md)                   | Specifies or retrieves the index of the current speaker size.                                           |
| [splineTension](equalizersettings-splinetension.md)               | Specifies or retrieves the spline tension for the equalizer control.                                    |
| [truBassLevel](equalizersettings-trubasslevel.md)                 | Specifies or retrieves the SRS TruBass level.                                                           |
| [wowLevel](equalizersettings-wowlevel.md)                         | Specifies or retrieves the SRS WOW Effect level.                                                        |



 

The **EQUALIZERSETTINGS** element supports the following methods.



| Method                                                 | Description                                                          |
|--------------------------------------------------------|----------------------------------------------------------------------|
| [nextPreset](equalizersettings-nextpreset.md)         | Applies the next equalizer preset.                                   |
| [presetTitle](equalizersettings-presettitle.md)       | Retrieves the name of the equalizer preset with the specified index. |
| [previousPreset](equalizersettings-previouspreset.md) | Applies the previous equalizer preset.                               |
| [reset](equalizersettings-reset.md)                   | Resets the gain levels of all bands to zero decibels.                |



 

The **EQUALIZERSETTINGS** element can implement the [attribute\_onchange](attribute-onchange.md) event handlers.

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




