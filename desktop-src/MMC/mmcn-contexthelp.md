---
title: MMCN\_CONTEXTHELP message
description: The MMCN\_CONTEXTHELP notification message is sent to the snap-in's IComponent implementation when the user requests help about a selected item by pressing the F1 key or Help button.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e12616c0-e5bc-4a0d-8199-467c1647acf6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_CONTEXTHELP message MMC
topic_type:
- apiref
api_name:
- MMCN_CONTEXTHELP
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_CONTEXTHELP message

The **MMCN\_CONTEXTHELP** notification message is sent to the snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation when the user requests help about a selected item by pressing the F1 key or **Help** button.

A snap-in responds to **MMCN\_CONTEXTHELP** by that displays a Help topic for the particular context by calling the [**IDisplayHelp::ShowTopic**](/windows/desktop/api/Mmc/nf-mmc-idisplayhelp-showtopic) method.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope or result item.

</dd> <dt>

*arg* 
</dt> <dd>

Zero.

</dd> <dt>

*param* 
</dt> <dd>

Zero.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in handles the notification message. See Remarks for details.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification message. MMC displays a default topic. See Remarks for details.

</dd> </dl>

## Remarks

If the snap-in handles the **MMCN\_CONTEXTHELP** notification, MMC expects the snap-in to specify a Help topic for the selected item. Consequently, in the notification handler for **MMCN\_CONTEXTHELP** notification, the snap-in has two options:

-   It can call [**IDisplayHelp::ShowTopic**](/windows/desktop/api/Mmc/nf-mmc-idisplayhelp-showtopic) or [*MMCPropertyHelp*](/windows/desktop/api/Mmc/nf-mmc-mmcpropertyhelp) to specify the Help topic and then return **S\_OK** to indicate success. Be aware that the snap-in should only return **S\_OK** if it specifies a Help topic. If the snap-in returns **S\_OK** without specifying a Help topic, no Help topic will be displayed.
-   It can return **S\_FALSE** to the notification. MMC then brings up the table of contents with the default MMC topic selected.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[Adding HTML Help Support](adding-html-help-support.md)
</dt> </dl>

 

 





