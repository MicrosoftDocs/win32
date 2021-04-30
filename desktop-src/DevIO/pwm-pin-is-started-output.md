---
description: Contains the current signal generation state of a pin.
ms.assetid: 07D76F8D-C5B5-4500-BFA2-452989868027
title: PWM_PIN_IS_STARTED_OUTPUT structure (Pwm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PWM_PIN_IS_STARTED_OUTPUT
api_type: 
- HeaderDef
api_location: 
- Pwm.h
---

# PWM\_PIN\_IS\_STARTED\_OUTPUT structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Contains the current signal generation state of a pin.

## Syntax


```C++
typedef struct _PWM_PIN_IS_STARTED_OUTPUT {
  BOOLEAN IsStarted;
} PWM_PIN_IS_STARTED_OUTPUT;
```



## Members

<dl> <dt>

**IsStarted**
</dt> <dd>

The pin current signal generation state. A value of true means that the pin is started. A value of false means that the pin is stopped.

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

[**IOCTL\_PWM\_PIN\_IS\_STARTED**](https://www.bing.com/search?q=**IOCTL\_PWM\_PIN\_IS\_STARTED**)
</dt> </dl>

 

 




