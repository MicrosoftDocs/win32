---
title: CCF\_AUTOPROF\_CONTEXT clipboard format
description: Provides the context of the operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0a22535-111d-465d-9ac5-b63f2d9d5cd4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_AUTOPROF_CONTEXT clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_AUTOPROF_CONTEXT
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_AUTOPROF\_CONTEXT clipboard format

The **CCF\_AUTOPROF\_CONTEXT** clipboard format provides the context of the operation. This clipboard format is published by all extensible Group Policy preferences nodes.

## Data Format

The data provided by this clipboard format is an integer defining the context of the operation. The possible values are defined in the [**DATA\_OBJECT\_TYPES**](/windows/desktop/api/Mmc/ne-mmc-_data_object_types) enumeration.

## Remarks

For an example that uses the [**CCF\_AUTOPROF\_XMLDOM**](ccf-autoprof-xmldom.md) clipboard format, see [Header Files](https://msdn.microsoft.com/library/cc512160).

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/> |
| Minimum supported server<br/> | Windows Server 2008<br/>    |



 

 





