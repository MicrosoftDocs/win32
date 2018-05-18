---
title: Example Creating Context-Sensitive Pop-up Help
description: Example Creating Context-Sensitive Pop-up Help
ms.assetid: 'DA4E6726-E415-4403-AE63-FE7CB0AE467D'
---

# Example: Creating Context-Sensitive Pop-up Help

Context-sensitive help enables a user to easily find information about a specific user interface element. Pop-up help appears in a pop-up window rather than in the Help Viewer. This example is a four-step process that explains how to create context-sensitive pop-up help.

To make context-sensitive pop-up help work, you need to create a text file for your help topics and a header (.h) file, and then include them in your project (.hhp) file.

-   The text file contains all of the topics that are used for pop-up help. Each topic ID in the text file must match a symbolic ID in the header file. You can create more than one text file for topics.
-   The header file lists the symbolic IDs and numeric IDs for all the dialog boxes and controls in a program. Your software development team should be able to supply a list of IDs for your header file.

The steps of the process are as follows:

1.  [Create a text file for pop-up help topics.](to-create-a-text-file-for-pop-up-help-topics.md)
2.  [Create a header file.](to-create-a-header-file.md)
3.  [Create a \[TEXT POPUPS\] section in your project file.](to-create-a-text-popups-section-in-a-project-file.md)
4.  [Include a header file in your project file.](to-include-a-header-file-in-a-project-file.md)

## Notes

-   Before proceeding, you may want to review some basic [guidelines for creating context-sensitive help topics](guidelines-for-creating-a-context-sensitive-help-file.md).
-   If your help doesn't work as expected, you can [troubleshoot pop-up help problems](troubleshooting-context-sensitive-help.md).

## Related topics

<dl> <dt>

[About Creating Context-Sensitive Help](create-context-sensitive-help.md)
</dt> </dl>

 

 




