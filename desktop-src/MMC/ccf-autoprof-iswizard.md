---
title: CCF\_AUTOPROF\_ISWIZARD clipboard format
description: Indicates the item being pasted was created with a wizard or is currently displayed using a wizard.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a714785-1428-4896-b3f7-c841e66e8572'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CCF_AUTOPROF_ISWIZARD clipboard format MMC"]
topic_type:
- apiref
api_name:
- CCF_AUTOPROF_ISWIZARD
api_type:
- NA
---

# CCF\_AUTOPROF\_ISWIZARD clipboard format

The **CCF\_AUTOPROF\_ISWIZARD** clipboard format indicates the item being pasted was created with a wizard or is currently displayed using a wizard. This clipboard format is published by all extensible Group Policy preferences nodes.

## Data Format

The data provided by this clipboard format is a **BOOL**.

Return **TRUE** to indicate the item being pasted was created with a wizard or is currently displayed using a wizard.

Return **FALSE** to indicate the item being pasted was not created with a wizard or is not currently displayed using a wizard.

## Remarks

For an example that uses the [**CCF\_AUTOPROF\_XMLDOM**](ccf-autoprof-xmldom.md) clipboard format, see [Header Files](https://msdn.microsoft.com/library/cc512160).

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/> |
| Minimum supported server<br/> | Windows Server 2008<br/>    |



 

 





