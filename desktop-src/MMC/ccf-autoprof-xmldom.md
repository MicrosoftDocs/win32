---
title: CCF\_AUTOPROF\_XMLDOM clipboard format
description: Provides the XML data object associated with the scope or result panes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 197a5e80-4542-4d52-89f9-20b06b0b8256
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_AUTOPROF_XMLDOM clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_AUTOPROF_XMLDOM
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_AUTOPROF\_XMLDOM clipboard format

The **CCF\_AUTOPROF\_XMLDOM** clipboard format provides the XML data object associated with the scope or result panes as a DOM object. This clipboard format is published by all extensible Group Policy preferences nodes.

## Data Format

The data provided by this clipboard format is an interface pointer to an **IXMLDocument** object.

## Remarks

For an example that uses the **CCF\_AUTOPROF\_XMLDOM** clipboard format, see [Header Files](https://msdn.microsoft.com/library/cc512160).

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/> |
| Minimum supported server<br/> | Windows Server 2008<br/>    |



 

 





