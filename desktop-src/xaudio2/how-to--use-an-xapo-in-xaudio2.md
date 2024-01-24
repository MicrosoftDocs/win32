---
description: This topic shows you how to use an effect created with the XAPO API in an XAudio2 effect chain.
ms.assetid: d4d24177-25eb-13ca-0e38-0c876a273e0d
title: 'How to: Use an XAPO in XAudio2'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Use an XAPO in XAudio2

This topic shows you how to use an effect created with the XAPO API in an XAudio2 effect chain.

1.  Create the XAPO as described in [How to: Create an XAPO](how-to--create-an-xapo.md).

    You can also implement run-time parameter functionality as described in [How to: Add Run-time Parameter Support to an XAPO](how-to--add-run-time-parameter-support-to-an-xapo.md).

2.  Create an instance of the XAPO.

    ```
    IUnknown * pXAPO;
    pXAPO = new SimpleXAPO();
    ```

    

3.  Populate an [**XAUDIO2\_EFFECT\_DESCRIPTOR**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_descriptor) structure with data.

    ```
    XAUDIO2_EFFECT_DESCRIPTOR descriptor;
    descriptor.InitialState = true;
    descriptor.OutputChannels = 1;
    descriptor.pEffect = pXAPO;
    ```

    

4.  Populate an [**XAUDIO2\_EFFECT\_CHAIN**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_effect_chain) structure with data.

    ```
    XAUDIO2_EFFECT_CHAIN chain;
    chain.EffectCount = 1;
    chain.pEffectDescriptors = &descriptor;
    ```

    

5.  Apply the effect chain to an XAudio2 voice with the [**SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain) function.

    ```
    pVoice->SetEffectChain(&chain);
    ```

    

    > [!Note]  
    > An effect chain can also be applied to a voice when the voice is created by passing the chain as a parameter to [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice), [**IXAudio2::CreateSubmixVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsubmixvoice), or [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice).

     

6.  Release the effect with IUnknown::Release.

    When you create an XAPO, it will have a reference count of 1. When the XAPO is passed to XAudio2 with [**SetEffectChain**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectchain), XAudio2 increments the reference count on the XAPO. Releasing the client's reference to the XAPO allows XAudio2 to take ownership of the XAPO. If XAudio2 has the only reference to the XAPO, it will be disposed of when it is no longer being used by XAudio2. If the client code needs to maintain a reference to the XAPO for later reuse, for example, you should skip this step.

    ```
    pXAPO->Release();
    ```

    

7.  Populate the parameter structure, if any, associated with the effect. In this case, the percentage of full strength at which the effect should be applied.

    ```
    XAPO_PARAMETERS XAPOParameters;
    XAPOParameters.Level = 0.75;
    ```

    

8.  Pass the effect parameter structure to the effect by calling the [**SetEffectParameters**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-seteffectparameters) function on the voice to which the effect is attached.

    ```
    hr = pVoice->SetEffectParameters( 0, &XAPOParameters, sizeof( XAPO_PARAMETERS ) );
    ```

    

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAPO Overview](xapo-overview.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> </dl>

 

 
