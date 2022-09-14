---
title: VIEW.timerInterval
description: The timerInterval attribute specifies or retrieves the interval, in milliseconds, at which the timer fires events to the ontimer event handler.
ms.assetid: 1a69890f-5ea4-493a-8a9e-04fe60a41804
keywords:
- VIEW.timerInterval Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.timerInterval
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIEW.timerInterval

The **timerInterval** attribute specifies or retrieves the interval, in milliseconds, at which the timer fires events to the **ontimer** event handler.

``` syntax
        elementID.timerInterval
```

## Possible Values

This attribute is a read/write **Number** (**long**) with a default value of 1000.



| Value        | Description                    |
|--------------|--------------------------------|
| 0            | The timer event does not fire. |
| 50 and above | The interval in milliseconds.  |



 

Any value below 50 (including negative numbers, but not including zero) generates an error and the previous value is maintained.

## Remarks

This will not fire automatically if no **ontimer** event handler is implemented. Thus there is no performance degradation even though the default value is nonzero.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.ontimer**](view-ontimer.md)
</dt> </dl>

 

 





