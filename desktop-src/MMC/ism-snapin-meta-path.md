---
title: ISM\_SNAPIN\_META\_PATH clipboard format
description: The ISM\_SNAPIN\_META\_PATH clipboard format returns the unique path of the selected item. The IIS and SMTP snap-ins support this clipboard format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ef10014-f55c-4b0f-b3bc-45e1b9c858f0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ISM_SNAPIN_META_PATH clipboard format MMC
topic_type:
- apiref
api_name:
- ISM_SNAPIN_META_PATH
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISM\_SNAPIN\_META\_PATH clipboard format

The **ISM\_SNAPIN\_META\_PATH** clipboard format returns the unique path of the selected item. The IIS and SMTP snap-ins support this clipboard format.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. The returned data is of the form: L"&lt;computer name&gt;/&lt;service name&gt;/&lt;instance&gt;/&lt;parent path&gt;/&lt;node&gt;. For the &lt;computer name&gt; portion, the value, L"LM", indicates the local machine. An empty string, L"", is returned for this clipboard format if the selected node type is a Machine node.

 

 




