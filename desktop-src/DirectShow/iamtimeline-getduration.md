---
description: The GetDuration method retrieves the duration of the timeline.
ms.assetid: d60269b8-597a-4ba4-932a-54b4a36e9a7a
title: IAMTimeline::GetDuration method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetDuration
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::GetDuration method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDuration` method retrieves the duration of the timeline.

## Syntax


```C++
HRESULT GetDuration(
   REFERENCE_TIME *pDuration
);
```



## Parameters

<dl> <dt>

*pDuration* 
</dt> <dd>

Receives the duration of the timeline, in 100-nanosecond units.

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

 

 




