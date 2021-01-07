---
description: This topic describes XAudio2 volume and pitch control.
ms.assetid: dedc2d01-af83-d7d2-5b64-743dcebc83f7
title: XAudio2 Volume and Pitch Control
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Volume and Pitch Control

This topic describes XAudio2 volume and pitch control.

## Volume Control

Volume levels are expressed as floating-point amplitude multipliers between -XAUDIO2\_MAX\_VOLUME\_LEVEL and XAUDIO2\_MAX\_VOLUME\_LEVEL (-224 to 224), with a maximum gain of 144.5 dB. A volume of 1.0 means there is no attenuation or gain; 0 means silence; and negative levels can be used to invert the audio's phase. Two inline functions are provided in XAudio2.h to convert between volume units: [**XAudio2DecibelsToAmplitudeRatio**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2decibelstoamplituderatio) and [**XAudio2AmplitudeRatioToDecibels**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2amplituderatiotodecibels).

You can apply a volume level to the audio at several points as it flows through the XAudio2 graph:

-   All voice types apply an overall volume level to their input, which they control using the [**IXAudio2Voice::SetVolume**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setvolume) method. In submix and mastering voices, the overall volume level is applied just before the voice's built-in filter and effect chain. In source voices, the overall volume level is applied after the voice's built-in filter and effect chain.
-   Voices apply a per-channel volume level to their output, which they control using the [**IXAudio2Voice::SetChannelVolumes**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setchannelvolumes) method. The per-channel volume level is applied just after the voice's final sample rate conversion, and before it is sent to other voices.
-   Every connection between one voice and another has a table of levels used to send audio from each source channel to each target channel, which is controlled using the [**IXAudio2Voice::SetOutputMatrix**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voice-setoutputmatrix) method.

All overall volumes and channel volumes default to 1.0 initially. All send-level matrices default to appropriate values that preserve signal power and channel positioning as accurately as possible. See the [XAudio2 Default Channel Mapping](xaudio2-default-channel-mapping.md) overview for details.

> [!Note]  
> XAudio2 automatically adjusts volume levels based on the user's speaker settings to maintain a consistent volume level across configurations. If the user's settings don't match their physical configuration the volume will either be too loud or too soft compared to a system with accurate settings. For example, a system configured for 5.1 surround sound speakers that only has two speakers connected will sound too soft. XAudio2 is unable to detect whether the user speaker settings correctly match their physical setup.

 

## Pitch Control

Pitches are expressed as input rate/output rate ratios between 1/1,024 and 1,024/1, inclusive. A ratio of 1/1,024 lowers pitch by 10 octaves, while a ratio of 1,024/1 raises it by 10 octaves. You can only use the [**IXAudio2SourceVoice::SetFrequencyRatio**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-setfrequencyratio) method to apply pitch adjustments to source voices, and only if they were not created with the XAUDIO2\_VOICE\_NOPITCH flag. The default frequency ratio is 1/1: that is, no pitch change. Two inline functions are provided in XAudio2.h to convert between frequency ratios and semitones: [**XAudio2FrequencyRatioToSemitones**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2frequencyratiotosemitones) and [**XAudio2SemitonesToFrequencyRatio**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2semitonestofrequencyratio).

## Related topics

<dl> <dt>

[Volume and Pitch Control](volume-and-pitch-control.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Change Voice Pitch](how-to--change-voice-pitch.md)
</dt> <dt>

[How to: Change Voice Volume](how-to--change-voice-volume.md)
</dt> </dl>

 

 
