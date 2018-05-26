---
title: CCF\_SNAPIN\_CLASSID clipboard format
description: The CCF\_SNAPIN\_CLASSID clipboard format is required for a snap-in to specify its CLSID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5b6f675-9646-4e61-9c20-6f3bbb50f178
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_SNAPIN_CLASSID clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_SNAPIN_CLASSID
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_SNAPIN\_CLASSID clipboard format

The CCF\_SNAPIN\_CLASSID clipboard format is required for a snap-in to specify its CLSID.

## Data Format

CLSID. Return the snap-in's CLSID.

## Remarks

Every snap-in must support this format in its **IDataObject::GetDataHere** implementation.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





