---
title: CCF\_AUTOPROF\_MULTISELECT clipboard format
description: Indicates the item represents more than one object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 799249c6-ba03-41c2-8dd8-369ce51af393
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_AUTOPROF_MULTISELECT clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_AUTOPROF_MULTISELECT
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_AUTOPROF\_MULTISELECT clipboard format

The **CCF\_AUTOPROF\_MULTISELECT** clipboard format indicates the item represents more than one object. This clipboard format is published by all extensible Group Policy preferences nodes.

## Data Format

The data provided by this clipboard format is a **BOOL**.

Return **TRUE** to indicate the item represents more than one object.

Return **FALSE** to indicate the item represents one object.

## Remarks

For an example that uses the [**CCF\_AUTOPROF\_XMLDOM**](ccf-autoprof-xmldom.md) clipboard format, see [Header Files](https://msdn.microsoft.com/library/cc512160).

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/> |
| Minimum supported server<br/> | Windows Server 2008<br/>    |



 

 





