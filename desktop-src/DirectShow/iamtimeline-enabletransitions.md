---
description: The EnableTransitions method enables or disables all transitions in the timeline.
ms.assetid: 8610337a-a247-44f0-8674-3cbc43f636d5
title: IAMTimeline::EnableTransitions method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline.EnableTransitions
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IAMTimeline::EnableTransitions method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `EnableTransitions` method enables or disables all transitions in the timeline. If transitions are disabled, the render engines treats them as cuts; that is, the rendered output jumps instantly from one track to the next. The default cut point is halfway through the duration of the transition. You can change the cut point by calling the [**IAMTimelineTrans::SetCutPoint**](iamtimelinetrans-setcutpoint.md) method on the transition. Disabled transitions are not removed from the timeline.

## Syntax


```C++
HRESULT EnableTransitions(
   BOOL fEnabled
);
```



## Parameters

<dl> <dt>

*fEnabled* 
</dt> <dd>

Boolean value that specifies whether to enable or disable transitions. If **TRUE**, transitions are enabled. If **FALSE**, transitions are disabled.

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

 

 




