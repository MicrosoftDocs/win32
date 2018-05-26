---
title: CCF\_HTML\_DETAILS clipboard format
description: For MMC 2.0 and later, the CCF\_HTML\_DETAILS clipboard format is provided by snap-ins using the Extended View extension.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 608826eb-e0ae-423c-98ed-4519d77e6d84
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_HTML_DETAILS clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_HTML_DETAILS
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_HTML\_DETAILS clipboard format

For MMC 2.0 and later, the CCF\_HTML\_DETAILS clipboard format is provided by snap-ins using the [Extended View extension](using-the-extended-view-extension.md). A node that supports this clipboard format can support HTML processing within the view. Specifically, the HTML can be used to add user interface elements to the view, and the script can use [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md).

Be aware that CCF\_HTML\_DETAILS is also the name of a property recognized by the Extended View extension. Instead of supporting CCF\_HTML\_DETAILS as a clipboard format, a snap-in can support the CCF\_HTML\_DETAILS property by implementing the [**INodeProperties**](inodeproperties.md) interface.

If the Extended View is unable to retrieve the CCF\_HTML\_DETAILS property using the [**INodeProperties**](inodeproperties.md) interface, then the Extended View will query for the CCF\_HTML\_DETAILS clipboard format using the HGLOBAL medium in a call to [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere). If this medium is not supported, then the Extended View will query for the CCF\_HTML\_DETAILS clipboard format using the IStream medium in a call to **IDataObject::GetDataHere**.

## Data Format

A string that represents the HTML text that is in effect for the view. The data must be plain text. For example, the following text results in text and a link that appears in the HTML details area.


```VB
"Display <A HREF = javascript:external.ExecuteSelectionMenuItem('_PROPERTIES')>Properties </A>"
```



The following displays what the user will see in the HTML details area (below the name of the selected node).


```VB
Display Properties
```



If the user clicks the Properties link, then the properties menu item will be executed for the selected item (be aware that the selected item must have a Properties menu item for this example to work). The [**external object**](_inet_external_object_scr) in the script refers to the MMC 2.0 Automation Object Model [**view object**](view-object.md).

## Remarks

The HTML details area appears below the name of the selected node. If the [**CCF\_DESCRIPTION**](ccf-description.md) property or clipboard format is supported, a description will appear below the HTML details area.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[Using the Extended View Extension](using-the-extended-view-extension.md)
</dt> <dt>

[**CCF\_DESCRIPTION**](ccf-description.md)
</dt> </dl>

 

 





