---
title: System Policies for Shortcut and WinHelp Commands
description: Two system policies have been introduced to address various security issues related to the Shortcut and WinHelp commands.
ms.assetid: AEDD45D1-B6B1-4fd6-9674-4C73D83A243E
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System Policies for Shortcut and WinHelp Commands

There are features in HTML Help that make it possible to run executable programs from a help file (.chm) . The "Shortcut" command is used to run an executable program that is external to the Help file. The "WinHelp" command is used to run WinHLP32.exe to display a Winhelp (.hlp) file.

Two system policies have been introduced to address various security issues related to the Shortcut and WinHelp commands. These policies can be used to control where Help shortcuts can run on the local machine, and which programs can be launched from a compiled Help (.chm) file. You can access these policies and edit their respective properties using the Group Policy snap-in (gpedit.msc).

> [!Note]  
> Administrator privileges are required to edit system policies.

 

The following topics describe the system policies:

-   [Restrict potentially unsafe HTML Help functions to specified folders](restrict-potentially-unsafe-html-help-functions-to-specified-folders.md)
-   [Restrict these programs from being launched from Help](restrict-these-programs-from-being-launched-from-help.md)
-   [Troubleshooting HTML Help Shortcut Issues](troubleshooting-html-help-shortcut-issues.md)

**To access the system policies**

1.  Ensure that you are logged into Windows with administrator privileges.
2.  Launch the Group Policy snap-in. Click **Start**, click **Run**, type **gpedit.msc**, and click **OK**.
3.  In the left pane, select the following node: **Local Computer Policy**, **Computer Configuration**, **Administrative Templates**, **System**. The policies are listed in the right pane as follows:

    **Restrict potentially unsafe HTML Help functions to specified folders**

    **Restrict these programs from being launched from Help**

4.  Double-click the desired policy to display the **Properties** dialog box for the policy. Here you can enable, disable, and set options for the policy.

 

 




