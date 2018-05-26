---
title: CCF\_NODEID clipboard format
description: In MMC 1.1 and later, the CCF\_NODEID clipboard format enables a snap-in to specify the node ID for the selected enumerated item in the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12c600c7-b904-4e7a-ae78-76e90de5e0aa
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_NODEID clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_NODEID
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CCF\_NODEID clipboard format

In MMC 1.1 and later, the **CCF\_NODEID** clipboard format enables a snap-in to specify the node ID for the selected enumerated item in the scope pane. MMC uses this node ID to identify the selected item and select that item when a console file is reopened. This format can also be used to specify that an item should not be restored when the console file is reopened.

## Data Format

[**SNodeID**](/windows/win32/Mmc/ns-mmc-_snodeid?branch=master) structure. Return an **SNodeID** structure that contains the node ID for the scope item.

## Remarks

Your snap-in should support this clipboard format in its [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method if any of its enumerated items has a volatile display name (such as the current computer name) or if any enumerated items should not be restored when the console file is reopened.

MMC calls the [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method with this clipboard format in the following cases:

-   When the console file is saved. MMC does this to preserve the root item and the selected item for a window when either is an enumerated node (item).
-   When a new view (MDI window) is created, using the New window from here menu command or drag-and-drop. If the snap-in specifies that it does not want the item persisted, MMC marks the view as not-to-be-persisted and does not open an empty view when the console is reopened.
-   When the console file is loaded. MMC calls [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) on each of the snap-in's items (starting from the first item) until it finds the saved node IDs so it can identify selected and root items.

When a console file (.msc) is saved, MMC persists some information about the selected item in the scope pane so that it can restore the scope tree with that particular item selected. When the .msc file is saved, MMC calls the [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method with the **CCF\_NODEID** clipboard format on the selected item's data object.

The snap-in's [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method implementation can specify the node ID that should be persisted for that item so that MMC can identify and select the appropriate item when the .msc file is reopened. The snap-in should fill in the **SNodeID** structure and return **S\_OK** in the **IDataObject::GetData** method.

The snap-in can also specify that an item should not be re-expanded when the console is reopened. To do this, set the **cBytes** member of the [**SNodeID**](/windows/win32/Mmc/ns-mmc-_snodeid?branch=master) structure to 0 (zero) and return **S\_OK** in the [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method. Be aware that this setting not only keeps the selected item from being persisted but also prevents its parent item from automatically expanding when the console file is reopened.

If the snap-in's [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) method does not support the **CCF\_NODEID** clipboard format or if a FAILED **HRESULT** is returned by the **IDataObject::GetData** method, MMC uses the display name of the item as the node ID.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





