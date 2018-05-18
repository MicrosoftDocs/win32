---
title: Restrict potentially unsafe HTML Help functions to specified folders
description: Restrict potentially unsafe HTML Help functions to specified folders
ms.assetid: 'C735FBF3-A664-4550-B691-472E01B89451'
---

# Restrict potentially unsafe HTML Help functions to specified folders

**Requirements:** At least Internet Explorer 6 Service Pack 1.

With this policy, you can restrict certain HTML Help commands to function only in HTML Help (.chm) files within specified folders and their subfolders. Alternatively, you can disable these commands on the entire system. It is strongly recommended that only folders requiring power user or administrative privileges to write or change files be added to this policy.

When this policy is disabled, or not configured, these commands are fully functional for all Help files.

When this policy is enabled, the commands will function only for .chm files in the specified folders and their subfolders.

The settings for this policy are located in the following key of the Windows registry (default settings shown):

\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Policies\\Microsoft\\windows\\System\]

"HelpQualifiedRootDir"="%windir%\\\\help;%programfiles%"

**To restrict the commands to one or more folders**

1.  Launch the Group Policy snap-in. Click **Start**, click **Run**, type **gpedit.msc**, and click **OK**.
2.  In the left pane, select the following node: **Local Computer Policy**, **Computer Configuration**, **Administrative Templates**, **System**. From the list in the right pane, double-click **Restrict potentially unsafe HTML Help functions to specified folders**.
3.  Enable the policy and enter the desired folders in the text box on the **Settings** tab of the Policy Properties dialog box. Use a semicolon to separate folders. For example, to restrict the commands to only .chm files in the %windir%\\help folder and C:\\MyFolder, add the following string to the edit box: "%windir%\\help; C:\\MyFolder ".

> [!Note]  
> An environment variable may be used, (for example, %windir%), so long as it is defined on the system. For example, %programfiles% is not defined on some early versions of Windows.

 

> [!Note]  
> Only folders on the local computer can be specified in this policy. You cannot use this policy to enable the "Shortcut" and "WinHelp" commands for .chm files that are stored on mapped drives or accessed using network (UNC) paths.

 

**To disallow the "Shortcut" and "WinHelp" commands on the entire local system**

1.  Launch the Group Policy snap-in. Click **Start**, **Run**, type "gpedit.msc" (without the quotes), and click **OK**.
2.  In the left pane, select the following node: **Local Computer Policy**, **Computer Configuration**, **Administrative Templates**, **System**. From the list in the right pane, double-click **Restrict potentially unsafe HTML Help functions to specified folders**.
3.  Enable the policy and leave the text box on the **Settings** tab of the **Policy Properties** dialog box blank.

> [!Note]  
> For more information about editing the Windows registry, go to the [Microsoft Support Knowledge Base](http://support.microsoft.com/search/) and search for "regedit".

 

## Related topics

<dl> <dt>

[Restrict these programs from being launched from Help](restrict-these-programs-from-being-launched-from-help.md)
</dt> </dl>

 

 




