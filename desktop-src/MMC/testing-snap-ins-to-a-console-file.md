---
title: Testing Snap-ins to a Console File
description: Ensures that a snap-in can be properly added to a console.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 75139303-9957-489b-a2e2-4ec8a11d7bc4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in testing MMC , testing to a console file
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing Snap-ins to a Console File

The following tests are recommended to ensure that your snap-in can be added to a console properly:

-   Ensure that a snap-in is not registered with a full path name, because if the user renames the folder that contains the snap-in, the user must use Regsvr32 again to register the snap-in.
-   Be sure to run tests both after adding your snap-in using the **Add/Remove Snap-in** dialog box and after adding it by using the console file.
-   If your snap-in is a primary snap-in, try running it with different extensions enabled and disabled.

 

 




