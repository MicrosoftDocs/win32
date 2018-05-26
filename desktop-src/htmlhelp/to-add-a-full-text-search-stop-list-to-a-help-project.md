---
title: To add a full-text search stop list to a help project
description: To add a full-text search stop list to a help project
ms.assetid: C66ED202-82FC-4cbf-931C-8B9679574214
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To add a full-text search stop list to a help project

1.  [Create a full-text search stop list](to-create-a-full-text-search-stop-list.md).
2.  Open a project (.hhp) file, and then click **Change Project Options**. 

    |                        |                                                                           |
    |------------------------|---------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings.<br/> |

    

     

3.  Click the **Files** tab, and then enter the name of your stop list (.stp) file in the **Full text search stop list file** box.

## Notes

-   A stop list decreases the size of the full-text search index, which results in a smaller compiled help (.chm) file because fewer words are indexed. This is especially important if you have a large documentation set. All words in the stop list are omitted from the search. These are usually commonly occurring words or numbers, such as "the," "and," or "1" that a user is unlikely to search for.
-   You can create a full-text search stop list from the [sample list](to-create-a-full-text-search-stop-list.md) that comes with HTML Help Workshop, and then include it in your project file.
-   For the 1.3 release of HTML Help, the size of this file is limited to 512 bytes.
-   Do not set the stop list as read-only, it will not function if this property is set.

## Related topics

<dl> <dt>

[About Full-Text Search](adding-a-search-tab.md)
</dt> </dl>

 

 





