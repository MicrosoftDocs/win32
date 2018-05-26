---
Description: The GetStartStop2 method retrieves the objects start and stop times, relative to the objects parent. This method is equivalent to IAMTimelineObjGetStartStop, but takes REFTIME values.
ms.assetid: 140842f5-3a24-4947-a360-ef97cba414ee
title: IAMTimelineObjGetStartStop2 method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAMTimelineObj::GetStartStop2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetStartStop2` method retrieves the object's start and stop times, relative to the object's parent. This method is equivalent to [**IAMTimelineObj::GetStartStop**](iamtimelineobj-getstartstop.md), but takes [**REFTIME**](reftime.md) values.

## Syntax


```C++
HRESULT GetStartStop2(
   REFTIME *pStart,
   REFTIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Receives the start time, in seconds.

</dd> <dt>

*pStop* 
</dt> <dd>

Receives the stop time, in seconds.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](http://go.microsoft.com/fwlink/p/?linkid=129787). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

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

 

 




