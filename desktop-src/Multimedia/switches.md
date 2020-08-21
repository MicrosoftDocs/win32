---
title: Switches
description: Switches
ms.assetid: ab92d30d-97ab-4229-aed8-1080b6e6dc88
keywords:
- audio mixers,controls
- audio mixers,switches
- mixers,controls
- mixers,switches
- switch controls
- MIXERCONTROLDETAILS_BOOLEAN structure
- Boolean control
- button control
- on/off control
- mono control
- loudness control
- stereo enhanced control
ms.topic: article
ms.date: 05/31/2018
---

# Switches

The switch controls are two-state switches. These controls use the [**MIXERCONTROLDETAILS\_BOOLEAN**](/previous-versions//dd757295(v=vs.85)) structure to retrieve and set control properties. The following table describes the types of switches.



| Control         | Description                                                                                                                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Boolean         | The generic switch. It can be set to **TRUE** or **FALSE**.                                                                                                                                                                           |
| Button          | Set to **TRUE** for all buttons that the driver should handle as though they had been pressed. If the value is **FALSE**, no action is taken.                                                                                         |
| On/Off          | An alternative switch that is represented by a graphic other than the one used for the Boolean switch. It can be set to ON or OFF.                                                                                                    |
| Mute            | Mutes an audio line (suppressing the data flow of the line) or allows the audio data to play. This switch is frequently used to help control the lines feeding into the mixer.                                                        |
| Mono            | Switches between mono and stereo output for a stereo audio line. Set to OFF to play stereo data as separate channels. Set to ON to combine data from both channels into a mono audio line.                                            |
| Loudness        | Boosts low-volume bass for an audio line. Set to ON to boost low-volume bass. Set to OFF to set volume levels to normal. The amount of boost is hardware specific. For more information, see the documentation for your mixer device. |
| Stereo Enhanced | Increases stereo separation. Set to ON to increase stereo separation. Set to OFF for no enhancement.                                                                                                                                  |



 

 

 