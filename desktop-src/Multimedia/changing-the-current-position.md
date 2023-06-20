---
title: Changing the Current Position
description: Changing the Current Position
ms.assetid: f8c4b9b5-c5fb-4292-8418-41650dcd65c0
keywords:
- MCI_SEEK command message
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Changing the Current Position

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To change the current position in a device element, use the [**MCI\_SEEK**](mci-seek.md) command message along with the MCI\_TO flag and the [**MCI\_SEEK\_PARMS**](mci-seek-parms.md) structure. If you use the **dwTo** member to specify a seek position with MCI\_SEEK, you should query the time format and set it, if necessary.

In addition to specifying a position with the **dwTo** member, you can specify the MCI\_SEEK\_TO\_START or MCI\_SEEK\_TO\_END flags for the *dwParam1* parameter of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to find the starting and ending positions of the device element. If you use one of these flags, don't specify the MCI\_TO flag.

 

 