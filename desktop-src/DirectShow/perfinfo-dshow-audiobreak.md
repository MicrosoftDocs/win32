---
description: The PERFINFO\_DSHOW\_AUDIOBREAK structure contains data for a trace event of type GUID\_AUDIOBREAK.The DirectSound Renderer filter logs this event when there is a break in the audio stream.
ms.assetid: 9e7abdca-7d4c-4006-997f-9605f8d18e1d
title: PERFINFO_DSHOW_AUDIOBREAK structure (Perfstruct.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PERFINFO_DSHOW_AUDIOBREAK
api_type: 
- HeaderDef
api_location: 
- Perfstruct.h
---

# PERFINFO\_DSHOW\_AUDIOBREAK structure

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

 

 




