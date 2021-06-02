---
description: Pulse Width Modulation (PWM) is the technique of generating a rectangular pulse wave that has a pulse width that is modulated to result in the variation of the average value of the waveform.
ms.assetid: 16B1E46F-2C42-4D94-949E-BE8F53EB1E1E
title: PWM API
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# PWM API

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Pulse Width Modulation (PWM) is the technique of generating a rectangular pulse wave that has a pulse width that is modulated to result in the variation of the average value of the waveform. Most common uses include driving servo motors, dimming LEDs, or other related functions. PWM is intended to be used primarily for Internet of Things scenarios.

## About Pulse Width Modulation

A PWM waveform can be categorized by two parameters:

-   A waveform period (T)

-   The duty cycle, where the waveform frequency (f) is the reciprocal of the period f=1/T

The duty cycle describes the proportion of the **on**/**Active** time with respect to the regular interval or **Period** of time. A low duty cycle corresponds to an average of low output power, because the power is off for most of the time. Duty cycle is expressed as a percentage. Fully on is 100%. Fully off is 0%. **Active** half the time is 50%.

Developers looking to implement PWM in their IoT applications should investigate the [WinRT PWM documentation.](/uwp/api/windows.devices.pwm)

## Pulse Width Modulation types

PWM uses [these IO control codes](pwm-control-codes.md), [structures](pwm-structures.md), and [enumerations.](pwm-enumeration-types.md)

PWM also uses the following function: [**PwmParsePinPath**](/windows-hardware/drivers/ddi/content/pwmutil/nf-pwmutil-pwmparsepinpath).

 

 
