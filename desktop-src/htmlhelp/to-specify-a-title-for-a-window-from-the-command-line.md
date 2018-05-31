---
title: To specify a title for a window from the command line
description: To specify a title for a window from the command line
ms.assetid: E1F64804-9049-4072-8F98-D42D112A6491
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To specify a title for a window from the command line

1.  [Create a window](to-create-an-800-x-600-window-from-the-command-line.md).

2.  From a command prompt or from the **Run** command, type **-title** *text* to specify the title for the window.

## Notes

-   The -800 switch creates an 800 X 600 display window that does not cover the Windows taskbar at the bottom of the screen. You can use it as a standalone command or add it to a program or to a Windows shortcut.
-   This command is ignored if you have specified any default window types in your compiled help file.
-   Client-side command line switches are part of the HTML Help executable program (Hh.exe) and therefore work when HTML Help Workshop is not set up.

## Related topics

<dl> <dt>

[About Command Line Switches](using-command-line-switches.md)
</dt> </dl>

 

 




