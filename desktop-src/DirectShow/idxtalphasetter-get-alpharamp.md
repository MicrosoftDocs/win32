---
description: The get\_AlphaRamp method retrieves the alpha ramp property. The alpha ramp is the percentage by which the alpha values in the original image are adjusted. For example, if the alpha ramp is 0.5, the alpha values in the image are reduced 50%.
ms.assetid: e142a562-2e78-4418-94e9-b41320d4af57
title: IDxtAlphaSetter::get_AlphaRamp method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtAlphaSetter.get_AlphaRamp
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IDxtAlphaSetter::get\_AlphaRamp method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_AlphaRamp` method retrieves the alpha ramp property. The alpha ramp is the percentage by which the alpha values in the original image are adjusted. For example, if the alpha ramp is 0.5, the alpha values in the image are reduced 50%.

## Syntax


```C++
HRESULT get_AlphaRamp(
  [out, retval] double *pAlpha
);
```



## Parameters

<dl> <dt>

*pAlpha* \[out, retval\]
</dt> <dd>

Receives the alpha ramp. A negative value indicates that no alpha ramp is set.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                               | Description                          |
|-------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success<br/>                   |



 

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

[**IDxtAlphaSetter Interface**](idxtalphasetter.md)
</dt> </dl>

 

 




