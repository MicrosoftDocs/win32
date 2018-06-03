---
title: CCF\_NODETYPE clipboard format
description: The CCF\_NODETYPE clipboard format is required for a snap-in to specify the node type (in GUID form) of the scope item represented by the data object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60a6d2bc-547f-4ae7-916f-abfdf2425e07
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_NODETYPE clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_NODETYPE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_NODETYPE clipboard format

The CCF\_NODETYPE clipboard format is required for a snap-in to specify the node type (in GUID form) of the scope item represented by the data object.

## Data Format

GUID. Return the GUID that represents the node type of the data object.

## Remarks

Every snap-in must support this format in its **IDataObject::GetDataHere** implementation.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





