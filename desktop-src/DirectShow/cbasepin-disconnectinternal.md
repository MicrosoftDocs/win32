---
description: The DisconnectInternal method breaks the current pin connection.
ms.assetid: 070301ad-d079-4ad3-abdf-d5de88872e52
title: CBasePin.DisconnectInternal method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.DisconnectInternal
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.DisconnectInternal method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DisconnectInternal` method breaks the current pin connection.

## Syntax


```C++
HRESULT DisconnectInternal();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                         | Description                                                                        |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>             | The pin was not connected.<br/>                                              |
| <dl> <dt>**S\_OK**</dt> </dl>                | Success.<br/>                                                                |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl> | The filter is active and the pin does not support dynamic reconnection.<br/> |



 

## Remarks

The [**CBasePin::Disconnect**](cbasepin-disconnect.md) method delegates the disconnect process to this method. This method calls the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method. It also releases the reference count on the other pin, which is held by the [**CBasePin::m\_Connected**](cbasepin-m-connected.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




