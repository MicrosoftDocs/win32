---
description: The put\_Size method sets the output size and stretch mode.
ms.assetid: 1186eee4-b5c1-4216-abb3-86ea03b2da40
title: IResize::put_Size method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize.put_Size
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IResize::put\_Size method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Size` method sets the output size and stretch mode.

## Syntax


```C++
HRESULT put_Size(
  [in] int Height,
  [in] int Width,
  [in] int Flags
);
```



## Parameters

<dl> <dt>

*Height* \[in\]
</dt> <dd>

The video height, in pixels.

</dd> <dt>

*Width* \[in\]
</dt> <dd>

The video width, in pixels.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

The stretch mode. See [**Resize Flags**](resize-flags.md) for possible values.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

DES may call this method before or after calling **put\_MediaType**. If DES calls this method before calling **put\_MediaType**, the filter should select a default value for the bit depth and use the size values to construct an output media type. If DES calls this method after calling **put\_MediaType**, the filter should modify its current output type with the new sizes.

DES may also call this method after the output pin is connected. In that case, modify the output type and reconnect the output pin with the new type. See [Reconnecting Pins](reconnecting-pins.md) for more information.

The *Flags* parameter specifies how the filter should perform the resizing operation.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IResize Interface**](iresize.md)
</dt> </dl>

 

 




