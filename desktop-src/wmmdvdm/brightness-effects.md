---
title: Brightness Effects
description: Brightness Effects
ms.assetid: 'a702351e-7aed-4880-981f-f9450657ed90'
keywords: ["Windows Movie Maker,brightness effects", "Movie Maker,brightness effects", "programming reference,Windows Movie Maker effects", "reference for Windows Movie Maker,effects", "brightness effects", "effects,brightness"]
---

# Brightness Effects

The following XML defines the "brightness" category of effects in Windows Movie Maker. These effects brighten or darken the video image.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62882" iconid="2" guid="Brightness, Decrease" comment="Brightness, Decrease" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Brightness" />
                <Semantics>
                    <PercentBrightness Evaluation="Step" type="float">
                        <Point time="0.0" value="-0.25"/>
                    </PercentBrightness>
                </Semantics>
            </Effect>
            <Effect nameID="62881" iconid="3" guid="Brightness, Increase" comment="Brightness, Increase" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Brightness" />
                <Semantics>
                    <PercentBrightness Evaluation="Step" type="float">
                        <Point time="0.0" value="0.25"/>
                    </PercentBrightness>
                </Semantics>
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter   | Value      |
|-------------|------------|
| *Animation* | FX         |
| *FXFile*    | Parity.fx  |
| *Technique* | Brightness |



 

## Customizable Parameters



| Parameter or element | Type  | Range/Options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *PercentBrightness*  | float | -1.0 – 8      | The degree of brightness of the video. The higher the number, the brighter the picture.                                                                                                                                                                                                                                                                                                                               |
| **Point**            | float | 0.0 – 1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





