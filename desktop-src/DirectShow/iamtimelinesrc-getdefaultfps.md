---
description: The GetDefaultFPS method retrieves the source object's default frame rate. The render engine uses this value if it cannot determine the frame rate from the original source.
ms.assetid: c167cd85-e9bb-46ff-9b35-c88898a6c5a3
title: IAMTimelineSrc::GetDefaultFPS method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# IAMTimelineSrc::GetDefaultFPS method

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

 

 




