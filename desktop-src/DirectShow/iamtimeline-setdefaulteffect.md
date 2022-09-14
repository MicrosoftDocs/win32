---
description: The SetDefaultEffect method sets the default effect. If the render engine cannot render an effect, it substitutes the default effect.
ms.assetid: 6ee94d86-c27f-4378-9a10-f3993a3ae657
title: IAMTimeline::SetDefaultEffect method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.SetDefaultEffect
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::SetDefaultEffect method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDefaultEffect` method sets the default effect. If the render engine cannot render an effect, it substitutes the default effect.

## Syntax


```C++
HRESULT SetDefaultEffect(
   GUID *pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Pointer to the GUID of the default effect.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If you do not set a default effect, or if the effect that you specify as a default causes an error, DES uses its own default effect.

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

 

 




