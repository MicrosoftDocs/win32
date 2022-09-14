---
description: This topic shows you how to use one of the effects included in XAPOFX in an XAudio2 effect chain.
ms.assetid: dc325584-13f7-231a-e0c7-17f38d54ae11
title: 'How to: Use XAPOFX in XAudio2'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Use XAPOFX in XAudio2

This topic shows you how to use one of the effects included in XAPOFX in an XAudio2 effect chain.

## To use an effect from XAPOFX in an XAudio2 effect chain

1.  Create the effect by passing the CLSID of an XAPOFX effect to the [**CreateFX**](/windows/desktop/api/XAPOFX/nf-xapofx-createfx) function.

    In this case, the simplified reverb effect FXReverb is being created.

    ```
    IUnknown * pXAPO;
    CreateFX(__uuidof(FXReverb),&pXAPO);
    ```

    

2.  Populate an [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_descriptor) structure with data.

    ```
    XAUDIO2_EFFECT_DESCRIPTOR descriptor;
    descriptor.InitialState = true;
    descriptor.OutputChannels = 1;
    descriptor.pEffect = pXAPO;
    ```

    

3.  Populate an [**XAUDIO2\_EFFECT\_CHAIN**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_chain) structure with data.

    ```
    XAUDIO2_EFFECT_CHAIN chain;
    chain.EffectCount = 1;
    chain.pEffectDescriptors = &descriptor;
    ```

    

4.  Apply the effect chain to an XAudio2 voice with the [**SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain) function.

    ```
    pVoice->SetEffectChain(&chain);
    ```

    

    > [!Note]  
    > You can also apply an effect chain to a voice when you create the voice by passing the chain as a parameter to [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice), [**IXAudio2::CreateSubmixVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsubmixvoice), or [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice).

     

5.  Release the effect with IUnknown::Release. When you create an XAPO, it will have a reference count of 1. When the XAPO is passed to XAudio2 with [**SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain), XAudio2 increments the reference count on the XAPO. Releasing the client's reference to the XAPO allows XAudio2 to take ownership of the XAPO. If XAudio2 has the only reference to the XAPO, this reference is disposed of when it is no longer being used by XAudio2. If the client code needs to maintain a reference to the XAPO—for example, for reuse later—you can skip this step.

    ```
    pXAPO->Release();
    ```

    

6.  Populate the parameter structure, if any, associated with the effect.

    In this case, the [**FXREVERB\_PARAMETERS**](/windows/desktop/api/xapofx/ns-xapofx-fxreverb_parameters) structure is used to set the diffusion and room size that the reverb effect should use.

    ```
    FXREVERB_PARAMETERS XAPOParameters;
    XAPOParameters.Diffusion = FXREVERB_DEFAULT_DIFFUSION;
    XAPOParameters.RoomSize = FXREVERB_DEFAULT_ROOMSIZE;
    ```

    

7.  Pass the effect parameter structure to the effect by calling the [**SetEffectParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectparameters) function on the voice to which the effect is attached.

    ```
    hr = pVoice->SetEffectParameters( 0, &XAPOParameters, sizeof( FXREVERB_PARAMETERS ) );
    ```

    

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> </dl>

 

 
