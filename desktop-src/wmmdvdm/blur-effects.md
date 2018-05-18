---
title: Blur Effects
description: Blur Effects
ms.assetid: 'e7911264-4e28-496d-ae7e-eaf759c46b31'
keywords: ["Windows Movie Maker,blur effects", "Movie Maker,blur effects", "programming reference,Windows Movie Maker effects", "reference for Windows Movie Maker,effects", "blur effects", "effects,blur"]
---

# Blur Effects

The following XML defines the "blur" category of effects in Windows Movie Maker. These are effects that blur video, making the picture less sharp to differing degrees.

Following the XML are tables that specify which parameters of this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62890" iconid="1" guid="Blur" comment="Blur" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Blur" />
                <BlurSize value="7" />
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
| *Technique* | Blur      |



 

## Customizable Parameters



| Parameter or element | Type  | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *BlurSize*           | int   | 0 – 25        | The degree of blurriness of the video. The higher the number, the blurrier the picture.                                                                                                                                                                                                                                                                                                                               |
| **Point**            | float | 0.0 – 1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/> |



 

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





