---
description: The SetCutPoint method sets the time at which the transition cuts from one source to the next, if the transition is rendered as a cut.
ms.assetid: 2660f4a8-e249-45d7-8866-02a9f2ef52b8
title: IAMTimelineTrans::SetCutPoint method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.SetCutPoint
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrans::SetCutPoint method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetCutPoint` method sets the time at which the transition cuts from one source to the next, if the transition is rendered as a cut.

## Syntax


```C++
HRESULT SetCutPoint(
   REFERENCE_TIME TLTime
);
```



## Parameters

<dl> <dt>

*TLTime* 
</dt> <dd>

Cut point relative to the start of the transition, in 100-nanosecond units. If the value falls outside the bounds of the transition, it is truncated to the nearest valid time.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

By default, the cut-point is the middle of the transition. For example, in a transition that spans one second, the default cut point is 0.5 seconds into the transition.

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

 

 




