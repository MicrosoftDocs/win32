---
title: Clipboard Information
description: The MMC application places its own data object onto the clipboard; this data object contains snap-in-provided data objects that are created as a result of Cut or Copy operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '95cda384-d50f-4c7a-895e-418b1e3fff54'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Clipboard Information

The MMC application places its own data object onto the clipboard; this data object contains snap-in-provided data objects that are created as a result of Cut or Copy operations. A snap-in data object is clipboard-valid as long as the scope node responsible for it is not deleted. Deleting a scope node will make any data objects associated with not valid and the data object will not provide data transfer.

These guidelines also apply to data objects that are created as a result of drag-and-drop operations.

If a "cut" result-pane item is being deleted, MMC does not release the associated data object from the clipboard. This behavior is consistent in MMC 1.2 and MMC 2.0 and allows a user to cut and delete a result item and paste it to a different node. To support this capability, a snap-in that allows clipboard operations must ensure the data object is not tied to the result item, and that it is valid at least for the lifetime of the scope node that created it.

MMC does not flush data to the clipboard. When a snap-in's node is deleted, its data object is removed from the clipboard. Additionally, when you exit MMC, MMC data objects will be removed from the clipboard.

MMC will always expose all data formats of the snap-in data object if the selection contains data from only one snap-in. This enables a snap-in to enable pasting to non-MMC applications, provided the snap-in supports a well-known data format such as **CF\_TEXT**.

MMC 2.0 also supports the participation of static nodes in clipboard operations. However, a clipboard operation cannot be used to change the position of a static node within the console file.

 

 




