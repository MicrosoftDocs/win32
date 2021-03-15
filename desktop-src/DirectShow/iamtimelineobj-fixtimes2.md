---
description: The FixTimes2 method rounds the specified start and stop times to the nearest frame boundaries, as defined by the parent group's frame rate setting. This method is equivalent to IAMTimelineObj::FixTimes, but takes REFTIME values.
ms.assetid: bdb3d999-2c91-4108-9286-c6e1f3362c09
title: IAMTimelineObj::FixTimes2 method (Qedit.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.FixTimes2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::FixTimes2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `FixTimes2` method rounds the specified start and stop times to the nearest frame boundaries, as defined by the parent group's frame rate setting. This method is equivalent to [**IAMTimelineObj::FixTimes**](iamtimelineobj-fixtimes.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT FixTimes2(
   REFTIME *pStart,
   REFTIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Pointer to a variable that contains the start time, in seconds. If the call succeeds, this variable is set to the rounded time.

</dd> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that contains the stop time, in seconds. If the call succeeds, this variable is set to the rounded time.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_NOTINTREE if the object is not part of a group.

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




