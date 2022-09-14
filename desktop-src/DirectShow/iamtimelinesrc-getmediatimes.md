---
description: The GetMediaTimes method retrieves the media start and stop times.
ms.assetid: c6a7d992-ceb5-4378-aee2-f2d778b41516
title: IAMTimelineSrc::GetMediaTimes method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetMediaTimes
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::GetMediaTimes method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetMediaTimes` method retrieves the media start and stop times.

## Syntax


```C++
HRESULT GetMediaTimes(
   REFERENCE_TIME *pStart,
   REFERENCE_TIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Receives the media start time, in 100-nanosecond units.

</dd> <dt>

*pStop* 
</dt> <dd>

Receives the media stop time, in 100-nanosecond units.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The media times are relative to the original media file. For more information, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

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

 

 




