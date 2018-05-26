---
title: Using Copy as the Default Drag-and-Drop Verb
description: The available drag-and-drop operations are determined by the enabled state of the Copy and Cut verbs, as shown in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 61d18dc4-cc6f-4ec8-a23b-cdd4d7ac7fb8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Copy as the Default Drag-and-Drop Verb

The available drag-and-drop operations are determined by the enabled state of the Copy and Cut verbs, as shown in the following table.



| Copy     | Cut      | Available operations |
|----------|----------|----------------------|
| Enabled  | Enabled  | Copy, Move           |
| Enabled  | Disabled | Copy                 |
| Disabled | Enabled  | Move                 |
| Disabled | Disabled | None                 |



 

When both Copy and Move are available (as is the case when the Copy and Cut verbs are enabled), the snap-in has the ability to specify whether Move or Copy is the default operation. (Be aware that in MMC 1.2, Move, or "Move Here", was the default operation, and it was not modifiable). The default operation is executed when no keys are pressed while the user performs a left-button drag-and-drop operation; the default operation also appears as a bold context menu item when the user is prompted after performing a right-button drag-and-drop operation. If your snap-in wants Move ("Move Here") as the default operation, no action must be taken. If your snap-in wants Copy ("Copy Here") as the default operation, specify the **MMC\_DEFAULT\_OPERATION\_COPY** flag when responding to the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification; the snap-in can specify this flag using the pointer to the **DWORD** value passed as the **MMCN\_QUERY\_PASTE**'s *param* parameter.

If the user presses the CONTROL or SHIFT key during left-button drag-and-drop operation, the use of **MMC\_DEFAULT\_OPERATION\_COPY** has no effect. The following depicts the left-button drag-and-drop operation based on the user's choice of keys (if any) and the snap-in's use of **MMC\_DEFAULT\_OPERATION\_COPY** in response to [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md). Assume that both Cut and Copy are enabled.



| Key pressed | MMC\_DEFAULT\_OPERATION\_COPY not set | MMC\_DEFAULT\_OPERATION\_COPY set |
|-------------|---------------------------------------|-----------------------------------|
| (None)      | "Move Here"                           | "Copy Here"                       |
| Control     | "Copy Here"                           | "Copy Here"                       |
| Shift       | "Move Here"                           | "Move Here"                       |



 

 

 




