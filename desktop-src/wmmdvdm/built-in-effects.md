---
title: Built-in Effects
description: Built-in Effects
ms.assetid: 'd96f0f0a-c715-4b10-be9e-8ce163016655'
keywords: ["Windows Movie Maker,effects", "Movie Maker,effects", "programming guide,Windows Movie Maker effects", "creating custom transforms using XML,effects", "XML,effects", "transforms,effects", "custom transforms,effects", "effects", "built-in effects"]
---

# Built-in Effects

The following XML code defines the built-in effects in Windows Movie Maker 6.0.


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
            <Effect nameID="62890" iconid="1" guid="Blur" comment="Blur" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Blur" />
                <BlurSize value="7" />
            </Effect>
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
            <Effect nameID="62885" iconid="15" guid="Grayscale" comment="Grayscale" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Grayscale" />
            </Effect>
            <Effect nameID="62867" iconid="16" guid="Hue" comment="Hue, Cycles Entire Color Spectrum" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="HueCycle" />
            </Effect>
            <Effect nameID="62886" iconid="48" guid="Film Grain" comment="Film Grain" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="FilmGrain" />
                <Param name="GenerateNoiseTexture" value="1"/>
            </Effect>
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
            <Effect nameID="62889" iconid="30" guid="Watercolor" comment="Watercolor" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Kuwahara" />
                <Param name="Alpha1" value="TRUE" type="bool" />
            </Effect>
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
            <Effect nameID="62863" iconid="25" guid="Sepia Tone" comment="Sepia Tone" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Sepia" />
            </Effect>
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
            <Effect nameID="62798" iconid="26" guid="Sharpen" comment="Sharpen" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="Sharpen" />
            </Effect>
            <Effect nameID="62799" iconid="4" guid="Dream" comment="Dream">
                <Param name="Animation" value="Simple3D" />
                <Param name="WarpXA" value="0.5" />
            </Effect>
            <Effect nameID="62941" iconid="7" guid="Edge Detection" comment="Edge Detection" shadermodel="2">
                <Param name="Animation" value="FX" />
                <Param name="FXFile" value="Parity.fx" />
                <Param name="Technique" value="EdgeDetect" />
            </Effect>
            <Effect guid="{00000000-0000-0000-0000-000000000000}" nameID="62861" iconid="28" speed="2.0" comment="Speed up">
            </Effect>
            <Effect guid="{00000000-0000-0000-0000-000000000000}" nameID="62862" iconid="27" speed="0.5" comment="Slow down">
            </Effect>
        </EffectDLL>
    </Effects>
</TransitionsAndEffects>
```



## Related topics

<dl> <dt>

[**Transition and Effect Objects Provided by Windows Movie Maker**](transition-and-effect-objects-provided-by-windows-movie-maker.md)
</dt> </dl>

 

 




