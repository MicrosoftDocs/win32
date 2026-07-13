---
description: The GetDueCommand method retrieves a pointer to the next command that is due.
ms.assetid: f23434a6-ad2c-4b64-90b1-2f486a16e7e6
title: CCmdQueue.GetDueCommand method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.GetDueCommand
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CCmdQueue.GetDueCommand method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetDueCommand` method retrieves a pointer to the next command that is due.

## Syntax


```C++
virtual HRESULT GetDueCommand(
   CDeferredCommand **ppCmd,
   long             msTimeout
);
```



## Parameters

<dl> <dt>

*ppCmd* 
</dt> <dd>

Address of a pointer to the deferred command.

</dd> <dt>

*msTimeout* 
</dt> <dd>

Amount of time to wait before carrying out the time-out.

</dd> </dl>

## Return value

Returns E\_ABORT if a time-out occurs. Returns S\_OK if successful; otherwise, returns an error. Returns an object that has been incremented using **IUnknown::AddRef**.

## Remarks

This member function blocks until a pending command is due. The member function blocks for the amount of time, in milliseconds, specified in the *msTimeout* parameter. Stream-time commands become due only between the [**CCmdQueue::Run**](ccmdqueue-run.md) and [**CCmdQueue::EndRun**](ccmdqueue-endrun.md) member functions. The command remains queued until run or canceled.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




