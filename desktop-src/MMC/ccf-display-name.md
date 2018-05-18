---
title: CCF\_DISPLAY\_NAME clipboard format
description: The CCF\_DISPLAY\_NAME clipboard format is required for a snap-in to specify the display name for the snap-in's static node, which is displayed in the Standalone tab of the Add/Remove Snap-ins dialog box and the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '437d1216-de2f-4076-95a5-cefd6ac0add4'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CCF_DISPLAY_NAME clipboard format MMC"]
topic_type:
- apiref
api_name:
- CCF_DISPLAY_NAME
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# CCF\_DISPLAY\_NAME clipboard format

The CCF\_DISPLAY\_NAME clipboard format is required for a snap-in to specify the display name for the snap-in's static node, which is displayed in the Standalone tab of the Add/Remove Snap-ins dialog box and the scope pane.

## Data Format

WCHAR string. Return a string that contains the name to display for the snap-in's static node.

## Remarks

Every snap-in must support this format in its [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) implementation.

When a stand-alone snap-in is added to a console file, MMC calls the snap-in's [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) method requesting the CCF\_DISPLAY\_NAME clipboard format to retrieve the display name for the snap-in's static node. Be aware that **IDataObject::GetDataHere** is called when the static node is first displayed in the Standalone tab of the Add/Remove Snap-ins dialog box and when the static node is first added to the scope pane. After the initial creation of the static node, a snap-in must use the [**IConsoleNameSpace2::SetItem**](iconsolenamespace2-setitem.md) method to change the static node's name.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





