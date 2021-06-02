---
description: The SetDefaultTransition method sets the default transition. If the render engine cannot render a transition, it substitutes the default transition.
ms.assetid: 5ee84a12-402f-4f1c-9f08-206431c7ecdb
title: IAMTimeline::SetDefaultTransition method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.SetDefaultTransition
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::SetDefaultTransition method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SetDefaultTransition` method sets the default transition. If the render engine cannot render a transition, it substitutes the default transition.

## Syntax


```C++
HRESULT SetDefaultTransition(
   GUID *pGuid
);
```



## Parameters

<dl> <dt>

*pGuid* 
</dt> <dd>

Pointer to a variable that contains the GUID of the default transition.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If you do not set a default transition, or if the transition that you specify as a default causes an error, DES uses its own default transition.

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

 

 




