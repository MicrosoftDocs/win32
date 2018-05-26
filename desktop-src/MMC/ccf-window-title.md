---
title: CCF\_WINDOW\_TITLE clipboard format
description: The CCF\_WINDOW\_TITLE clipboard format enables a snap-in to specify the string used to represent the snap-ins static node in the title bar of windows created programmatically using IConsole2 NewWindow(MMC\_NW\_OPTION\_CUSTOMTITLE).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c02011e-0013-4cf4-8caa-0b2a2faf2870
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_WINDOW_TITLE clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_WINDOW_TITLE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_WINDOW\_TITLE clipboard format

The CCF\_WINDOW\_TITLE clipboard format enables a snap-in to specify the string used to represent the snap-in's static node in the title bar of windows created programmatically using **IConsole2::NewWindow(MMC\_NW\_OPTION\_CUSTOMTITLE)**.

## Data Format

WCHAR string. Return a string that contains the name to display for the snap-in's static node in the title bar of the window in which the snap-in appears.

## Remarks

This clipboard format is optional. Be aware that the scope path from the root node of the window is displayed in the title bar. When a stand-alone snap-in's static node or one of its child items is selected in the scope pane, MMC calls the snap-in's **IDataObject::GetDataHere** method requesting the CCF\_WINDOW\_TITLE clipboard format to retrieve the name that the snap-in wants to use to represent its static node in the scope path in the title bar.

To specify the title bar name for the snap-in's static node, the snap-in must support this format in its **IDataObject::GetDataHere** implementation.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IS\_SPECIAL\_COOKIE**](/windows/win32/Mmc/nf-mmc-is_special_cookie?branch=master)
</dt> </dl>

 

 





