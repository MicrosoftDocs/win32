---
description: An XAudio2 client has full control of the mapping from the channels of a voice to the channels of each of its destination voices.
ms.assetid: 219d5b70-3f07-f973-f9ec-1cb3cf0be37e
title: XAudio2 Default Channel Mapping
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Default Channel Mapping

An XAudio2 client has full control of the mapping from the channels of a voice to the channels of each of its destination voices. It controls the mapping through the use of the [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) method. In some circumstances, however, XAudio2 simplifies this task by setting up a default send matrix automatically. It does this by using the channel mask, if any, associated with a voice's audio channels. A channel mask is a combination of SPEAKER\_xxx bit masks as defined in X3DAudio.h and elsewhere. XAudio2 requires channel masks to be 0 or have the same number of bits set as the number of channels.

The following table shows the channel mask requirements and defaults for the formats supported by XAudio2. 

| Format | Channel Mask Requirement             | Default Mask                        | Corresponding Structure Member                            |
|--------|--------------------------------------|-------------------------------------|-----------------------------------------------------------|
| PCM    | File might contain a channel mask    | Channel mask is 0, or absent        | WAVEFORMATEXTENSIBLE.dwChannelMask or none (WAVEFORMATEX) |
| ADPCM  | File does not contain a channel mask | Default Channel Mask is always used | None (ADPCMWAVEFORMAT)                                    |



 

For submix and mastering voices, and for source voices without a channel mask or a channel mask of 0, XAudio2 assumes default speaker positions according to the following table. 

| Channels  | Implicit Channel Positions                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| 1         | Always maps to FrontLeft and FrontRight at full scale in both speakers (special case for mono sounds)                 |
| 2         | FrontLeft, FrontRight (basic stereo configuration)                                                                    |
| 3         | FrontLeft, FrontRight, LowFrequency (2.1 configuration)                                                               |
| 4         | FrontLeft, FrontRight, BackLeft, BackRight (quadraphonic)                                                             |
| 5         | FrontLeft, FrontRight, FrontCenter, SideLeft, SideRight (5.0 configuration)                                           |
| 6         | FrontLeft, FrontRight, FrontCenter, LowFrequency, SideLeft, SideRight (5.1 configuration) (see the following remarks) |
| 7         | FrontLeft, FrontRight, FrontCenter, LowFrequency, SideLeft, SideRight, BackCenter (6.1 configuration)                 |
| 8         | FrontLeft, FrontRight, FrontCenter, LowFrequency, BackLeft, BackRight, SideLeft, SideRight (7.1 configuration)        |
| 9 or more | No implicit positions (one-to-one mapping)                                                                            |



 

If a given voice pair in the audio graph has no speaker positions associated with either its source or target voice (one voice has more than eight channels), neither voice is playable until the source voice has a send matrix set explicitly using the [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) method. Calling the [**IXAudio2SourceVoice::Start**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start) method for either voice will fail until you do this.

If the source voice and target voice have different numbers of speaker positions and [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) has not been called on the source voice, XAudio2 sends each source channel to the nearest target speaker (or speakers) available, proportionally to how close they are to the intended speaker. There are two special cases where the default behavior is different.

1.  If the source audio is mono and is positioned at SPEAKER\_FRONT\_CENTER or has no defined position, it is always sent to SPEAKER\_FRONT\_LEFT and SPEAKER\_FRONT\_RIGHT if they exist in the output audio. If they do not exist, it falls back to the normal case.
2.  If the source and destination are both 6-channel and are positioned at either of the standard 5.1 speaker setups (Left+Right+Center+Sub+BackL+BackR or Left+Right+Center+Sub+SideL+SideR), channels are mapped through one to one. In other words, SideLeft/Right and BackLeft/Right are treated equivalently. This is because there has been historical confusion around these setups. Therefore, the assumed intent is always to map one to one.

## Related topics

<dl> <dt>

[Voices](voices.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[**GetChannelMask**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2masteringvoice-getchannelmask)
</dt> </dl>

 

 
