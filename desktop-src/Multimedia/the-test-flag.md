---
title: The Test Flag
description: The Test Flag
ms.assetid: d103a96e-8d55-413d-ac84-15c3d8dccfbe
keywords:
- MCI_TEST flag
ms.topic: article
ms.date: 05/31/2018
---

# The Test Flag

The "test" (MCI\_TEST) flag queries the device to determine if it can execute the command. The device returns an error if it cannot execute the command. It returns no error if it can handle the command. When you specify this flag, MCI returns control to the application without executing the command.

This flag is supported by digital-video and VCR devices for all commands except [**open**](open.md) ([**MCI\_OPEN**](mci-open.md)) and [**close**](close.md) ([**MCI\_CLOSE**](mci-close.md)).

 

 




