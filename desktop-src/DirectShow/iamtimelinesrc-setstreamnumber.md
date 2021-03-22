---
description: The SetStreamNumber method specifies which stream to read from the source file associated with this source object.
ms.assetid: d40d0889-3b28-4114-9dd2-529e380eaeb8
title: IAMTimelineSrc::SetStreamNumber method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SetStreamNumber
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::SetStreamNumber method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetStreamNumber` method specifies which stream to read from the source file associated with this source object.

## Syntax


```C++
HRESULT SetStreamNumber(
   long Val
);
```



## Parameters

<dl> <dt>

*Val* 
</dt> <dd>

The stream number, from the set of streams matching the media type of the parent group.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The *Val* parameter specifies a stream number from the set of streams that matches the parent group's media type, not from the entire set of streams in the source file. For example, For example, suppose that a file contains two video streams and two audio streams. If the source object is inside a video group, setting *Val* to 0 selects the first video stream. The caller is responsible for specifying a valid stream number.

The stream number defaults to zero.

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

 

 




