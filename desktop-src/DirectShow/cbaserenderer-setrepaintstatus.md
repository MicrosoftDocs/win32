---
description: The SetRepaintStatus method enables or disables repaint events.
ms.assetid: 94ae4935-459e-4009-9f64-c7c5b14504ae
title: CBaseRenderer.SetRepaintStatus method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SetRepaintStatus
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.SetRepaintStatus method

The `SetRepaintStatus` method enables or disables repaint events.

## Syntax


```C++
void SetRepaintStatus(
   BOOL bRepaint
);
```



## Parameters

<dl> <dt>

*bRepaint* 
</dt> <dd>

Boolean value indicating whether repaint events are enabled. If **TRUE**, the filter will sent [**EC\_REPAINT**](ec-repaint.md) events to the filter graph manager. Otherwise, it will not send EC\_REPAINT events.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method ensures that the filter graph manager is not flooded with redundant EC\_REPAINT events. After the filter sends an [**EC\_REPAINT**](ec-repaint.md) event, it calls this method with the value **TRUE**. The filter does not send more EC\_REPAINT events until it receives more data.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




