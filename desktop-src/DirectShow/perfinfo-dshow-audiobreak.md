---
description: The PERFINFO\_DSHOW\_AUDIOBREAK structure contains data for a trace event of type GUID\_AUDIOBREAK.The DirectSound Renderer filter logs this event when there is a break in the audio stream.
ms.assetid: 9e7abdca-7d4c-4006-997f-9605f8d18e1d
title: PERFINFO_DSHOW_AUDIOBREAK structure (Perfstruct.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PERFINFO_DSHOW_AUDIOBREAK
api_type: 
- HeaderDef
api_location: 
- Perfstruct.h
ms.custom: UpdateFrequency5
---

# PERFINFO\_DSHOW\_AUDIOBREAK structure

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PERFINFO_DSHOW_AUDIOBREAK` structure contains data for a trace event of type GUID\_AUDIOBREAK.

The [DirectSound Renderer](directsound-renderer-filter.md) filter logs this event when there is a break in the audio stream.

## Syntax


```C++
typedef struct PERFINFO_DSHOW_AUDIOBREAK {
  ULONGLONG cycleCounter;
  ULONGLONG dshowClock;
  ULONGLONG sampleTime;
  ULONGLONG sampleDuration;
} PERFINFO_DSHOW_AUDIOBREAK, *PPERFINFO_DSHOW_AUDIOBREAK;
```



## Members

<dl> <dt>

**cycleCounter**
</dt> <dd>

Latest clock cycle count (RDTSC instruction).

</dd> <dt>

**dshowClock**
</dt> <dd>

Current write position in the DirectSound buffer.

</dd> <dt>

**sampleTime**
</dt> <dd>

Start of the audio break in the DirectSound buffer.

</dd> <dt>

**sampleDuration**
</dt> <dd>

Duration of the break, in milliseconds.

</dd> </dl>

## Remarks

To enable this event, you must set the AUDIOBREAK\_BIT flag in the *EnableFlag* parameter when you call **EnableTrace**. This flag is defined in the header file Dxmperf.h, which is included in the DirectShow base classes.

To log this event from a DirectShow filter, use the **PERFLOG\_AUDIOBREAK** macro, which is defined in Dxmperf.h.

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

 

 




