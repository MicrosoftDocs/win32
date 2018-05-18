---
Description: 'This topic lists the IOCTLs for Pulse Width Modulation.'
ms.assetid: '2ED7A06A-A7EC-4C44-AB22-4A52CF2DF2C5'
title: PWM Control Codes
---

# PWM Control Codes

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This topic lists the IOCTLs for Pulse Width Modulation.

## In this section



| Topic                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_PWM\_CONTROLLER\_GET\_ACTUAL\_PERIOD**](ioctl-pwm-controller-get-actual-period.md)<br/>                   | Retrieves the effective output signal period of the Pulse Width Modulation (PWM) controller as it would be measured on its output channels.<br/>                                                                                                                                                                                  |
| [**IOCTL\_PWM\_CONTROLLER\_GET\_INFO**](ioctl-pwm-controller-get-info.md)<br/>                                      | Retrieves information about a Pulse Width Modulation (PWM) controller. This information does not change after the controller is initialized. <br/>                                                                                                                                                                                |
| [**IOCTL\_PWM\_CONTROLLER\_SET\_DESIRED\_PERIOD**](ioctl-pwm-controller-set-desired-period.md)<br/>                 | Sets the output signal period of a Pulse Width Modulation (PWM) controller to a suggested value. <br/>                                                                                                                                                                                                                            |
| [**IOCTL\_PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](ioctl-pwm-pin-get-active-duty-cycle-percentage.md)<br/> | Retrieves the current duty cycle percentage for a pin or channel. The control code returns the percentage as a [**PWM\_PIN\_GET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_OUTPUT**](pwm-pin-get-active-duty-cycle-percentage-output.md) structure.<br/>                                                                                  |
| [**IOCTL\_PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE**](ioctl-pwm-pin-set-active-duty-cycle-percentage.md)<br/> | Set a desired duty cycle percentage value for the controller pin or channel. The control code specifies the percentage as a [**PWM\_PIN\_SET\_ACTIVE\_DUTY\_CYCLE\_PERCENTAGE\_INPUT**](pwm-pin-set-active-duty-cycle-percentage-input.md) structure. <br/>                                                                      |
| [**IOCTL\_PWM\_PIN\_GET\_POLARITY**](ioctl-pwm-pin-get-polarity.md)<br/>                                            | Retrieves the current signal polarity of the pin or channel. The control code gets the signal polarity as a [**PWM\_PIN\_GET\_POLARITY\_OUTPUT**](pwm-pin-get-polarity-output.md) structure. The signal polarity is either Active High or Active Low, as defined in the [**PWM\_POLARITY**](pwm-polarity.md) enumeration. <br/> |
| [**IOCTL\_PWM\_PIN\_SET\_POLARITY**](ioctl-pwm-pin-set-polarity.md)<br/>                                            | Sets the signal polarity of the pin or channel. The control code sets the signal polarity based on a [**PWM\_PIN\_SET\_POLARITY\_INPUT**](pwm-pin-set-polarity-input.md) structure. The signal polarity is either Active High or Active Low, as defined in the [**PWM\_POLARITY**](pwm-polarity.md) enumeration.<br/>           |
| [**IOCTL\_PWM\_PIN\_START**](ioctl-pwm-pin-start.md)<br/>                                                           | Starts generation of Pulse Width Modulation (PWM) signal on a pin or channel. To check whether a pin is started, use [**IOCTL\_PWM\_PIN\_IS\_STARTED**](base-ioctl_ioctl_pwm_pin_is_started).<br/>                                                                                                                                |
| [**IOCTL\_PWM\_PIN\_STOP**](ioctl-pwm-pin-stop.md)<br/>                                                             | Stops generation of Pulse Width Modulation (PWM) signal on a pin or channel. To check whether a pin is started, use [**IOCTL\_PWM\_PIN\_IS\_STARTED**](base-ioctl_ioctl_pwm_pin_is_started).<br/>                                                                                                                                 |
| [**IOCTL\_PWM\_PIN\_IS\_STARTED**](ioctl-pwm-pin-is-started.md)<br/>                                                | Retrieves the state of signal generation for a pin or channel. Each pin has a state of started or stopped as a [**PWM\_PIN\_IS\_STARTED\_OUTPUT**](pwm-pin-is-started-output.md) structure.<br/>                                                                                                                                 |



 

 

 




