---
description: The SetOutputBuffering method specifies the number of frames rendered in advance during preview.
ms.assetid: 6e69b196-a6ce-4ce0-8c48-58b1738fb197
title: IAMTimelineGroup::SetOutputBuffering method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.SetOutputBuffering
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::SetOutputBuffering method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetOutputBuffering` method specifies the number of frames rendered in advance during preview.

## Syntax


```C++
HRESULT SetOutputBuffering(
  [in] int nBuffer
);
```



## Parameters

<dl> <dt>

*nBuffer* \[in\]
</dt> <dd>

Number of frames to buffer during preview. Must be two or greater.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

A larger buffer requires more memory but can result in smoother previewing, especially during effects or transitions that require more time to render. The default buffer is 30 frames.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




