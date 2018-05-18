---
title: CCF\_SZNODETYPE clipboard format
description: The CCF\_SZNODETYPE clipboard format is required for a snap-in to specify the node type (in string form) of the scope item represented by the data object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cdd26a7c-ecd5-4582-8c60-cd33f42d6f6c'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CCF_SZNODETYPE clipboard format MMC"]
topic_type:
- apiref
api_name:
- CCF_SZNODETYPE
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# CCF\_SZNODETYPE clipboard format

The CCF\_SZNODETYPE clipboard format is required for a snap-in to specify the node type (in string form) of the scope item represented by the data object.

## Data Format

WCHAR string. Return a string that contains the GUID that represents the node type of the data object.

## Remarks

Every snap-in must support this format in its **IDataObject::GetDataHere** implementation.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





