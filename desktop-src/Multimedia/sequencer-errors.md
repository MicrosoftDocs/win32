---
title: Sequencer Errors
description: Sequencer Errors
ms.assetid: 07f2d6c5-8c23-4f3e-8b8a-4f659eda57f7
keywords:
- MCIERR return values,sequencer errors
- multimedia reference,sequencer errors
- reference for multimedia,sequencer errors
- Media Control Interface (MCI),sequencer errors
- MCI (Media Control Interface),sequencer errors
- reference for MCI,sequencer errors
- MCI reference,sequencer errors
- Media Control Interface (MCI),errors
- MCI (Media Control Interface),errors
- reference for MCI,errors
- MCI reference,errors
- sequencer errors
- MCI sequencer errors
ms.topic: article
ms.date: 05/31/2018
---

# Sequencer Errors

The following additional return values are defined for MCI sequencers:



| Value                          | Meaning                                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| MCIERR\_SEQ\_DIV\_INCOMPATIBLE | The time formats of the "song pointer" and SMPTE are singular. You can't use them together.                                                              |
| MCIERR\_SEQ\_NOMIDIPRESENT     | This system has no installed MIDI devices. Use the Drivers option from the Control Panel to install a MIDI driver.                                       |
| MCIERR\_SEQ\_PORT\_INUSE       | The specified MIDI port is already in use. Wait until it is free; then, try again.                                                                       |
| MCIERR\_SEQ\_PORT\_MAPNODEVICE | The current MIDI Mapper setup refers to a MIDI device that is not installed on the system. Use the MIDI Mapper from the Control Panel to edit the setup. |
| MCIERR\_SEQ\_PORT\_MISCERROR   | An error occurred with specified port.                                                                                                                   |
| MCIERR\_SEQ\_PORT\_NONEXISTENT | The specified MIDI device is not installed on the system. Use the Drivers option from the Control Panel to install a MIDI device.                        |
| MCIERR\_SEQ\_PORTUNSPECIFIED   | The system does not have a current MIDI port specified.                                                                                                  |
| MCIERR\_SEQ\_TIMER             | All multimedia timers are being used by other applications. Quit one of these applications; then, try again.                                             |



 

 

 




