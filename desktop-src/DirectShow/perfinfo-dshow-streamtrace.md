---
description: The PERFINFO\_DSHOW\_STREAMTRACE structure contains data for a DirectShow trace event of type GUID\_STREAMTRACE.
ms.assetid: 41fbf95c-e86c-4c64-898f-01fbf5f8839c
title: PERFINFO_DSHOW_STREAMTRACE structure (Perfstruct.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PERFINFO_DSHOW_STREAMTRACE
api_type: 
- HeaderDef
api_location: 
- Perfstruct.h
---

# PERFINFO\_DSHOW\_STREAMTRACE structure

The `PERFINFO_DSHOW_STREAMTRACE` structure contains data for a DirectShow trace event of type GUID\_STREAMTRACE.

## Syntax


```C++
typedef struct _PERFINFO_DSHOW_STREAMTRACE {
  ULONG     id;
  ULONG     reserved;
  ULONGLONG dshowClock;
  ULONGLONG data[4];
} PERFINFO_DSHOW_STREAMTRACE, *PPERFINFO_DSHOW_STREAMTRACE;
```



## Members

<dl> <dt>

**id**
</dt> <dd>

Event identifier. See Remarks.

</dd> <dt>

**reserved**
</dt> <dd>

Reserved. Set to zero.

</dd> <dt>

**dshowClock**
</dt> <dd>

Stream time for this event, in 100-nanosecond units. This value is optional and can be zero.

</dd> <dt>

**data**
</dt> <dd>

Optional event data consisting of four **ULONGLONG** values. The meaning of this data depends on the event identifier.

</dd> </dl>

## Remarks

The following event identifiers are defined.




| Event identifier | Description | 
|------------------|-------------|
| PERFINFO_STREAMTRACE_MPEG2DEMUX_PTS_TRANSLATION | Logged when the <a href="mpeg-2-demultiplexer.md">MPEG-2 Demultiplexer</a> filter converts a presentation time stamp (PTS) to stream time.<ul><li><strong>data</strong>[0]: Converted start time.</li><li><strong>data</strong>[1]: Converted stop time.</li><li><strong>data</strong>[2]. Stream identifier for the input pin.</li><li><strong>data</strong>[3]: PTS that was converted.</li></ul> | 
| PERFINFO_STREAMTRACE_MPEG2DEMUX_SAMPLE_RECEIVE | Logged when MPEG-2 Demultiplexer receives a sample.<ul><li><strong>data</strong>[0]: Current time returned by <a href="/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter"><strong>QueryPerformanceCounter</strong></a>.</li></ul> | 
| PERFINFO_STREAMTRACE_VMR_BEGIN_ADVISE | Logged when the VMR schedules a sample for rendering, immediately before the VMR calls <a href="/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-advisetime"><strong>IReferenceClock::AdviseTime</strong></a>.<ul><li><strong>data</strong>[0]: Reference time when streaming began, which corresponds to stream time zero.</li></ul> | 
| PERFINFO_STREAMTRACE_VMR_BEGIN_DECODE | Logged when the VMR begins a decoding operation—that is, when the decoder calls <a href="/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-beginframe"><strong>IAMVideoAccelerator::BeginFrame</strong></a>. No event data. | 
| PERFINFO_STREAMTRACE_VMR_BEGIN_DEINTERLACE | Logged when the VMR begins a deinterlacing or video compositing operation. No event data. | 
| PERFINFO_STREAMTRACE_VMR_DROPPED_FRAME | Logged when the VMR drops a frame; for example, if a sample was late.<ul><li><strong>data</strong>[0]: Sample start time.</li><li><strong>data</strong>[1]: Sample end time.</li></ul> | 
| PERFINFO_STREAMTRACE_VMR_END_ADVISE | Logged when the VMR receives an advise notification from the reference clock. No event data. | 
| PERFINFO_STREAMTRACE_VMR_END_DECODE | Logged when the VMR ends a decoding operation—that is, when the decoder calls <a href="/previous-versions/windows/desktop/api/videoacc/nf-videoacc-iamvideoaccelerator-endframe"><strong>IAMVideoAccelerator::EndFrame</strong></a>. No event data. | 
| PERFINFO_STREAMTRACE_VMR_END_DEINTERLACE | Logged when the VMR completes a deinterlacing or video compositing operation. No event data. | 
| PERFINFO_STREAMTRACE_VMR_RECEIVE | Logged when the VMR receives a new sample. No event data. | 
| PERFINFO_STREAMTRACE_VMR_RENDER_TIME | Logged when the VMR finishes rendering a frame.<ul><li><strong>data</strong>[0]: Time that it took to render this frame.</li><li><strong>data</strong>[1]: Running average of frame rendering times.</li></ul> | 




 

To log this event from a DirectShow filter, use the **PERFLOG\_STREAMTRACE** function, which is defined in the header file Dxmperf.h. This header is included in the DirectShow base classes.

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

 

 
