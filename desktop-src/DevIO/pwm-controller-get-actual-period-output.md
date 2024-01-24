---
description: Contains the effective output signal period for a Pulse Width Modulation (PWM) controller.
ms.assetid: 280F564F-FF7F-4121-B726-9F9AF9E98EB7
title: PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT structure (Pwm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT
api_type: 
- HeaderDef
api_location: 
- Pwm.h
---

# PWM\_CONTROLLER\_GET\_ACTUAL\_PERIOD\_OUTPUT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Contains the effective output signal period for a Pulse Width Modulation (PWM) controller.

## Syntax


```C++
typedef struct _PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT {
  PWM_PERIOD ActualPeriod;
} PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT;
```



## Members

<dl> <dt>

**ActualPeriod**
</dt> <dd>

The effective output signal period as it would be measured on the output channels of the controller.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                             |
| Minimum KMDF version<br/>     | 1.19<br/>                                                                                  |
| Minimum UMDF version<br/>     | 2.19<br/>                                                                                  |
| Header<br/>                   | <dl> <dt>Pwm.h (include Pwm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_PWM\_CONTROLLER\_GET\_ACTUAL\_PERIOD**](https://www.bing.com/search?q=**IOCTL\_PWM\_CONTROLLER\_GET\_ACTUAL\_PERIOD**)
</dt> </dl>

 

 




