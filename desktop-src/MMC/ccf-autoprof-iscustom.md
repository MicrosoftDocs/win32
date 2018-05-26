---
title: CCF\_AUTOPROF\_ISCUSTOM clipboard format
description: Indicates the item is custom.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 10e70679-5dc4-44f8-bb6c-fc0b67acd6f8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_AUTOPROF_ISCUSTOM clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_AUTOPROF_ISCUSTOM
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_AUTOPROF\_ISCUSTOM clipboard format

The **CCF\_AUTOPROF\_ISCUSTOM** clipboard format indicates the item is custom, meaning, there is a set of property pages defined by the Group Policy preferences snap-in. This clipboard format is published by all extensible Group Policy preferences nodes.

## Data Format

The data provided by this clipboard format is a **BOOL**.

Return **TRUE** to indicate a set of property pages defined by the Group Policy preferences snap-in exists for this item.

Return **FALSE** to indicate a set of property pages defined by the Group Policy preferences snap-in does not exist for this item.

## Remarks

For an example that uses the [**CCF\_AUTOPROF\_XMLDOM**](ccf-autoprof-xmldom.md) clipboard format, see [Header Files](https://msdn.microsoft.com/library/cc512160).

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/> |
| Minimum supported server<br/> | Windows Server 2008<br/>    |



 

 





