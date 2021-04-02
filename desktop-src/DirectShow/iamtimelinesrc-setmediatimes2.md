---
description: The SetMediaTimes2 method sets the media stop and start times. This method is equivalent to IAMTimelineSrc::SetMediaTimes, but takes REFTIME values.
ms.assetid: 9eea7965-46c5-416c-97df-134d29130c8a
title: IAMTimelineSrc::SetMediaTimes2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.SetMediaTimes2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::SetMediaTimes2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetMediaTimes2` method sets the media stop and start times. This method is equivalent to [**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT SetMediaTimes2(
   REFTIME Start,
   REFTIME Stop
);
```



## Parameters

<dl> <dt>

*Start* 
</dt> <dd>

Media start time, in seconds.

</dd> <dt>

*Stop* 
</dt> <dd>

Media stop time, in seconds.

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

[**IAMTimelineSrc Interface**](iamtimelinesrc.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




