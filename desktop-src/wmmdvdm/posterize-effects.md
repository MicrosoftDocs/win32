---
title: Posterize Effects
description: Posterize Effects
ms.assetid: 7a07d1fc-4f6a-4859-983d-8197ee49d5cd
keywords:
- Windows Movie Maker,posterize effects
- Movie Maker,posterize effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- posterize effects
- effects,posterize
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Posterize Effects

The following XML defines the "posterize" category of effects in Windows Movie Maker. These effects reduce the number of color tones in an image by combining similar tones into fewer tones.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62865" iconid="20" guid="Posterize" comment="Posterize" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Posterize" />
                <Semantics>
                    <PosterizeLevels Evaluation="Step" type="int">
                        <Point time="0.0" value="5"/>
                    </PosterizeLevels>
                </Semantics>
            </Effect>
            <Effect nameID="62866" iconid="29" guid="Threshold" comment="Threshold" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Posterize" />
                <Semantics>
                    <PosterizeLevels Evaluation="Step" type="int">
                        <Point time="0.0" value="1"/>
                    </PosterizeLevels>
                </Semantics>
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter   | Value     |
|-------------|-----------|
| *Animation* | FX        |
| *FXFile*    | Parity.fx |
| *Technique* | Posterize |



 

## Customizable Parameters



| Parameter or element | Type  | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PosterizeLevels*    | int   | 1   255       | The number of colors to which the image will be reduced.                                                                                                                                                                                                                                                                                                                                                              |
| **Point**            | float | 0.0   1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





