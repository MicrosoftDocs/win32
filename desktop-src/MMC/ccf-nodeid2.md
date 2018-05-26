---
title: CCF\_NODEID2 clipboard format
description: The CCF\_NODEID2 clipboard format replaces the CCF\_NODEID format in MMC 1.2. The CCF\_NODEID2 format uses an SNodeID2 structure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 898f1691-6024-4873-a217-c8fb1b528400
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_NODEID2 clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_NODEID2
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_NODEID2 clipboard format

The CCF\_NODEID2 clipboard format replaces the [**CCF\_NODEID**](ccf-nodeid.md) format in MMC 1.2. The CCF\_NODEID2 format uses an [**SNodeID2**](/windows/win32/Mmc/ns-mmc-_snodeid2?branch=master) structure.

CCF\_NODEID2 behaves in the same way as the [**CCF\_NODEID**](ccf-nodeid.md) format. The format enables a snap-in to specify the node ID for the selected enumerated item in the scope pane. MMC uses this node ID to identify the selected item and select that item when a console file is reopened. This format can also be used to specify that an item should not be restored when the console file is reopened.

If the CCF\_NODEID2 clipboard format is supported by a data object, the [**CCF\_NODEID**](ccf-nodeid.md) format is not used.

## Data Format

[**SNodeID2**](/windows/win32/Mmc/ns-mmc-_snodeid2?branch=master) structure. Be aware that returning cBytes=0 is illegal for CCF\_NODEID2. The [**CCF\_NODEID**](ccf-nodeid.md) format permitted SNodeID.cBytes to be zero to designate that the item should not be persisted. In the **SNodeID2** structure, this is indicated by setting SNodeID2.dwFlags to **MMC\_NODEID\_SLOW\_RETRIEVAL**.

## Remarks

Your snap-in should support this clipboard format in its IDataObject::GetData method if any of its enumerated items has a volatile display name (such as the current computer name) or if any enumerated items should not be restored when the console file is reopened.

MMC calls the IDataObject::GetData method with this clipboard format in the following cases:

-   When the console file is saved. MMC does this to preserve the root item and the selected item for a window when either is an enumerated node (item).
-   When a new view (MDI window) is created, using the New window from here menu command or drag-and-drop. If the snap-in specifies that it does not want the item persisted, MMC marks the view as not-to-be-persisted and does not open an empty view when the console is reopened.
-   When the console file is loaded. MMC calls IDataObject::GetData on each of the snap-in items (starting from the first item) until it finds the saved node IDs so it can identify selected and root items.

When a console file (.msc) is saved, MMC persists some information about the selected item in the scope pane so that it can restore the scope tree with that particular item selected. When the .msc file is saved, MMC calls the IDataObject::GetData method with the CCF\_NODEID2 clipboard format on the selected item's data object.

The snap-in's IDataObject::GetData method implementation can specify the node ID that should be persisted for that item so that MMC can identify and select the appropriate item when the .msc file is reopened. The snap-in should fill in the SNodeID2 structure and return S\_OK in the IDataObject::GetData method.

The snap-in can also specify that a item should not be re-expanded when the console is reopened, for example when the item cannot be re-created quickly from a persistent representation. To do this, set the dwFlags member of the SNodeID2 structure to MMC\_NODEID\_SLOW\_RETRIEVAL and return S\_OK in the IDataObject::GetData method. This will prevent MMC from persisting the item except where absolutely necessary, as for example for console taskpads. Console taskpads always persist the target item and task target items. Be aware that this setting not only keeps the selected item from being persisted but also prevents its parent item from automatically expanding when the console file is reopened.

If the snap-in's IDataObject::GetData method does not support the CCF\_NODEID2 clipboard format, MMC will call IDataObject::GetData with the [**CCF\_NODEID**](ccf-nodeid.md) format.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





