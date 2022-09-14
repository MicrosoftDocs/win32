---
description: The FixTimes method rounds the specified start and stop times to the nearest frame boundaries, as defined by the parent group's frame rate setting.
ms.assetid: 033ac221-7616-4c62-937e-c5585bc73a16
title: IAMTimelineObj::FixTimes method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineObj.FixTimes
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineObj::FixTimes method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `FixTimes` method rounds the specified start and stop times to the nearest frame boundaries, as defined by the parent group's frame rate setting.

## Syntax


```C++
HRESULT FixTimes(
   REFERENCE_TIME *pStart,
   REFERENCE_TIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Pointer to a variable that contains the start time, in 100-nanosecond units. If the call succeeds, this variable is set to the rounded time.

</dd> <dt>

*pStop* 
</dt> <dd>

Pointer to a variable that contains the stop time, in 100-nanosecond units. If the call succeeds, this variable is set to the rounded time.

</dd> </dl>

## Return value

Returns S\_OK if successful, or E\_NOTINTREE if the object is not part of a group.

## Remarks

During rendering, DES rounds the object's start and stop times to the nearest frame boundary. However, DES does not overwrite the object's times. If you change the group frame rate, the rounded times are always calculated from the original times. For more information, see [Time in DirectShow Editing Services](time-in-directshow-editing-services.md).

Use this method to determine accurate start and stop times in the rendered project. For example, you should seek to the rounded times, rather than the object's original start and stop times. Call [**IAMTimelineObj::GetStartStop**](iamtimelineobj-getstartstop.md) to obtain the original times, and pass those values to `FixTimes`.

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

[**IAMTimelineObj Interface**](iamtimelineobj.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




