---
title: Driver Support for MCI Commands
description: Driver Support for MCI Commands
ms.assetid: 1adea076-c04e-4613-a793-60de41b2e9db
ms.topic: article
ms.date: 05/31/2018
---

# Driver Support for MCI Commands

MCI drivers provide the functionality for MCI commands. The system software performs some basic data-management tasks, but all the multimedia playback, presentation, and recording is handled by the individual MCI drivers.

Drivers vary in their support for MCI commands and command flags. Because multimedia devices can have widely different capabilities, MCI is designed to let individual drivers extend or reduce the command sets to match the capabilities of the device. For example, the [**record**](record.md) ([**MCI\_RECORD**](mci-record.md)) command is part of the command set for MIDI sequencers, but the MCISEQ driver included with Windows does not support this command. The reference topic for the record command explains that devices of the **sequencer** device type recognize the command; this does not mean that all devices of this type support the command. Applications should use the [**capability**](capability.md) ([**MCI\_GETDEVCAPS**](mci-getdevcaps.md)) command to determine the capabilities of a particular device.

 

 




