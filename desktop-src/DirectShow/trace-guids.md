---
Description: The following GUIDs are used for event tracing in DirectShow.
ms.assetid: 438938fe-37e7-45d6-b49a-d96698307f25
title: Trace GUIDs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Trace GUIDs

The following GUIDs are used for event tracing in DirectShow.



| GUID                                                                                                                                                                   | Description                                                                                                                                                  |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GUID_AUDIOBREAK"></span><span id="guid_audiobreak"></span><dl> <dt>**GUID\_AUDIOBREAK**</dt> </dl>    | Audio break event. Events of this type use the [**PERFINFO\_DSHOW\_AUDIOBREAK**](perfinfo-dshow-audiobreak.md) structure for event data.<br/>         |
| <span id="GUID_DSHOW_CTL"></span><span id="guid_dshow_ctl"></span><dl> <dt>**GUID\_DSHOW\_CTL**</dt> </dl>      | DirectShow event provider.<br/>                                                                                                                        |
| <span id="GUID_STREAMTRACE"></span><span id="guid_streamtrace"></span><dl> <dt>**GUID\_STREAMTRACE**</dt> </dl> | General streaming event. Events of this type use the [**PERFINFO\_DSHOW\_STREAMTRACE**](perfinfo-dshow-streamtrace.md) structure for event data.<br/> |
| <span id="GUID_VIDEOREND"></span><span id="guid_videorend"></span><dl> <dt>**GUID\_VIDEOREND**</dt> </dl>       | Video rendering event. Events of this type use the [**PERFINFO\_DSHOW\_AVREND**](perfinfo-dshow-avrend.md) structure for event data.<br/>             |



## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PerfStruct.h</dt> </dl> |



## See also

<dl> <dt>

[Event Tracing in DirectShow](event-tracing-in-directshow.md)
</dt> </dl>

 

 




