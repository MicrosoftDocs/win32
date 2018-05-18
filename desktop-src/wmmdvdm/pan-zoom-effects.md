---
title: Pan/Zoom Effects
description: Pan/Zoom Effects
ms.assetid: '32726c61-d42a-4d8c-8726-cc97a13695b1'
keywords: ["Windows Movie Maker,pan/zoom effects", "Movie Maker,pan/zoom effects", "programming reference,Windows Movie Maker effects", "reference for Windows Movie Maker,effects", "pan/zoom effects", "effects,pan/zoom"]
---

# Pan/Zoom Effects

The following XML defines the "pan/zoom" category of effects in Windows Movie Maker. These effects pan the viewport from one part of the video image to another and zoom the viewport in and out.

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Effects>
        <EffectDLL guid="TFX">
            <Effect nameID="62868" iconid="5" guid="Ease In" comment="Ease In" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,1.0,1.0"/>
                        <Point time="1.0" value="0.075,0.075,0.85,0.85"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62869" iconid="6" guid="Ease Out" comment="Ease Out" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.075,0.075,0.85,0.85"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62884" iconid="17" guid="Mirror, Horizontal" comment="Mirror, Horizontal" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="1.0,0.0,-1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62870" iconid="18" guid="Mirror, Vertical" comment="Mirror, Vertical" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="0.0,1.0,1.0,-1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62779" iconid="31" guid="Zoom In, to Upper Right" comment="Zoom In, to Upper Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,1.0,1.0"/>
                        <Point time="1.0" value="0.333334,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62780" iconid="32" guid="Zoom In, to Upper Left" comment="Zoom In, to Upper Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,1.0,1.0"/>
                        <Point time="1.0" value="0.0,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62781" iconid="33" guid="Zoom In, to Lower Left" comment="Zoom In, to Lower Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,1.0,1.0"/>
                        <Point time="1.0" value="0.0,0.333334,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62782" iconid="34" guid="Zoom In, to Lower Right" comment="Zoom In, to Lower Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,1.0,1.0"/>
                        <Point time="1.0" value="0.333334,0.333334,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62783" iconid="35" guid="Zoom Out, from Upper Right" comment="Zoom Out, from Upper Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.333334,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62784" iconid="36" guid="Zoom Out, from Upper Left" comment="Zoom Out, from Upper Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62785" iconid="37" guid="Zoom Out, from Lower Left" comment="Zoom Out, from Lower Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.333334,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62786" iconid="38" guid="Zoom Out, from Lower Right" comment="Zoom Out, from Lower Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.333334,0.333334,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62787" iconid="39" guid="Zoom, Focus Upper Right" comment="Zoom, Focus Upper Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="0.333334,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62788" iconid="40" guid="Zoom, Focus Upper Left" comment="Zoom, Focus Upper Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62789" iconid="41" guid="Zoom, Focus Lower Left" comment="Zoom, Focus Lower Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="0.0,0.333334,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62790" iconid="42" guid="Zoom, Focus Lower Right" comment="Zoom, Focus Lower Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Step" type="float4">
                        <Point time="0.0" value="0.333334,0.333334,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62791" iconid="47" guid="Pan, Down and Zoom Out" comment="Pan, Down and Zoom Out" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.166667,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,1.0,1.0"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62792" iconid="46" guid="Pan, Left to Right" comment="Pan, Left to Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.166667,0.666666,0.666666"/>
                        <Point time="1.0" value="0.333334,0.166667,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62793" iconid="36" guid="Pan, Upper Left to Lower Right" comment="Pan, Upper Left to Lower Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.333334,0.333334,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62794" iconid="43" guid="Pan, Upper Right to Upper Left" comment="Pan, Upper Right to Upper Left" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.333334,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.0,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
            <Effect nameID="62795" iconid="44" guid="Pan, Upper Left to Upper Right" comment="Pan, Upper Left to Upper Right" shadermodel="2">
                <Param name="Animation" value="FXPanZoom" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="PanZoom" />
                <Semantics>
                    <TextureViewport evaluation="Linear" type="float4">
                        <Point time="0.0" value="0.0,0.0,0.666666,0.666666"/>
                        <Point time="1.0" value="0.333334,0.0,0.666666,0.666666"/>
                    </TextureViewport>
                </Semantics>
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter   | Value     |
|-------------|-----------|
| *Animation* | FXPanZoom |
| *FXFile*    | Parity.fx |
| *Technique* | PanZoom   |



 

## Customizable Elements



| Element             | Type   | Range/options | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------|--------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TextureViewport** | float4 | 0.0 – 1.0     | The **TextureViewport** element defines the part of the video image that is visible—the *viewport*. The image coordinates range from 0.0 to 1.0, with the upper-left corner having the coordinates (0.0,0.0), and the lower-right corner having the coordinates (1.0,1.0).The **TextureViewport** element is defined as a list of 4 floating-point values. The first two values define the location of the upper-left corner of the viewport within the image. The third and fourth coordinates define the width and height of the viewport (in image coordinates).<br/> For more information on the **TextureViewport** element, see Step 5 of [Making Your Own XML File](making-your-own-xml-file.md).<br/> |
| **Point**           | float  | 0.0 – 1.0     | The point within the duration of the effect at which the enclosing element will have the specified **value**. When the **time** attribute is equal to 0.0, it indicates the starting point of the clip; when the **time** attribute is equal to 1.0, it indicates the end point of the clip.For more information on the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).<br/>                                                                                                                                                                                                                                                                                                      |



 

**Note** The "float4" type refers to a comma-delimited array of four floating point numbers. For instance, "(0.0,1.0,0.2,0.4)".

## Related topics

<dl> <dt>

[**Effects**](effects.md)
</dt> </dl>

 

 





