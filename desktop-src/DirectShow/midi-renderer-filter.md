---
Description: 'The MIDI Renderer filter renders MIDI data from the MIDI Parser filter.'
ms.assetid: '2675a21d-41d0-4095-96c4-f12f52c00d5a'
title: MIDI Renderer Filter
---

# MIDI Renderer Filter

The MIDI Renderer filter renders MIDI data from the [MIDI Parser](midi-parser-filter.md) filter.



|                                          |                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMClockSlave**](iamclockslave.md), [**IAMDirectSound**](iamdirectsound.md), [**IAMResourceControl**](iamresourcecontrol.md), [**IBaseFilter**](ibasefilter.md), [**IBasicAudio**](ibasicaudio.md), [**IMediaPosition**](imediaposition.md), [**IMediaSeeking**](imediaseeking.md), [**IQualityControl**](iqualitycontrol.md), [**IReferenceClock**](ireferenceclock.md) |
| Input Pin Media Types                    | MEDIATYPE\_Midi, MEDIASUBTYPE\_NULL                                                                                                                                                                                                                                                                                                                                                  |
| Input Pin Interfaces                     | [**IMemInputPin**](imeminputpin.md), [**IPin**](ipin.md), [**IQualityControl**](iqualitycontrol.md)                                                                                                                                                                                                                                                                               |
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

 

 




