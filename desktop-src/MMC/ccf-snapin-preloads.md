---
title: CCF\_SNAPIN\_PRELOADS clipboard format
description: The CCF\_SNAPIN\_PRELOADS clipboard format is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fbd81606-84c8-45a1-9916-25ec6b78648e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_SNAPIN_PRELOADS clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_SNAPIN_PRELOADS
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_SNAPIN\_PRELOADS clipboard format

The CCF\_SNAPIN\_PRELOADS clipboard format is introduced in MMC 1.1.

The CCF\_SNAPIN\_PRELOADS clipboard format is for extension snap-ins that want to be preloaded when their parent is selected but before they are displayed.

## Data Format

BOOL. Return **TRUE** to preload. Return **FALSE** to not preload.

## Remarks

When a console file is saved, MMC stores the state of the tree in the scope pane. It also stores the scope item image and display name for each item that is visible in the scope pane so that the overhead of loading and expanding all snap-ins at console file open is not incurred just for the purpose of that displays the tree in the scope pane. For some items, this can be undesirable. For example, if the name of an item is dynamic based on what computer the console is running on, you want the correct computer name to appear on that item when a user opens the console file on another computer. In this case, you can implement this clipboard format in a snap-in to tell MMC to load that snap-in when its parent is selected and then send that snap-in an [**MMCN\_PRELOAD**](mmcn-preload.md) notification as the snap-in's first notification. The snap-in can handle this notification in its [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method.

When a console file is saved, MMC calls **IDataObject::GetDataHere** on each loaded snap-in using the CCF\_SNAPIN\_PRELOADS clipboard format. If the snap-in handles the CCF\_SNAPIN\_PRELOADS clipboard format and returns **TRUE**, MMC calls the [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method of the snap-in with the [**MMCN\_PRELOAD**](mmcn-preload.md) notification when the snap-in's parent is first visible.

For example, suppose primarysnap returned **TRUE** for CCF\_SNAPIN\_PRELOADS. If the .msc file was saved and closed with the following tree in the scope pane, primarysnap would get an [**MMCN\_PRELOAD**](mmcn-preload.md) notification when the .msc file was opened again (because its parent is the console root, which is expanded when the .msc file is opened):

console root

primarysnap

primarysnapitem1

primarysnapitem2

As another example, suppose primarysnap2 returned **TRUE** for CCF\_SNAPIN\_PRELOADS. If the .msc file was saved and closed with the following tree in the scope pane with primarysnap2 added beneath primarysnap1, primarysnap2 would get an [**MMCN\_PRELOAD**](mmcn-preload.md) notification when the .msc file was opened again:

console root

primarysnap1

primarysnap2

primarysnap2item1

primarysnap2item2

primarysnap1item1

primarysnap1item2

If the scope pane appeared with primarysnap1 collapsed and the .msc file was saved and closed, primarysnap2 would not get the MMCN\_PRELOAD until primarysnap1 was selected in the scope pane:

console root

primarysnap1

## Examples

The following code example (with s\_cfPreload as the static member holding the clipboard format) handles the CCF\_SNAPIN\_PRELOADS clipboard format and returns **TRUE**:


```C++
if (cf == s_cfPreload)
    {
        //
        BOOL bPreload = TRUE;
        hr = pStream->Write( (PVOID)&amp;bPreload, sizeof(BOOL), NULL );
    }
```



## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





