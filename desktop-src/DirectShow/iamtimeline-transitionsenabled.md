---
description: The TransitionsEnabled method determines whether transitions are enabled.
ms.assetid: c961d8d7-4509-444b-a49f-6ab79fc31f7e
title: IAMTimeline::TransitionsEnabled method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.TransitionsEnabled
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::TransitionsEnabled method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The **TransitionsEnabled** method determines whether transitions are enabled.

## Syntax


```C++
HRESULT TransitionsEnabled(
   BOOL *pfEnabled
);
```



## Parameters

<dl> <dt>

*pfEnabled* 
</dt> <dd>

Receives a Boolean value. If **TRUE**, transitions are enabled. Otherwise, transitions are disabled.

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

[**IAMTimeline::EnableTransitions**](iamtimeline-enabletransitions.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




