---
description: X3DAudio is an API used with XAudio2 to position sound in 3D space to create the illusion of sound coming from a point in space relative to the position of the camera.
ms.assetid: 1638e848-4186-5dea-18e8-5369eee544ae
title: X3DAudio Overview
ms.topic: article
ms.date: 05/31/2018
---

# X3DAudio Overview

X3DAudio is an API used with [XAudio2](programming-guide.md) to position sound in 3D space to create the illusion of sound coming from a point in space relative to the position of the camera.In particular, titles that feature 3D scenes will want to use X3DAudio. Sounds not requiring 3D positioning, such as soundtracks or non-positioned ambient sounds, may bypass X3DAudio completely.

## Listeners and Emitters

To manage sounds in 3D space, X3DAudio employs the concepts of *listeners* and *emitters*. Listeners and emitters represent the position of whatever is hearing 3D sounds, and the point from which those sounds originate.

-   A listener is defined as a point in space and an orientation. It is the position at which the sound is *heard*. The position and orientation of the listener generally is the same as the position and orientation of the camera. This is true whether a title uses a first-person or third-person perspective view. The listener's position is expressed in world coordinates. It is important to note that it is the listener's position *relative* to an emitter that determines how to calculate the final speaker volumes.
-   An emitter is defined as one (or more) points in space from which a sound *originates*. The position of the emitter can be anywhere in 3D space. Like a listener, an emitter's position is expressed in world coordinates. It is the emitter's position *relative* to the listener that determines how the final speaker volumes are calculated.
-   X3DAudio uses left-handed coordinates. To use with right-handed coordinates, developers need to negate the .z element of the OrientTop, OrientFront, Position, and Velocity members of X3DAUDIO\_LISTENER and X3DAUDIO\_EMITTER.

In addition to position, listeners and emitters can include velocity. Unlike a 3D rendering engine, X3DAudio only uses velocity to calculate Doppler effects (it is not used to calculate position).

For more details about listeners and emitters, see the [**X3DAUDIO\_LISTENER**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_listener) and [**X3DAUDIO\_EMITTER**](/windows/desktop/api/x3daudio/ns-x3daudio-x3daudio_emitter) structure reference topics.

## Using X3DAudio with XAudio2

For all interaction between X3DAudio and XAudio2, use the following X3DAudio functions.

-   [**X3DAudioInitialize**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudioinitialize)

    Call the [**X3DAudioInitialize**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudioinitialize) function to initialize X3DAudio. Typically, you only need to call **X3DAudioInitialize** once in the lifetime of a game, unless the speaker configuration is changed.

-   [**X3DAudioCalculate**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudiocalculate)

    After you initialize X3DAudio, you can determine volume and other values for a given sound by passing the sound's emitter and the listener to the [**X3DAudioCalculate**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudiocalculate) function. The values calculated by **X3DAudioCalculate** can then be applied to XAudio2 voices or effects as appropriate for the flags passed to the function. You can apply volume and pitch values calculated by X3DAudio to a voice with the [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) and [**IXAudio2SourceVoice::SetFrequencyRatio**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-setfrequencyratio) methods. Other values calculated by X3DAudio will need to be applied to a [**reverb effect**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createreverb) using the [**IXAudio2Voice::SetEffectParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectparameters) method.

For a step-by-step example of using X3DAudio with XAudio2, see [How to: Integrate X3DAudio with XAudio](how-to--integrate-x3daudio-with-xaudio2.md)

## Related topics

<dl> <dt>

[X3DAudio](x3daudio.md)
</dt> </dl>

 

 
