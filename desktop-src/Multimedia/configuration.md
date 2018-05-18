---
title: Configuration
description: Configuration
ms.assetid: '677241d2-3ddd-423a-a1e7-b5fa3ce0a4eb'
keywords: ["installable drivers,configuration", "installable drivers,DRV_CONFIGURE message", "DRV_CONFIGURE message", "DRV_QUERYCONFIGURE message", "DRVCONFIGINFO message", "configuring installable drivers"]
---

# Configuration

An installable driver can let users choose configuration settings for the driver and associated hardware by displaying a configuration dialog box when processing the [**DRV\_CONFIGURE**](drv-configure.md) message. The driver is responsible for creating and managing the dialog box, processing any user input from the dialog box, and changing the configuration of the driver or hardware as requested by the user. The driver must provide a separate dialog box procedure to process window messages for the dialog box and a dialog box template to define the appearance and content of the dialog box.

Before receiving the DRV\_CONFIGURE message, a driver receives the [**DRV\_QUERYCONFIGURE**](drv-queryconfigure.md) message. The driver must return a nonzero value to the query to ensure receipt of the subsequent DRV\_CONFIGURE message.

When initializing the configuration dialog box, the driver typically retrieves configuration information from the registry. To help locate this information, the DRV\_CONFIGURE message usually includes the address of a [**DRVCONFIGINFO**](drvconfiginfo.md) structure that contains the names of the registry key and value associated with the driver. If the user requests changes to the configuration, the driver should update the configuration information in the registry.

 

 




