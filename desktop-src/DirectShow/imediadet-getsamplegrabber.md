---
description: The GetSampleGrabber method retrieves a pointer to the ISampleGrabber interface, which enables an application to retrieve individual samples from a media stream.
ms.assetid: ecfa1909-f1ba-40ac-a0fc-8bfbeed8d148
title: IMediaDet::GetSampleGrabber method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.GetSampleGrabber
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IMediaDet::GetSampleGrabber method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSampleGrabber` method retrieves a pointer to the [**ISampleGrabber**](isamplegrabber.md) interface, which enables an application to retrieve individual samples from a media stream.

## Syntax


```C++
HRESULT GetSampleGrabber(
  [out] ISampleGrabber **ppVal
);
```



## Parameters

<dl> <dt>

*ppVal* \[out\]
</dt> <dd>

Receives a pointer to the [**ISampleGrabber**](isamplegrabber.md) interface.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Call [**IMediaDet::EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md) before calling this method. The [**ISampleGrabber**](isamplegrabber.md) interface enables you to retrieve individual media samples from the stream. If you just need a bitmap from a video frame, call the [**IMediaDet::GetBitmapBits**](imediadet-getbitmapbits.md) method instead. The **ISampleGrabber** interface is more flexible, but requires more work by the application.

If this method succeeds, the [**ISampleGrabber**](isamplegrabber.md) interface that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




