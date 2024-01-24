---
description: An audio effect is an object that takes incoming audio data, and performs some operation on the data before passing it on. You can use an effect to perform a variety of tasks, including adding reverb to an audio stream and monitoring peak volume levels.
ms.assetid: 8c3fa4ca-dcff-bd23-7220-7d0aeb6c6068
title: XAudio2 Audio Effects
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Audio Effects

An audio effect is an object that takes incoming audio data, and performs some operation on the data before passing it on. You can use an effect to perform a variety of tasks, including adding reverb to an audio stream and monitoring peak volume levels.

## Effect Chains

Any XAudio2 voice can host a chain of audio effects. You can use an array of [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_descriptor) structures to specify effect chains. Each descriptor contains a pointer to an effect object provided by the client. These objects must implement the Audio Processing Object (APO) interfaces. See the [XAPO Overview](xapo-overview.md) for more information about the APO model.

Effect chains can be modified by the client dynamically (while the XAudio2 engine is running), effects can be enabled or disabled individually, and effect parameters can be changed—all without any interruption of the audio. Whenever any aspect of the effect graph changes, XAudio2 optimizes the graph again to avoid unnecessary processing. See [**IXAudio2Voice::SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain), [**IXAudio2Voice::EnableEffect**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-enableeffect), and [**IXAudio2Voice::SetEffectParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectparameters).

After an effect is attached to an XAudio2 voice, XAudio2 takes control of the effect, and the client should not make any further calls to it. The simplest way to ensure this is to release all pointers to the effect.

The effects in a given XAudio2 voice's effect chain must consume and produce floating-point audio at that voice's processing sample rate. The only aspect of the audio format they can change is the channel count (for example, a reverb effect can convert mono data to 5.1). The client can use the [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_descriptor).**OutputChannels** field to specify the number of channels that each effect should produce. The effect chain fails if any of the effects cannot fulfill these requirements, or if an effect produces a number of channels that the next effect cannot handle. Any [**IXAudio2Voice::EnableEffect**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-enableeffect) or [**IXAudio2Voice::DisableEffect**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-disableeffect) calls that cause the effect chain to stop fulfilling these requirements will fail.

APO interfaces used in XAudio2 must be *destructive*. This means they always overwrite any data they find in their output buffers. Otherwise, the resulting audio might be incorrect because XAudio2 makes no guarantee that these buffers have been initialized previously with silence.

## XAudio2 Built-in Effects

The following table lists the set of built-in audio effects provided by XAudio2 and their creation methods. 

| Effect       | Creation Method                                              |
|--------------|--------------------------------------------------------------|
| Reverb       | [**XAudio2CreateReverb**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createreverb)           |
| Volume Meter | [**XAudio2CreateVolumeMeter**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createvolumemeter) |



 

For an example of creating and using an instance of an audio effect, see [How to: Create an Effect Chain](how-to--create-an-effect-chain.md).

## Custom Effects in XAudio2

The [XAPO](xapo-overview.md) API provides a framework for creating custom audio effects that you can use in XAudio2. For an example of creating a custom effect with XAPO, see [How to: Create an XAPO](how-to--create-an-xapo.md).

## XAPO Effect Library (XAPOFX)

[XAPOFX](xapofx-overview.md) provides an additional library of XAPOs and common mechanism for creating them. For an example of using XAPOFX with XAudio2, see [How to: Use XAPOFX in XAudio2](how-to--use-xapofx-in-xaudio2.md).

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> </dl>

 

 
