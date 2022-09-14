---
description: The GetOutputFPS method retrieves the output frame rate of this group.
ms.assetid: e6dfa4a9-4d44-4ce7-9aec-3564fd337ff6
title: IAMTimelineGroup::GetOutputFPS method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetOutputFPS
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetOutputFPS method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetOutputFPS` method retrieves the output frame rate of this group.

## Syntax


```C++
HRESULT GetOutputFPS(
   double *pFPS
);
```



## Parameters

<dl> <dt>

*pFPS* 
</dt> <dd>

Receives the output frame rate, in frames per second.

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

[**IAMTimelineGroup Interface**](iamtimelinegroup.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




