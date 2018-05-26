---
title: To define categories and information types
description: To define categories and information types
ms.assetid: 6E9A8D64-F6D4-4952-8059-1F2A8B8F9FC0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To define categories and information types

1.  Open a contents (.hhc) file, and then click **Contents Properties**.

    

    |                          |                                                                     |
    |--------------------------|---------------------------------------------------------------------|
    | ![](images/sb-conpr.gif) | Defines the general appearance of the table of contents.<br/> |

    

     

2.  Click the **Information Types** tab, and then click **Add**.
3.  In the **Category name** box, type the name for the first category you want (for example, Experience Level).
4.  In the **Description** box, type a description for the category. Descriptions for categories and information types are important because they are viewed by the user in the wizard that walks them through information type selection.
5.  In the **Information type name** box, type the name of the information type you want (for example, Advanced).
6.  In the **Description** box, type a description of the information type. For example, "topics for advanced users."
7.  Click either **Inclusive Type** or **Exclusive Type** to assign an information type attribute.

## Notes

-   You may want to make a backup copy of your contents file before you add information types to it.
-   After you define information types, you can [assign them to a topic](to-assign-an-information-type-to-a-contents-entry.md).
-   You can create up to 10 categories and 32 separate information types. The name for an information type cannot exceed 255 characters.
-   Categories are optional, if you use them, all information types must be added to a category.
-   If used with a [large collection](manage-large-document-sets.md) of merged compiled help (.chm) files, categories should be standardized for all the files in the collection.
-   Information types are not supported when using a [binary table of contents](about-binary-contents-files.md).

## Related topics

<dl> <dt>

[About Assigning Information Types](assign-information-types.md)
</dt> </dl>

 

 





