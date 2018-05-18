---
Description: 'Contains the current duty cycle percentage for a pin or channel in a Pulse Width Modulation (PWM) controller.'
ms.assetid: '09C0232A-DF5C-4A1C-8138-D3D65E45731B'
title: 'PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_OUTPUT structure'
---

# PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_OUTPUT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Contains the current duty cycle percentage for a pin or channel in a Pulse Width Modulation (PWM) controller.

## Syntax


```C++
typedef struct _PWM_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE_OUTPUT {
  PWM_PERCENTAGE Percentage;
} PWM_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE_OUTPUT;
```



## Members

<dl> <dt>

**Percentage**
</dt> <dd>

The current PWM signal duty cycle, as a PWM\_PERCENTAGE, which is a ULONGLONG value.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                             |
| Minimum KMDF version<br/>     | 1.19<br/>                                                                                  |
| Minimum UMDF version<br/>     | 2.19<br/>                                                                                  |
| Header<br/>                   | <dl> <dt>Pwm.h (include Pwm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](base-ioctl_ioctl_pwm_pin_get_active_duty_cycle_percentage)
</dt> </dl>

 

 




