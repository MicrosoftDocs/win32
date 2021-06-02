---
description: This topic shows you how you can raise or lower the pitch of audio data by changing its rate of playback using the SetFrequencyRatio function on a source voice.
ms.assetid: 93408116-1c1f-307f-7e1f-090f2663ff0b
title: 'How to: Change Voice Pitch'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Change Voice Pitch

This topic shows you how you can raise or lower the pitch of audio data by changing its rate of playback using the [**SetFrequencyRatio**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-setfrequencyratio) function on a source voice.

## To change the pitch of a source voice

1.  Determine the desired frequency ratio for the [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice).

    See [XAudio2 Volume and Pitch Control](xaudio2-volume-and-pitch-control.md) for more information about calculating the frequency ratio.

    ```
    float frequencyRatio = sourceRate / targetRate;
    ```

    

2.  Use the [**SetFrequencyRatio**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-setfrequencyratio) function to set the frequency ratio of the source voice.

    ```
    pSourceVoice->SetFrequencyRatio(frequencyRatio);
    ```

    

## Related topics

<dl> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[XAudio2 Volume and Pitch Control](volume-and-pitch-control.md)
</dt> </dl>

 

 
