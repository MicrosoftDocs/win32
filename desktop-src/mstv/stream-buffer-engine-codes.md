---
title: Stream Buffer Engine Event Codes
description: Stream Buffer Engine Event Codes
ms.assetid: 84364aa4-7306-40ee-9f4d-0683c47965b5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Engine Event Codes

This topic applies only to Windows XP Service Pack 1 or later.

The Stream Buffer Engine posts the following events to the Filter Graph Manager.



| Event notification code                    | Description                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STREAMBUFFER\_EC\_CONTENT\_BECOMING\_STALE | The Stream Buffer Source has lagged behind the Stream Buffer Sink by more than a pre-set number of backing files. For more information, see [**IStreamBufferConfigure::GetBackingFileCount**](/previous-versions/windows/desktop/api/Sbe/nf-sbe-istreambufferconfigure-getbackingfilecount).                                                                                                                                 |
| STREAMBUFFER\_EC\_PRIMARY\_AUDIO           | The Stream Buffer Engine is processing primarily audio data. This event is sent if video samples are captured at a very low frame rate. This event most often occurs with audio services on a DVB stream, but it might also indicate a problem with capturing or encoding the video. (Applies to Update Rollup 2 for Microsoft Windows XP Media Center Edition 2005 or later.) |
| STREAMBUFFER\_EC\_RATE\_CHANGED            | The playback rate has changed.*param1* = old playback rate x 1000<br/> *param2* = new playback rate x 1000<br/> For example, 2x speed is represented as 2000.<br/>                                                                                                                                                                                           |
| STREAMBUFFER\_EC\_READ\_FAILURE            | A read failure has occurred.*param1* = **HRESULT** code of the failure<br/> *param2* = not used<br/>                                                                                                                                                                                                                                                               |
| STREAMBUFFER\_EC\_STALE\_DATA\_READ        | The Stream Buffer Source is reading a backing file that has been marked for deletion.                                                                                                                                                                                                                                                                                          |
| STREAMBUFFER\_EC\_STALE\_FILE\_DELETED     | A backing file has been deleted.                                                                                                                                                                                                                                                                                                                                               |
| STREAMBUFFER\_EC\_TIMEHOLE                 | The Stream Buffer Source filter has reached a gap in the content.*param1* = Time of the start of the gap, in milliseconds, relative to the content start.<br/> *param2* = Duration of the gap, in milliseconds.<br/>                                                                                                                                               |
| STREAMBUFFER\_EC\_WRITE\_FAILURE           | A write failure has occurred.                                                                                                                                                                                                                                                                                                                                                  |
| SBE2\_STREAM\_DESC\_EVENT (Windows 7)      | An SBE2 stream has been updated. The event data is in a [**DVR\_STREAM\_DESC**](/previous-versions/windows/desktop/api/sbe/ns-sbe-__midl___midl_itf_sbe_0000_0015_0002) structure.                                                                                                                                                                                                                                                                |
| EVENTID\_SBE2RecControlStarted (Windows 7) | An SBE2 [Recording](recording-object.md) object has started recording.                                                                                                                                                                                                                                                                                                        |
| EVENTID\_SBE2RecControlStopped (Windows 7) | An SBE2 [Recording](recording-object.md) object has stopped recording.                                                                                                                                                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Buffering in the Stream Buffer Engine](buffering-in-the-stream-buffer-engine.md)
</dt> <dt>

[Event Notification in DirectShow](https://msdn.microsoft.com/library/windows/desktop/dd375626)
</dt> <dt>

[Stream Buffer Engine Reference](stream-buffer-engine-reference.md)
</dt> </dl>

 

 





