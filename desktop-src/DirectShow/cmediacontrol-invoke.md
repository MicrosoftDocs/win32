---
description: CMediaControl.Invoke method - Provides access to properties and methods exposed by an object.
ms.assetid: 05006f1e-24ff-4ed2-8291-2ba48495fec0
title: CMediaControl.Invoke method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaControl.Invoke
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaControl.Invoke method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides access to properties and methods exposed by an object.

## Syntax


```C++
HRESULT Invoke(
   DISPID     dispidMember,
   REFIID     riid,
   LCID       lcid,
   WORD       wFlags,
   DISPPARAMS *pdispparams,
   VARIANT    *pvarResult,
   EXCEPINFO  *pexcepinfo,
   UINT       *puArgErr
);
```



## Parameters

<dl> <dt>

*dispidMember* 
</dt> <dd>

Identifier of the member. Use [**CMediaControl::GetIDsOfNames**](cmediacontrol-getidsofnames.md) or the object's documentation to obtain the dispatch identifier.

</dd> <dt>

*riid* 
</dt> <dd>

Reserved for future use. Must be IID\_NULL.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale context in which to interpret arguments.

</dd> <dt>

*wFlags* 
</dt> <dd>

Flags describing the context of the `CMediaControl::Invoke` call.

</dd> <dt>

*pdispparams* 
</dt> <dd>

Pointer to a structure containing an array of arguments, an array of argument dispatch IDs for named arguments, and counts for number of elements in the arrays.

</dd> <dt>

*pvarResult* 
</dt> <dd>

Pointer to where the result is to be stored, or **NULL** if the caller expects no result.

</dd> <dt>

*pexcepinfo* 
</dt> <dd>

Pointer to a structure containing exception information.

</dd> <dt>

*puArgErr* 
</dt> <dd>

Pointer to the index of the first argument, within the **DISPPARAMS** structure's **rgvarg** array, that has an error. For more information on **DISPPARAMS**, see the Platform SDK.

</dd> </dl>

## Return value

Returns DISP\_E\_UNKNOWNINTERFACE if *riid* is not IID\_NULL. Returns one of the error codes from [**CMediaControl::GetTypeInfo**](cmediacontrol-gettypeinfo.md) if the call fails. Otherwise, returns the **HRESULT** from the call to **IDispatch::Invoke**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




