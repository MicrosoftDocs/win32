---
description: Writes the filter's data to the given stream.
ms.assetid: 1b405050-6cfd-4b69-b449-f00a6ecfac6a
title: CPersistStream.WriteToStream method (Pstream.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream.WriteToStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPersistStream.WriteToStream method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Writes the filter's data to the given stream.

## Syntax


```C++
virtual HRESULT WriteToStream(
   IStream *pStream
);
```



## Parameters

<dl> <dt>

*pStream* 
</dt> <dd>

Pointer to an **IStream** interface that specifies the filter data's destination stream.

</dd> </dl>

## Return value

Returns S\_OK. The derived class should return a valid **HRESULT** value.

## Remarks

The default version writes nothing; it can be overridden to write data specific to your class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




