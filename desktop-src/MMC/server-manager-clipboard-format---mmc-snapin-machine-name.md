---
title: MMC\_SNAPIN\_MACHINE\_NAME clipboard format
description: Provides the full DNS name of the server that the Server Manager is currently targeting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 28871751-83d7-4860-b076-620f4e5f2ac9
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC\_SNAPIN\_MACHINE\_NAME clipboard format

The **MMC\_SNAPIN\_MACHINE\_NAME** clipboard format provides the full DNS name of the server that the Server Manager is currently targeting. Although Server Manager never publishes an empty string for this clipboard format, if this value is an empty string the extension may assume that Server Manager is targeting the local host. This helps to maintain consistency with the way the Computer Management snap-in uses this clipboard format. This clipboard format is published by all extensible Server Manager nodes.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

 





