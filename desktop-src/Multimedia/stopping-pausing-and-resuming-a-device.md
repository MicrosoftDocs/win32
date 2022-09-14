---
title: Stopping, Pausing, and Resuming a Device
description: Stopping, Pausing, and Resuming a Device
ms.assetid: df9ca4ab-4711-44dd-a058-909f291a1652
keywords:
- MCI_STOP command
- MCI_PAUSE command
- MCI_RESUME command
ms.topic: article
ms.date: 05/31/2018
---

# Stopping, Pausing, and Resuming a Device

The [**stop**](stop.md) ([**MCI\_STOP**](mci-stop.md)) command suspends the playing or recording of a device. Many devices also support the [**pause**](pause.md) ([**MCI\_PAUSE**](mci-pause.md)) command. The difference between **stop** and **pause** depends on the device. Usually **pause** suspends operation but leaves the device ready to resume playing or recording immediately.

Using the [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)) or [**record**](record.md) ([**MCI\_RECORD**](mci-record.md)) command to restart a device resets the locations specified with the "to" (MCI\_TO) and "from" (MCI\_FROM) flags before the device was paused or stopped. Without the "from" flag, these commands reset the starting location to the current position. Without the "to" flag, they reset the ending location to the end of the media. To continue playing or recording without resetting a previously specified stop position, use the **play** or **record** command's "to" flag to specify an ending position.

Some devices support the [**resume**](resume.md) ([**MCI\_RESUME**](mci-resume.md)) command to restart a paused device. This command does not change the "to" and "from" locations specified with the **play** or **record** command that preceded the [**pause**](pause.md) command.

 

 




