---
title: To create a shortcut in a help topic
description: To create a shortcut in a help topic
ms.assetid: 'C1528B34-6E45-4153-846F-3EB4BD16B988'
---

# To create a shortcut in a help topic

Shortcuts are hotspots that can launch another application, or take the user to a specific dialog box within an application. You can also use shortcuts to activate things like Windows control panels. Use shortcuts to make things easier for novice users, and speed experienced users through complex procedures.

Using the **Shortcut** command, you can specify which program to open, which file to open in the program (if any), the Window class for the program, and a standard Windows message followed by WPARAM and LPARAM values. You can also specify an HTML file to jump to if the program cannot be found.

You can use the [HTML Help ActiveX Control Wizard](example--creating-a-shortcut.md) to insert a **Shortcut** command, or [insert the code manually](shortcut.md).

The shortcut feature only works when the following conditions are met:

-   The shortcut must be in a compiled help file.
-   The compiled help file must be located on a local or network drive (a file accessed through HTTP will not work).
-   The compiled help file must appear in the Help Viewer; a shortcut will not work in a file that appears in Microsoft Internet Explorer.

Click here to see a shortcut in action (this one launches notepad.exe).

## Notes

-   Consider the security risks if you create a shortcut that initiates an event from a compiled help (.chm) file to the Internet.
-   For detailed information about the **Shortcut** command, see the [HTML Help ActiveX control reference](shortcut.md).

## Related topics

<dl> <dt>

[About Hooking Up Help to a Program](hook-up-help-to-a-program.md)
</dt> </dl>

 

 




