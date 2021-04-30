---
description: The GetSwapInputs method retrieves a value that indicates whether the transition inputs are swapped.
ms.assetid: 84cb5c3d-7c3a-4c35-aac7-97d812d99a38
title: IAMTimelineTrans::GetSwapInputs method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimelineTrans.GetSwapInputs
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimelineTrans::GetSwapInputs method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetSwapInputs` method retrieves a value that indicates whether the transition inputs are swapped.

By default, a transition goes from the composite of all lower-priority layers to the layer where the transition resides. You can reverse this progression, so the transition goes from the layer where it resides back to the composite of lower-priority layers.

## Syntax


```C++
HRESULT GetSwapInputs(
   BOOL *pVal
);
```



## Parameters

<dl> <dt>

*pVal* 
</dt> <dd>

Receives a Boolean value. If the value is **FALSE**, the transition goes from the composite of all lower-priority layers to the transition layer. If the value is **TRUE**, the transition goes in the opposite direction. The default value is **FALSE**.

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

[**IAMTimelineTrans Interface**](iamtimelinetrans.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




