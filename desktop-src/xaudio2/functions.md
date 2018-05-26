---
Description: This section contains information about functions provided by the Microsoft XAudio2 API.
ms.assetid: 870a0425-3226-7848-bcc0-0ba7145135cb
title: Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

This section contains information about functions provided by the Microsoft XAudio2 API.

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFX**](/windows/win32/XAPOFX/nf-xapofx-createfx?branch=master)<br/>                                                                     | Creates an instance of the requested [XAPOFX](xapofx-overview.md) effect.<br/>                                                                                                                                                         |
| [**CreateHrtfApo**](/windows/win32/HrtfApoApi/nf-hrtfapoapi-createhrtfapo?branch=master)<br/>                                                           | Creates an instance of the [**IXAPO**](/windows/win32/XAPO/nn-xapo-ixapo?branch=master) interface for head-related transfer function (HRTF) processing.<br/>                                                                                                                  |
| [**ReverbConvertI3DL2ToNative**](/windows/win32/xaudio2fx/nf-xaudio2fx-reverbconverti3dl2tonative?branch=master)<br/>                                 | Inline function that converts I3DL2 (Interactive 3D Audio Rendering Guidelines Level 2.0) parameters to native XAudio2 parameters.<br/>                                                                                                 |
| [**X3DAudioCalculate**](/windows/win32/x3daudio/nf-x3daudio-x3daudiocalculate?branch=master)<br/>                                                   | Calculates DSP settings with respect to 3D parameters.<br/>                                                                                                                                                                             |
| [**X3DAudioInitialize**](/windows/win32/x3daudio/nf-x3daudio-x3daudioinitialize?branch=master)<br/>                                                 | Sets all global 3D audio constants.<br/>                                                                                                                                                                                                |
| [**XAudio2AmplitudeRatioToDecibels**](/windows/win32/xaudio2/nf-xaudio2-xaudio2amplituderatiotodecibels?branch=master)<br/>                       | Inline function that converts an amplitude ratio value to a decibel value.<br/>                                                                                                                                                         |
| [**XAudio2Create**](/windows/win32/xaudio2/nf-xaudio2-xaudio2create?branch=master)<br/>                                                           | Creates a new **XAudio2** object and returns a pointer to its [**IXAudio2**](/windows/win32/xaudio2/nn-xaudio2-ixaudio2?branch=master) interface.<br/>                                                                                                                              |
| [**XAudio2CreateReverb**](/windows/win32/xaudio2fx/nf-xaudio2fx-xaudio2createreverb?branch=master)<br/>                                               | Creates a new reverb audio processing object (APO), and returns a pointer to it.<br/>                                                                                                                                                   |
| [**XAudio2CreateVolumeMeter**](/windows/win32/xaudio2fx/nf-xaudio2fx-xaudio2createvolumemeter?branch=master)<br/>                                     | Creates a new volume meter audio processing object (APO) and returns a pointer to it.<br/>                                                                                                                                              |
| [**XAudio2CutoffFrequencyToOnePoleCoefficient**](/windows/win32/xaudio2/nf-xaudio2-xaudio2cutofffrequencytoonepolecoefficient?branch=master)<br/> | Inline function that converts from filter cutoff frequencies expressed in hertz to the filter coefficients used with the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_filter_parameters?branch=master) structure.<br/>   |
| [**XAudio2CutoffFrequencyToRadians**](/windows/win32/xaudio2/nf-xaudio2-xaudio2cutofffrequencytoradians?branch=master)<br/>                       | Inline function that converts from filter cutoff frequencies expressed in hertz to the radian frequency values used in the **Frequency** member of the [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_filter_parameters?branch=master) structure.<br/> |
| [**XAudio2DecibelsToAmplitudeRatio**](/windows/win32/xaudio2/nf-xaudio2-xaudio2decibelstoamplituderatio?branch=master)<br/>                       | Inline function that converts a decibel value to an amplitude ratio value.<br/>                                                                                                                                                         |
| [**XAudio2FrequencyRatioToSemitones**](/windows/win32/xaudio2/nf-xaudio2-xaudio2frequencyratiotosemitones?branch=master)<br/>                     | Inline function that converts a frequency ratio value to a semitone value.<br/>                                                                                                                                                         |
| [**XAudio2RadiansToCutoffFrequency**](/windows/win32/xaudio2/nf-xaudio2-xaudio2radianstocutofffrequency?branch=master)<br/>                       | Inline function that converts from the radian frequencies used in [**XAUDIO2\_FILTER\_PARAMETERS**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_filter_parameters?branch=master) back to absolute frequencies in hertz.<br/>                                                          |
| [**XAudio2SemitonesToFrequencyRatio**](/windows/win32/xaudio2/nf-xaudio2-xaudio2semitonestofrequencyratio?branch=master)<br/>                     | Inline function that converts a semitone value to a frequency ratio value.<br/>                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[XAudio2::Programming Reference](programming-reference.md)
</dt> </dl>

 

 




