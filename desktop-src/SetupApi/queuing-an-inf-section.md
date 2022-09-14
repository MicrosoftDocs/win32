---
description: In addition to queuing file operations individually, you can also queue all the files listed in an INF section.
ms.assetid: 456e1a19-7e9b-40c8-9295-42bb8f740f58
title: Queuing an INF Section
ms.topic: article
ms.date: 05/31/2018
---

# Queuing an INF Section

In addition to queuing file operations individually, you can also queue all the files listed in an INF section.

You can queue all the files listed in a **Copy Files** section of an INF file by calling [**SetupQueueCopySection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuecopysectiona). For this function to be successful, the **Copy Files** section must be in the proper format and the INF file, or one of its appended files, must contain the **SourceDisksFiles** and **SourceDisksNames** sections.

Similarly, if you want to delete all the files specified in a **Delete Files** section of an INF file, you can call [**SetupQueueDeleteSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuedeletesectiona). To rename all the files in a **Rename Files** section of an INF file use [**SetupQueueRenameSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueuerenamesectiona).

 

 



