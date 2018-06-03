---
title: FILEMGMT\_TRANSPORT clipboard format
description: The FILEMGMT\_TRANSPORT clipboard format returns the transport protocol used by the client; this clipboard format applies to a selected Share, Session, or Open File result item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc5d68d7-42cf-4c92-9730-4b1ac4c1ba00
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- FILEMGMT_TRANSPORT clipboard format MMC
topic_type:
- apiref
api_name:
- FILEMGMT_TRANSPORT
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FILEMGMT\_TRANSPORT clipboard format

The **FILEMGMT\_TRANSPORT** clipboard format returns the transport protocol used by the client; this clipboard format applies to a selected Share, Session, or Open File result item.

## Data Format

The data provided by this clipboard format is a **DWORD**, and can be one of the following values.



| Data value | Transport protocol                         |
|------------|--------------------------------------------|
| 0          | Server Message Block (SMB)                 |
| 1          | File and Print Services for NetWare (FPNW) |
| 2          | Services for Macintosh (SFM)               |



 

 

 




