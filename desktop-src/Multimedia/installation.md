---
title: Installation
description: Installation
ms.assetid: 8d007ea4-b75a-4b3f-965f-8091fcd4cb2f
keywords:
- installable drivers,installing
- installable drivers,DRV_INSTALL message
- installable drivers,DRV_REMOVE message
- DRV_INSTALL message
- DRV_REMOVE message
- DRVCONFIGINFO message
- installing drivers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Installation

An installable driver can carry out driver-specific installation tasks when processing the [**DRV\_INSTALL**](drv-install.md) and [**DRV\_REMOVE**](drv-remove.md) messages. An installation application, such as a Control Panel application, sends the messages to the driver when installing or removing the driver, respectively.

When processing the DRV\_INSTALL message, the driver typically verifies that the required hardware is present and then displays the configuration dialog box to let the user choose the initial configuration settings for the driver and associated hardware. The message includes the address of a [**DRVCONFIGINFO**](drvconfiginfo.md) structure that contains the names of the registry key and value associated with the driver; the driver checks the registry value for default configuration information. Finally, the driver also creates any additional registry keys and values needed for successful operation.

When processing the DRV\_REMOVE message, the driver removes any registry keys and values it may have created.

 

 




