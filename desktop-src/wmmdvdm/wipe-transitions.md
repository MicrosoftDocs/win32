---
title: Wipe Transitions
description: Wipe Transitions
ms.assetid: 22307111-ffaa-4f85-9983-ba937411782d
keywords:
- Windows Movie Maker,wipe transitions
- Movie Maker,wipe transitions
- programming reference,Windows Movie Maker transitions
- reference for Windows Movie Maker,transitions
- wipe transitions
- transitions,wipe
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Wipe Transitions

The following XML defines the "wipe" category of transitions in Windows Movie Maker. These are gradual transitions from one scene to another using a distinct edge to "wipe" across the screen. The wipe transitions all use an *Animation* parameter set to "Wipe".

Following the XML are tables that specify which parameters in this XML can be changed, and which cannot.


```C++
<TransitionsAndEffects Version="2.8">
    <Transitions>
        <TransitionDLL guid="TFX">
            <Transition nameID="62836" iconid="23" guid="Bow Tie, Horizontal" comment="Bow Tie, Horizontal|(smpte 44)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Bow Tie" />
                <Param name="Edge" value="Soft" />
                <Param name="Out" value="FALSE" />
                <Param name="GradientWidth" value="0.1" />
            </Transition>
            <Transition nameID="62835" iconid="51" guid="Bow Tie, Vertical" comment="Bow Tie, Vertical|(smpte 43)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Bow Tie" />
                <Param name="Edge" value="Soft" />
                <Param name="Out" value="TRUE" />
                <Param name="GradientWidth" value="0.1" />
            </Transition>
            <Transition nameID="62815" iconid="4" guid="Checkerboard, Across" comment="Checkerboard, Across" >
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Checkerboard" />
                <Param name="Edge" value="Sharp" />
                <Param name="Columns" value="6" />
                <Param name="Rows" value="10" />
                <Param name="TwoWay" value="Vertical" />
            </Transition>
            <Transition nameID="62848" iconid="80" guid="Circle" comment="Circle, One|(smpte 119)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Circle" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
            </Transition>
            <Transition nameID="62849" iconid="81" guid="Circles" comment="Circles|(smpte 119)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Circles" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
                <Param name="Numbers" value="8" />
            </Transition>
            <Transition nameID="62838" iconid="7" guid="Diagonal, Box Out" comment="Diagonal, Box Out|(smpte 48)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Diagonal Box" />
                <Param name="Edge" value="Soft" />
                <Param name="Out" value="TRUE" />
                <Param name="GradientWidth" value="0.1" />
            </Transition>
            <Transition nameID="62837" iconid="8" guid="Diagonal, Cross Out" comment="Diagonal, Cross Out|(smpte 47)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Diagonal Cross" />
                <Param name="Edge" value="Soft" />
                <Param name="Out" value="TRUE" />
                <Param name="GradientWidth" value="0.1" />
            </Transition>
            <Transition nameID="62834" iconid="9" guid="Diagonal, Down Right" comment="Diagonal, Down Right|(smpte 41)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Diagonal Down" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWayDiagonal" value="Slash" />
                <Param name="Out" value="TRUE" />
                <Param name="GradientWidth" value="0.4" />
            </Transition>
            <Transition nameID="62847" iconid="11" guid="Diamond" comment="Diamond|(smpte 102)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Diamond" />
                <Param name="Edge" value="Sharp" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62857" iconid="3" guid="Eye" comment="Eye|(smpte 122)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Eye" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
            </Transition>
            <Transition nameID="62860" iconid="88" guid="Fan, In" comment="Fan, In|(smpte 263)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fan In" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="TwoWay" value="Vertical" />
            </Transition>
            <Transition nameID="62859" iconid="87" guid="Fan, Out" comment="Fan, Out|(smpte 262)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fan Out" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="FALSE" />
                <Param name="TwoWay" value="Horizontal" />
            </Transition>
            <Transition nameID="62839" iconid="16" guid="Filled V, Down" comment="Filled V, Down|(smpte 61)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fill V" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="FourWay" value="upper" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62840" iconid="15" guid="Filled V, Left" comment="Filled V, Left|(smpte 62)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fill V" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="FourWay" value="right" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62842" iconid="14" guid="Filled V, Right" comment="Filled V, Right|(smpte 64)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fill V" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="FourWay" value="left" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62841" iconid="13" guid="Filled V, Up" comment="Filled V, Up|(smpte 63)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fill V" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="FourWay" value="lower" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62852" iconid="18" guid="Heart" comment="Heart Shape|(smpte 130)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Heart" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
            </Transition>
            <Transition nameID="62829" iconid="28" guid="Inset, Down Left" comment="Inset, Down Left|(smpte 4)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Inset" />
                <Param name="Edge" value="Sharp" />
                <Param name="FourWayDiagonal" value="upperright" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62828" iconid="27" guid="Inset, Down Right" comment="Inset, Down Right|(smpte 3)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Inset" />
                <Param name="Edge" value="Sharp" />
                <Param name="FourWayDiagonal" value="upperleft" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62830" iconid="25" guid="Inset, Up Left" comment="Inset, Up Left|(smpte 5)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Inset" />
                <Param name="Edge" value="Sharp" />
                <Param name="FourWayDiagonal" value="lowerright" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62831" iconid="24" guid="Inset, Up Right" comment="Inset, Up Right|(smpte 6)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Inset" />
                <Param name="Edge" value="Sharp" />
                <Param name="FourWayDiagonal" value="lowerleft" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62813" iconid="29" guid="Iris" comment="Iris">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Iris" />
                <Param name="Edge" value="Sharp" />
            </Transition>
            <Transition nameID="62853" iconid="30" guid="Keyhole" comment="Keyhole|(smpte 131)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Keyhole" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
            </Transition>
            <Transition nameID="62846" iconid="39" guid="Rectangle" comment="Rectangle|(smpte 101)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Rectangle" />
                <Param name="Edge" value="Sharp" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62827" iconid="40" guid="Reveal, Down" comment="Reveal, Down|(smpte 2)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Sharp" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62826" iconid="41" guid="Reveal, Right" comment="Reveal, Right|(smpte 1)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Sharp" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62833" iconid="22" guid="Split, Horizontal" comment="Split, Horizontal|(smpte 22)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Split" />
                <Param name="Edge" value="Sharp" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62832" iconid="50" guid="Split, Vertical" comment="Split, Vertical|(smpte 21)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Split" />
                <Param name="Edge" value="Sharp" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62850" iconid="46" guid="Star, 5 Points" comment="Star, 5 Points|(smpte 128)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Star" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
                <Param name="Numbers" value="5" />
            </Transition>
            <Transition nameID="62851" iconid="83" guid="Stars, 5 Points" comment="Stars, 5 Points|(smpte 128)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Stars" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
                <Param name="Numbers" value="5" />
                <Param name="Columns" value="3" />
                <Param name="Rows" value="5" />
            </Transition>
            <Transition nameID="62854" iconid="84" guid="Sweep, In" comment="Sweep, In|(smpte 226)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Sweep In" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="FourWay" value="left" />
            </Transition>
            <Transition nameID="62855" iconid="85" guid="Sweep, Out" comment="Sweep, Out|(smpte 228)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Sweep Out" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="TwoWay" value="Vertical" />
            </Transition>
            <Transition nameID="62819" iconid="53" guid="Wheel, 4 Spokes" comment="Wheel, 4 Spokes">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Wheel" />
                <Param name="Edge" value="Sharp" />
                <Param name="Numbers" value="4" />
                <Param name="GradientWidth" value="0.05" />
            </Transition>
            <Transition nameID="62822" iconid="56" guid="Wipe, Narrow Down" comment="Wipe, Narrow Down">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="GradientWidth" value="0.2" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62825" iconid="55" guid="Wipe, Narrow Right" comment="Wipe, Narrow Right">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="GradientWidth" value="0.2" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62821" iconid="58" guid="Wipe, Normal Down" comment="Wipe, Normal Down">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="GradientWidth" value="0.4" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62823" iconid="59" guid="Wipe, Wide Right" comment="Wipe, Wide Right">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="GradientWidth" value="0.6" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62820" iconid="60" guid="Wipe, Wide Down" comment="Wipe, Wide Down">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="GradientWidth" value="0.6" />
                <Param name="Out" value="FALSE" />
            </Transition>
            <Transition nameID="62824" iconid="57" guid="Wipe, Normal Right" comment="Wipe, Normal Right">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Swipe" />
                <Param name="Edge" value="Soft" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="GradientWidth" value="0.4" />
                <Param name="Out" value="TRUE" />
            </Transition>
            <Transition nameID="62845" iconid="62" guid="Zig Zag, Horizontal" comment="Zig Zag, Horizontal|(smpte 74)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Zigzag" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="TwoWay" value="Vertical" />
                <Param name="Out" value="TRUE" />
                <Param name="Numbers" value="9" />
                <Param name="Ratio" value="0.1" />
            </Transition>
            <Transition nameID="62844" iconid="64" guid="Zig Zag, Vertical" comment="Zig Zag, Vertical|(smpte 73)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Zigzag" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="TwoWay" value="Horizontal" />
                <Param name="Out" value="TRUE" />
                <Param name="Numbers" value="9" />
                <Param name="Ratio" value="0.1" />
            </Transition>
            <Transition nameID="62856" iconid="82" guid="Fan, In, Vertical" comment="Fan, In, Vertical|(smpte 231)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Fan Up" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="FourWay" value="upper" />
            </Transition>
            <Transition nameID="62858" iconid="86" guid="Swinging Door, Bottom" comment="Swinging Door, Bottom|(smpte 253)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Sweep Up" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="FALSE" />
                <Param name="FourWay" value="lower" />
            </Transition>
        </TransitionDLL>
    </Transitions>
</TransitionsAndEffects>
```



## Non-Customizable Parameters



| Parameter   | Required value |
|-------------|----------------|
| *Animation* | Wipe           |



 

## Customizable Parameters



| Parameter       | Type   | Possible values                          | Description                                                                                           |
|-----------------|--------|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| *Mesh*          | string | Any *Mesh* value from the preceding XML. | Defines the wipe pattern that is applied.                                                             |
| *Edge*          | string | Soft or Sharp                            | Indicates whether the edges of the wipe pattern should be soft or sharp.                              |
| *Out*           | string | True or False                            | Toggles the direction in which the wipe is applied.                                                   |
| *GradientWidth* | float  | 0.0 – 1.0                                | The width of the gradient transition area between the two inputs, as a percentage of the output size. |



 

## Related topics

<dl> <dt>

[**Transitions**](transitions.md)
</dt> </dl>

 

 




