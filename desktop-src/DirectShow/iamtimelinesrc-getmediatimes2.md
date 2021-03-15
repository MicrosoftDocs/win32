---
description: The GetMediaTimes2 method retrieves the media start and stop times. This method is equivalent to IAMTimelineSrc::GetMediaTimes, but takes REFTIME values.
ms.assetid: c3961c2c-7198-44bd-8734-7301a7c5b21e
title: IAMTimelineSrc::GetMediaTimes2 method (Qedit.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.GetMediaTimes2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::GetMediaTimes2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetMediaTimes2` method retrieves the media start and stop times. This method is equivalent to [**IAMTimelineSrc::GetMediaTimes**](iamtimelinesrc-getmediatimes.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT GetMediaTimes2(
   REFTIME *pStart,
   REFTIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Receives the media start time, in seconds.

</dd> <dt>

*pStop* 
</dt> <dd>

Receives the media stop time, in seconds.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




