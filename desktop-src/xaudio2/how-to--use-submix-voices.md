---
Description: This topic shows you how you can set groups of voices to send their output to the same submix voice. This enables a single change to a submix voice to affect a whole group of voices.
ms.assetid: 76c1c138-4846-9c4f-7875-446867436ee9
title: How to Use Submix Voices
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to: Use Submix Voices

This topic shows you how you can set groups of voices to send their output to the same submix voice. This enables a single change to a submix voice to affect a whole group of voices.

1.  Create a [**submix voice**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2submixvoice?branch=master) to which all of the game's sound effect voices will send.
    ```
    IXAudio2SubmixVoice * pSFXSubmixVoice;
    pXAudio2->CreateSubmixVoice(&amp;pSFXSubmixVoice,1,44100,0,0,0,0);
    ```

    

2.  Create an [**XAUDIO2\_VOICE\_SENDS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_voice_sends?branch=master) structure that contains a reference to the submix voice.
    ```
    XAUDIO2_SEND_DESCRIPTOR SFXSend = {0, pSFXSubmixVoice};
    XAUDIO2_VOICE_SENDS SFXSendList = {1, &amp;SFXSend};
    ```

    

3.  Pass the [**XAUDIO2\_VOICE\_SENDS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_voice_sends?branch=master) structure to new source voices as they are created.
    ```
    IXAudio2SourceVoice* pSFXSourceVoice;
    if( FAILED(hr = pXaudio2->CreateSourceVoice( &amp;pSFXSourceVoice, (WAVEFORMATEX*)&amp;wfx,
        0, XAUDIO2_DEFAULT_FREQ_RATIO, pCallback, pSFXSendList, NULL ) ) )
        return hr;
    ```

    

4.  Apply changes to all sound effect voices by adjusting the submix voice.

    In this example, changing the volume of the submix voice with the [**SetVolume**](ixaudio2voice-interface-setvolume.md) function effectively changes the volume of all voices that output to it.

    ```
    pSFXSubmixVoice->SetVolume(0.1);
    ```

    

## Related topics

<dl> <dt>

[Voices](voices.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> </dl>

 

 



