---
title: ISM\_SNAPIN\_NODE clipboard format
description: The ISM\_SNAPIN\_NODE clipboard format returns the name of the selected item. The IIS and SMTP snap-ins support this clipboard format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 87645ff1-613f-47ba-a0e1-3cf0424cba1f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ISM_SNAPIN_NODE clipboard format MMC
topic_type:
- apiref
api_name:
- ISM_SNAPIN_NODE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ISM\_SNAPIN\_NODE clipboard format

The **ISM\_SNAPIN\_NODE** clipboard format returns the name of the selected item. The IIS and SMTP snap-ins support this clipboard format.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. An empty string, L"", is returned for this clipboard format if the selected node type is a Machine node or an Instance node.

 

 




