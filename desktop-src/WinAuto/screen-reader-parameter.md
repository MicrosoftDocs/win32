---
title: Screen reader parameter
description: The screen reader parameter indicates whether an application should provide textual information in situations where it would otherwise present the information graphically.
ms.assetid: ac79c389-511c-4403-a8d5-75b2eba2b39f
ms.topic: article
ms.date: 05/31/2018
---

# Screen reader parameter

The screen reader parameter indicates whether an application should provide textual information in situations where it would otherwise present the information graphically.

This parameter is typically set by accessibility aids such as screen readers. Applications use the **SPI\_GETSCREENREADER** and **SPI\_SETSCREENREADER** flags with the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function to get and set the screen reader parameter.

> [!Note]  
> Narrator, the screen reader that is included with Windows, does not set the **SPI\_SETSCREENREADER** or **SPI\_GETSCREENREADER** flags.

 

 

 