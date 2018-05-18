---
title: Guidelines for Creating a Context-Sensitive Help File
description: Guidelines for Creating a Context-Sensitive Help File
ms.assetid: '26000CD1-47EE-42ee-9BC3-BB2848753A8A'
---

# Guidelines for Creating a Context-Sensitive Help File

When you write context-sensitive help, you first [create a file containing context-sensitive help topics](to-create-a-text-file-for-pop-up-help-topics.md) to which you have assigned unique IDs. Then you create a [header file](to-create-a-header-file.md) that lists the symbolic IDs and numeric IDs for all the dialog boxes and controls in a program.

Before you begin writing, consider the following:

-   Depending on your program, you could end up with hundreds or even thousands of context-sensitive help topics. If you develop a good tracking system it will save time when you communicate with software developers or test your files.
-   If you use IDH as the prefix for your context-sensitive help topic IDs, HTML Help Workshop automatically checks that the topics mapped in your project file actually exist in your compiled help (.chm) file. It also makes sure that your context-sensitive help topics are all mapped in your project (.hhp) file.
-   You do not need to write topics or add code for the **OK**, **Cancel**, **Save**, **Open**, **Print** and other buttons that are associated with common Windows 95 dialog boxes, because they are already included. However, if your software developer has modified the common dialog template to add a custom control to a dialog box, you must write help topics for any additional items.
-   Make sure that your software developer maps the help to include the labels, as well as the controls, in a program's dialog box. Some users click the control in a dialog box, such as a button or text box, to get help, while others click the label for the control. You probably want the same help topic to appear in either situation.
-   If there are several items in a group box, you might want separate help topics for each item. In this case, you can assign the group box label a generic topic that tells users to click each item in the group for specific information. If there is only one item in the group box, associate the group box label with the topic for the item.
-   You can map a topic ID to any number, but the numeric values defined in a help file must all be unique. You can specify numeric values in either decimal or standard hexadecimal format. Often, the software developer will create the mapping for you in a header (.h) file that you can include in your project.

> [!Note]  
> Information for software developers about creating the code for context-sensitive help is in the [HTML Help API reference](about-the-html-help-api-reference.md).

 

## Related topics

<dl> <dt>

[About Creating Context-Sensitive Help](create-context-sensitive-help.md)
</dt> </dl>

 

 




