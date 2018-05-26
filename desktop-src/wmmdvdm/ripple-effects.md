---
title: Ripple Effects
description: Ripple Effects
ms.assetid: 23e559cf-0fb2-40a6-9f6a-8ef15d11a2fe
keywords:
- Windows Movie Maker,ripple effects
- Movie Maker,ripple effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- ripple effects
- effects,ripple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ripple Effects

The following XML defines the "ripple" category of effects in Windows Movie Maker. These effects make the video image appear as if there were ripples of water on top of it.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62797" iconid="0" guid="3D Ripple" comment="3D Ripple" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Ripple" />
                <Semantics>
                    <WaveControls evaluation="Linear" type="float2">
                        <Point time="0.0" value="1.0,0.0"/>
                        <Point time="1.0" value="0.0,1.0"/>
                    </WaveControls>
                    <WaveCenter evaluation="Step" type="float2">
                        <Point time="0.0" value="0.5,0.5"/>
                    </WaveCenter>
                    <Frequency value="4.0" type="float">
                    </Frequency>
                    <Speed value="9.5" type="float">
                    </Speed>
                    <Height value="0.125" type="float">
                    </Height>
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
| *Technique* | Ripple    |



 

## Customizable Parameters



| Parameter or element | Type   | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|--------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *WaveControls*       | float2 | 0.0   1.0     | Defines the oscillation of the wave.                                                                                                                                                                                                                                                                                                                                                                                  |
| *WaveCenter*         | float2 | 0.0   1.0     | The image coordinates of the origin of the ripple waves.                                                                                                                                                                                                                                                                                                                                                              |
| *Frequency*          | float  | 1.0   10.0    | The frequency of the ripple waves.                                                                                                                                                                                                                                                                                                                                                                                    |
| *Speed*              | float  | 1.0   50.0    | The speed of the ripple waves.                                                                                                                                                                                                                                                                                                                                                                                        |
| *Height*             | float  | 0.0   1.0     | The height of each ripple wave.                                                                                                                                                                                                                                                                                                                                                                                       |
| **Point**            | float  | 0.0   1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

**Note** The "float2" type refers to a comma-delimited array of two floating point numbers. For instance, "(0.0,1.0)".

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





