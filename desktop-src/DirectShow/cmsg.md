---
description: The CMsgThread class provides support for a worker thread to which requests can be posted asynchronously instead of sent directly.
ms.assetid: 1cf159c9-80d0-4e3b-88d8-2ba4cd18e768
title: CMsg class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsg
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CMsg class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**CMsgThread**](cmsgthread.md) class provides support for a worker thread to which requests can be posted asynchronously instead of sent directly. The [**CAMThread**](camthread.md) class provides a worker thread to which single requests can be sent. Only one client can make a request at a time, and the client blocks until the worker thread has completed the request. By contrast, the **CMsgThread** class provides a worker thread to which any number of requests can be posted. The requests (in the form of a `CMsg` object) are queued and executed in order, asynchronously. No reply or return value is received.



| Data Members              | Description                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dwFlags                   | Flag parameter to the request code.                                                                                                                                               |
| lpParam                   | Data required by the worker thread as parameter or return values. This data should not be stack-based, as it will be referenced some time after completing the queuing operation. |
| pEvent                    | Event object that a worker thread can signal to indicate the completion of the operation.                                                                                         |
| uMsg                      | Request code that is defined by the client of the thread class and understood by the overridden worker thread function.                                                           |
| Member Functions          | Description                                                                                                                                                                       |
| [**CMsg**](cmsg-cmsg.md) | Constructs a [**CMsg**](cmsg-cmsg.md) object.                                                                                                                                    |



 

 

 



