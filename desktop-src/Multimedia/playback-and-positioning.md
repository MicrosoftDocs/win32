---
title: Playback and Positioning
description: Playback and Positioning
ms.assetid: fbf9294e-c644-45c7-ab60-dd903409a44f
ms.topic: article
ms.date: 05/31/2018
---

# Playback and Positioning

A number of MCI commands, such as [**play**](play.md) ([**MCI\_PLAY**](mci-play.md)), [**stop**](stop.md) ([**MCI\_STOP**](mci-stop.md)), [**pause**](pause.md) ([**MCI\_PAUSE**](mci-pause.md)), [**resume**](resume.md) ([**MCI\_RESUME**](mci-resume.md)), and [**seek**](seek.md) ([**MCI\_SEEK**](mci-seek.md)), affect the playback or positioning of a multimedia file. If an MCI device receives a playback command while another playback command is in progress, it accepts the command and either stops or supersedes the previous command.

Many MCI commands, such as [**set**](set.md) ([**MCI\_SET**](mci-set.md)), do not affect playback. A notification from one of these commands does not interfere with pending playback or position commands as long as the notifications are not performed from the same instance of the driver. For example, you can issue a **set** or [**status**](status.md) ([**MCI\_STATUS**](mci-status.md)) command while a device is performing a **seek** command without stopping or superseding the **seek** command.

However, there can be only one pending notification. For example, if an application requests a notification for **play** and follows that request with **status** "start position notify," the **play** notification will return "superseded" and the notification for the status command will return when it is finished. In this case, however, the **play** command will still succeed, even though the application did not receive the notification.

 

 




