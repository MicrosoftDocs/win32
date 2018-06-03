---
title: Add/Remove Snap-in Dialog Box
description: The Add/Remove Snap-in dialog box allows authors of saved console files to identify available snap-ins and add and remove snap-ins. The dialog box is available only for saved console files in Author mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88804dc3-f290-4f1e-9dbe-9c2486ec51a0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Add/Remove Snap-in dialog box MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add/Remove Snap-in Dialog Box

The Add/Remove Snap-in dialog box allows authors of saved console files to identify available snap-ins and add and remove snap-ins. The dialog box is available only for saved console files in Author mode.

The console identifies snap-ins by the information you make available through the system registry. This is explained in [MMC Registry Entries](mmc-registry-entries.md).

The Add/Remove Snap-in dialog box presents a list of available snap-in components. The dialog box relies on complete and accurate entries in the system registry. Accordingly, snap-ins should be self-registering and should complete this task as part of the installation sequence.

Snap-in developers are encouraged to implement the [**ISnapinAbout**](/windows/desktop/api/Mmc/nn-mmc-isnapinabout) interface to provide MMC with a snap-in's About information. This information is only displayed in the Add/Remove Snap-in dialog box.

When a snap-in is added using the Add/Remove Snap-in dialog box, the console requests the snap-in to optionally display a configuration wizard for gathering settings during the insertion process. This is done by calling the snap-in's [**IComponentData::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-querydataobject) method with the CCT\_SNAPIN\_MANAGER as the value for the types parameter.

 

 




