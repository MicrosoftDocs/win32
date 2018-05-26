---
Description: This topic lists the IOCTLs for Pulse Width Modulation.
ms.assetid: 2ED7A06A-A7EC-4C44-AB22-4A52CF2DF2C5
title: PWM Control Codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PWM Control Codes

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This topic lists the IOCTLs for Pulse Width Modulation.

## In this section



| Topic                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_PWM\_CONTROLLER\_GET\_ACTUAL\_PERIOD**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_controller_get_actual_period?branch=master)<br/>                   | Retrieves the effective output signal period of the Pulse Width Modulation (PWM) controller as it would be measured on its output channels.<br/>                                                                                                                                                                                  |
| [**IOCTL\_PWM\_CONTROLLER\_GET\_INFO**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_controller_get_info?branch=master)<br/>                                      | Retrieves information about a Pulse Width Modulation (PWM) controller. This information does not change after the controller is initialized. <br/>                                                                                                                                                                                |
| [**IOCTL\_PWM\_CONTROLLER\_SET\_DESIRED\_PERIOD**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_controller_set_desired_period?branch=master)<br/>                 | Sets the output signal period of a Pulse Width Modulation (PWM) controller to a suggested value. <br/>                                                                                                                                                                                                                            |
| [**IOCTL\_PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_get_active_duty_cycle_percentage?branch=master)<br/> | Retrieves the current duty cycle percentage for a pin or channel. The control code returns the percentage as a [**PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_OUTPUT**](pwm-pin-get-active-duty-cycle-percentage-output.md) structure.<br/>                                                                                  |
| [**IOCTL\_PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_set_active_duty_cycle_percentage?branch=master)<br/> | Set a desired duty cycle percentage value for the controller pin or channel. The control code specifies the percentage as a [**PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_INPUT**](pwm-pin-set-active-duty-cycle-percentage-input.md) structure. <br/>                                                                      |
| [**IOCTL\_PWM\_PIN\_GET\_POLARITY**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_get_polarity?branch=master)<br/>                                            | Retrieves the current signal polarity of the pin or channel. The control code gets the signal polarity as a [**PWM\_PIN\_GET\_POLARITY\_OUTPUT**](pwm-pin-get-polarity-output.md) structure. The signal polarity is either Active High or Active Low, as defined in the [**PWM\_POLARITY**](/windows/win32/Pwm/ne-pwm-_pwm_polarity?branch=master) enumeration. <br/> |
| [**IOCTL\_PWM\_PIN\_SET\_POLARITY**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_set_polarity?branch=master)<br/>                                            | Sets the signal polarity of the pin or channel. The control code sets the signal polarity based on a [**PWM\_PIN\_SET\_POLARITY\_INPUT**](/windows/win32/Pwm/ns-pwm-_pwm_pin_set_polarity_input?branch=master) structure. The signal polarity is either Active High or Active Low, as defined in the [**PWM\_POLARITY**](/windows/win32/Pwm/ne-pwm-_pwm_polarity?branch=master) enumeration.<br/>           |
| [**IOCTL\_PWM\_PIN\_START**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_start?branch=master)<br/>                                                           | Starts generation of Pulse Width Modulation (PWM) signal on a pin or channel. To check whether a pin is started, use [**IOCTL\_PWM\_PIN\_IS\_STARTED**](base-ioctl_ioctl_pwm_pin_is_started).<br/>                                                                                                                                |
| [**IOCTL\_PWM\_PIN\_STOP**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_stop?branch=master)<br/>                                                             | Stops generation of Pulse Width Modulation (PWM) signal on a pin or channel. To check whether a pin is started, use [**IOCTL\_PWM\_PIN\_IS\_STARTED**](base-ioctl_ioctl_pwm_pin_is_started).<br/>                                                                                                                                 |
| [**IOCTL\_PWM\_PIN\_IS\_STARTED**](/windows/win32/Pwm/ni-pwm-ioctl_pwm_pin_is_started?branch=master)<br/>                                                | Retrieves the state of signal generation for a pin or channel. Each pin has a state of started or stopped as a [**PWM\_PIN\_IS\_STARTED\_OUTPUT**](pwm-pin-is-started-output.md) structure.<br/>                                                                                                                                 |



 

 

 




