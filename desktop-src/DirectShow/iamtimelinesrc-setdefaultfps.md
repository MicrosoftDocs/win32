---
description: The SetDefaultFPS method sets the source object's default frame rate.
ms.assetid: ea93acde-3e05-43d5-8130-9ab2ee841b4e
title: IAMTimelineSrc::SetDefaultFPS method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SetDefaultFPS
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimelineSrc::SetDefaultFPS method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDefaultFPS` method sets the source object's default frame rate.

## Syntax


```C++
HRESULT SetDefaultFPS(
   double FPS
);
```



## Parameters

<dl> <dt>

*FPS* 
</dt> <dd>

Default frame rate, in frames per second.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_INVALIDARG if the specified frame rate is less than zero.

## Remarks

The render engine uses this value if it cannot determine the frame rate from the original source file.

Call this method only for source files without a predefined frame rate. For bitmap and JPEG files, the default frame rate is zero, which causes the source to be rendered as a still image. To use the image as the first frame in a DIB sequence set the frame rate to a value greater than zero. For more information, see [Working with Sources](working-with-sources.md).

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

 

 




