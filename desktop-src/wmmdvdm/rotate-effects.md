---
title: Rotate Effects
description: Rotate Effects
ms.assetid: bc113299-4e3a-46cb-9ca5-ca87b90f3557
keywords:
- Windows Movie Maker,rotate effects
- Movie Maker,rotate effects
- programming reference,Windows Movie Maker effects
- reference for Windows Movie Maker,effects
- rotate effects
- effects,rotate
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Rotate Effects

The following XML defines the "rotate" category of effects in Windows Movie Maker. These effects rotate the video image by a specified number of degrees.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62871" iconid="21" guid="Rotate 90" comment="Rotate 90" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Rotate" />
                <RotationDegree value="90" />
            </Effect>
            <Effect nameID="62872" iconid="22" guid="Rotate 180" comment="Rotate 180" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Rotate" />
                <RotationDegree value="180" />
            </Effect>
            <Effect nameID="62873" iconid="23" guid="Rotate 270" comment="Rotate 270" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Rotate" />
                <RotationDegree value="270" />
            </Effect>
            <Effect nameID="62796" iconid="24" guid="Spin 360" comment="Spin 360" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Rotate" />
                <RotationDegree evaluation="Linear" type="float">
                    <Point time="0.0" value="0.0"/>
                    <Point time="1.0" value="360.0"/>
                </RotationDegree>
                <CameraZoom evaluation="Linear" type="float">
                    <Point time="0.0" value="1.0"/>
                    <Point time="0.35" value="0.80"/>
                    <Point time="0.5" value="0.75"/>
                    <Point time="0.65" value="0.80"/>
                    <Point time="1.0" value="1.0"/>
                </CameraZoom>
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
| *Technique* | Rotate    |



 

## Customizable Parameters



| Parameter or element | Type  | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *RotationDegree*     | int   | 0   360       | The number of degrees to rotate the output video.                                                                                                                                                                                                                                                                                                                                                                     |
| *CameraZoom*         | float | 0.0   1.0     | The relative "distance" of the viewport from the original video image. The smaller this value is, the higher the zoom magnification.                                                                                                                                                                                                                                                                                  |
| **Point**            | float | 0.0   1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





