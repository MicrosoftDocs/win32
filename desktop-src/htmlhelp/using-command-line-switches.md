---
title: Using Command Line Switches
description: Using Command Line Switches
ms.assetid: 939F6C8E-5C2E-411d-8CEE-A505F935E8DC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Command Line Switches

Several client-side command line switches are available to help authors that are part of the HTML Help executable program (Hh.exe) and therefore work when HTML Help Workshop is not set up.

From a DOS prompt or from the **Run** command, you can perform the following tasks.



| Option     | Purpose                                                                                                                                                                                    | API equivalent                                                | Notes                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------|
| -800       | Display the Help viewer in an 800x600 window, without covering the Windows taskbar. For more information, see [800 X 600 window](to-create-an-800-x-600-window-from-the-command-line.md). | None                                                          | Disabled in safe mode. |
| -title     | Sets the title to use for an 800 X 600 window. For more information, see [Specify the title](to-specify-a-title-for-a-window-from-the-command-line.md).                                   | None                                                          | Disabled in safe mode. |
| -register  | Registers hh.exe (the calling process) as the shell-open command handler for .chm files                                                                                                    | None                                                          | Disabled in safe mode. |
| -decompile | Decompiles a .chm file to a command-line specified location. For more information, see [Decompile a .chm file](to-decompile-a-compiled-help-file-from-the-command-line.md).               | None                                                          | Disabled in safe mode. |
| -mapid     | Opens the requested .chm in the Help viewer, and uses a context ID to request a URL to display. For more information, see [map ID](using-a-map-id-from-the-command-line.md).              | [HH\_HELP\_CONTEXT](hh-help-context-command.md)              | Disabled in safe mode. |
| -safe      | Forces Help content to run in safe mode (all shortcuts are disabled).                                                                                                                      | [HH\_SAFE\_DISPLAY\_TOPIC](hh-safe-display-topic-command.md) |                        |



 

## Related topics

<dl> <dt>

[HTML Help Reference](html-help-references.md)
</dt> </dl>

 

 




