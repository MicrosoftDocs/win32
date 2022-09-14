---
description: The EnableEffects method enables or disables all effects in the timeline. If effects are disabled, they remain in the timeline but are not rendered.
ms.assetid: 5344cd49-6515-4211-9637-ca58219b3b56
title: IAMTimeline::EnableEffects method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.EnableEffects
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::EnableEffects method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `EnableEffects` method enables or disables all effects in the timeline. If effects are disabled, they remain in the timeline but are not rendered.

## Syntax


```C++
HRESULT EnableEffects(
   BOOL fEnabled
);
```



## Parameters

<dl> <dt>

*fEnabled* 
</dt> <dd>

Boolean value that specifies whether to enable or disable effects. If **TRUE**, effects are enabled. If **FALSE**, effects are disabled.

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

 

 




