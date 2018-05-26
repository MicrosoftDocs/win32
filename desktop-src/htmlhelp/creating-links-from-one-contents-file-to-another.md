---
title: Creating Links from One Contents File to Another
description: HTML Help provides the capability to link from one contents file to another.
ms.assetid: 4684B6A8-03E2-433c-BEEE-45A96DBCAE0E
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Links from One Contents File to Another

HTML Help provides the capability to link from one contents file to another. This is extremely useful for creating and maintaining modular documentation. Rather than maintaining several versions of a table of contents, you can selectively combine them by linking.

## To create a contents file that includes links to other contents files

1.  Click the **Contents** tab, and then click **Insert a Heading**. 

    |                          |                                                                                                                          |
    |--------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | ![](images/sb-inshd.gif) | Adds a heading level icon to a table of contents with its associated name, file, URL, and style information. <br/> |

    

     

2.  Type a name for the heading that will include your contents entries from another help file, and then click **OK**.
3.  Right-click the heading, and then click **Insert File**.
4.  In the **File to include** box, type the following syntax:

    ```
    file name.chm::/contents.hhc
    ```

    

    where file name.chm is the name of the compiled help file and contents.hhc is the name of the contents file to which you want to link.

    > [!Note]  
    > The contents are merged at run time, which is when the compiled help (.chm) file is opened. Because of this, you must always ship the compiled help file whose contents you are merging with your main help file, and they must be stored in the same directory.

     

## Related topics

<dl> <dt>

[About Creating Table of Contents Files](create-a-table-of-contents-file.md)
</dt> </dl>

 

 





