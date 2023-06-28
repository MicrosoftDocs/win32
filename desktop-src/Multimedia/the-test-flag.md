---
title: The Test Flag
description: The Test Flag
ms.assetid: d103a96e-8d55-413d-ac84-15c3d8dccfbe
keywords:
- MCI_TEST flag
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# The Test Flag

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The "test" (MCI\_TEST) flag queries the device to determine if it can execute the command. The device returns an error if it cannot execute the command. It returns no error if it can handle the command. When you specify this flag, MCI returns control to the application without executing the command.

This flag is supported by digital-video and VCR devices for all commands except [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) and [**close**](close.md) ([**MCI\_CLOSE**](mci-close.md)).

 

 




