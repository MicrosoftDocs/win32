---
Description: 'Contains a polarity value to return.'
ms.assetid: '432C10EF-AC08-4781-9BCA-A31E0DF12704'
title: 'PWM\_PIN\_GET\_POLARITY\_OUTPUT structure'
---

# PWM\_PIN\_GET\_POLARITY\_OUTPUT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Contains a polarity value to return.

## Syntax


```C++
typedef struct _PWM_PIN_GET_POLARITY_OUTPUT {
  PWM_POLARITY Polarity;
} PWM_PIN_GET_POLARITY_OUTPUT;
```



## Members

<dl> <dt>

**Polarity**
</dt> <dd>

The polarity of the pin or channel as a [**PWM\_POLARITY**](pwm-polarity.md) value. The polarity is either Active High or Active Low.

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

[**IOCTL\_PWM\_PIN\_GET\_POLARITY**](base-ioctl_ioctl_pwm_pin_get_polarity)
</dt> <dt>

[**PWM\_POLARITY**](basel-pwm_polarity)
</dt> </dl>

 

 




