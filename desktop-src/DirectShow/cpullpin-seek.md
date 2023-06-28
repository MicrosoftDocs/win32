---
description: The Seek method sets the start and stop positions of the stream.
ms.assetid: d84476f5-688c-429d-a51b-7020a6316e35
title: CPullPin.Seek method (Pullpin.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPullPin.Seek
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPullPin.Seek method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Seek` method sets the start and stop positions of the stream.

## Syntax


```C++
HRESULT Seek(
   REFERENCE_TIME tStart,
   REFERENCE_TIME tStop
);
```



## Parameters

<dl> <dt>

*tStart* 
</dt> <dd>

Specifies the start position, in bytes multiplied by 10,000,000.

</dd> <dt>

*tStop* 
</dt> <dd>

Specifies the stop position, in bytes multiplied by 10,000,000.

</dd> </dl>

## Return value

Returns S\_OK if the method succeeds, or an error code otherwise.

## Remarks

If the worker thread is running, the method pauses the thread, flushes the filter graph, and resumes the thread. The thread begins pulling data from the new start position. Otherwise, the new position values become effective whenever the thread is started.

Positions are relative to the start of the original source. Multiply the desired byte offsets by the constant UNITS, which is defined in the base class library as 10,000,000.

When the pin first connects, the stop and start positions default to the beginning and end of the stream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pullpin.h</dt> </dl>                                                                                                       |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPullPin Class**](cpullpin.md)
</dt> </dl>

 

 




