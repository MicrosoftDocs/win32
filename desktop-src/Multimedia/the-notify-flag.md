---
title: The Notify Flag
description: The Notify Flag
ms.assetid: ed5dbb0b-ce4d-4bda-8daa-c62cfda717d1
keywords:
- MCI_NOTIFY flag
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Notify Flag

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The "notify" (MCI\_NOTIFY) flag directs the device to post an [**MM MCINOTIFY**](mm-mcinotify.md) message when the device completes an action. Your application must have a window procedure to process the MM\_MCINOTIFY message for notification to have any effect. An MM\_MCINOTIFY message indicates that the processing of a command has completed, but it does not indicate whether the command was completed successfully, failed, or was superseded or aborted.

The application specifies the handle to the destination window for the message when it issues a command. In the command-string interface, this handle is the last parameter of the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function. In the command-message interface, the handle is specified in the low-order word of the **dwCallBack** member of the structure sent with the command message. (Every structure associated with a command message contains this member.)

 

 