---
description: The TransGetCount method retrieves the number of transitions on this object.
ms.assetid: f7fb4a99-c841-4680-b7f1-e4d887f12707
title: IAMTimelineTransable::TransGetCount method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTransable.TransGetCount
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTransable::TransGetCount method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `TransGetCount` method retrieves the number of transitions on this object.

## Syntax


```C++
HRESULT TransGetCount(
   long *pCount
);
```



## Parameters

<dl> <dt>

*pCount* 
</dt> <dd>

Receives the number of transitions.

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

[**IAMTimelineTransable Interface**](iamtimelinetransable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




