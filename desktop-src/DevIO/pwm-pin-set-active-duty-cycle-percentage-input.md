---
description: Contains a desired duty cycle percentage for a pin or channel in a Pulse Width Modulation (PWM) controller.
ms.assetid: CA699703-2D9B-4841-99AD-9C27FF428394
title: PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT structure (Pwm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT
api_type: 
- HeaderDef
api_location: 
- Pwm.h
---

# PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_INPUT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Contains a desired duty cycle percentage for a pin or channel in a Pulse Width Modulation (PWM) controller.

## Syntax


```C++
typedef struct _PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT {
  PWM_PERCENTAGE Percentage;
} PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT;
```



## Members

<dl> <dt>

**Percentage**
</dt> <dd>

The desired PWM signal duty cycle, as a PWM\_PERCENTAGE, which is a ULONGLONG value.

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

[**IOCTL\_PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](https://www.bing.com/search?q=**IOCTL\_PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**)
</dt> </dl>

 

 




