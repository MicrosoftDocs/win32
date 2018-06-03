---
title: Film Age Effects
description: Film Age Effects
ms.assetid: 714f1d65-c72e-417e-92ed-8fe33bd233ac
keywords:
- Windows Movie Maker,film age effects
- Movie Maker,film age effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- film age effects
- effects,film age
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Film Age Effects

The following XML defines the "film age" category of effects in Windows Movie Maker. These effects appear to "age" video, giving it a classic, old-time movie look. The film age effects all use an *Animation* parameter set to "FXAge".

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62876" iconid="12" guid="Film Age, Old" comment="Film Age, Old" shadermodel="2">
                <Param name="Animation" value="FXAge" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="FilmAgeOld" />
                <Param name="Alpha0" value="TRUE" type="bool" />
                <Param name="Alpha1" value="TRUE" type="bool" />
                <Param name="NoiseFrequency" value="0.25" />
                <Param name="SplotchFrequency" value="0.05" />
                <Param name="NoiseLineFrequency" value="0.10" />
                <Param name="LintFrequency" value="0.05" />
                <Param name="PosterizeLevels" value="128" />
                <Param name="ShakeFactor" value="0.00"/>
                <Param name="BlurSize" value="3"/>
                <Param name="GenerateNoiseTexture" value="1"/>
            </Effect>
            <Effect nameID="62875" iconid="13" guid="Film Age, Older" comment="Film Age, Older" shadermodel="2">
                <Param name="Animation" value="FXAge" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="FilmAgeOlder" />
                <Param name="NoiseFrequency" value="0.40" />
                <Param name="SplotchFrequency" value="0.10" />
                <Param name="NoiseLineFrequency" value="0.20" />
                <Param name="LintFrequency" value="0.15" />
                <Param name="PosterizeLevels" value="7" />
                <Param name="ShakeFactor" value="0.05"/>
                <Param name="BlurSize" value="5"/>
                <Param name="GenerateNoiseTexture" value="1"/>
            </Effect>
            <Effect nameID="62874" iconid="14" guid="Film Age, Oldest" comment="Film Age, Oldest" shadermodel="2">
                <Param name="Animation" value="FXAge" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="FilmAgeOldest" />
                <Param name="NoiseFrequency" value="1.00" />
                <Param name="SplotchFrequency" value="0.20" />
                <Param name="NoiseLineFrequency" value="0.30" />
                <Param name="LintFrequency" value="0.40" />
                <Param name="PosterizeLevels" value="5" />
                <Param name="ShakeFactor" value="0.20"/>
                <Param name="BlurSize" value="7"/>
                <Param name="GenerateNoiseTexture" value="1"/>
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter   | Value     |
|-------------|-----------|
| *Animation* | FXAge     |
| *FXFile*    | Parity.fx |



 

## Customizable Parameters



| Parameter or element   | Type   | Range/options                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------|--------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Technique*            | string | "FilmAgeOld" , "FilmAgeOlder" , or "FilmAgeOldest" | Name of the predefined technique that you want to apply to the effect.                                                                                                                                                                                                                                                                                                                                                |
| *NoiseFrequency*       | float  | 0.0   1.0                                          | Adds noise to the image, where 0 creates the least noise and 1.0 the most.                                                                                                                                                                                                                                                                                                                                            |
| *SplotchFrequency*     | float  | 0.0   1.0                                          | Adds splotches to the image, where 0 creates the least number of splotches and 1.0 the most.                                                                                                                                                                                                                                                                                                                          |
| *NoiseLineFrequency*   | float  | 0.0   1.0                                          | The frequency of white traveling "cracks" or lines in the image, where 0 creates the fewest lines and 1.0 the most.                                                                                                                                                                                                                                                                                                   |
| *LintFrequency*        | float  | 0.0   1.0                                          | The frequency of "lint" or "tears" on the screen, where 0 creates the least lint and 1.0 the most.                                                                                                                                                                                                                                                                                                                    |
| *ShakeFactor*          | float  | 0.0   1.0                                          | Degree of film jerkiness, where 0 is least and 1.0 is most.                                                                                                                                                                                                                                                                                                                                                           |
| *BlurSize*             | int    | 1   8                                              | Level of blurriness. Higher values mean a blurrier image.                                                                                                                                                                                                                                                                                                                                                             |
| *GenerateNoiseTexture* | int    | 0 or 1                                             | Specifies whether to generate "noise".                                                                                                                                                                                                                                                                                                                                                                                |
| *PosterizeLevels*      | int    | 0   255                                            | The number of color levels that should remain after posterization (reduction of number of color levels).                                                                                                                                                                                                                                                                                                              |
| **Point**              | float  | 0.0   1.0                                          | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





