---
title: Pixelate Effects
description: Pixelate Effects
ms.assetid: d06775fa-71d6-458d-b496-356a466e0a8a
keywords:
- Windows Movie Maker,pixelate effects
- Movie Maker,pixelate effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- pixelate effects
- effects,pixelate
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Pixelate Effects

The following XML defines the "pixelate" category of effects in Windows Movie Maker. These effects pixelate video, causing it to appear coarser and less detailed.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62818" iconid="19" guid="Pixelate" comment="Pixelate" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Pixelate" />
                <Semantics>
                    <PixelationSize evaluation="Linear" type="float">
                        <Point time="0.0" value="1.0"/>
                        <Point time="1.0" value="40.0"/>
                    </PixelationSize>
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
| *Technique* | Pixelate  |



 

## Customizable Parameters



| Parameter or element | Type  | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PixelationSize*     | float | 1.0   50.0    | The number of squares of pixelation. The larger the number, the coarser the picture appears.                                                                                                                                                                                                                                                                                                                          |
| **Point**            | float | 0.0   1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





