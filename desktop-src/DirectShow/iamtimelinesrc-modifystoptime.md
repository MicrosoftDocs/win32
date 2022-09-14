---
description: The ModifyStopTime method sets the stop time, relative to the timeline.
ms.assetid: 0d9b6cf7-d029-4c35-9045-82cbeff1e3ae
title: IAMTimelineSrc::ModifyStopTime method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineSrc.ModifyStopTime
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineSrc::ModifyStopTime method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `ModifyStopTime` method sets the stop time, relative to the timeline.

## Syntax


```C++
HRESULT ModifyStopTime(
   REFERENCE_TIME Stop
);
```



## Parameters

<dl> <dt>

*Stop* 
</dt> <dd>

New stop time, in 100-nanosecond units.

</dd> </dl>

## Return value

Returns S\_OK, or E\_INVALIDARG if the specified time is not valid.

## Remarks

This method is equivalent to calling [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md) with the original start time and a new stop time.

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

 

 




