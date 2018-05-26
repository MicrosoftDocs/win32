---
title: Fade Effects
description: Fade Effects
ms.assetid: a820e8ff-fcce-45d3-9a22-df84772c1f6d
keywords:
- Windows Movie Maker,fade effects
- Movie Maker,fade effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- fade effects
- effects,fade
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fade Effects

The following XML defines the "fade" category of effects in Windows Movie Maker. These effects fade video in or out, from or to a specified color.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62878" iconid="10" guid="Fade In, From Black" comment="Fade In, From Black" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Fade" />
                <Semantics>
                    <FadeColor evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.0,1.0"/>
                        <Point time="1.0" value="0.0,0.0,0.0,0.0"/>
                    </FadeColor>
                </Semantics>
            </Effect>
            <Effect nameID="62880" iconid="11" guid="Fade In, From White" comment="Fade In, From White" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Fade" />
                <Semantics>
                    <FadeColor evaluation="Linear" type="float4">
                        <Point time="0.0" value="1.0,1.0,1.0,1.0"/>
                        <Point time="1.0" value="1.0,1.0,1.0,0.0"/>
                    </FadeColor>
                </Semantics>
            </Effect>
            <Effect nameID="62877" iconid="8" guid="Fade Out, To Black" comment="Fade Out, To Black" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Fade" />
                <Semantics>
                    <FadeColor evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.0,0.0"/>
                        <Point time="1.0" value="0.0,0.0,0.0,1.0"/>
                    </FadeColor>
                </Semantics>
            </Effect>
            <Effect nameID="62879" iconid="9" guid="Fade Out, To White" comment="Fade Out, To White" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Fade" />
                <Semantics>
                    <FadeColor evaluation="Linear" type="float4">
                        <Point time="0.0" value="1.0,1.0,1.0,0.0"/>
                        <Point time="1.0" value="1.0,1.0,1.0,1.0"/>
                    </FadeColor>
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
| *Technique* | Fade      |



 

## Customizable Parameters



| Parameter or element | Type   | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|--------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *FadeColor*          | float4 | 0.0   1.0     | Represents the color (and alpha value) applied to the image/video.The *FadeColor* is defined as an array of 4 floats. Each float represents a color channel, in this order: Red, Green, Blue, Alpha.<br/>                                                                                                                                                                                                       |
| **Point**            | float  | 0.0   1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

**Note** The "float4" type refers to a comma-delimited array of four floating point numbers. For instance, "(0.0,1.0,0.2,0.4)".

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





