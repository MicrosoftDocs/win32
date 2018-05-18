---
title: ISM\_SNAPIN\_INSTANCE clipboard format
description: The ISM\_SNAPIN\_INSTANCE clipboard format returns the instance identification number (such as \ 0034;1 \ 0034;, \ 0034;2 \ 0034;, and so on) of the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4b430a6a-b694-4104-a9ee-4100c3cae35a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ISM_SNAPIN_INSTANCE clipboard format MMC"]
topic_type:
- apiref
api_name:
- ISM_SNAPIN_INSTANCE
api_type:
- NA
---

# ISM\_SNAPIN\_INSTANCE clipboard format

The **ISM\_SNAPIN\_INSTANCE** clipboard format returns the instance identification number (such as "1", "2", and so on) of the node. For the IIS snap-in, the Default FTP Site and Default website nodes are instance number "1", and any subsequent new instance numbers are incremented. For the SMTP snap-in, the Default SMTP Virtual Server is instance number "1", and any subsequent new instance numbers are incremented.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string. An empty string, L"", is returned for this clipboard format if the selected node type is a Machine node.

 

 




