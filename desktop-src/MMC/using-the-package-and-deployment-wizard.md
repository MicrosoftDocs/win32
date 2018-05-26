---
title: Using the Package and Deployment Wizard
description: Describes the use of the package and deployment wizard.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d6986f9-5e88-4d52-aeb8-770e908f8f2a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using the Package and Deployment Wizard

Use the Visual Basic Package and Deployment Wizard to create a package and setup program for a snap-in created in Visual Basic.

The following files are required for a Visual Basic snap-in installation:

-   Snap-in dynamic-link library (DLL) created by Visual Basic
-   Snap-in designer runtime (Mssnapr.dll)
-   Visual Basic 6.0 runtime (Msvbvm60.dll)

You can also use the Package and Deployment Wizard to create a package for a saved console file. Before you start, place the console file (.msc) in a directory that contains a snap-in project, and then use the following procedure.

**To create a package for a saved console file**

1.  On the Visual Basic **Tools** menu, click Package and Deployment Wizard.
2.  In the **Select Project** drop-down list box, click the snap-in project you want to use or click the **Browse** button to locate the snap-in project.
3.  Click **Next** to continue to the page entitled "Package and Deployment Wizard–Included Files," and then click **Add**.
4.  In the **Files of type** drop-down list box, click **All Files**.
5.  Select the saved console file (.msc), and then click Open.
6.  Proceed to the Start Menu Items page, and then click New Item.
7.  In the **Target** drop-down list box, click the .msc file to use.
8.  In the **Name** text box, type the name you want for your icon, and then click **OK**.
9.  Click **Finish** to close the **Package and Deployment** Wizard.

 

 




