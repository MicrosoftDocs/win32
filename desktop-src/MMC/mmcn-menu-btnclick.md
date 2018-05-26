---
title: MMCN\_MENU\_BTNCLICK message
description: Sent to the snap-in IExtendControlbar interface when the user clicks a snap-in defined menu button.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0455eb0-a773-4b03-a44a-339b48d5d57d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_MENU_BTNCLICK message MMC
topic_type:
- apiref
api_name:
- MMCN_MENU_BTNCLICK
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_MENU\_BTNCLICK message

The **MMCN\_MENU\_BTNCLICK** notification message is sent to the snap-in [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) interface when the user clicks a snap-in defined menu button.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

Not used.

</dd> <dt>

*arg* 
</dt> <dd>

The data object for a currently selected scope or result item.

</dd> <dt>

*param* \[in\]
</dt> <dd>

A pointer to a [**MENUBUTTONDATA**](/windows/win32/Mmc/ns-mmc-_menubuttondata?branch=master) structure.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification.

</dd> </dl>

## Remarks

The **idCommand** member of the [**MENUBUTTONDATA**](/windows/win32/Mmc/ns-mmc-_menubuttondata?branch=master) structure holds the user-specified command ID of the menu item that was clicked. The **x** and **y** members of this structure specify the position, if any, at which the snap-in's context menu is to be displayed.

The snap-in should display a context menu at the specified position and perform the required tracking and item selection processing.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master)
</dt> <dt>

[**IMenuButton::SetButtonState**](/windows/win32/Mmc/nf-mmc-imenubutton-setbuttonstate?branch=master)
</dt> </dl>

 

 





