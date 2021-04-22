---
description: The MIDI Renderer filter renders MIDI data from the MIDI Parser filter.
ms.assetid: 2675a21d-41d0-4095-96c4-f12f52c00d5a
title: MIDI Renderer Filter (Windows.devices.midi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MIDI
api_type: 
- HeaderDef
api_location: 
- windows.devices.midi.h
---

# MIDI Renderer Filter

The MIDI Renderer filter renders MIDI data from the [MIDI Parser](midi-parser-filter.md) filter.



| Label | Value |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMClockSlave**](/windows/desktop/api/Strmif/nn-strmif-iamclockslave), [**IAMDirectSound**](/previous-versions/windows/desktop/api/Amaudio/nn-amaudio-iamdirectsound), [**IAMResourceControl**](/windows/desktop/api/Strmif/nn-strmif-iamresourcecontrol), [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter), [**IBasicAudio**](/windows/desktop/api/Control/nn-control-ibasicaudio), [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition), [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol), [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) |
| Input Pin Media Types                    | MEDIATYPE\_Midi, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                                                                                                                  |
| Input Pin Interfaces                     | [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin), [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin), [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol)                                                                                                                                                                                                                                                                               |
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



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.devices.midi.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 




