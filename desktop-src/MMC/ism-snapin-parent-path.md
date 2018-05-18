---
title: ISM\_SNAPIN\_PARENT\_PATH clipboard format
description: The ISM\_SNAPIN\_PARENT\_PATH clipboard format returns the path to the selected item, relative to the computer targeted by the snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '010259d8-9d45-4807-82ae-281aa896c582'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ISM_SNAPIN_PARENT_PATH clipboard format MMC"]
topic_type:
- apiref
api_name:
- ISM_SNAPIN_PARENT_PATH
api_type:
- NA
---

# ISM\_SNAPIN\_PARENT\_PATH clipboard format

The **ISM\_SNAPIN\_PARENT\_PATH** clipboard format returns the path to the selected item, relative to the computer targeted by the snap-in. An empty string, L"", is returned for this clipboard format if the selected node type is a Machine node. The value, L"Root", indicates the current computer. The IIS and SMTP snap-ins support this clipboard format.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string.

 

 




