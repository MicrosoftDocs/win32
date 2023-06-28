---
description: The CanSeekBackward method determines whether the stream can be seeked backward. This method implements the IMediaPosition::CanSeekBackward method.
ms.assetid: 6443980f-6863-4941-b2dd-4a31257b5810
title: CPosPassThru.CanSeekBackward method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.CanSeekBackward
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPosPassThru.CanSeekBackward method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CanSeekBackward` method determines whether the stream can be seeked backward. This method implements the [**IMediaPosition::CanSeekBackward**](/windows/desktop/api/Control/nf-control-imediaposition-canseekbackward) method.

## Syntax


```C++
HRESULT CanSeekBackward(
   LONG *pCanSeekBackward
);
```



## Parameters

<dl> <dt>

*pCanSeekBackward* 
</dt> <dd>

Pointer to a variable that receives the value OATRUE if the filter can seek backward, or OAFALSE otherwise.

</dd> </dl>

## Return value

Returns the **HRESULT** value from the connected pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




