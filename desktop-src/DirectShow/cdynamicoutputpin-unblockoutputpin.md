---
description: The UnblockOutputPin method unblocks the pin. When the pin is unblocked, it can deliver samples, change its output format, and reconnect itself.
ms.assetid: ea6e6312-8c7f-44db-ac7f-165dc45dec23
title: CDynamicOutputPin.UnblockOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.UnblockOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDynamicOutputPin.UnblockOutputPin method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `UnblockOutputPin` method unblocks the pin. When the pin is unblocked, it can deliver samples, change its output format, and reconnect itself.

## Syntax


```C++
HRESULT UnblockOutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                           |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Pin was already unblocked.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                   |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




