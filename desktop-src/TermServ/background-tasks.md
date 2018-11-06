---
title: Guidelines for background tasks in Remote Desktop Services
description: To maximize CPU availability for all users, either disable background tasks when running in a Remote Desktop Services environment or create efficient background tasks that are not resource-intensive.
ms.assetid: c3688319-dbe7-4be5-8895-622a8f8797d2
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for background tasks in Remote Desktop Services

Background tasks—tasks performed when an application's message loop is idle—provide a mechanism for handling low-priority tasks in a single-user environment. In a Remote Desktop Services environment, however, one user's background task competes for CPU cycles with another user's foreground tasks. When multiple users are running both foreground and background tasks, the CPU demands are much higher than when all users are running only foreground tasks. To maximize CPU availability for all users, either disable background tasks when running in a Remote Desktop Services environment or create efficient background tasks that are not resource-intensive.

For more information, see [Detecting the Remote Desktop Services environment](detecting-the-terminal-services-environment.md). After you detect the Remote Desktop Services environment, you can disable or reconfigure background tasks for the application using the same set of APIs that you used to manage the tasks.

 

 




