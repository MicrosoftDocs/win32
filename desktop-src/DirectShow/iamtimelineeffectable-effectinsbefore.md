---
description: The EffectInsBefore method inserts an effect into the object at the specified priority level.
ms.assetid: 6c98e24a-5bac-4273-ae3c-2ab3c9d9465b
title: IAMTimelineEffectable::EffectInsBefore method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineEffectable.EffectInsBefore
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineEffectable::EffectInsBefore method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `EffectInsBefore` method inserts an effect into the object at the specified priority level.

## Syntax


```C++
HRESULT EffectInsBefore(
   IAMTimelineObj *pFX,
   long           Priority
);
```



## Parameters

<dl> <dt>

*pFX* 
</dt> <dd>

Pointer to the [**IAMTimelineObj**](iamtimelineobj.md) interface of the effect.

</dd> <dt>

*Priority* 
</dt> <dd>

Priority level at which to insert the effect. Use the value –1 to insert the effect at the end of the priority list.

</dd> </dl>

## Return value

Returns S\_OK if successful or E\_NOTIMPL if the object is not an effect. Otherwise, returns another **HRESULT** value indicating the cause of the error.

## Remarks

The start and stop times of the effect are clipped within the bounds of the object's time range, if necessary. If there is already an effect at the specified priority level, all the effects from that point on move down the priority list to make room for the new effect.

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

 

 




