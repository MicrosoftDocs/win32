---
description: The SetDefaultEffectB method sets the default effect. This method is equivalent to IAMTimeline::SetDefaultEffect, but takes a BSTR value, rather than a pointer to a GUID.
ms.assetid: ffee9728-f69e-48a4-ac0a-d41347a20deb
title: IAMTimeline::SetDefaultEffectB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.SetDefaultEffectB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::SetDefaultEffectB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDefaultEffectB` method sets the default effect. This method is equivalent to [**IAMTimeline::SetDefaultEffect**](iamtimeline-setdefaulteffect.md), but takes a BSTR value, rather than a pointer to a GUID.

## Syntax


```C++
HRESULT SetDefaultEffectB(
   BSTR pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

BSTR value representing the GUID of the default effect.

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

 

 




