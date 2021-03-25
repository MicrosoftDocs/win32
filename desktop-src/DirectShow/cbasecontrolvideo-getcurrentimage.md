---
description: The GetCurrentImage method retrieves a copy of the current image at the renderer.
ms.assetid: fa322bd2-18e4-481d-bde1-92deb0f7de61
title: CBaseControlVideo.GetCurrentImage method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.GetCurrentImage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.GetCurrentImage method

The `GetCurrentImage` method retrieves a copy of the current image at the renderer.

## Syntax


```C++
HRESULT GetCurrentImage(
   long *pBufferSize,
   long *pVideoImage
);
```



## Parameters

<dl> <dt>

*pBufferSize* 
</dt> <dd>

Pointer to the size of the output buffer.

</dd> <dt>

*pVideoImage* 
</dt> <dd>

Pointer to the output buffer for the image.

</dd> </dl>

## Return value

Returns an **HRESULT** value that depends on the implementation; can be one of the following values, or other values not listed.



| Return code                                                                                        | Description                                                                       |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Failure.<br/>                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Invalid argument.<br/>                                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Out of memory. Returned when the *pVideoInfo* parameter is **NULL**.<br/>   |
| <dl> <dt>**NOERROR**</dt> </dl>             | Success.<br/>                                                               |
| <dl> <dt>**VFW\_E\_NOT\_PAUSED**</dt> </dl> | The operation could not be performed because the filter is not paused.<br/> |



 

## Remarks

This member function retrieves the image from the sample and copies it into the output buffer. The section of video copied into the output buffer reflects the source rectangle set through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface. It does not reflect the destination rectangle.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




