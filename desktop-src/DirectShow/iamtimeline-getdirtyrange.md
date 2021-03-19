---
description: Not supported.
ms.assetid: 6e45b542-be3f-4da8-808a-6aa8b4299519
title: IAMTimeline::GetDirtyRange method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetDirtyRange
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::GetDirtyRange method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

Not supported.

## Syntax


```C++
HRESULT GetDirtyRange(
   REFERENCE_TIME *pStart,
   REFERENCE_TIME *pStop
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Reserved.

</dd> <dt>

*pStop* 
</dt> <dd>

Reserved.

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
</dt> </dl>

 

 




