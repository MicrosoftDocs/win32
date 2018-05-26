---
title: Create Context-Sensitive Help
description: Create Context-Sensitive Help
ms.assetid: 23A161B9-8851-46d4-9558-0266FDD21605
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Create Context-Sensitive Help

Context-sensitive help assists users by providing help based on a specific dialog box or control in a program. This enables users to get specific information about whatever part of the program they are using at any given moment.

Help authors work with developers to create context-sensitive help. The help author creates a compiled help (.chm) file that contains the context-sensitive help topics and information that maps the topics to specific dialog boxes or controls. The developer modifies the program code so that the correct topic appears when a user requests help.

Context-sensitive help commonly appears in a [pop-up window](about-context-sensitive-pop-up-help.md), which displays a help topic about a specific user interface element. For example, you can design your program to have a question mark button in the title bar of a dialog box. When a user clicks the question mark button, and then clicks anywhere in the dialog box, they will see a pop-up help topic that provides information about the user interface element they clicked.

You can also design context-sensitive help topics to appear in a [secondary window](creating-secondary-windows.md), an [embedded window](creating-embedded-help-windows.md), or in a Web browser.

## Related topics

<dl> <dt>

[About Hooking Up Help to a Program](hook-up-help-to-a-program.md)
</dt> </dl>

 

 




