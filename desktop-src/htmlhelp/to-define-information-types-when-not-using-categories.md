---
title: To define information types when not using categories
description: To define information types when not using categories
ms.assetid: 2F42CD68-0D04-4e2a-8653-2FDDDA2E0D96
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# To define information types when not using categories

1.  Open a contents (.hhc) file, and then click **Contents Properties**.

    

    |                          |                                                                     |
    |--------------------------|---------------------------------------------------------------------|
    | ![](images/sb-conpr.gif) | Defines the general appearance of the table of contents.<br/> |

    

     

2.  Click the **Information Types** tab, and then click **Add**.
3.  In the **Information type name** box, type the name of the information type you want (for example, Overview).
4.  In the **Description** box, type a description of the information type. The description is important because it is viewed by the user in the wizard that walks them through information type selection.
5.  Click either **Inclusive Type** or **Exclusive Type** to assign an information type attribute.

## Notes

-   You may want to make a backup copy of your contents file before you add information types to it.
-   After you define information types, you can [assign them to a table of contents entry](to-assign-an-information-type-to-a-contents-entry.md).
-   You can create up to 32 separate information types. The name for an information type cannot exceed 255 characters.
-   If used with a [large collection](manage-large-document-sets.md) of merged compiled help (.chm) files, information types should be standardized in all the files in the collection.
-   Information types are not supported when using a [binary table of contents](about-binary-contents-files.md).

## Related topics

<dl> <dt>

[About Assigning Information Types](assign-information-types.md)
</dt> </dl>

 

 





