---
description: The GetCurrentPosition method retrieves the current position, relative to the total duration of the stream. This method implements the IMediaSeeking::GetCurrentPosition method.
ms.assetid: 07020182-2199-4153-9bab-f30d112bc09f
title: CPosPassThru.GetCurrentPosition method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.GetCurrentPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPosPassThru.GetCurrentPosition method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetCurrentPosition` method retrieves the current position, relative to the total duration of the stream. This method implements the [**IMediaSeeking::GetCurrentPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getcurrentposition) method.

## Syntax


```C++
HRESULT GetCurrentPosition(
   LONGLONG *pCurrent
);
```



## Parameters

<dl> <dt>

*pCurrent* 
</dt> <dd>

Pointer to a variable that receives the current position, in units of the current time format.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                               | Description                           |
|-------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Method is not supported.<br/>   |
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/> |



 

## Remarks

This method calls the [**CPosPassThru::GetMediaTime**](cpospassthru-getmediatime.md) method to retrieve the most recent position. If **GetMediaTime** fails, the method calls **IMediaSeeking::GetCurrentPosition** on the connected pin.

The **GetMediaTime** method fails by default in the base class. If your filter caches the current position, override **GetMediaTime** to return the cached value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




