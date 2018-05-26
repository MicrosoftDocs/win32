---
Description: The MIDI Renderer filter renders MIDI data from the MIDI Parser filter.
ms.assetid: 2675a21d-41d0-4095-96c4-f12f52c00d5a
title: MIDI Renderer Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MIDI Renderer Filter

The MIDI Renderer filter renders MIDI data from the [MIDI Parser](midi-parser-filter.md) filter.



|                                          |                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMClockSlave**](/windows/win32/Strmif/nn-strmif-iamclockslave?branch=master), [**IAMDirectSound**](/windows/win32/Amaudio/nn-amaudio-iamdirectsound?branch=master), [**IAMResourceControl**](/windows/win32/Strmif/nn-strmif-iamresourcecontrol?branch=master), [**IBaseFilter**](/windows/win32/Strmif/nn-strmif-ibasefilter?branch=master), [**IBasicAudio**](/windows/win32/Control/nn-control-ibasicaudio?branch=master), [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master), [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master), [**IReferenceClock**](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master) |
| Input Pin Media Types                    | MEDIATYPE\_Midi, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                                                                                                                  |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/win32/Strmif/nn-strmif-imeminputpin?branch=master), [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master), [**IQualityControl**](/windows/win32/Strmif/nn-strmif-iqualitycontrol?branch=master)                                                                                                                                                                                                                                                                               |
| Output Pin Media Types                   | Not applicable                                                                                                                                                                                                                                                                                                                                                                       |
| Output Pin Interfaces                    | Not applicable                                                                                                                                                                                                                                                                                                                                                                       |
| Filter CLSID                             | CLSID\_AVIMIDIRender                                                                                                                                                                                                                                                                                                                                                                 |
| Property Page CLSID                      | No property page                                                                                                                                                                                                                                                                                                                                                                     |
| Executable                               | quartz.dll                                                                                                                                                                                                                                                                                                                                                                           |
| [Merit](merit.md)                       | MERIT\_PREFERRED                                                                                                                                                                                                                                                                                                                                                                     |
| [Filter Category](filter-categories.md) | CLSID\_MidiRendererCategory                                                                                                                                                                                                                                                                                                                                                          |



 

## Remarks

The GUID for the format type is **NULL**, but the format block contains the following structure:


```C++
typedef struct _MIDIFORMAT {
    DWORD       dwDivision;
    DWORD       dwReserved[7];
} MIDIFORMAT, FAR * LPMIDIFORMAT;
```



The **dwDivision** member specifies the time division of the file. The time division is given in the header of any standard MIDI file (SMF), in the `MThd` chunk. The MIDI Renderer sets this property on the MIDI data stream by calling the **midiStreamProperty** function.

Samples from the MIDI Parser filter contain one second of MIDI data. The MIDI Renderer uses the **midiStreamOut** function to render the MIDI data. Each sample is a synchronization point: the start of the buffer contains all of the commands necessary to set the correct state for rendering that buffer.

## Requirements



|                   |                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.devices.midi.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




