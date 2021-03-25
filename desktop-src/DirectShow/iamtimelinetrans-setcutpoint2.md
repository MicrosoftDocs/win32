---
description: The SetCutPoint2 method sets the time at which the transition cuts from one source to the next, if the transition is rendered as a cut. This method is equivalent to IAMTimelineTrans::SetCutPoint, but takes a REFTIME value.
ms.assetid: d06d3ee7-04a2-4266-9995-bfabea24aef9
title: IAMTimelineTrans::SetCutPoint2 method (Qedit.h) (2)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.SetCutPoint2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrans::SetCutPoint2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetCutPoint2` method sets the time at which the transition cuts from one source to the next, if the transition is rendered as a cut. This method is equivalent to [**IAMTimelineTrans::SetCutPoint**](iamtimelinetrans-setcutpoint.md), but takes a [**REFTIME**](reftime.md) value.

## Syntax


```C++
HRESULT SetCutPoint2(
   REFTIME TLTime
);
```



## Parameters

<dl> <dt>

*TLTime* 
</dt> <dd>

Cut point relative to the start of the transition, in seconds.

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

[**IAMTimelineTrans Interface**](iamtimelinetrans.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




