---
description: The GetCutsOnly method determines whether the transition is rendered as a cut. If so, the transition occurs instantaneously at the cut point.
ms.assetid: d7959816-1152-4bc4-b3f8-bed69b450530
title: IAMTimelineTrans::GetCutsOnly method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.GetCutsOnly
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrans::GetCutsOnly method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetCutsOnly` method determines whether the transition is rendered as a cut. If so, the transition occurs instantaneously at the cut point.

## Syntax


```C++
HRESULT GetCutsOnly(
   BOOL *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives a Boolean value specifying whether the transition is rendered as a cut. If **TRUE**, the transition is an instantaneous cut. If **FALSE**, the transition occurs over its normal duration.

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

[**IAMTimelineTrans::SetCutsOnly**](iamtimelinetrans-setcutsonly.md)
</dt> <dt>

[**IAMTimelineTrans::GetCutPoint**](iamtimelinetrans-getcutpoint.md)
</dt> <dt>

[**IAMTimeline::TransitionsEnabled**](iamtimeline-transitionsenabled.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




