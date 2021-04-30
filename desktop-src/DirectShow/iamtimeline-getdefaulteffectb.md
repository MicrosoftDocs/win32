---
description: The GetDefaultEffectB method retrieves the default effect. This method is equivalent to IAMTimeline::GetDefaultEffect, but receives a BSTR value rather than a GUID.
ms.assetid: 62c37a61-9875-4140-8552-83d82c060715
title: IAMTimeline::GetDefaultEffectB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.GetDefaultEffectB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::GetDefaultEffectB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetDefaultEffectB` method retrieves the default effect. This method is equivalent to [**IAMTimeline::GetDefaultEffect**](iamtimeline-getdefaulteffect.md), but receives a **BSTR** value rather than a GUID.

## Syntax


```C++
HRESULT GetDefaultEffectB(
  [out, retval] BSTR *pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* \[out, retval\]
</dt> <dd>

Receives a **BSTR** value representing the GUID of the default effect.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

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

 

 




