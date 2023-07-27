---
description: CDeferredCommand.CDeferredCommand constructor - Constructor method.
ms.assetid: 0b372fa2-78a9-4e38-813c-f18123716c6d
title: CDeferredCommand.CDeferredCommand constructor (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.CDeferredCommand
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDeferredCommand.CDeferredCommand constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CDeferredCommand(
   CCmdQueue *pQ,
   LPUNKNOWN pUnk,
   HRESULT   *phr,
   LPUNKNOWN pUnkExecutor,
   REFTIME   time,
   GUID      *iid,
   long      dispidMethod,
   short     wFlags,
   long      cArgs,
   VARIANT   *pDispParams,
   VARIANT   *pvarResult,
   short     *puArgErr,
   BOOL      bStream
);
```



## Parameters

<dl> <dt>

*pQ* 
</dt> <dd>

Pointer to an object that exposes the [**IQueueCommand**](/windows/desktop/api/Control/nn-control-iqueuecommand) interface.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the outer **IUnknown** interface for aggregation.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a returned **HRESULT** value.

</dd> <dt>

*pUnkExecutor* 
</dt> <dd>

Pointer to the object that will carry out this command.

</dd> <dt>

*time* 
</dt> <dd>

Time at which the command will be run.

</dd> <dt>

*iid* 
</dt> <dd>

Pointer to the globally unique identifier (**GUID**) of the interface that contains the method.

</dd> <dt>

*dispidMethod* 
</dt> <dd>

Method on the interface to call.

</dd> <dt>

*wFlags* 
</dt> <dd>

Context of the invocation.

</dd> <dt>

*cArgs* 
</dt> <dd>

Number of arguments passed.

</dd> <dt>

*pDispParams* 
</dt> <dd>

Pointer to a list of argument variant types.

</dd> <dt>

*pvarResult* 
</dt> <dd>

Pointer to a returned variant type list, if any.

</dd> <dt>

*puArgErr* 
</dt> <dd>

Pointer to the last argument in the *pDispParams* parameter list with an error.

</dd> <dt>

*bStream* 
</dt> <dd>

Value indicating whether the deferred command time is in stream time (**TRUE**) or presentation time (**FALSE**).

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




