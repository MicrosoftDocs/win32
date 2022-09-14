---
description: XAPOFX is a collection of audio effects implementing the XAPO interfaces for use in XAudio2. XAPOFX contains several effects, and a common mechanism for creating effect instances.
ms.assetid: 762062de-4e19-5e42-8059-e2f8741bd362
title: XAPOFX Overview
ms.topic: article
ms.date: 05/31/2018
---

# XAPOFX Overview

XAPOFX is a collection of audio effects implementing the [XAPO](xapo-overview.md) interfaces for use in XAudio2. XAPOFX contains several effects, and a common mechanism for creating effect instances.

## Included Effects

The following table describes the effects included in XAPOFX. 

| Effect             | Description                                                                                                                                                                                           | Parameter Structure                                                     | Parameter Constants                                              | Requirements                                                                                                              |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| FXECHO             | An echo effect.                                                                                                                                                                                       | [**FXECHO\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxecho_parameters)                         | [**FXECHO Constants**](fxecho-constants.md)                     | Only supports FLOAT32 audio formats.                                                                                      |
| FXEQ               | A four band equalizer.                                                                                                                                                                                | [**FXEQ\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxeq_parameters)                             | [**FXEQ Constants**](fxeq-constants.md)                         | Only supports FLOAT32 audio formats. The sample rate must be between 22,000 Hz and 48,000 Hz.                             |
| FXMasteringLimiter | A volume limiter.                                                                                                                                                                                     | [**FXMASTERINGLIMITER\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxmasteringlimiter_parameters) | [**FXMASTERINGLIMIT Constants**](fxmasteringlimit-constants.md) | Only supports FLOAT32 audio formats.                                                                                      |
| FXReverb           | A simple reverb effect.<br/> XAudio2 also provides an effect implementing Princeton Digital Reverb that can be instantiated with [**XAudio2CreateReverb**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createreverb).<br/> | [**FXREVERB\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxreverb_parameters)                     | [**FXREVERB Constants**](fxreverb-constants.md)                 | Only supports FLOAT32 audio formats. Also, it only supports mono input to mono output, and stereo input to stereo output. |



 

## Creating an Instance of an Effect Included in XAPOFX

XAPOFX provides the [**CreateFX**](/windows/desktop/api/XAPOFX/nf-xapofx-createfx) function as a common mechanism for creating effect instances. **CreateFX** takes the CLSID of an effect, and returns an IUnknown interface pointer to an instance of the effect.

## Using XAPOFX in XAudio2

Effects instantiated with [**CreateFX**](/windows/desktop/api/XAPOFX/nf-xapofx-createfx) are used in XAudio2 by attaching them to voices. Each XAudio2 voice has an effect chain containing zero or more audio effects. Audio data sent to a voice is passed through each effect in the chain before it is sent to the voice's output targets. The voice takes the output of each effect, and feeds it into the next effect in the chain until no effects are left in the chain. To attach an XAPOFX effect to an XAudio2 voice, fill out an [**XAUDIO2\_EFFECT\_CHAIN**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_chain) structure with the effect's information, and pass it to [**IXAudio2Voice::SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain).

For more information about XAudio2 effect chains, see [XAudio2 Audio Effects](xaudio2-audio-effects.md).

For an example of using XAPOFX in XAudio2, see [How to: Use XAPOFX in XAudio2](how-to--use-xapofx-in-xaudio2.md).

## XAudio2 Implicit Effects

In addition to the library of XAPOs provided by XAPOFX, XAudio2 has built-in reverb and volume meter audio effects. You can create these built-in effects with [**XAudio2CreateReverb**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createreverb) and [**XAudio2CreateVolumeMeter**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createvolumemeter). See [How to: Create an Effect Chain](how-to--create-an-effect-chain.md) for an example of using one of these built-in effects.

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> </dl>

 

 
