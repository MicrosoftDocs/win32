---
description: The EffectGetCount method retrieves the number of effects on this object.
ms.assetid: 6cf3b5b1-f38f-4ee1-8567-3c55f4f89cbb
title: IAMTimelineEffectable::EffectGetCount method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffectable.EffectGetCount
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineEffectable::EffectGetCount method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `EffectGetCount` method retrieves the number of effects on this object.

## Syntax


```C++
HRESULT EffectGetCount(
   long *pCount
);
```



## Parameters

<dl> <dt>

*pCount* 
</dt> <dd>

Receives the number of effects.

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

[**IAMTimelineEffectable Interface**](iamtimelineeffectable.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




