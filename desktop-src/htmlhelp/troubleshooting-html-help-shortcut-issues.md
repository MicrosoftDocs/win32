---
title: Troubleshooting HTML Help Shortcut Issues
description: This topic outlines the most common issues associated with the Shortcut and WinHelp commands, and provides workarounds where possible.
ms.assetid: CD928A85-F274-4bca-94D4-83EEBD6C4D61
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Troubleshooting HTML Help Shortcut Issues

This topic outlines the most common issues associated with the Shortcut and WinHelp commands, and provides workarounds where possible.

## One or both system policies are applied.

If you have administrator privileges on the computer, you can edit the system policy using the Group Policy snap-in, or by updating the appropriate key in the Windows Registry. See [Restrict potentially unsafe HTML Help functions to specified folders](restrict-potentially-unsafe-html-help-functions-to-specified-folders.md), and [Restrict these programs from being launched from Help](restrict-these-programs-from-being-launched-from-help.md) for more information.

## The .chm file is located on a network drive.

Shortcuts will not work when called from a .chm on a network drive. In order for the Shortcut and WinHelp commands to work properly, the .chm must be located on the local drive.

## The target executable is not located within the System Path, or within the current working directory.

Help authors need to ensure that shortcut targets are located within the system path, or within the current working directory for the calling application. In all cases, the manual steps required to launch a shortcut target should be documented. This is critical in the event that shortcuts are disabled on a user's computer.

## ActiveX Controls are turned off OR the Shortcut command was invoked through scripting, but scripting is turned off.

Because the Shortcut and WinHelp commands rely on an ActiveX control, they will not work if this feature is turned off. Likewise, if scripting is disabled some instances of shortcuts may not work as expected. Use the following procedure to check these settings and reset if necessary.

## To set Internet Options

1.  Click **Start** &gt; **Settings** &gt; **Control Panel**, and open **Internet Options**.
2.  On the **Security** tab, select the **Local Intranet** zone and click the **Custom Level** button.
3.  Verify that ActiveX controls and/or scripting, are enabled for the local intranet zone.

    These settings can also be accessed through the **Tools** menu of Internet Explorer.

## Related topics

<dl> <dt>

[System policies for Shortcut and WinHelp Commands](system-policies-for-shortcut-and-winhelp-commands.md)
</dt> </dl>

 

 




