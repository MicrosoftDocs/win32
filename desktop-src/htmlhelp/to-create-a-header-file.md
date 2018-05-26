---
title: To create a header file
description: To create a header file
ms.assetid: 7E35EBCC-0F68-4aa8-8498-1B0CC1F1B909
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create a header file

1.  Open Microsoft Notepad or another text editor.
2.  Create an entry for each symbolic ID, followed by its corresponding numeric ID, using the following format:

    ```
    #define IDH_symbolicID    1000
    ```

    

3.  Where `symbolicID` is the symbolic ID for part of the program (such as a dialog box or control) and 1000 is the numeric ID. The numeric IDs in the header file are used only by the HTML Help compiler. The compiler maps numeric IDs in the header file to help topics.
4.  Save the file with a .h extension.

The following sample header file is taken from HTML Help Workshop:

![](images/header-sample.gif)

## Note

If you use an IDH\_ prefix with the symbolic ID, as shown in the example above, HTML Help Workshop will automatically check that the topics mapped in your project file actually exist in your compiled help (.chm) file, and that your context-sensitive help topics are all mapped in your project file.

## Related topics

<dl> <dt>

[Step 3: Create a \[TEXT POPUPS\] Section in a Project File](to-create-a-text-popups-section-in-a-project-file.md)
</dt> </dl>

 

 




