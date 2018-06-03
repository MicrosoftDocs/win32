---
title: MMC\_SNAPIN\_MACHINE\_NAME clipboard format
description: The MMC\_SNAPIN\_MACHINE\_NAME clipboard format provides the name of the computer currently being managed.The Computer Management, Services, and Shared Folders snap-ins support the MMC\_SNAPIN\_MACHINE\_NAME clipboard format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4d3433c5-6c3c-4af3-bf35-46f3d63dd2d7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC_SNAPIN_MACHINE_NAME clipboard format MMC
topic_type:
- apiref
api_name:
- MMC_SNAPIN_MACHINE_NAME
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC\_SNAPIN\_MACHINE\_NAME clipboard format

The **MMC\_SNAPIN\_MACHINE\_NAME** clipboard format provides the name of the computer currently being managed.The Computer Management, Services, and Shared Folders snap-ins support the **MMC\_SNAPIN\_MACHINE\_NAME** clipboard format. An empty string will be returned by this clipboard format if the local computer is being managed.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. Extension snap-ins must allocate global memory of a size greater than or equal to `MAX_PATH*sizeof(WCHAR)` for storage space when consuming **MMC\_SNAPIN\_MACHINE\_NAME** clipboard format data.

 

 




