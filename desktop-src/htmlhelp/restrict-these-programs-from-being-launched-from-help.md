---
title: Restrict these programs from being launched from Help
description: Restrict these programs from being launched from Help
ms.assetid: F419BE73-403C-4f14-BB8C-17D1DE4085E4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Restrict these programs from being launched from Help

**Requirements:** At least Microsoft Windows XP Professional or Windows Server 2003.

This policy allows you to restrict programs from being run from online Help.

The settings for this policy are located in the following key of the Windows registry (default settings shown):

\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Policies\\Microsoft\\windows\\System\]

"DisableInHelp"="cmd.exe,command.com"

If you enable this setting, you can prevent programs that you specify from being allowed to be run from Help. When you enable this setting, enter the list of the programs you want to restrict. Enter the file name of the executable for each application, separated by commas.

If you disable or do not configure this setting, users will be able to run applications from online Help.

> [!Note]  
> This setting is available under both **Computer Configuration** and **User Configuration**. If both are set, the list of programs specified in each of these will be restricted.

 

> [!Note]  
> You can also restrict users from running applications by using the Software Restriction settings available in **Local Computer Policy**, **Computer Configuration**, **Security Settings**.

 

> [!Note]  
> For more information about editing the Windows registry, go to the [Microsoft Support Knowledge Base](http://support.microsoft.com/search/) and search for "regedit".

 

## Related topics

<dl> <dt>

[Restrict potentially unsafe HTML Help functions to specified folders](restrict-potentially-unsafe-html-help-functions-to-specified-folders.md)
</dt> </dl>

 

 




