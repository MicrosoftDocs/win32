---
description: The QueryInternalConnections method retrieves the pins that are connected internally to this pin (within the filter). This method implements the IPin::QueryInternalConnections method.
ms.assetid: 08344fc5-38b2-4dbe-8ef9-30d2fcd64187
title: CBasePin.QueryInternalConnections method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.QueryInternalConnections
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.QueryInternalConnections method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueryInternalConnections` method retrieves the pins that are connected internally to this pin (within the filter). This method implements the [**IPin::QueryInternalConnections**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryinternalconnections) method.

## Syntax


```C++
HRESULT QueryInternalConnections(
   IPin  *apPin,
   ULONG *nPin
);
```



## Parameters

<dl> <dt>

*apPin* 
</dt> <dd>

Address of an array of [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) pointers.

</dd> <dt>

*nPin* 
</dt> <dd>

On input, specifies the size of the array. When the method returns, the value is set to the number of pointers returned in the array.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                               | Description                         |
|-------------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Insufficient array size.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                 |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | Failure.<br/>                 |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Not implemented.<br/>         |



 

## Remarks

On some filters, input pins correspond to particular output pins. For each pin, this method fills an array with pointers to the corresponding pins. If every input pin provides data for every output pin, return E\_NOTIMPL.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




