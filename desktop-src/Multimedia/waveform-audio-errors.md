---
title: Waveform-Audio Errors
description: Waveform-Audio Errors
ms.assetid: c898552a-a60a-4deb-ab4a-ed74b08a7d05
keywords:
- MCIERR return values,waveform-audio errors
- multimedia reference,waveform-audio errors
- reference for multimedia,waveform-audio errors
- Media Control Interface (MCI),waveform-audio errors
- MCI (Media Control Interface),waveform-audio errors
- reference for MCI,waveform-audio errors
- MCI reference,waveform-audio errors
- Media Control Interface (MCI),errors
- MCI (Media Control Interface),errors
- reference for MCI,errors
- MCI reference,errors
- waveform-audio errors
- MCI waveform-audio errors
ms.topic: article
ms.date: 05/31/2018
---

# Waveform-Audio Errors

The following additional return values are defined for MCI waveform-audio devices:



| Value                             | Meaning                                                                                                                                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MCIERR\_WAVE\_INPUTSINUSE         | All waveform devices that can record files in the current format are in use. Wait until one of these devices is free; then, try again.                              |
| MCIERR\_WAVE\_INPUTSUNSUITABLE    | No installed waveform device can record files in the current format. Use the Drivers option from the Control Panel to install a suitable waveform recording device. |
| MCIERR\_WAVE\_INPUTUNSPECIFIED    | You can specify any compatible waveform recording device.                                                                                                           |
| MCIERR\_WAVE\_OUTPUTSINUSE        | All waveform devices that can play files in the current format are in use. Wait until one of these devices is free; then, try again.                                |
| MCIERR\_WAVE\_OUTPUTSUNSUITABLE   | No installed waveform device can play files in the current format. Use the Drivers option from the Control Panel to install a suitable waveform device.             |
| MCIERR\_WAVE\_OUTPUTUNSPECIFIED   | You can specify any compatible waveform playback device.                                                                                                            |
| MCIERR\_WAVE\_SETINPUTINUSE       | The current waveform device is in use. Wait until the device is free; then, try again to set the device for recording.                                              |
| MCIERR\_WAVE\_SETINPUTUNSUITABLE  | The device you are using to record a waveform cannot recognize the data format.                                                                                     |
| MCIERR\_WAVE\_SETOUTPUTINUSE      | The current waveform device is in use. Wait until the device is free; then, try again to set the device for playback.                                               |
| MCIERR\_WAVE\_SETOUTPUTUNSUITABLE | The device you are using to playback a waveform cannot recognize the data format.                                                                                   |



 

 

 




