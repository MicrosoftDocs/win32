---
Description: 'Note  This interface is deprecated. New applications should not use it. Creates a stream sample using the specified DirectDraw surface object.'
ms.assetid: '85041c71-f9fc-48fc-8fe2-fec21efb831b'
title: 'IDirectDrawMediaStream::CreateSample method'
---

# IDirectDrawMediaStream::CreateSample method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Creates a stream sample using the specified DirectDraw surface object.

## Syntax


```C++
HRESULT CreateSample(
  [in]        IDirectDrawSurface      *pSurface,
  [in]  const RECT                    *pRect,
  [in]        DWORD                   dwFlags,
  [out]       IDirectDrawStreamSample **ppSample
);
```



## Parameters

<dl> <dt>

*pSurface* \[in\]
</dt> <dd>

Pointer to an existing DirectDraw surface. Use **QueryInterface** to obtain the **IDirectDrawSurface** interface from an **IDirectDrawSurface7** interface pointer.

</dd> <dt>

*pRect* \[in\]
</dt> <dd>

Pointer to the clipping rectangle you want to use with the specified surface. Set this parameter to **NULL** if you want to use the entire surface.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Specifies miscellaneous flags. The following flag is defined:



| Value                    | Description                                                                                                                                                                                                                                             |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DDSFF\_PROGRESSIVERENDER | If this flag is set, sample updates are performed directly on the surface. When this flag is absent, if the decoder uses delta frames, an extra copy is performed internally. Setting this flag can improve performance but can also introduce tearing. |



 

</dd> <dt>

*ppSample* \[out\]
</dt> <dd>

Address of a pointer to an [**IDirectDrawStreamSample**](idirectdrawstreamsample.md) interface that will point to the newly created sample.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                              | Description                                                                                          |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DDERR\_INVALIDPIXELFORMAT**</dt> </dl> | The specified pixel format is incompatible with the stream format.<br/>                        |
| <dl> <dt>**DDERR\_INVALIDRECT**</dt> </dl>        | The specified clipping rectangle is invalid.<br/>                                              |
| <dl> <dt>**DDERR\_INVALIDSURFACETYPE**</dt> </dl> | The specified surface is incompatible with the stream format.<br/>                             |
| <dl> <dt>**E\_POINTER**</dt> </dl>                | One or more of the required parameters is invalid.<br/>                                        |
| <dl> <dt>**MS\_E\_SAMPLEALLOC**</dt> </dl>        | The stream already has allocated samples and the surface doesn't match the sample format.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success.<br/>                                                                                  |



 

## Remarks

This method creates a sample from the current stream and attaches the sample to this surface.

If the stream doesn't have an allocated surface and the specified surface doesn't match the stream's format, this method calls the [**IDirectDrawMediaStream::SetFormat**](idirectdrawmediastream-setformat.md) method on the stream so the two will match.

To perform a progressive render, create a single sample and repeatedly use that sample for successive frames of video. Video decompressors use this technique to do partial updates to the previous frame.

The *pRect* parameter should match the format of the stream (see [**IDirectDrawMediaStream::GetFormat**](idirectdrawmediastream-getformat.md)). If the wrong clip rectangle is set or no clip rectangle is set, and the surface size does not match the movie size, the movie might not play. If a primary surface is used, it is advisable to use a clipping rectangle because the primary surface size can change if the user changes display settings.

## See also

<dl> <dt>

[**IDirectDrawMediaStream Interface**](idirectdrawmediastream.md)
</dt> </dl>

 

 




