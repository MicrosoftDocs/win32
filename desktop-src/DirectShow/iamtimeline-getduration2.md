---
description: The GetDuration2 method retrieves the duration of the timeline. This method is equivalent to IAMTimeline::GetDuration, but takes a parameter of type double.
ms.assetid: 49f5eed3-7fab-4f08-b65c-300349b197cb
title: IAMTimeline::GetDuration2 method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetDuration2
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::GetDuration2 method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDuration2` method retrieves the duration of the timeline. This method is equivalent to [**IAMTimeline::GetDuration**](iamtimeline-getduration.md), but takes a parameter of type **double**.

## Syntax


```C++
HRESULT GetDuration2(
   double *pDuration
);
```



## Parameters

<dl> <dt>

*pDuration* 
</dt> <dd>

Receives the duration of the timeline, in fractional seconds.

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

[**IAMTimeline Interface**](iamtimeline.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




