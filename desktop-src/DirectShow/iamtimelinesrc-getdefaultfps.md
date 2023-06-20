---
description: The GetDefaultFPS method retrieves the source object's default frame rate. The render engine uses this value if it cannot determine the frame rate from the original source.
ms.assetid: c167cd85-e9bb-46ff-9b35-c88898a6c5a3
title: IAMTimelineSrc::GetDefaultFPS method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetDefaultFPS
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSrc::GetDefaultFPS method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDefaultFPS` method retrieves the source object's default frame rate. The render engine uses this value if it cannot determine the frame rate from the original source.

## Syntax


```C++
HRESULT GetDefaultFPS(
   double *pFPS
);
```



## Parameters

<dl> <dt>

*pFPS* 
</dt> <dd>

Receives the default frame rate, in frames per second.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The default frame rate is not required if the file format specifies the frame rate. This is the case for audio and video formats.

If the source is a bitmap or JPEG image, the render engine uses it as the first image in a device-independent bitmap (DIB) sequence, with a frame rate equal to the default frame rate. To render a static image, rather than a DIB sequence, set the default frame rate to 0.

If the source is a GIF, do not set the frame rate. For animated GIFs, the GIF file specifies the delay between each image.

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




