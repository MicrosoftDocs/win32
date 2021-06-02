---
description: The GetOutputBuffering method retrieves the number of frames rendered in advance during preview.
ms.assetid: 93cb8d18-f1b7-48f9-af41-97f010304b05
title: IAMTimelineGroup::GetOutputBuffering method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineGroup.GetOutputBuffering
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineGroup::GetOutputBuffering method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetOutputBuffering` method retrieves the number of frames rendered in advance during preview.

## Syntax


```C++
HRESULT GetOutputBuffering(
  [out] int *pnBuffer
);
```



## Parameters

<dl> <dt>

*pnBuffer* \[out\]
</dt> <dd>

Receives the number of buffered frames.

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

 

 




