---
description: The EffectSwapPriorities method switches the priority levels of two effects.
ms.assetid: ff5ab294-3963-4df7-9299-ee7c7165e72f
title: IAMTimelineEffectable::EffectSwapPriorities method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffectable.EffectSwapPriorities
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineEffectable::EffectSwapPriorities method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `EffectSwapPriorities` method switches the priority levels of two effects.

Given two priority values, this method swaps the effects at those priorities. When the method returns, the effect that was at the first priority level is at the second priority level, and vice versa.

## Syntax


```C++
HRESULT EffectSwapPriorities(
   long PriorityA,
   long PriorityB
);
```



## Parameters

<dl> <dt>

*PriorityA* 
</dt> <dd>

First priority level at which to swap effects.

</dd> <dt>

*PriorityB* 
</dt> <dd>

Second priority level at which to swap effects.

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

 

 




