---
description: The PERFINFO\_DSHOW\_AVREND structure contains data for a trace event of type GUID\_VIDEOREND.The VMR logs this event immediately before rendering a frame.
ms.assetid: 95deda21-0ef4-4bf0-9fa3-826a813757b9
title: PERFINFO_DSHOW_AVREND structure (Perfstruct.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PERFINFO_DSHOW_AVREND
api_type: 
- HeaderDef
api_location: 
- Perfstruct.h
ms.custom: UpdateFrequency5
---

# PERFINFO\_DSHOW\_AVREND structure

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PERFINFO_DSHOW_AVREND` structure contains data for a trace event of type GUID\_VIDEOREND.

The VMR logs this event immediately before rendering a frame.

## Syntax


```C++
typedef struct PERFINFO_DSHOW_AVREND {
  ULONGLONG cycleCounter;
  ULONGLONG dshowClock;
  ULONGLONG sampleTime;
} PERFINFO_DSHOW_AVREND, *PPERFINFO_DSHOW_AVREND;
```



## Members

<dl> <dt>

**cycleCounter**
</dt> <dd>

Latest clock cycle count (RDTSC instruction).

</dd> <dt>

**dshowClock**
</dt> <dd>

Current reference time, as returned by the [**IReferenceClock::GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) method.

</dd> <dt>

**sampleTime**
</dt> <dd>

Start time of the sample.

</dd> </dl>

## Remarks

To enable this event, you must set the DXMPERF\_VIDEOREND flag in the *EnableFlag* parameter when you call **EnableTrace**. This flag is defined in the header file Dxmperf.h, which is included in the DirectShow base classes.

To log this event from a DirectShow filter, use the **PERFLOG\_VIDEOREND** macro, which is defined in Dxmperf.h.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Perfstruct.h</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Structures](directshow-structures.md)
</dt> <dt>

[Event Tracing in DirectShow](event-tracing-in-directshow.md)
</dt> <dt>

[Trace Event GUIDs](trace-guids.md)
</dt> </dl>

 

 




