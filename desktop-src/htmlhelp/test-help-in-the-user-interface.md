---
title: Test Help in the User Interface
description: If your help system is designed so that a help file can be opened from a Help menu or other item in the user interface, test to ensure that help will start when users expect it to.
ms.assetid: 9661CBAA-7AA0-4151-8714-0563351F5E63
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Test Help in the User Interface

If your help system is designed so that a help file can be opened from a Help menu or other item in the user interface, test to ensure that help will start when users expect it to.

## Suggested tasks for testing

-   If your help system uses a Help menu, click the menu item and make sure that the correct help file opens.
-   If your help system is designed so that a help file opens when a user presses the F1 key, test that the correct help topic opens.
-   Open each dialog box that has links to help and test that the correct help topic opens. If your program has help buttons in dialog boxes, try all of them. If your program uses a question mark or right-click help, test any items that have help connected to them.
-   Double-click the icon for the help file. Make sure the Help Viewer or the frameset you have created opens and that the correct index, table of contents, or topic appears in the correct window.
-   If your help system contains files for optional components, test help files with each component installed or not installed to ensure that the correct files appear at the correct times.
-   If you use information types in your help topics, test to ensure that the topics are reaching the appropriate audiences.
-   If you are delivering a help system to different Web browsers or to users with different versions of the same Web browser, test your topics in each browser or browser version.

## Testing context-sensitive help

Unfortunately, there is no automated way to make sure that the correct context-sensitive help topic appears when the user requests help for an item. You need to test context-sensitive help in context by using your program. Open every dialog box and click every item where you expect context-sensitive help to appear.

## Related topics

<dl> <dt>

[Develop a Process for Testing Help Files](creating-a-process-for-testing.md)
</dt> </dl>

 

 




