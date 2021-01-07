---
description: This topic shows you how you can change the volume of a voice at an overall level, at each output channel, or between each channel of a voice and another voice in its sendlist.
ms.assetid: 40004128-4abb-4bcd-fe76-91276be8abec
title: 'How to: Change Voice Volume'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Change Voice Volume

This topic shows you how you can change the volume of a voice at an overall level, at each output channel, or between each channel of a voice and another voice in its [**sendlist**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_voice_sends).

## To set an overall volume level for the voice's input

-   Use the [**SetVolume**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setvolume) function.

    ```
    pSourceVoice->SetVolume(1.0);
    ```

    

## To set the volume of the voice's output channels

1.  Create an array of floating point numbers that contain the desired volumes of all the output channels in the voice.

    The array will have one entry for each channel in the voice.

    ```
    float SourceVoiceChannelVolumes[1] = {1.0};
    ```

    

2.  Use the [**SetChannelVolumes**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setchannelvolumes) function to set the volume of the output channels.

    ```
    hr = pSourceVoice->SetChannelVolumes(1,SourceVoiceChannelVolumes);
    ```

    

## To set the volume of connections

Set the connection volume between the voice and a voice in its [**sendlist**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_voice_sends).

1.  Create an array of floating point numbers that defines an output matrix if the voice sends to another voice.

    > [!Note]  
    > The array must have a number of entries equal to source voice channels × destination voice channels. In this example, the mapping is from a voice with one channel to a voice with two channels.

     

    ```
    float outputMatrix[2] = {1.0f,0.05f};
    ```

    

2.  Use the [**SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) function to set the output matrix.

    ```
    pSourceVoice->SetOutputMatrix(pSubmixVoice,1,2,outputMatrix);
    ```

    

## Related topics

<dl> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[XAudio2 Volume and Pitch Control](volume-and-pitch-control.md)
</dt> </dl>

 

 
