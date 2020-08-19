---
title: The Notify Flag
description: The Notify Flag
ms.assetid: ed5dbb0b-ce4d-4bda-8daa-c62cfda717d1
keywords:
- MCI_NOTIFY flag
ms.topic: article
ms.date: 05/31/2018
---

# The Notify Flag

The "notify" (MCI\_NOTIFY) flag directs the device to post an [**MM MCINOTIFY**](mm-mcinotify.md) message when the device completes an action. Your application must have a window procedure to process the MM\_MCINOTIFY message for notification to have any effect. An MM\_MCINOTIFY message indicates that the processing of a command has completed, but it does not indicate whether the command was completed successfully, failed, or was superseded or aborted.

The application specifies the handle to the destination window for the message when it issues a command. In the command-string interface, this handle is the last parameter of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function. In the command-message interface, the handle is specified in the low-order word of the **dwCallBack** member of the structure sent with the command message. (Every structure associated with a command message contains this member.)

 

 