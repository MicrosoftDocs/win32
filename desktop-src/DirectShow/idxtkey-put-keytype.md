---
description: The put\_KeyType method specifies the type of key.
ms.assetid: 4a6201e6-1939-4da6-8c9f-1c34b9713ecb
title: IDxtKey::put_KeyType method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.put_KeyType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IDxtKey::put\_KeyType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_KeyType` method specifies the type of key.

## Syntax


```C++
HRESULT put_KeyType(
  [in] int newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Specifies the key type. This parameter must be one of the following enumeration values.



| Value             | Description                                           |
|-------------------|-------------------------------------------------------|
| DXTKEY\_RGB       | Chroma key. (Key on RGB value.)                       |
| DXTKEY\_NONRED    | Nonred key. (Makes blue and green areas transparent.) |
| DXTKEY\_LUMINANCE | Luminance key.                                        |
| DXTKEY\_ALPHA     | Key by alpha value.                                   |
| DXTKEY\_HUE       | Key by hue.                                           |



 

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

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

[**IDxtKey Interface**](idxtkey.md)
</dt> </dl>

 

 




