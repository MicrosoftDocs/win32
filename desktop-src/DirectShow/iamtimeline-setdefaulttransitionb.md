---
description: The SetDefaultTransitionB method sets the default transition. This method is equivalent to IAMTimeline::SetDefaultTransition, but takes a BSTR value, rather than a pointer to a GUID.
ms.assetid: 1998fd31-2ab8-477e-89ee-93ca92dc10ec
title: IAMTimeline::SetDefaultTransitionB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.SetDefaultTransitionB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::SetDefaultTransitionB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDefaultTransitionB` method sets the default transition. This method is equivalent to [**IAMTimeline::SetDefaultTransition**](iamtimeline-setdefaulttransition.md), but takes a BSTR value, rather than a pointer to a GUID.

## Syntax


```C++
HRESULT SetDefaultTransitionB(
   BSTR pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

BSTR value representing the GUID of the default transition.

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

 

 




