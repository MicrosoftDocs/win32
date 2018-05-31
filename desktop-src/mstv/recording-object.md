---
title: Recording Object
description: Recording Object
ms.assetid: 717a3b99-d998-4e64-aab6-6b06e18991da
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Recording Object

This topic applies only to Windows XP Service Pack 1 or later.

The **Recording** object creates permanent recordings from streams that the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter captures.



|            |                                                                                                                                              |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| CLSID      | Not applicable; see Remarks.                                                                                                                 |
| Interfaces | [**IStreamBufferRecordControl**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferrecordcontrol), [**IStreamBufferRecordingAttribute**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferrecordingattribute) |



 

## Remarks

To create this object, call the [**IStreamBufferSink::CreateRecorder**](/previous-versions/windows/desktop/api/Sbe/nf-sbe-istreambuffersink-createrecorder) method on the Stream Buffer Sink filter.

After making a recording, stop the **Recording** object and release it before releasing the Stream Buffer Sink filter.

## Related topics

<dl> <dt>

[Creating Stream Buffer Recordings](creating-stream-buffer-recordings.md)
</dt> <dt>

[Stream Buffer Engine Objects](stream-buffer-engine-objects.md)
</dt> </dl>

 

 




