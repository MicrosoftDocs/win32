---
title: Built-in Transitions
description: Built-in Transitions
ms.assetid: 92ccf172-f516-419c-94d9-40a6ee7b8153
keywords:
- Windows Movie Maker,transitions
- Movie Maker,transitions
- programming guide,Windows Movie Maker transitions
- transitions,built-in
- built-in transitions
- XML,built-in transitions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Built-in Transitions

The following XML code defines the built-in transitions in Windows Movie Maker 6.0.


```C++
<TransitionsAndEffects Version="2.8">
    <Transitions>
        <TransitionDLL guid="TFX">
            <Transition nameID="62817" iconid="37" guid="Bars" comment="Bars">
                <Param name="Animation" value="Dissolve" />
                <Param name="DepthBufferFormat" value="75" />
                <Param name="DissolveType" value="HorizontalBars" />
            </Transition>
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
            <Transition nameID="62816" iconid="38" guid="Dissolve" comment="Dissolve" >
                <Param name="Animation" value="Dissolve" />
                <Param name="DepthBufferFormat" value="75" />
                <Param name="DissolveType" value="Dissolve2D" />
            </Transition>
            <Transition nameID="62857" iconid="3" guid="Eye" comment="Eye|(smpte 122)">
                <Param name="Animation" value="Wipe" />
                <Param name="Mesh" value="Eye" />
                <Param name="Edge" value="Soft" />
                <Param name="GradientWidth" value="0.1" />
                <Param name="Out" value="TRUE" />
                <Param name="Stretch" value="FALSE" />
            </Transition>
            <Transition nameID="62814" iconid="12" guid="Fade" comment="Fade">
                <Param name="Animation" value="Pixelate Transition" />
                <Param name="MaxSquare" value="1" />
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
            <Transition nameID="62800" iconid="91" guid="Flip, Right" comment="Flip, Right">
                <Param name="Animation" value="Simple3D" />
                <Param name="RevolveCamera" value="right" />
                <Param name="ShowAFront" value="true" />
                <Param name="ShowABack" value="false" />
                <Param name="ShowBFront" value="false" />
                <Param name="ShowBBack" value="true" />
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
            <Transition nameID="62805" iconid="89" guid="Page Curl, Up Right" comment="Page Curl, Up Right">
                <Param name="Animation" value="Simple3D" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="PageCurlA" value="lowerleft" />
                <Param name="ShowABack" value="true" />
                <Param name="VertexVelocity" value="600.0, 50.0, 600.0" />
                <Param name="FadeStartA" value="0.9" />
            </Transition>
            <Transition nameID="62806" iconid="90" guid="Page Curl, Up Left" comment="Page Curl, Up Left">
                <Param name="Animation" value="Simple3D" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="PageCurlA" value="lowerright" />
                <Param name="ShowABack" value="true" />
                <Param name="FadeStartA" value="0.9" />
                <Param name="VertexVelocity" value="-600.0, 50.0, 600.0" />
            </Transition>
            <Transition nameID="62818" iconid="36" guid="Pixelate Transition" comment="Pixelate Transition">
                <Param name="Animation" value="Pixelate Transition" />
                <Param name="MaxSquare" value="50" />
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
            <Transition nameID="62803" iconid="70" guid="Roll" comment="Roll">
                <Param name="Animation" value="Simple3D" />
                <Param name="RotateA" value="right" />
                <Param name="RotateCenterA" value="lowerright" />
            </Transition>
            <Transition nameID="62809" iconid="76" guid="Shatter, In" comment="Shatter, In">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="ScatterDirection" value="in" />
                <Param name="MaxParticles" value="600" />
                <Param name="SpinDirection" value="right" />
                <Param name="ParticleSpeed" value="400.0" />
                <Param name="ParticleSpinSpeed" value="0.5" />
                <Param name="ExponentialProgressDuration" value="0.9" />
                <Param name="ExponentialProgressScale" value="25" />
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
                <Param name="ExponentialProgressScale" value="0.33" />
            </Transition>
            <Transition nameID="62811" iconid="79" guid="Shatter, Up Right" comment="Shatter, Up Right">
                <Param name="Animation" value="ParticleSystem" />
                <Param name="DepthBufferFormat" value="80" />
                <Param name="MaxParticles" value="700" />
                <Param name="PulseMode" value="out" />
                <Param name="ScatterDirection" value="up, right" />
            </Transition>
            <Transition nameID="62812" iconid="71" guid="Shrink, In" comment="Shrink, In">
                <Param name="Animation" value="Simple3D" />
                <Param name="ScaleA" value="smaller" />
                <Param name="ZScaleAStart" value="0.5" />
                <Param name="FadeStartA" value="0.5" />
            </Transition>
            <Transition nameID="62801" iconid="72" guid="Slide" comment="Slide">
                <Param name="Animation" value="Simple3D" />
                <Param name="MoveA" value="up" />
            </Transition>
            <Transition nameID="62802" iconid="73" guid="Slide, Up Center" comment="Slide, Up Center">
                <Param name="Animation" value="Simple3D" />
                <Param name="MoveA" value="up" />
                <Param name="ScaleA" value="smaller" />
                <Param name="MoveSpeedA" value="0.75" />
            </Transition>
            <Transition nameID="62804" iconid="74" guid="Spin" comment="Spin">
                <Param name="Animation" value="Simple3D" />
                <Param name="ScaleA" value="smaller" />
                <Param name="RotateA" value="left" />
                <Param name="FadeStartA" value="0.2" />
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
            <Transition nameID="62777" iconid="92" guid="Dissolve, Rough" comment="Dissolve, Rough">
                <Param name="Animation" value="Dissolve" />
                <Param name="DepthBufferFormat" value="75" />
                <Param name="DissolveType" value="Rough2D" />
            </Transition>
            <Transition nameID="62778" iconid="93" guid="Dissolve, Vertical" comment="Dissolve, Vertical">
                <Param name="Animation" value="Dissolve" />
                <Param name="DepthBufferFormat" value="75" />
                <Param name="DissolveType" value="VerticalBars" />
            </Transition>
        </TransitionDLL>
    </Transitions>
</TransitionsAndEffects>
```



## Related topics

<dl> <dt>

[**Transition and Effect Objects Provided by Windows Movie Maker**](transition-and-effect-objects-provided-by-windows-movie-maker.md)
</dt> </dl>

 

 




