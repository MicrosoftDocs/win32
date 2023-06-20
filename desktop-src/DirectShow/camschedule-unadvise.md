---
description: The Unadvise method removes an advise request.
ms.assetid: b3dfda82-577e-4499-a114-1c8721e4af9e
title: CAMSchedule.Unadvise method (Dsschedule.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMSchedule.Unadvise
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMSchedule.Unadvise method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Unadvise` method removes an advise request.

## Syntax


```C++
HRESULT Unadvise(
   DWORD_PTR dwAdviseCookie
);
```



## Parameters

<dl> <dt>

*dwAdviseCookie* 
</dt> <dd>

Identifier of the advise request, returned by the [**CAMSchedule::AddAdvisePacket**](camschedule-addadvisepacket.md) method.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description          |
|-----------------------------------------------------------------------------------------|----------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Not found<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success<br/>   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Dsschedule.h (include Streams.h)</dt> </dl>                                                                                |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMSchedule Class**](camschedule.md)
</dt> </dl>

 

 




