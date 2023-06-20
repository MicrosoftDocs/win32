---
description: The put\_MaskNum method specifies the SMPTE wipe code of the wipe.
ms.assetid: d2d2382c-d920-49e7-b9b7-6897356a78de
title: IDxtJpeg::put_MaskNum method (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg.put_MaskNum
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IDxtJpeg::put\_MaskNum method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_MaskNum` method specifies the SMPTE wipe code of the wipe.

## Syntax


```C++
HRESULT put_MaskNum(
  [in] long newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Specifies the SMPTE wipe code. For a list of supported SMPTE wipes, see [SMPTE Wipe Transition](smpte-wipe-transition.md).

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

[**IDxtJpeg Interface**](idxtjpeg.md)
</dt> </dl>

 

 




