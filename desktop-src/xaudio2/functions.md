---
Description: 'This section contains information about functions provided by the Microsoft XAudio2 API.'
ms.assetid: '870a0425-3226-7848-bcc0-0ba7145135cb'
title: Functions
---

# Functions

This section contains information about functions provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFX**](createfx.md)<br/>                                                                     | Creates an instance of the requested [XAPOFX](xapofx-overview.md) effect.<br/>                                                                                                                                                         |
| [**CreateHrtfApo**](createhrtfapo.md)<br/>                                                           | Creates an instance of the [**IXAPO**](ixapo.md) interface for head-related transfer function (HRTF) processing.<br/>                                                                                                                  |
| [**ReverbConvertI3DL2ToNative**](reverbconverti3dl2tonative.md)<br/>                                 | Inline function that converts I3DL2 (Interactive 3D Audio Rendering Guidelines Level 2.0) parameters to native XAudio2 parameters.<br/>                                                                                                 |
| [**X3DAudioCalculate**](x3daudiocalculate.md)<br/>                                                   | Calculates DSP settings with respect to 3D parameters.<br/>                                                                                                                                                                             |
| [**X3DAudioInitialize**](x3daudioinitialize.md)<br/>                                                 | Sets all global 3D audio constants.<br/>                                                                                                                                                                                                |
| [**XAudio2AmplitudeRatioToDecibels**](xaudio2amplituderatiotodecibels.md)<br/>                       | Inline function that converts an amplitude ratio value to a decibel value.<br/>                                                                                                                                                         |
| [**XAudio2Create**](xaudio2create.md)<br/>                                                           | Creates a new **XAudio2** object and returns a pointer to its [**IXAudio2**](ixaudio2.md) interface.<br/>                                                                                                                              |
| [**XAudio2CreateReverb**](xaudio2createreverb.md)<br/>                                               | Creates a new reverb audio processing object (APO), and returns a pointer to it.<br/>                                                                                                                                                   |
| [**XAudio2CreateVolumeMeter**](xaudio2createvolumemeter.md)<br/>                                     | Creates a new volume meter audio processing object (APO) and returns a pointer to it.<br/>                                                                                                                                              |
| [**XAudio2CutoffFrequencyToOnePoleCoefficient**](xaudio2cutofffrequencytoonepolecoefficient.md)<br/> | Inline function that converts from filter cutoff frequencies expressed in hertz to the filter coefficients used with the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](xaudio2-filter-parameters.md) structure.<br/>   |
| [**XAudio2CutoffFrequencyToRadians**](xaudio2cutofffrequencytoradians.md)<br/>                       | Inline function that converts from filter cutoff frequencies expressed in hertz to the radian frequency values used in the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](xaudio2-filter-parameters.md) structure.<br/> |
| [**XAudio2DecibelsToAmplitudeRatio**](xaudio2decibelstoamplituderatio.md)<br/>                       | Inline function that converts a decibel value to an amplitude ratio value.<br/>                                                                                                                                                         |
| [**XAudio2FrequencyRatioToSemitones**](xaudio2frequencyratiotosemitones.md)<br/>                     | Inline function that converts a frequency ratio value to a semitone value.<br/>                                                                                                                                                         |
| [**XAudio2RadiansToCutoffFrequency**](xaudio2radianstocutofffrequency.md)<br/>                       | Inline function that converts from the radian frequencies used in [**XAUDIO2\_FILTER\_PARAMETERS**](xaudio2-filter-parameters.md) back to absolute frequencies in hertz.<br/>                                                          |
| [**XAudio2SemitonesToFrequencyRatio**](xaudio2semitonestofrequencyratio.md)<br/>                     | Inline function that converts a semitone value to a frequency ratio value.<br/>                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[XAudio2::Programming Reference](programming-reference.md)
</dt> </dl>

 

 




