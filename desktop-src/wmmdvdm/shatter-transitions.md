---
title: Shatter Transitions
description: Shatter Transitions
ms.assetid: c37562f6-7c6d-4d2a-9e02-9a498d7a2b15
keywords:
- Windows Movie Maker,shatter transitions
- Movie Maker,shatter transitions
- programming reference,Windows Movie Maker transitions
- reference for Windows Movie Maker,transitions
- shatter transitions
- transitions,shatter
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shatter Transitions

The following XML defines the "shatter" category of transitions in Windows Movie Maker. These are transitions that use a "shattering glass" or other particle-based effect. The shatter transitions all use an *Animation* parameter set to "ParticleSystem".

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Transitions>
        <TransitionDLL guid="TFX">
            <Transition nameID="62809" iconid="76" guid="Shatter, In" comment="Shatter, In">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="ScatterDirection" value="in" />
                <Param name="MaxParticles" value="600" />
                <Param name="SpinDirection" value="right" />
                <Param name="ParticleSpeed" value="400.0" />
                <Param name="ParticleSpinSpeed" value="0.5" />
                <Param name="ExponentialProgressDuration" value="0.9" />
            </Transition>
            <Transition nameID="62807" iconid="77" guid="Shatter, Right" comment="Shatter, Right">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="ScatterDirection" value="right" />
                <Param name="SpinDirection" value="down" />
                <Param name="PulseMode" value="in" />
                <Param name="XProgressStart" value="0.5" />
                <Param name="ParticleSpinSpeed" value="0.33" />
                <Param name="MaxParticles" value="200" />
            </Transition>
            <Transition nameID="62808" iconid="78" guid="Shatter, Up Left" comment="Shatter, Up Left">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="ScatterDirection" value="up, left" />
                <Param name="MaxParticles" value="64" />
                <Param name="PulseMode" value="out" />
                <Param name="ExponentialProgressDuration" value="0.4" />
            </Transition>
            <Transition nameID="62811" iconid="79" guid="Shatter, Up Right" comment="Shatter, Up Right">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="MaxParticles" value="700" />
                <Param name="PulseMode" value="out" />
                <Param name="ScatterDirection" value="up, right" />
            </Transition>
            <Transition nameID="62810" iconid="75" guid="Whirlwind" comment="Whirlwind">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="MaxParticles" value="200" />
                <Param name="ClipProgress" value="true" />
                <Param name="SpinDirection" value="right" />
                <Param name="ParticleSpinSpeed" value="0.4" />
            </Transition>
            <Transition nameID="62956" iconid="75" guid="Whirlwind from top" comment="Whirlwind from top">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="MaxParticles" value="200" />
                <Param name="ZProgressStart" value="0.6" />
                <Param name="ClipProgress" value="true" />
                <Param name="SpinDirection" value="right" />
                <Param name="ParticleSpinSpeed" value="0.4" />
                <Param name="PulseMode" value="OutALittle" />
            </Transition>
        </TransitionDLL>
    </Transitions>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter           | Value          |
|---------------------|----------------|
| *Animation*         | ParticleSystem |
| *DepthBufferFormat* | 80             |



 

## Customizable Parameters



| Parameter                     | Type   | Range/options                                      | Description                                                                                                                                                                                                                   |
|-------------------------------|--------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *ScatterDirection*            | string | "in" , "out" , "left" , "right" , "up" , or "down" | The direction in which the shattered particles will move.You can combine perpendicular directions such as "up, right" or "left, down". However, you cannot combine two opposite directions such as left and right.<br/> |
| *MaxParticles*                | int    | 10   8                                             | The number of particles into which the image is shattered.                                                                                                                                                                    |
| *SpinDirection*               | string | "in" , "out" , "left" , "right" , "up" , or "down" | The direction in which the scattered particles spin.                                                                                                                                                                          |
| *ParticleSpeed*               | float  | 10.0   1000.0                                      | The speed with which the shattered particles move.                                                                                                                                                                            |
| *ParticleSpinSpeed*           | float  | 0.0   1.0                                          | The speed with which the scattered particles spin.                                                                                                                                                                            |
| *PulseMode*                   | string | "in" , "out", or "OutALittle"                      | The direction in which the particles move.                                                                                                                                                                                    |
| *ExponentialProgressDuration* | float  | 0.0   1.0                                          | The duration of acceleration for the shattered particles (relative to the total duration).                                                                                                                                    |



 

## Related topics

<dl> <dt>

[**Transitions**](transitions.md)
</dt> </dl>

 

 





