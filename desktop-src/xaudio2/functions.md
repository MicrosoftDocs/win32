---
title: XAudio2 functions
description: This section contains information about functions provided by the Microsoft XAudio2 API.
ms.assetid: 870a0425-3226-7848-bcc0-0ba7145135cb
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 functions

This section contains information about functions provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFX**](/windows/desktop/api/XAPOFX/nf-xapofx-createfx)<br/>                                                                     | Creates an instance of the requested [XAPOFX](xapofx-overview.md) effect.<br/>                                                                                                                                                         |
| [**CreateHrtfApo**](/windows/desktop/api/HrtfApoApi/nf-hrtfapoapi-createhrtfapo)<br/>                                                           | Creates an instance of the [**IXAPO**](/windows/desktop/api/XAPO/nn-xapo-ixapo) interface for head-related transfer function (HRTF) processing.<br/>                                                                                                                  |
| [**ReverbConvertI3DL2ToNative**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-reverbconverti3dl2tonative)<br/>                                 | Inline function that converts I3DL2 (Interactive 3D Audio Rendering Guidelines Level 2.0) parameters to native XAudio2 parameters.<br/>                                                                                                 |
| [**X3DAudioCalculate**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudiocalculate)<br/>                                                   | Calculates DSP settings with respect to 3D parameters.<br/>                                                                                                                                                                             |
| [**X3DAudioInitialize**](/windows/desktop/api/x3daudio/nf-x3daudio-x3daudioinitialize)<br/>                                                 | Sets all global 3D audio constants.<br/>                                                                                                                                                                                                |
| [**XAudio2AmplitudeRatioToDecibels**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2amplituderatiotodecibels)<br/>                       | Inline function that converts an amplitude ratio value to a decibel value.<br/>                                                                                                                                                         |
| [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create)<br/>                                                           | Creates a new **XAudio2** object and returns a pointer to its [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) interface.<br/>                                                                                                                              |
| [**XAudio2CreateReverb**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createreverb)<br/>                                               | Creates a new reverb audio processing object (APO), and returns a pointer to it.<br/>                                                                                                                                                   |
| [**XAudio2CreateVolumeMeter**](/windows/desktop/api/xaudio2fx/nf-xaudio2fx-xaudio2createvolumemeter)<br/>                                     | Creates a new volume meter audio processing object (APO) and returns a pointer to it.<br/>                                                                                                                                              |
| [**XAudio2CutoffFrequencyToOnePoleCoefficient**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2cutofffrequencytoonepolecoefficient)<br/> | Inline function that converts from filter cutoff frequencies expressed in hertz to the filter coefficients used with the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters) structure.<br/>   |
| [**XAudio2CutoffFrequencyToRadians**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2cutofffrequencytoradians)<br/>                       | Inline function that converts from filter cutoff frequencies expressed in hertz to the radian frequency values used in the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters) structure.<br/> |
| [**XAudio2DecibelsToAmplitudeRatio**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2decibelstoamplituderatio)<br/>                       | Inline function that converts a decibel value to an amplitude ratio value.<br/>                                                                                                                                                         |
| [**XAudio2FrequencyRatioToSemitones**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2frequencyratiotosemitones)<br/>                     | Inline function that converts a frequency ratio value to a semitone value.<br/>                                                                                                                                                         |
| [**XAudio2RadiansToCutoffFrequency**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2radianstocutofffrequency)<br/>                       | Inline function that converts from the radian frequencies used in [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_filter_parameters) back to absolute frequencies in hertz.<br/>                                                          |
| [**XAudio2SemitonesToFrequencyRatio**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2semitonestofrequencyratio)<br/>                     | Inline function that converts a semitone value to a frequency ratio value.<br/>                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[XAudio2::Programming Reference](programming-reference.md)
</dt> </dl>

 

 




