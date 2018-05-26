---
title: RMT\_OC\_NFS clipboard format
description: If the value of this clipboard format is \ 0034;TRUE \ 0034;, it implies that the dynamic extension node is installed and the extension node should be displayed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3519cd88-2728-4337-a952-e98cf9353949
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- RMT_OC_NFS clipboard format MMC
topic_type:
- apiref
api_name:
- RMT_OC_NFS
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RMT\_OC\_NFS clipboard format

If the value of this clipboard format is "TRUE", it implies that the dynamic extension node is installed and the extension node should be displayed. A value of "FALSE" indicates that the dynamic extension node is not installed, and the extension node should not be displayed. This clipboard format is published by the "File Services" node.

## Data Format

The data provided by this clipboard format is a null-terminated Unicode string.

## Remarks

> [!Note]  
> Please note that the "TRUE" and "FALSE" values are not case sensitive.

 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

 





