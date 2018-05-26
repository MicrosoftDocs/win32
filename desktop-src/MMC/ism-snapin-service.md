---
title: ISM\_SNAPIN\_SERVICE clipboard format
description: The ISM\_SNAPIN\_SERVICE clipboard format returns the name of the service associated with the selected item. For the IIS snap-in, use this clipboard format to distinguish between FTP and WWW. The SMTP snap-in also supports this clipboard format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d439890c-1ab1-4583-9a4e-3fb7cf7d2be0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ISM_SNAPIN_SERVICE clipboard format MMC
topic_type:
- apiref
api_name:
- ISM_SNAPIN_SERVICE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ISM\_SNAPIN\_SERVICE clipboard format

The **ISM\_SNAPIN\_SERVICE** clipboard format returns the name of the service associated with the selected item. For the IIS snap-in, use this clipboard format to distinguish between FTP and WWW. The SMTP snap-in also supports this clipboard format.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. An empty string, L"", is returned for this clipboard format if the selected node type is a Machine node.

 

 




